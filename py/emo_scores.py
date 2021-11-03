#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:02:51 2021

@author: alfonso
"""

import numpy as np
from language_dependencies import _load_dictionary, _check_language, _negations
import compare_baseline as _cbsl
import itertools
from textutils import _clean_text, _handle_negations
import spacy
import pandas as pd
from formamentis_edgelist import get_formamentis_edgelist
from collections import namedtuple

def load_formamentis_edgelist(edgelist, spacy_model, target_word = None, language = 'english', duplicates = True, negation_strategy = 'ignore', negations = None, antonyms = None):
        
     # Check for edgelist consistency
    if len(edgelist) == 0:
        return []
    elif type(edgelist) == list:
        edgelist = pd.DataFrame(edgelist, columns = ['word', 'neighbor'])
        edgelist = edgelist.append(pd.DataFrame({'word': edgelist['neighbor'], 'neighbor': edgelist['word']}))
    elif 'pandas.core.frame.DataFrame' in str(type(edgelist)):
        edgelist.columns = ['word', 'neighbor']
        edgelist = edgelist.append(pd.DataFrame({'word': edgelist['neighbor'], 'neighbor': edgelist['word']}))  
        
    if negation_strategy != 'ignore':
        pass # do something here with negations
    
    
    if target_word:
        # Get neighbors of `target_word`
        L = edgelist.loc[edgelist['word'] == target_word, 'neighbor'].values
        
    else:
        # Get all words
        L = edgelist['neighbor'].values
        
    if not duplicates:
        L = list(set(L))
        
        
    return L
    

def load_text(text, spacy_model, language = 'english', duplicates = False, negation_strategy = 'ignore', negations = None, antonyms = None):
    
     # clean text
    text = _clean_text(text)
    
    # Check for language
    _check_language(language)
    
    # Getting or using spacy model
    if 'spacy.lang' in str(type(spacy_model)):
        nlp = spacy_model
    elif type(spacy_model) == str:
        try:
            nlp = spacy.load(spacy_model)
        except:
            raise ValueError("Can't find Spacy model '{}'. Please use a model from https://spacy.io/models.".format(spacy_model))

    # get tokens
    nlp.create_pipe('sentencizer')
    tokens = [[token for token in nlp(sentence.text)] for sentence in nlp(text).sents]
    tokens = itertools.chain(*tokens)
    tokens = [token.lemma_ for token in tokens]
    
    # Duplicates strategy
    if not duplicates:
        tokens = list(set(tokens))
        
    # Negation strategy
    if negation_strategy != 'ignore':
        tokens = _handle_negations(tokens, language = language, negations = negations, antonyms = antonyms, negation_strategy = negation_strategy)
    
    return tokens



def count_emotions(obj, 
                   emotion_lexicon = None, 
                   normalization_strategy = 'none', 
                   emotions = None, 
                   language = 'english',
                   spacy_model = 'en_core_web_sm',
                   duplicates = True,
                   negation_strategy = 'ignore',
                   negations = None,
                   antonyms = None,
                   method = 'default',
                   target_word = None,
                   wn = None,
                   emotion_model = 'plutchik'):
    
    """
    Count emotions in given wordlist.

    Required arguments:
    ----------
    *text*:
        The input text. 
        
    *emotion_lexicon*:
        A lexicon with every word-emotion association. By default, the NRCLexicon will be loaded.
        
    *normalize_strategy*:
        A string, whether to normalize emotion scores over the number of words. Accepted values are:
            'none': no normalization at all
            'text_lenght': normalize emotion counts over the total text length
            'emotion_words': normalize emotion counts over the number of words associated to an emotion
            
    *emotions*:
        A list of emotions, depending on the model required. Default is Pluthick's wheel of emotions model.
        
    *language*:
        Language of the text. Full support is offered for the languages supported by Spacy: 
            Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
            Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.
        Limited support for other languages is available.
        
    Returns:
    ----------
    *emo_counts*:
        A dict. For each emotion the associated counts.  
        
    *n_emotionwords*:
        An integer, the number of words associated with an emotion in wordlist.
    """        
    

    
    if not emotions and emotion_model == 'plutchik':
        emotions = ['anger', 'trust', 'surprise', 'disgust', 'joy', 'sadness', 'fear', 'anticipation']
        
    if type(obj) == list:
        wordlist = load_formamentis_edgelist(edgelist = obj,
                                 spacy_model = spacy_model,
                                 language = language,
                                 target_word = target_word,
                                 duplicates = duplicates,
                                 negation_strategy = negation_strategy,
                                 negations = negations,
                                 antonyms = antonyms)
        
        
    elif type(obj) == str and method == 'formamentis':
        edgelist, _ = get_formamentis_edgelist(text = obj, 
                                            language = language, 
                                            spacy_model = spacy_model,
                                            keepwords = [],
                                            stopwords = ['it'],
                                            antonyms = antonyms,
                                            wn = wn)
        
        wordlist = load_formamentis_edgelist(edgelist = edgelist,
                                 spacy_model = spacy_model,
                                 language = language,
                                 target_word = target_word,
                                 duplicates = duplicates,
                                 negation_strategy = negation_strategy,
                                 negations = negations,
                                 antonyms = antonyms)
    elif type(obj) == str:  
        
        if target_word and method != 'formamentis':
            raise ValueError("You must use the Formamentis networks if you want to target '{}' as target_word.".format(target_word))
        
        
        wordlist = load_text(text = obj, 
                             spacy_model = spacy_model, 
                             language = language,
                             duplicates = duplicates,
                             negation_strategy = negation_strategy,
                             negations = negations,
                             antonyms = antonyms
                             )
        
        
    emo_distr = _cbsl._emotion_distribution(wordlist = wordlist, emotion_lexicon = emotion_lexicon, emotions = emotions, language = language)   
    n_emotionwords = len(emo_distr)
    
    
    emo = list(itertools.chain(*emo_distr))
    emo_counts = {emotion: emo.count(emotion) for emotion in emotions}
    
    if normalization_strategy not in ['none', 'num_words', 'num_emotions']:
        raise ValueError("'normalization_strategy' must be one of 'none', 'num_words', 'num_emotions'.")
        
    if normalization_strategy == 'num_words':
        emo_counts = {key: val / len(wordlist) for key, val in emo_counts.items()}
    elif normalization_strategy == 'num_emotions':
        try:
            emo_counts = {key: val / n_emotionwords for key, val in emo_counts.items()}
        except ZeroDivisionError:
            emo_counts = {key: 0 for key, _ in emo_counts.items()}
    
    ecounts = namedtuple('emotion_counts', 'emotions num_emotion_words')
    return ecounts(emo_counts, n_emotionwords)
    


def stats(obj, 
          emotion_lexicon = None,
          emotions = None, 
          language = 'english',
          spacy_model = 'en_core_web_sm',
          duplicates = True,
          negation_strategy = 'ignore',
          negations = None,
          antonyms = None,
          method = 'default',
          target_word = None,
          wn = None,
          emotion_model = 'plutchik'):
    
    
    if not emotions and emotion_model == 'plutchik':
        emotions = ['anger', 'trust', 'surprise', 'disgust', 'joy', 'sadness', 'fear', 'anticipation']
        
    if type(obj) == list:
        wordlist = load_formamentis_edgelist(edgelist = obj,
                                 spacy_model = spacy_model,
                                 language = language,
                                 target_word = target_word,
                                 duplicates = duplicates,
                                 negation_strategy = negation_strategy,
                                 negations = negations,
                                 antonyms = antonyms)
        
        
    elif type(obj) == str and method == 'formamentis':
        edgelist, _ = get_formamentis_edgelist(text = obj, 
                                            language = language, 
                                            spacy_model = spacy_model,
                                            keepwords = [],
                                            stopwords = ['it'],
                                            wn = wn)
        
        wordlist = load_formamentis_edgelist(edgelist = edgelist,
                                 spacy_model = spacy_model,
                                 language = language,
                                 target_word = target_word,
                                 duplicates = duplicates,
                                 negation_strategy = negation_strategy,
                                 negations = negations,
                                 antonyms = antonyms)
    elif type(obj) == str:  
        
        if target_word and method != 'formamentis':
            raise ValueError("You must use the Formamentis networks if you want to target '{}' as target_word.".format(target_word))
        
        
        wordlist = load_text(text = obj, 
                             spacy_model = spacy_model, 
                             language = language,
                             duplicates = duplicates,
                             negation_strategy = negation_strategy,
                             negations = negations,
                             antonyms = antonyms
                             )
        
        
    emo_distr = _cbsl._emotion_distribution(wordlist = wordlist, emotion_lexicon = emotion_lexicon, emotions = emotions, language = language)   
    n_emotionwords = len(emo_distr)
    
    emo_distr_unique = _cbsl._emotion_distribution(wordlist = list(set(wordlist)), emotion_lexicon = emotion_lexicon, emotions = emotions, language = language)
    n_emotionwords_unique = len(emo_distr_unique)
    
    
    emo = list(itertools.chain(*emo_distr))
    emo_counts = {emotion: emo.count(emotion) for emotion in emotions}
    
    
    emo_unique = list(itertools.chain(*emo_distr_unique))
    emo_counts_unique = {emotion: emo_unique.count(emotion) for emotion in emotions}
    
 
    out = {}
    out['emotions'] = {'num_emotionwords': n_emotionwords,
                       'num_emotionwords_unique': n_emotionwords_unique,
                       'perc_emotionwords': n_emotionwords / len(wordlist),
                       'perc_emotionwords_unique': n_emotionwords_unique / len(set(wordlist))}
    
    for emotion in emotions:
        out[emotion] = {'num_words': emo_counts[emotion],
                        'num_words_unique': emo_counts_unique[emotion],
                        'perc_text': emo_counts[emotion] / len(wordlist),
                        'perc_text_unique': emo_counts_unique[emotion] / len(set(wordlist))}
    
    for emotion in emotions:
        try:
            out[emotion]['perc_emotionwords'] = out[emotion]['num_words'] / n_emotionwords
            out[emotion]['perc_emotionwords_unique'] = out[emotion]['num_words_unique'] / n_emotionwords_unique
        except:
            out[emotion]['perc_emotionwords'] = 0
            out[emotion]['perc_emotionwords_unique'] = 0
            
    negations = _negations[language] if not negations else negations
    out['negations'] = {'num_negations': len([word for word in wordlist if word in negations]),
                        'num_negations_unique': len([word for word in set(wordlist) if word in negations])}
    
    out['words'] = {'num_words': len(wordlist), 'num_words_unique': len(set(wordlist))}
    
    return out
    

def baseline_distribution(baseline, emotions = None, emotion_model = 'plutchik', normalization_strategy = 'num_emotions'):
    
    if not emotions and emotion_model == 'plutchik':
        emotions = ['anger', 'trust', 'surprise', 'disgust', 'joy', 'sadness', 'fear', 'anticipation']
    
    emo = list(itertools.chain(*baseline))
    emo_counts = {emotion: emo.count(emotion) for emotion in emotions}
    
    if normalization_strategy not in ['none', 'num_emotions']:
        raise ValueError("'normalization_strategy' must be one of 'none', 'num_emotions'.")
        
    elif normalization_strategy == 'num_emotions':
        emo_counts = {key: val / len(baseline) for key, val in emo_counts.items()}
        
    ecounts = namedtuple('emotion_counts', 'emotions num_emotion_words')
    return ecounts(emo_counts, len(baseline))


def make_baseline(baseline = None, emotion_lexicon = None, emotions = None, language = 'english', spacy_model = None):
    """
    Get emotion distribution in baseline_wordlist. If empty, use the lexicon as baseline_wordlist.

    Required arguments:
    ----------
    *baseline_wordlist*:
        A list of words. 
        
    *language*:
        Language of the text. Full support is offered for the languages supported by Spacy: 
            Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
            Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.
        Limited support for other languages is available.
    
    *emotion_lexicon*:
        A lexicon with every word-emotion association. By default, the NRCLexicon will be loaded.
            
    *emotions*:
        A list of emotions, depending on the model required. Default is Pluthick's wheel of emotions model.
    
    Returns:
    ----------
    *baseline_distr*:
        A list of lists. Each entry is a list of emotions associated to a word in wordlist.
    """
    
    baseline_distr = None
    
    if not emotion_lexicon:
        emotion_lexicon = _load_dictionary(language)
        emotion_lexicon = emotion_lexicon.groupby('word')['emotion'].apply(list).to_dict()
        
    
    if not emotions:
        emotions = ['anger', 'trust', 'surprise', 'disgust', 'joy', 'sadness', 'fear', 'anticipation']
        
    if not baseline:
        baseline_wordlist = list(emotion_lexicon.keys())
        baseline_distr = _cbsl._emotion_distribution(wordlist = baseline_wordlist, 
                                                         emotion_lexicon = emotion_lexicon, 
                                                         emotions = emotions, 
                                                         language = language)
    # String
    elif type(baseline) == str: 
        if spacy_model:
            baseline_wordlist = load_text(baseline,
                                          language = language, 
                                          spacy_model = spacy_model, 
                                          duplicates = False, 
                                          negation_strategy = 'ignore', 
                                          antonyms = None, 
                                          negations = None)
            
            
            baseline_distr = _cbsl._emotion_distribution(wordlist = baseline_wordlist, 
                                                         emotion_lexicon = emotion_lexicon, 
                                                         emotions = emotions, 
                                                         language = language)
            
        else:
            raise ValueError("Cannot build a baseline emotion distribution without a spacy model!")
            
    
    # Formamentis edgelist
    elif type(baseline) == list and type(baseline[0]) == tuple:
        baseline_wordlist = load_formamentis_edgelist(baseline,
                                          language = language, 
                                          spacy_model = spacy_model, 
                                          duplicates = False, 
                                          negation_strategy = 'ignore', 
                                          antonyms = None, 
                                          negations = None)
        
        baseline_distr = _cbsl._emotion_distribution(wordlist = baseline_wordlist, 
                                                         emotion_lexicon = emotion_lexicon, 
                                                         emotions = emotions, 
                                                         language = language)
        
    elif 'pandas.core.frame.DataFrame' in str(type(baseline)) :
        baseline_wordlist = load_formamentis_edgelist(baseline,
                                          language = language, 
                                          spacy_model = spacy_model, 
                                          duplicates = False, 
                                          negation_strategy = 'ignore', 
                                          antonyms = None, 
                                          negations = None)
        
        baseline_distr = _cbsl._emotion_distribution(wordlist = baseline_wordlist, 
                                                         emotion_lexicon = emotion_lexicon, 
                                                         emotions = emotions, 
                                                         language = language)
        
    # Baseline previously made by this library
    elif type(baseline) == list and type(baseline[0]) == list:
        baseline_distr = baseline
    
    
    if not baseline_distr:
            raise ValueError("Baseline has no emotions. Please provide a meaningful baseline or None.")
        
    return baseline_distr






def zscores(obj, 
           language = 'english', 
           spacy_model = 'en_core_web_sm',
           baseline = None, 
           emotion_lexicon = None, 
           duplicates = False, 
           negation_strategy = 'ignore', 
           antonyms = None, 
           negations = None, 
           n_samples = 300, 
           method = 'default',
           target_word = None,
           wn = None,
           emotion_model = 'plutchik'):
    
    """
    Get z-scores for each emotion detected in the any word of the wordlist.
    It compares emotions detected against mean and standard deviation of the same emotion
    in 300 random samples.

    Required arguments:
    ----------
    *text*:
        The input text. 
        
    *language*:
        Language of the text. Full support is offered for the languages supported by Spacy: 
            Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
            Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.
        Limited support for other languages is available.
    
    *spacy_model*:
        Either a string or a spacy object. If string, it must be the name of a spacy model installed on your system.
        
    *baseline*:
        A list of words. Wordlist's emotion distribution will be checked against the baseline's emotion distribution.
        Default is None: wordlist will be checked against a random sample from the emotion_lexicon.
        
    *emotion_lexicon*:
        A lexicon with every word-emotion association. By default, the NRCLexicon will be loaded.
        
    *negation_strategy*:
        A string, if words introduced by negations will be replaced by their antynomies.
        Default is ignore', for which no action will be done.
        Other values accepted are 'replace', i.e. words introduced by negations will be replaced,
        and 'delete', i.e. those words will be deleted.
    
    *antonyms*:
        A dict. For each word in the dict's keys, the correspondent value is its antynomy.
        Default is None: a pre-compiled dictionary will be loaded.
        
    *negations*:
        A custom-defined list of negations. 
        Default is None: a pre-compiled list will be loaded.
    
    *duplicates*:
        A boolean: if True, words associated with emotions will be counted as many times as they appear into the wordlist.
        If False, each word will be counted only once. Default is False.
        
    *n_samples*:
        An integer: how many times the wordlist will be checked against a random sample taken from a custom baseline.
        
    *emotion_model*:
        A string, what emotion model to use. Default is 'plutchik', i.e. the Plutchik's wheel of emotions.
    
    Returns:
    ----------
    
    *zscores*:
        A dict. For each emotion the associated z-score.    
    """
    
    
    # 1. load 
    # 2. get resources for emotion model == plutchik?
    # 3. check data duplicates
    # 4. handle negations
    # 5. get emotion counts
    # 6. manage the baseline
    # 7. get random samples distribution
    # 8. return z-scores
    
    
#    # Check for language
#    check_language(language)
    
    # Check emotions resources: lexicon and emtions
    emotion_lexicon, emotions = _cbsl._emotion_model_resources(emotion_lexicon = emotion_lexicon, 
                                                               emotion_model = emotion_model,
                                                               language = language)
    
    # check data format
    if len(obj) == 0:
        return {emo: np.nan for emo in emotions}
    
    
    # count emotions in wordlist
    emo_counts, n_emotionwords = count_emotions(obj = obj, 
                                                emotion_lexicon = emotion_lexicon,
                                                normalization_strategy = 'none',
                                                language = language,
                                                spacy_model = spacy_model, 
                                                duplicates = duplicates,
                                                negation_strategy = negation_strategy,
                                                negations = negations,
                                                antonyms = antonyms,
                                                emotions = emotions,
                                                method = method,
                                                target_word = target_word,
                                                wn = wn)
    
    # sample against baseline
    baseline = make_baseline(baseline = baseline, spacy_model = spacy_model, emotion_lexicon = emotion_lexicon, emotions = emotions, language = language)
    
    
    # Get emotions in 300 random samples
    emo_samples = _cbsl._samples(baseline_distr = baseline, sample_size = n_emotionwords, n_samples = n_samples, emotions = emotions)
    
    # Get z-scores
    zscores = {key.lower(): (emo_counts.get(key, 0) - emo_samples[key]['mean']) / emo_samples[key]['std'] for key in emotions}

    
    return zscores

 
    