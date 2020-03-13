#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    # insert all tickets in a hash table
    for ticket in tickets:
    #  insert first ticket
        if ticket.source == "NONE":
            route[0] = ticket.destination
        hash_table_insert(ht, ticket.source, ticket.destination) 

    # insert tickets in order, skipping first
    for index in range(len(route) - 1):
        route[index + 1] = hash_table_retrieve(ht, route[index])
    
    return route

