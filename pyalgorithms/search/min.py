# min.py
#
# Implemented function for minimals search algorithm.
# Jakub Kopiszka (c) 2026

def min(arr: list):
    min_val = arr[0]
    
    for i in arr:
        min_val = i if i < min_val else min_val
        
    return min_val