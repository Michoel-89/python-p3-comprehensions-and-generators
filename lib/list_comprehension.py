#!/usr/bin/env python3

def return_evens(num_list):
    
    list_comprehension = [n for n in num_list if n % 2 == 0]
    return list_comprehension

def make_exclamation(sentence_list):
    if(len(sentence_list) == 0):
        return []
    else:
        list_comprehension = [n+'!' for n in sentence_list]
        return list_comprehension