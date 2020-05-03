# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:11:52 2020

@author: Nadim Mahmud
"""


# Read Json Data

import json
import re
from functools import partial
import os

def open_json(subdir,file_name):
        
    fix_mojibake_escapes = partial(
         re.compile(rb'\\u00([\da-f]{2})').sub,
         lambda m: bytes.fromhex(m.group(1).decode()))
    
    with open(os.path.join(subdir, file_name), 'rb') as binary_data:
        repaired = fix_mojibake_escapes(binary_data.read())
        
    data = json.loads(repaired.decode('utf8'))      
    return data


# Separate Messages accoding to users
    
def serparate_two_users_message(data):
    
    msg1 = []
    msg2 = []
    
    user_one = data['messages'][0]['sender_name']
    previous_sender = ""

    for i in range(len(data['messages'])-1,0,-1):
        current_sender = data['messages'][i]['sender_name']
        if data['messages'][i]['type'] == 'Generic' and data['messages'][i].get('content','Mark') != 'Mark': 
            content = data['messages'][i]['content']
        else:
            content = ' :) '
        if user_one == current_sender:                   
            if current_sender != previous_sender:
                msg1.append([content])
            else :
                msg1[-1].append(content)
        else:
            if current_sender != previous_sender:
                msg2.append([content])
            else :
                msg2[-1].append(content)
        previous_sender = current_sender
        
    return (msg1,msg2)    

# Checking bangla word using unicode range

def is_bangla_word(word):
    for i in word:
        if 'ঀ' <= i <= '৿':
            return True
    return False
             






