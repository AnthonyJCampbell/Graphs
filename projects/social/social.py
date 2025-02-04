import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        
        
        # The number of users must be greater than the average number of friendships.
        if numUsers <= avgFriendships:
            print("Didn't you read the spec, dummy? Number of users should be greater than the average number of friendships!")
            return 

        # Add users
        for user_id in range(numUsers):
            self.addUser(user_id)

        # Create friendships
        # Create list of all possible combinations
        possible_friendships = []

        for i in range(1,numUsers+1):
            for j in range(1,numUsers+1):
                if j != i:
                    possible_friendships.append([i,j])
        
        # print(possible_friendships)

        # Shuffle the list
        for i in range(0, len(possible_friendships)):
            random_index = random.randint(i, len(possible_friendships) - 1)
            possible_friendships[random_index], possible_friendships[i] = possible_friendships[i], possible_friendships[random_index]

        # print(possible_friendships)
        num_friendships = int((numUsers * avgFriendships) / 2)
        limited_list = possible_friendships[:num_friendships]
        # print(limited_list)

        for pair in limited_list:
            # print(pair)
            userID = pair[0]
            friendID = pair[1]
            self.addFriendship(userID, friendID)

    def getAllSocialPaths(self, userID):
        visited = {}  # Note that this is a dictionary, not a set
        visited[userID] = [userID]
        # print(visited)
        qq = []
        qq.append([userID])
        
        print(f"Starting list of friendships is {self.friendships}")

        # Take the user id and see what it's friends are
        # While len(queueueueueue) > 0:
        while len(qq) > 0:
            path = qq.pop(0)
            current_friend = path[-1]

            # For every friend found in self.friendships for current_friend
            for friend in self.friendships[current_friend]:
                # If !visited[friend]
                if friend not in visited:
                    print(friend)
                    visited[friend] = path
                    # Add it to visited with the path it took you to get there
                    new_path = list(path)
                    new_path.append(friend)
                    qq.append(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
    pass
