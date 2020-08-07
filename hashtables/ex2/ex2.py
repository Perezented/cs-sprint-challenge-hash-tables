#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    locations = {}
    for i in tickets:
        if i.source == 'NONE':
            route.append(i.destination)
        else:
            locations[i.source] = i.destination
    for i in route:
        if i in locations:
            route.append(locations[i])

    return route
