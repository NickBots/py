from emotionslib import EmoScores


def get_scores(text, language):
    if((language == "spanish") | (language == "russian") | (language == "romanian") | (language == "portuguese") | (language == "polish") | (language == "norwegian") | (language == "macedonian") | (language == "lithuanian") | (language == "japanese") | (language == "italian") | (language == "greek") | (language == "german") | (language == "french") | (language == "english") | (language == "dutch") | (language == "danish") | (language == "chinese") | (language == "catalan")):
        emos = EmoScores(language=language)
        emo_counts = emos.zscores(text)
    else: 
        emo_counts = 0
    return emo_counts
