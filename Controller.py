# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:11:14 2020

@author: Nadim Mahmud
"""

import dataprocessingutility as dp

# Loading data
directory = "D:\Portable\Git reps\Project Facebook"
message_title = "message_1.json"

dataset = dp.open_json(directory,message_title)

# Seperating usrs message int two lists

incoming,response = dp.serparate_two_users_message(data = dataset)


# Fitting and using model

from wordmodel import WordModel as wd
wd.fit(incoming,response,1)
stored = wd.count_associativity()

print(wd.replay('mara kha', 10)[0])

x = wd.response

y = (stored['ki'])
