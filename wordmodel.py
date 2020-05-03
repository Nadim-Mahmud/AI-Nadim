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
    
    related_words = {}  
    
    def __init__(self, type):
        self.typ = type    
    
    def count_associativity(incoming,response):
        

        import dataprocessingutility as dp 
        # Loading data 
        dataset = dp.open_json("D:\Portable\Git reps\Project Facebook","message_1.json")        
        user2,user1 = dp.serparate_two_users_message(data = dataset)
        incoming = user2
        response = user1
        related_words = {}  
        cn=0
        
        # iterating throw incoming message
        for i in range(0,len(incoming)):
            for j in range(0,len(incoming[i])):
                tmp_incoming_words = incoming[i][j].lower().split()
                for k in range(0,len(tmp_incoming_words)):
                    # iterating throw response 
                    for l in range(0,len(response[i])):
                        tmp_response_words = response[i][l].lower().split()
                        for m in tmp_response_words:
                            if related_words.get(tmp_incoming_words[k],'_nOtFound_') =='_nOtFound_': 
                                dictionary_initizer = {}
                                dictionary_initizer[m] = 1
                                related_words[tmp_incoming_words[k]] = [dictionary_initizer]
                            else:
                                if related_words[tmp_incoming_words[k]].get(m,'_nOtFound_') =='_nOtFound_':
                                    dictionary_initizer = {}
                                    dictionary_initizer[m] = 1
                                    related_words[tmp_incoming_words[k]] = [dictionary_initizer]
                                else:
                                   related_words[tmp_incoming_words[k]][m] += 1
        return WordModel.related_words


























                        
                    