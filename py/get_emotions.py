import random

def random_emotions_generation():
    emotions = ['joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation']
    emotions = {emo: random.uniform(0, 1) for emo in emotions}
    return emotions
        