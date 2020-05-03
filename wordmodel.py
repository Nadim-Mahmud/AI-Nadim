# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:21:03 2020

@author: Nadim Mahmud
"""

"""
    defining my won fun model.... whiched i named count and associate
    it mainly count the replay word association with a response ...
    when a response come it will replay accordinly accordingly word count rank
"""

class WordModel:
    related_word = {}
    
    def count_associativity(incoming,response):
        # iterating throw incoming message
        for i in range(0,len(user1)):
            for j in range(0,len(user1[i])):
                tmp = user1[i][j].split()
                for k in range(0,len(tmp)):
                    