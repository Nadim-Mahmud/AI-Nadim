# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:11:14 2020

@author: Nadim Mahmud
"""

import dataprocessingutility as dp

# Loading data

dataset = dp.open_json("D:\Portable\Git reps\Project Facebook","message_1.json")

# Seperating usrs message int two lists

incoming,response = dp.serparate_two_users_message(data = dataset)


from wordmodel import WordModel as wd
wd.fit(incoming,response)
stored = wd.count_associativity()

#print(wd.response)

print(wd.replay('hi', 10))


