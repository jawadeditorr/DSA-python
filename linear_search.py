"""
LINEAR SEARCH
"""

arr = [5, 3, 8, 2, 7, 1, 6]

def linear_search(arr,query):
    size = len(arr)
    for i in range(size):
        if arr[i]==query:
            return i


print(linear_search(arr,8))