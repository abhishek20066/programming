call_durations = (12, 5, 0, 20, 7, 3, 15)

duration_list = list(call_durations)

duration_list = [time for time in duration_list if time >= 5]

call_durations = tuple(duration_list)

print(call_durations)