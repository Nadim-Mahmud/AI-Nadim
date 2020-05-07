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
    
    connected_words = {}
    
    
    def __init__(self, type):
        self.typ = type    
    
    def count_associativity(incoming,response):
        
        # iterating throw incoming message
        for i in range(0,len(incoming)):
            for j in range(0,len(incoming[i])):
                tmp_incoming_words = incoming[i][j].lower().split()
                for k in range(0,len(tmp_incoming_words)):
                    # iterating throw response 
                    for l in range(0,len(response[i])):
                        tmp_response_words = response[i][l].lower().split()
                        for m in tmp_response_words:
                            if WordModel.connected_words.get(tmp_incoming_words[k],'_nOtFound_') =='_nOtFound_': 
                                WordModel.connected_words[tmp_incoming_words[k]] = []
                                WordModel.connected_words[tmp_incoming_words[k]].append([m])
                                WordModel.connected_words[tmp_incoming_words[k]].append([1])
                            else:
                                if m not in WordModel.connected_words[tmp_incoming_words[k]][0]:
                                    WordModel.connected_words[tmp_incoming_words[k]][0].append(m)
                                    WordModel.connected_words[tmp_incoming_words[k]][1].append(1)
                                else:
                                    index = WordModel.connected_words[tmp_incoming_words[k]][0].index(m)
                                    WordModel.connected_words[tmp_incoming_words[k]][1][index] += 1
        return WordModel.related_words


























                        
                    