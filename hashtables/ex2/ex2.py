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
    hashtable = HashTable(length)
    # route = [None] * length
    route = []

    """
    YOUR CODE HERE
    """

     #ran into many errors
    # Implementation #1
    #  Get the tickets into the HT, key = source and val = destination
    # for i in tickets:
    #     if i.source is "NONE": 
    #         hash_table_insert(hashtable, "home", i.destination)
    #     else:
    #         hash_table_insert(hashtable, i.source, i.destination)

    # start = "home"

    # for i in range(0, len(route)):
    #     dest = hash_table_retrieve(hashtable, start)

    #     route[i] = dest
    #     start = dest

    # return route

    # Implementation #2
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    starting = hash_table_retrieve(hashtable, 'NONE')
    route.append(starting)

    for _ in range(1, len(tickets)):
        next_location = hash_table_retrieve(hashtable, starting)
        starting = next_location
        route.append(next_location)

    return route


tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG")
]

reconstruct_trip(tickets, len(tickets))