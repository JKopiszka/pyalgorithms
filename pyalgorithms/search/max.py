# max.py
#
# Implemented function for maximals search algorithm.
# Jakub Kopiszka (c) 2026

def max(arr: list):
    max_val = arr[0]
    
    for i in arr:
        max_val = i if i > max_val else max_val
        
    return max_val