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
    
    def count_associativity(self,incoming,response):
        
        # iterating throw incoming message
        for i in range(0,len(incoming)):
            for j in range(0,len(incoming[i])):
                tmp_incoming_words = incoming[i][j].split()
                for k in range(0,len(tmp_incoming_words)):
                    # iterating throw response 
                    for l in range(0,len(response[i])):
                        tmp_response_words = response[i][l].split()
                        for m in tmp_response_words:
                            if self.related_words.get(tmp_incoming_words[k],'_nOtFound_') =='_nOtFound_':
                                self.related_words[tmp_incoming_words[k]] = m
                                self.related_words[tmp_incoming_words][m] = 1
                            else:
                                if self.related_words[tmp_incoming_words].get(m,'_nOtFound_') =='_nOtFound_':
                                    self.related_words[tmp_incoming_words][m] = 1
                                else:
                                    self.related_words[tmp_incoming_words][m] += 1
                                


























                        
                    