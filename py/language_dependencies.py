#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:07:11 2021

@author: alfonso
"""

_negations = {
    "german": ['nicht', 'nein'],
    "english": ['no', 'neither', 'not', 'cannot', 'never', 'nothing', "n't"], 
    "italian": ['non', 'no', 'né'],
    "french": ['non', 'pas', 'ne'],
    "danish": ['nej', 'ikke'],
    "dutch": ['nee', 'niet'],
    "catalan": ['no', 'tampoc'],
    "chinese": ['都不是', '不'],
    "greek": ['δεν', 'ούτε', 'όχι'],
    "japanese": ['いいえ'],
    "lituanian": ['ne', 'nei'],
    "macedonian": ['не', 'ниту'],
    "norvegian": ['ikke', 'nei'],
    "polish": ['nie', 'ani'],
    "portuguese": ['não', 'nem'],
    "romanian": ['nu', 'nici'],
    "russian": ['нет', 'ни'],
    "spanish": ['no', 'ni']
}

_pronouns = {
    "german": ['dir', 'mich', 'es', 'ihnen', 'unser', 'uns', 'wir', 'euer', 'sein', 'sie', 'du', 
        'mein', 'er', 'dein', 'euch', 'dich', 'ihr', 'ich', 'mir', 'ihn', 'ihm', 'sich'],
    "english": ['he', 'his', 'we', 'her', 'them', 'i', 'it', 'they', 'me', 'us', 'you', 'she'],
    "italian": ['ella', 'esso', 'io', 'te', 'lei', 'egli', 'vi', 'voi', 'tu', 'noi', 'essa', 'lui', 'essi', 'ci', 'me', 'loro'],
    "french": ['ils', 'elle', 'elles', 'il', 'on', 'tu', 'vous', 'nous', 'je'],
    "danish": ['de', 'hun', 'han', 'vi', 'jeg', 'i', 'du'],
    "dutch": ['jullie', 'u', 'ik', 'jij', 'zij', 'hij', 'wij'],
    "catalan": ['jo', 'ella', 'nosaltres', 'ells', 'vós', 'tu', 'vos', 'vosaltres', 'el'],
    "chinese": ['您', '你们', '我', '他们', '它', '你', '它们', '我们', '她们', '咱们', '她', '他'],
    "greek": ['εσείς', 'αυτος', 'αυτά', 'eγώ', 'αυτή', 'αυτη', 'αυτα', 'αυτο', 'αυτοι', 'εμείς', 'αυτοί', 'αυτός', 'αυτες', 'εσύ'],
    "japanese": ['僕', '私', '我々', '彼', '俺', 'おれ', '方', 'お前', '彼女', 'かのじょ', '貴方', 
    'あのひと', 'あなた', 'あの人', '私達', '君', 'ぼく', 'わたし', 'おまえ', 'かれ', 'きみ'],
    "lituanian": ['jóms', 'jám', 'tavyjè', 'tavimì', 'noi', 'mùms', 'jùs', 'manè', 'jiẽ", "essi', 'jomìs', 
        'mán', 'jū̃s', 'mùs', 'mumysè', 'mẽs', 'jumìs', 'jùms', 'juosè', 'jaĩs', 'jõs', 'jái', 'jumysè', 'jį̃', 
        'mumìs', 'josè', 'mū́sų', 'jojè', 'jàs', 'juõs', 'jà', 'j¡ems', 'voi', 'táu', 'tavè', 'esse', 'juõ', 
        'manimì', 'ją̃', 'jū́sų', 'jamè', 'jų̃', 'manyjè'],
    "macedonian": ['ти', 'јас', 'таа', 'тие', 'вие', 'ние', 'тој'],
    "norvegian": ['de', 'hun', 'han', 'henne', 'dem', 'han, ham', 'seg', 'det', 'vi', 'jeg', 'dere', 'deg', 'den', 'oss', 'meg', 'du'],
    "polish": ['wy', 'on', 'ja', 'my', 'ty', 'ona', 'oni', 'pan'],
    "portuguese": ['nós', 'vós', 'elas', 'eu', 'ele', 'tu', 'eles', 'ela'],
    "romanian": ['dumneaei', 'ei', 'eu', 'ele', 'dvs', 'voi', 'tu', 'dumnealui', 'noi', 'dumnealor', 'dumneavoastră', 'ea', 'el'],
    "russian": ['o ней', 'онa', 'ими', 'мне', 'вами', 'них', 'нами', 'ему', 'тебе', 'нам', 
        'o вас', 'её', 'вас', 'ей', 'они', 'o нас', 'его', 'я', 'меня', 'oбo мне', 'тобой', 
        'него', 'ты', 'тебя', 'неё', 'вам', 'он/оно', 'их', 'o нём', 
        'вы', 'нас', 'мы', 'o тебe', 'мной', 'им', 'о них'],
    "spanish": ['ella', 'vosotros', 'vosotras', 'las', 'usted', 'los', 'nos', 
        'vusted', 'te', 'yo', 'le', 'ellos', 'vustedes', 'os', 'nosotros', 'vuecencia',
        'vuecencias', 'ustedes', 'les', 'ello', 'nosotras', 'vusías', 'ellas', 'me', 
        'la', 'tú', 'se', 'lo', 'vusía', 'él']
}



def _load_dictionary( language ):
    """
    It loads the emotional lexicon for the required languages.

    Required arguments:
    ----------
    
    *language*:
        One of the languages supported by Spacy: 
            Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
            Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.   
    
    Returns:
    ----------
    *lang_df*:
        A pandas dataframe: the table that contains the association < word, emotion >.    
        
    """
    
    if language == 'catalan':
        from langs.catalan import lang_df
        
    elif language == 'chinese':
        from langs.chinese import lang_df
        
    elif language == 'danish':
        from langs.danish import lang_df
        
    elif language == 'dutch':
        from langs.dutch import lang_df
        
    elif language == 'english':
        from langs.english import lang_df
        
    elif language == 'french':
        from langs.french import lang_df
        
    elif language == 'german':
        from langs.german import lang_df
        
    elif language == 'greek':
        from langs.greek import lang_df
        
    elif language == 'italian':
        from langs.italian import lang_df
        
    elif language == 'japanese':
        from langs.japanese import lang_df
        
    elif language == 'lithuanian':
        from langs.lithuanian import lang_df
        
    elif language == 'norwegian':
        from langs.norwegian import lang_df
        
    elif language == 'polish':
        from langs.polish import lang_df
        
    elif language == 'portuguese':
        from langs.portuguese import lang_df
        
    elif language == 'romanian':
        from langs.romanian import lang_df
        
    elif language == 'russian':
        from langs.russian import lang_df
        
    elif language == 'spanish':
        from langs.spanish import lang_df
        
    elif language == 'macedonian':
        from langs.macedonian import lang_df
        
    return lang_df


def load_antonyms(language):
    
    if language == 'catalan':
        from antonyms.catalan import _antonyms
        return _antonyms
    if language == 'chinese':
        from antonyms.chinese import _antonyms
        return _antonyms
    if language == 'danish':
        from antonyms.danish import _antonyms
        return _antonyms
    if language == 'dutch':
        from antonyms.dutch import _antonyms
        return _antonyms
    if language == 'english':
        from antonyms.english import _antonyms
        return _antonyms
    if language == 'french':
        from antonyms.french import _antonyms
        return _antonyms
    if language == 'german':
        from antonyms.german import _antonyms
        return _antonyms
    if language == 'greek':
        from antonyms.greek import _antonyms
        return _antonyms
    if language == 'italian':
        from antonyms.italian import _antonyms
        return _antonyms
    if language == 'japanese':
        from antonyms.japanese import _antonyms
        return _antonyms
    if language == 'lithuanian':
        from antonyms.lithuanian import _antonyms
        return _antonyms
    if language == 'macedonian':
        from antonyms.macedonian import _antonyms
        return _antonyms
    if language == 'norwegian':
        from antonyms.norwegian import _antonyms
        return _antonyms
    if language == 'polish':
        from antonyms.polish import _antonyms
        return _antonyms
    if language == 'portuguese':
        from antonyms.portuguese import _antonyms
        return _antonyms
    if language == 'romanian':
        from antonyms.romanian import _antonyms
        return _antonyms
    if language == 'russian':
        from antonyms.russian import _antonyms
        return _antonyms
    if language == 'spanish':
        from antonyms.spanish import _antonyms
        return _antonyms


def _language_code3(language):
    
    missing = ['russian', 'macedonian', 'german']
    if language in missing:
        return None
    
    if language == 'chinese':
        return 'cmn'
    if language == 'greek':
        return 'ell'
    if language == 'norwegian':
        return 'nno'
    if language == 'romanian':
        return 'ron'
    if language == 'japanese':
        return 'jpn'
    if language == 'dutch':
        return 'nld'
    if language == 'french':
        return 'fra'
    
    ok_lang = ['catalan', 'danish', 'spanish', 'italian', 'polish', 'english', 'lithuanian', 'portuguese']
    if language in ok_lang:
        return language[:3]
    
    return None


def _check_language( language ):
    
     # Check for language
    try:
        allowed_languages = ['catalan', 'chinese', 'danish', 'dutch', 'english', 'french', 'german', 'greek',
                            'japanese', 'italian', 'lithuanian', 'macedonian', 'norwegian', 'polish', 'portuguese',
                            'romanian', 'russian', 'spanish']
        assert language in allowed_languages
    except:
        raise ValueError("'{}' is not allowed as a language. Please specify a language among '{}'.".format(language, "', '".join(allowed_languages)))
    
    return


def _language_correction_tokens(token, language):
    if language == 'italian':
        if "'" in token:
            return token.split("'")[1]
    return token

def _language_correction_text(text, language):
    if language == 'italian':
        return text.replace("'", "o ")
    return text