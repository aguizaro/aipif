# Jasmine Task List

# add twee to debug options
 # -> http://aipif-2023.s3.amazonaws.com/favicon.ico
# emoji for story title 


arn:aws:s3:::aipif-2023

# first button labeled "psst..... click me!"
# "the end" button take you to story selection


# test rq generation
# make env setup part of launch
# DEBUG why duplicate ending?

# illustration summary page vote up / down  with poorly voted being regenerated 
# music summary page with votes
# sounds summary page with votes
# story structure summary page ? add / remove branches?


# fix make_picture prompt style 
## Token indices sequence length is longer than the specified maximum sequence length for this model (81 > 77). Running this sequence through the model will result in indexing errors The following part of your input was truncated because CLIP can only handle sequences up to 77 tokens: ['art from quentin blake']


# replace generating image with ours
# swicth illustrations to jpg
# update prompts to remove duplication near end
# swap in larger context gpt near end?
# fix n>1 protagonist_reqaction prompts
# setup and test local llm? wizard?
# midi music maker ?
# try and uncensored model?

## XML to Twee / Twine / Tweego
### run experiments creating the published child experience aka twines / HTML

## research 
### which twine dialect is best for our purpose?
### what do we want our twines to do ? 
#### play music? => abcjs 
#### sound effects? => ???

## update sample picture prompts to be less complex 

## emji DB

---------------------

## web service setup
### "sells the service" -> shows concept slide
### hosts interviews
### makes AI api calls
### generates story twines

## child interview
### design - emoji?
### implementation - html+js?

## text_maker - connect python to LLM
### implementation

# DONE
## story representation => XML

## making the twine file better
### make buttons nicer(center them?)
### add a settings tab 

## prompts
### story outline

### (child_data => story_type => dilema_decision) => dpre_outline

### dpre_outline => dpre_segment_list 

### dpre_segment_list => dpost_outline_list

### dpost_outline_list_entry => dpost_segment_list

# cutline

## parent interview
### design - word cloud?
### implementation - html+js?




<branch index="1">
<protagonist_reaction>Emily, proud of her artistic accomplishment, approached Sarah and whispered, "Would you like to create a collaborative artwork with me?" Sarah's eyes widened with excitement as she nodded eagerly, ready to embark on a new creative adventure.</protagonist_reaction>
<scene name="Final Character Arcs" act="Resolution" part="Conclusion" branch_count="1" index="14" key="rb1b1b1b1b1b1b1b1b2b1b1b1b1">
<introduction>As the art exhibition came to a close, Emily and Sarah stood side by side, admiring their collaborative artwork. It was a vibrant masterpiece that showcased their shared creativity and friendship.</introduction>
<dialogue>"Sarah, we did it!" Emily exclaimed, her voice filled with pride. "Our artwork turned out even better than I imagined."</dialogue>
<illustration url="http://aipif-2023.s3-website-us-west-1.amazonaws.com/_asset/172f3386.png">Emily and Sarah's collaborative artwork was a burst of color and imagination. It depicted a whimsical world filled with magical creatures and breathtaking landscapes. Each stroke of paint and every carefully placed detail told a story of friendship and creativity.</illustration>
<sound url="http://aipif-2023.s3-website-us-west-1.amazonaws.com/_asset/1ef4bdbb.mp3">The sound of applause filled the air as people gathered around Emily and Sarah's artwork, expressing their admiration and appreciation.</sound>
<music url="http://aipif-2023.s3-website-us-west-1.amazonaws.com/_asset/81e2921b.mp3">A cheerful and uplifting melody played in the background, adding to the joyful atmosphere of the art exhibition.</music>


<branch index="1">
<protagonist_reaction>Emily turned to Sarah and said, "Let's continue creating art together. We make an amazing team!" Sarah nodded enthusiastically, excited to embark on more creative adventures with her newfound friend.</protagonist_reaction>
<scene name="Sense of Closure" act="Resolution" part="Conclusion" branch_count="0" index="15" key="rb1b1b1b1b1b1b1b1b2b1b1b1b1b1">
<introduction>As the art exhibition came to a close, Emily and Sarah stood side by side, admiring their collaborative artwork. It was a vibrant masterpiece that showcased their shared creativity and friendship.</introduction>
<dialogue>"Sarah, we did it!" Emily exclaimed, her voice filled with pride. "Our artwork turned out even better than I imagined."</dialogue>
<illustration url="http://aipif-2023.s3-website-us-west-1.amazonaws.com/_asset/172f3386.png">Emily and Sarah's collaborative artwork was a burst of color and imagination. It depicted a whimsical world filled with magical creatures and breathtaking landscapes. Each stroke of paint and every carefully placed detail told a story of friendship and creativity.</illustration>
<sound url="http://aipif-2023.s3-website-us-west-1.amazonaws.com/_asset/ba86dcf7.mp3">The sound of applause filled the air as people admired Emily and Sarah's artwork, expressing their awe and appreciation.</sound>
<music url="http://aipif-2023.s3-website-us-west-1.amazonaws.com/_asset/81e2921b.mp3">A cheerful and uplifting melody played in the background, adding to the joyful atmosphere of the art exhibition.</music>
</scene>
</branch>