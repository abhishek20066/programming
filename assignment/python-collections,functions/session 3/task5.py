def video_views(titles, views):
    return [(title, round(count, -3)) for title, count in zip(titles, views)]


titles = ["Python Tutorial", "Django Tutorial", "SQL Tutorial"]
views = [12450, 27890, 45320]

result = video_views(titles, views)

print(result)