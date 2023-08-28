"""uses freesound api to write sound data into temp_directory/sound_data.txt and download sound previews to temp_directory"""

import os
import time
import freesound
import json
from sounds.negative_prompt_samples import negative_prompt_text
    
freesound_client = freesound.FreesoundClient()
freesound_client.set_token(os.getenv('FREESOUND_API_KEY'))
temp_directory= os.getenv('TEMP_DIRECTORY')
 
def collect_sounds(prompt, max_tries= 3):
    """Collect sounds from a text based query to freesound and write results to temp_directory/sound_data.txt file as json data

    Args:
    -   `prompt`(string): search query as a string

    Returns:
        dict: dictionary mapping sound ids to sound objects or `None` if a freesound error occurs
    """
    try:
        hi_quality_sounds= []
        collected_sound_objs= {}
        results_pager = freesound_client.text_search(
            query=f'{prompt} -music',
            filter="duration:[1.0 TO 8.0] license:\"Creative Commons 0\"",
            page_size=150,
            sort="score",
            fields="id,name,score,avg_rating,description,tags,num_ratings,previews"
        )

        # Collect max 50 high quality sounds
        for sound in results_pager:
            if len(hi_quality_sounds) >= 50:
                break
            if sound.num_ratings >= 3 and sound.avg_rating >= 4:
                if has_valid_tags(sound.tags): # Only collect sounds with no musical tags
                    hi_quality_sounds.append({"id": sound.id, "name": sound.name, "description": sound.description, "tags": sound.tags, "rating": sound.avg_rating})
                    collected_sound_objs[sound.id]= sound
            
        # Write serialized sound data into sound_data.txt
        sound_data= json.dumps(hi_quality_sounds, indent=1)
        write_to_file(sound_data, f"{temp_directory}sound_data.txt")
        return collected_sound_objs
    
    except freesound.FreesoundException as e:
        if e.code == 429: # Too many requests
            if max_tries < 1:
                return None
            print("Waiting for freesound api throttle to expire...")
            time.sleep(60)
            collect_sounds(prompt, max_tries-1)
                
        

def preview_sound(sound_id, sounds):
    """Download sound preview to temp directory
    
    Arguments:
    -   `sound_id`(int): sound id of requested sound
    -   `sounds`(dict): dictionary mapping sound ids to sound objects
    """
    sounds[sound_id].retrieve_preview(directory=temp_directory, name=f"{sound_id}")
    
def write_to_file(data, file_path):
    """Write `data` to `file_path`

    Args:
    -   `data`(any): sound data to write to the file
    -   `file_path`(string): path to new or existing file to store sound data
    """
    with open(file_path, 'w') as file:
        file.write("\"This data represents sounds from freesound and their descriptions.\"\n\n")
        file.write(data)
        
def has_valid_tags(word_list):
    """Returns `True` if all words/tags in `word_list` are valid, otherwise returns `False`.
    A word/tag is not valid if it is listed in `negative_prompt_text`.

    Args:
    -   word_list (list[str]): list of words to check

    Returns:
        bool: `True` or `False`
    """
    prohibited_words= [word.lower() for word in negative_prompt_text]
    for word in word_list:
        if word.lower() in prohibited_words:
            return False
    return True 
