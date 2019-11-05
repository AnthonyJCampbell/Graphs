
def earliest_ancestor(ancestors, starting_node):
    # Ancestors is a graph of relationships, a list of (parent, child) pairs i.e. (1, 3) -> 1 is a child of 3. i.e. [(1, 3), (2,3), (3,6), etc.]

    # We need to return their earliest know ancestor, assuming that every step 'up' has the same weight. Therefore, whichever path has the most 'steps'/edges going up leads to the earliest known ancestor.

    # A reversed version of BFT should lend itself to this. We start at the given starting_node and bubble out on layer.
    # We check if the current ancestor has any known ancestors.
        # If so, we move up one and re-do the checks

    # We'll have to keep track of multiple paths
    # When all paths up have been exhausted, we'll evaluate all paths and return index[-1] of the longest one.
        # If there's > 1 tied for the longest path, return whichever one's ID is lowest.
    
    # If starting_node has no parents, return -1

    # For every ancestor
        # Look for places where ancestor[1] is current ancestor
        # Then move to those places
    print(ancestors[-1])






    pass

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 2)



class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
