#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 12:09:56 2021

@author: alfonso
"""

import tweepy
import sys


def tweetsRetriever(username):
    auth = tweepy.OAuthHandler(
        'O9qiJasA7qZy0aY13H5ben5GF', 'vKL8wQykDky7ga4NEV5ta4tTUlYktqcWkTajXL1eKojjvtEWVZ')
    auth.set_access_token('72806677-GjaymBCl8sybBHQ9PPzK89nMqV7NYFalbtQA145Wd',
                          '8CrXIrKQwGViJvt4Wu0ORZvG1mwxOZKb7wDIhpdmjQ6s1')
    api = tweepy.API(auth, wait_on_rate_limit=True)
    tw_handle = username
    texts = []
    for i, tweets in enumerate(tweepy.Cursor(api.user_timeline, id=tw_handle, count=200).pages()):
        texts += [tw._json['text'] for tw in tweets]
        if i == 4: 
            break
    return texts
