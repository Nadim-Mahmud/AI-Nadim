# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:11:14 2020

@author: Nadim Mahmud
"""

import dataprocessingutility as dp

# Loading data

dataset = dp.open_json("D:\Portable\Git reps\Project Facebook","message_1.json")
data = dp.open_json("D:\Portable\Git reps\AI_Message\src", "avrodict.json")

# Seperating usrs message int two lists

user2,user1 = dp.serparate_two_users_message(data = dataset)

#normalization

mp = {}

cn=0

for i in range(0,len(user1)):
    for j in range(0,len(user1[i])):
        tmp = user1[i][j].split()
        for k in range(0,len(tmp)):
            cn += 1
            if mp.get(tmp[k],'AQ') == 'AQ':
                mp[str(tmp[k])] = 1
            else:
                mp[str(tmp[k])] += 1

for i in range(0,len(user2)):
    for j in range(0,len(user2[i])):
        tmp = user2[i][j].split()
        for k in range(0,len(tmp)):
            cn += 1
            if mp.get(tmp[k],'AQ') == 'AQ':
                mp[str(tmp[k])] = 1
            else:
                mp[str(tmp[k])] += 1



    
x = sorted(mp.items(), key = lambda kv:(kv[1], kv[0]),reverse = True)
        





