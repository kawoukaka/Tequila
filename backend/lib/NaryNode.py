class NaryNode:
    def __init__(self, name, position,team):
        self.name = name
        self.position = position
        self.team = team
        self.followers = []
    def add_follower(self, follower):
        self.followers.append(follower)
    # Return a string representation of the node and its followers.
    def __str__(self):
        result = f'{self.name}:'
        for follower in self.followers:
            result += f' {follower.name}'
        return result