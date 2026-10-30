def format_followers(count):
    if count >= 1000000:
        return str(round(count / 1000000, 1)) + "M"
    elif count >= 1000:
        return str(round(count / 1000, 1)) + "K"
    else:
        return str(count)


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

    def display_profile(self):
        print("Username:", self.username)
        print("Followers:", format_followers(self.followers))
        print("Badge:", self.badge)


user1 = VerifiedInfluencer("rahul123", "rahul@gmail.com", 1500000, "Verified")

user1.display_profile()