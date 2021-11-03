#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 18:52:01 2021

@author: alfonso
"""
import re

def _clean_text(text):
    """ Preliminary text cleaning: removing weird punctuation from words, stripping spaces. """
    
    text = text.replace('’', "'")
    text = text.replace('"', '')
    text = text.replace('”', '')
    text = text.replace('“', '')
    text = text.replace('«', '')
    text = text.replace('»', '')
    text = re.sub('\t', ' ', text)
    text = re.sub('\n', ' ', text)
    text = re.sub('[ ]+', ' ', text)
    text = text.lower()
#    text.encode("utf-8", "ignore").decode() 
    text = re.sub('\<u\+[0-9A-Za-z]+\>', '', text)
    # eccezioni e parole troppo corte
    text = text.strip()
    return text



def _handle_negations(wordlist, negations = None, language = 'english', antonyms = None, negation_strategy = 'ignore'):
    """
    Delete words preceded by negations.

    Required arguments:
    ----------
    *wordlist*:
        A list of words. 
        
    *negations*:
        A custom-defined list of negations. 
        Default is None: a pre-compiled list will be loaded.
        
    *language*:
        Language of the text. Full support is offered for the languages supported by Spacy: 
            Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
            Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.
        Limited support for other languages is available.
    
    Returns:
    ----------
    
    *wordlist*:
        A list of words. Words preceded by negations have been eliminated.    
    """
    
    if not negations:
        from language_dependencies import _negations as negs
        
        negations = negs[language]
            
        
    if negation_strategy == 'delete':
        wordlist = [wordlist[i] for i in range(len(wordlist)) if (i == 0 or wordlist[i-1] not in negations)]
        
    elif negation_strategy == 'replace':
        wordlist = [antonyms.get(wordlist[i], wordlist[i]) if (i > 0 and wordlist[i-1] in negations) else wordlist[i] for i in range(len(wordlist))]
    
    elif negation_strategy == 'add':
        wordlist += [antonyms.get(wordlist[i], wordlist[i]) for i in range(len(wordlist)) if (i > 0 and wordlist[i-1] in negations)]        

    return wordlist
    
