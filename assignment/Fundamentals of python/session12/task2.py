def format_follower_count(count):
    if count >= 1000000:
        return f"{count / 1000000:.1f}M"
    elif count >= 1000:
        return f"{count / 1000:.1f}K"
    else:
        return str(count)


print(format_follower_count(1500))
print(format_follower_count(1200000))
print(format_follower_count(850))