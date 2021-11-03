#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 18:00:50 2021

@author: alfonso
"""

import spacy
import networkx as nx
import itertools
from textutils import _clean_text
from language_dependencies import _negations, _pronouns, _language_code3
import re


def _wordnet_synonims(vertexlist, edgelist, language, wn):
    """
    1. For each word `i` in vertexlist, get all synonims `S_i`
    2. For each pair of word in vertexlist that are synonims, draw an edge
       like (i, j \in S_i)
    """
    lang = _language_code3(language)
    if not lang:
        return edgelist
    
    
    
    synonims_list = [list(set(itertools.chain(*[w.lemma_names(lang) for w in wn.synsets(x, lang = lang)]))) for x in vertexlist]
    synonims_pairs = [list(itertools.combinations(syn, 2)) for syn in synonims_list if len(syn) > 0]
    
    synonims_pairs = [[(a, b) for (a, b) in w if a in vertexlist and b in vertexlist] for w in synonims_pairs]
    synonims_pairs = list(set(itertools.chain(*synonims_pairs)))
    
    edgelist += synonims_pairs

    return edgelist    
    

def _get_edges_vertex(text, spacy_model, language = 'english', keepwords = [], stopwords = [], antonyms = {}, wn = None, max_distance = 2):
    """ Get an edgelist, with also stopwords in it, and a vertex list with no stopwords in it. """
    
    
    edgelist = []
    vertexlist = []

#     keeptags = ['JJ', 'JJR', 'JJS', 'CD', 'PRP', 'NN', 'NNS', 'FW', 'NNP', 'NNPS', 'PDT', 'RB', 'RBR', 
#                 'RBS', 'RP', 'VB', 'VBZ', 'VBP', 'VBD', 'VBN', 'VBG'] # this goes with .tag_
    keeppos = ['VERB', 'AUX', 'NOUN', 'PROPN', 'ADJ', 'NUM'] # this goes with .pos_
    
    # Getting or using spacy model
    if 'spacy.lang' in str(type(spacy_model)):
        nlp = spacy_model
    elif type(spacy_model) == str:
        try:
            nlp = spacy.load(spacy_model)
        except:
            raise ValueError("Can't find Spacy model '{}'. Please use a model from https://spacy.io/models.".format(spacy_model))

    # get sentences
    nlp.create_pipe('sentencizer')
    sentences = nlp(text).sents
    

    for sentence in sentences:
        
        
        sent_edges = []
        sent_vertex = []
        negations_lemmas = []
        to_negate = []
    
        # tokenize sentence
        tokens = [(index, token) for index, token in enumerate(nlp(sentence.text))]
        for i, token in tokens:
            token.lemma_ = '{}__'.format(i) + token.lemma_
        tokens = [token for _, token in tokens]    
        
        for token in tokens:
        
            #lemmatization
            stem = token.lemma_
            stem_head = token.head.lemma_
            
            #is it a negation?
            if token.text in _negations[language]:
                negations_lemmas += [token.lemma_, token.text]
                
            # a pair < word, parent_word > unless word is ROOT
            if token.dep_ != 'ROOT':
                sent_edges += [(stem, stem_head)]
            
            # Handle negations part 1
            # add edges with negated words (negation is parent)
            if token.head.text in negations_lemmas:
                num, ss = stem.split('__')
                
                if ss in antonyms.keys():
                    sent_edges += [(num + '__' + antonyms[ss], stem)]
                    to_negate += [stem]
                    
            # Handle negations part 2
            # add edges with negated words (negation is children)
            if token.text in negations_lemmas:
                num, ss = stem_head.split('__')
                
                if ss in antonyms.keys():
                    sent_edges += [(num + '__' + antonyms[ss], stem_head)]
                    to_negate += [stem_head]
                
            # should you keep the word? Yes if it is in keeppos or it is a negation or a pronoun
            keep = (token.pos_ in keeppos)
            keep = keep or (token.text in _negations[language]) or (token.text in _pronouns[language]) 
            # reasons to overtake on keep
            nokeep = (token.text in stopwords) or (token.is_stop) or (len(token.text) <= 2) or bool(re.search('[0-9]', token.text))
            # reasons to overtake on everything
            yakeep = token.text in keepwords
            
            if (keep and not nokeep) or yakeep:
                sent_vertex += [stem]
                
                # add negated words to vertex
                if stem in to_negate:
                    num, ss = stem.split('__')
                    if ss in antonyms.keys():
                        sent_vertex += [num + '__' + antonyms[ss]]
                                                
                        
        # Get all pairs of edges between words at distance <= max_distance
        sent_edges, sent_vertex = _get_network(sent_edges, sent_vertex, max_distance)        
        
        
         # Remove unique identifiers, only lemmas
        sent_edges = [(a.split('__')[1], b.split('__')[1]) for a, b in sent_edges]
        
        # Get vertex list
        sent_vertex = list(set([vertex.split('__')[1] for vertex in sent_vertex]))
    
        # Add synonims
        sent_edges = _wordnet_synonims(sent_vertex, sent_edges, language, wn)
        
        # Uniques
        sent_edges = list(set(sent_edges))
        sent_vertex = list(set(sent_vertex))
        
        
        edgelist += sent_edges
        vertexlist += sent_vertex   
    
    
    return edgelist, vertexlist


    
def _get_network(edges, vertex, max_distance = 2):
    """ Builds a graph from the edgelist, keeps only pairs of vertex that:
        - are at maximum distance of `max_distance` links
        - are both in the vertex list
    """

    G = nx.Graph(edges)

#     spl = nx.all_pairs_shortest_path_length(G, cutoff = max_distance)
#     print(dict(spl))
    spl = nx.all_pairs_shortest_path_length(G, cutoff = max_distance)

    # spl is {source: {target: distance}, ... }
    # must check that: 
    # 1. source != target
    # 2. source in vertex, target in vertex
    # 3. distance <= max_distance
    edges = [[(source, target) for target, distance in path.items() if (1 <= distance <= max_distance) and (target in vertex)] for source, path in dict(spl).items() if source in vertex]
    
    # unlist
    edges = list(itertools.chain(*edges))
    
    # list of lists of tuples (a, b), where a < b, no duplicates
    edges = [(a, b) for a, b in edges if a < b]
    
    return edges, vertex
    

    
def get_formamentis_edgelist(text, 
                             language = 'english', 
                             spacy_model = 'en_core_web_sm',
                             target_word = None,
                             keepwords = [],
                             stopwords = [],
                             antonyms = None,
                             wn = None,
                             max_distance = 2
                             ):
    """
    FormaMentis edgelist from input text.
    
    Required arguments:
    ----------
          
    *text*:
        A string, the text to extract emotions from.
   
    *language*:
        Language of the text. Full support is offered for the languages supported by Spacy: 
            Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
            Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.
        Limited support for other languages is available.
        
    *target_word*:
        A string or None. If a string and method is 'formamentis', it will be computed the emotion distribution
        only of the neighborhood of 'target_word' in the formamentis network.
        
    *keepwords*:
        A list. Words that shall be included in formamentis networks regardless from their part of speech. Default is an empty list.
        By default implementation, a pre-compiled list of negations and pronouns will be loaded and used as keepwords.
        
    *stopwords*:
        A list. Words that shall be discarded from formamentis networks regardless from their part of speech. Default is an empty list.
        If a word is both in stopwords and in keepwords, the word will be discarded.
        
    *max_distance*:
        An integer, by default 2. Links in the formamentis network will be established from each word to each neighbor within a distance
        defined by max_distance.
        
    Returns:
    ----------
    *edges*:
        A list of 2-items tuples, defining the edgelist of the formamentis network.
    
    *vertex*:
        A list of string, defining the list of vertices of the network.
        
    """
    
    
    text = _clean_text(text)
    edges, vertex = _get_edges_vertex(text = text, spacy_model = spacy_model, language = language, 
                                      keepwords = keepwords, stopwords = stopwords, 
                                      antonyms = antonyms, wn = wn,
                                      max_distance = max_distance)
    
    # TODO: synonims from WordNet
    
    # target words!
    if target_word:
        neighbors = list(set(list(itertools.chain(*[e for e in edges if target_word in e]))))
        edges = [(a, b) for a, b in edges if a in neighbors and b in neighbors]
        vertex = list(set.union(set([a for a, _ in edges]), set([b for _, b in edges])))
        
    return edges, vertex