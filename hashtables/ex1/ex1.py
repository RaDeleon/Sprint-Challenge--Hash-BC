#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
                        )

                        # REMOVED NOT USING => hash_table_resize or hash_table_remove


# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

"""
takes in three arguments:
1. weights - a list of integers
2. length - the length of the list
3. limit - the integer to solve for 

What it do?:

1.loop through weights and add them to the hash table. key = weight, value = index
2.look through weights and check, is limit - weight[i] in the ht?
3.ht has linked list functionality so will need to traverse the entries at each index to confirm the above ** retrieve does this for me
4. return the first pair that satisfies these conditions, in ascending index order (i.e. whichever comes first in the array)
"""


# * BRUTE FORCE SOLUTION USED Wit 2 nested loopz

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for k, v in enumerate(weights):
        hash_table_insert(ht, v, k)
        
    for k, v in enumerate(weights):
        difference = limit - v
        if hash_table_retrieve(ht, difference) is not None:
            
            difference_index = hash_table_retrieve(ht, difference)
            
            if difference_index >= k:
                return [difference_index, k]
            else: 
                return [k, difference_index]
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
