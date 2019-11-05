
def earliest_ancestor(ancestors, starting_node):
    # Ancestors is a graph of relationships, a list of (parent, child) pairs i.e. (1, 3) -> 1 is a child of 3
    # We need to return their earliest know ancestor, assuming that every step 'up' has the same weight. Therefore, whichever path has the most 'steps'/edges going up leads to the earliest known ancestor.

    # A reversed version of BFT should lend itself to this. We start at the given starting_node and bubble out on layer.
    # We check if the current ancestor has any known ancestors.
        # If so, we move up one and re-do the checks

    # We'll have to keep track of multiple paths
    # When all paths up have been exhausted, we'll evaluate all paths and return index[-1] of the longest one.
        # If there's > 1 tied for the longest path, return whichever one's ID is lowest.
    
    # If starting_node has no parents, return -1
    

    pass