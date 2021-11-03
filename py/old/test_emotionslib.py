#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:46:28 2021

@author: alfonso
"""

from emotionslib import EmoScores

emos = EmoScores(language = 'italian')


"""
1. bisogna istanziare l'oggetto EmoScore come sopra, se la lingua è diversa da 'english' bisogna specificare
2. sotto ci sono esempi di uso, nello specifico
    2.1 conteggio delle emozioni da testo (il conteggio si può normalizzare con l'apposito parametro `normalization_strategy`)
    2.2 calcolo zscores dal testo (quanto varia la distribuzione di emozioni nel testo rispetto a una baseline neutra)
    2.3 conteggio emozioni e calcolo zscores dalla formamentis network di un testo (rete di relazioni fra parole)
    
Il modello linguistico, la baseline e altri parametri possono essere generati e caricati anzitempo, oppure passati a EmoScore come parametro.
"""


## Undefined texts
text = 'some text'
def load_random_text():
    return 'some other text'

""" 1. Get emotion counts """
emo_counts = emos.emotions(text)

print("[text] Emotion counts: ")
print(emo_counts)
print()

""" OUTPUT 

[text] Emotion counts: 
{'anger': 13, 'trust': 27, 'surprise': 8, 'disgust': 6, 'joy': 11, 'sadness': 10, 'fear': 9, 'anticipation': 12}
"""

""" 2. Get zscores against default baseline """
zscores = emos.zscores(text)

print("[text] Z-scores (default baseline):")
print(zscores)
print()

""" OUTPUT 

[text] Z-scores (default baseline):
{'anger': -0.8171071954896871, 'trust': 3.3487528739313928, 'surprise': 0.4436369169408276, 'disgust': -2.2990848274763507, 'joy': 0.7421027380772303, 'sadness': -1.4405429846486246, 'fear': -2.8836222633140407, 'anticipation': 0.4608692902798836}
"""


""" 3.1 Get zscores against custom baseline """
baseline = load_random_text()
zscores = emos.zscores(text, baseline = baseline)

print("[text] Z-scores (custom baseline as parameter):")
print(zscores)
print()

""" OUTPUT 

[text] Z-scores (custom baseline as parameter):
{'anger': 0.6435058922098025, 'trust': 0.36180018887451487, 'surprise': 2.937316212560913, 'disgust': -0.09109765611280045, 'joy': 2.029200562474832, 'sadness': -2.8796921920375764, 'fear': -2.545851766157043, 'anticipation': -1.0609764073382204}
"""


""" 3.2 Load a permanent baseline (works best for multiple files) """
# baseline same as before
emos.load_baseline(baseline)
zscores = emos.zscores(text)

print("[text] Z-scores (custom baseline, loaded):")
print(zscores)
print()

""" OUTPUT 

[text] Z-scores (custom baseline, loaded):
{'anger': 0.6896966515308854, 'trust': 0.39570526222056, 'surprise': 2.7170436510273395, 'disgust': -0.0357846461555281, 'joy': 1.9867038675394, 'sadness': -2.941512999560478, 'fear': -2.322203619090994, 'anticipation': -1.2780023423280957}
"""


""" 4. Get a formamentis network and print emotion counts """
edges, vertex = emos.formamentis_network(text)
emo_counts = emos.emotions(edges)

print("[formamentis] Emotion counts: ")
print(emo_counts)
print()

""" OUTPUT 

[formamentis] Emotion counts: 
{'anger': 225, 'trust': 511, 'surprise': 120, 'disgust': 118, 'joy': 173, 'sadness': 226, 'fear': 133, 'anticipation': 209}
"""


""" 5. Get a formamentis network and print z-scores """
# baseline same as before
edges, vertex = emos.formamentis_network(text)
zscores = emos.zscores(edges)

print("[formamentis] Z-scores (custom baseline, now loaded permanently):")
print(zscores)
print()

""" OUTPUT 

[formamentis] Z-scores (custom baseline, now loaded permanently):
{'anger': 1.9388523801940707, 'trust': 3.1030630289870658, 'surprise': 8.325015117991716, 'disgust': 0.37906373879824756, 'joy': 5.809358493545078, 'sadness': -9.185919302329598, 'fear': -12.453743262012452, 'anticipation': -5.638223966304567}
"""


""" 6. Get a formamentis network about "vaccino" and print emotion counts """
edges, vertex = emos.formamentis_network(text)
emo_counts = emos.emotions(edges, target_word = "vaccino")

print("[formamentis] Emotion counts: ")
print(emo_counts)
print()

""" OUTPUT 

[formamentis] Emotion counts: 
{'anger': 6, 'trust': 11, 'surprise': 1, 'disgust': 4, 'joy': 3, 'sadness': 5, 'fear': 3, 'anticipation': 4}
"""


""" 7. Get a formamentis network about "vaccion" and print z-scores """
# baseline same as before
edges, vertex = emos.formamentis_network(text)
zscores = emos.zscores(edges, target_word = "vaccino")

print("[formamentis] Z-scores (custom baseline, now loaded permanently):")
print(zscores)
print()

""" OUTPUT 

[formamentis] Z-scores (custom baseline, now loaded permanently):
{'anger': 0.6374845852765537, 'trust': 0.34371414869300376, 'surprise': -0.2941524104331357, 'disgust': 0.9124658860276003, 'joy': 0.26476390213185397, 'sadness': -1.570670263340505, 'fear': -1.8785004045487563, 'anticipation': -1.1153604029189612}
"""


""" 8. What if we ask for the neighbors of "vaccino" without using formamentis? """
try:
    # baseline same as before
    zscores = emos.zscores(text, target_word = "vaccino")

except Exception as e:
    print("[text with target word?]", e)
    print()
    
""" OUTPUT 

[text with target word?] You must use the Formamentis networks if you want to target 'vaccino' as target_word.
"""

    
""" 9. Loading a formamentis and asking z-scores is best when working with multiple files. 
       You can also just get emotion counts and ask to use formamentis networks as well. 
"""
# baseline same as before
zscores = emos.zscores(text, method = 'formamentis', target_word = "vaccino")

print("[formamentis by text] Z-scores (custom baseline, now loaded permanently):")
print(zscores)
print()


""" OUTPUT 

[formamentis by text] Z-scores (custom baseline, now loaded permanently):
{'anger': 0.8059067801393653, 'trust': 0.3475448910209246, 'surprise': -0.26977079219858136, 'disgust': 0.9896850371656553, 'joy': 0.32422624936546546, 'sadness': -1.3473477245660648, 'fear': -1.7208334043810871, 'anticipation': -1.1572922229660068}
"""










