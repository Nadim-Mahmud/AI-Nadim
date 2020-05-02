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
    
    user = data['messages'][i]['sender_name']
    name = ""
    data['messages'][i]['sender_name'] == sender_name 
    
    for i in range(0,len(data['messages'])):
        current_sender = data['messages'][i]['sender_name']
        if data['messages'][i]['type'] == 'Generic' and data['messages'][i].get('content','A') != 'A': 
            content = data['messages'][i]['content']
            if user == current_sender:                   
                if current_sender != name:
                    msg1.append([content])
                else :
                    msg1[-1].append(data['messages'][i]['content'])
            else:
                if current_sender != name:
                    msg2.append([data['messages'][i]['content']])
                else :
                    msg2[-1].append(data['messages'][i]['content'])
        else:
            if name == current_sender:
                msg2.append([😶])
            else:
                msg1.append([😶])
        name = data['messages'][i]['sender_name'] 
        
    return (msg1,msg2)    


