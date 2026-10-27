scores = {}

scores.setdefault("CSK", {})
scores["CSK"]["Dhoni"] = 45
scores["CSK"]["Ruturaj"] = 60
scores["CSK"]["Jadeja"] = 30

scores.setdefault("MI", {})
scores["MI"]["Rohit"] = 70
scores["MI"]["Surya"] = 55
scores["MI"]["Hardik"] = 25

print("Rohit ke runs:", scores["MI"]["Rohit"])