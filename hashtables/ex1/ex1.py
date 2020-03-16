#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in weights[0:length-1]:
        zeroth = weights.index(i)
        for j in weights[1:]:
            first = weights.index(j)
            if  hash_table_retrieve(ht, i + j) == limit:
                answer = (zeroth, first)
            else:
                answer = None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
