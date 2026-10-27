def display_friends(friends):
    for username, followers in friends.items():
        print(f"{username}: {followers / 1000:.1f}K followers")


friends = {
    "rahul": 2300,
    "amit": 4500,
    "neha": 1200
}

display_friends(friends)