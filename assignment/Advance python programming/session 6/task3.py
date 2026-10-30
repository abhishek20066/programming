class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge


user1 = VerifiedInfluencer("rahul123", "rahul@gmail.com", 15000, "Blue Tick")

print("Username:", user1.username)
print("Email:", user1.email)
print("Followers:", user1.followers)
print("Badge:", user1.badge)