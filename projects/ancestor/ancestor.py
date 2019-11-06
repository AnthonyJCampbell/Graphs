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


def earliest_ancestor(ancestors, starting_node):
    # Ancestors is a graph of relationships, a list of (parent, child) pairs i.e. (1, 3) -> 1 is a child of 3. i.e. [(1, 3), (2,3), (3,6), etc.]

    # We need to return their earliest know ancestor, assuming that every step 'up' has the same weight. Therefore, whichever path has the most 'steps'/edges going up leads to the earliest known ancestor.

    # A reversed version of BFT should lend itself to this. We start at the given starting_node and bubble out on layer.
    # We check if the current ancestor has any known ancestors.
        # If so, we move up one and re-do the checks

    # We'll have to keep track of multiple paths
    # When all paths up have been exhausted, we'll evaluate all paths and return index[-1] of the longest one.
        # If there's > 1 tied for the longest path, return whichever one's ID is lowest.
    

    # For every ancestor
        # Then move to those places

    
    # Conditional to proceed with the rest of the functionality
    found_any_ancestors = False
    # Check if starting_node has parents
    # If starting_node has no parents, return -1
    for ancestor in ancestors:
        # Look for ancestors who have starting_node as a child, thereby making them ancestors
        if ancestor[1] == starting_node:
            found_any_ancestors = True
    
    if found_any_ancestors is False:
        print(f"I'm afraid {starting_node} has no ancestors that we know off. Perhaps he just popped into existence?")
        return -1

    qq = Queue()
    qq.enqueue([starting_node])
    dead_ends = []

    # We want to cover all possible permutations, so we want to keep going until the entire queueueueueueue is empty
    while qq.size() > 0:
        # Deque the path
        lineage = qq.dequeue()
        # print(lineage)

        # Take the last ancestor/vertex of the path, since we're going to be looking for its ancestors.

        current_ancestor = lineage[-1]
        # For every ancestor, we want to check if someone has the current_ancestor as a child, thereby making them the ancestor
        found_any_new_ancestors = False

        for ancestor in ancestors:
            # If anyone has the current node as a child
            if ancestor[1] == current_ancestor:
                # set found_any to True, so we can proceed after the loop
                found_any_new_ancestors = True
                next_lineage = list(lineage)
                next_lineage.append(ancestor[0])
                qq.enqueue(next_lineage)
                # print(qq.queue)

        if found_any_new_ancestors == False:
            dead_ends.append(lineage)
            continue
        
    # Once we've finished the loop and have gone through all possible ancestors
    # Find the longest list/lineage in our dead_ends list
    
    longest_length = 0
    storage = []

    for lineage in dead_ends:
        # print(lineage)
        # print(longest_length)
        # print(len(lineage))
        # if len(lineage) > longest_length, the previous strorage list has become useless so should be reinitialized
        if len(lineage) > longest_length:
            storage = []
            longest_length = len(lineage)
            storage.append(lineage[-1])
            continue

        # If length of current lineage is the same as the values that are already in the storage list, we should just add them. (Since they're both equally long)
        elif len(lineage) == longest_length:
            # Store [-1] of each of the longest in a list
            storage.append(lineage[-1])

    # print(storage)
    # If we've found more than once, return the smallest one
    lowest_ancestor = min(storage)
    print(lowest_ancestor)
    return lowest_ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 6)


