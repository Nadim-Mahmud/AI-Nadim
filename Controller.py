# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:11:14 2020

@author: Nadim Mahmud
"""

import dataprocessingutility as dp

# Loading data

dataset = dp.open_json("D:\Portable\Git reps\Project Facebook","message_1.json")

# Seperating usrs message int two lists

user2,user1 = dp.serparate_two_users_message(data = dataset)

#normalization

x = "ঊনচিল্লশ"

for i in x:
    print(i)

print((ord('ল')  -ord( 'ন')))
