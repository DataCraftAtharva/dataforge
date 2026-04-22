# -------------------------------
# REAL AGGREGATION SYSTEM
# -------------------------------

user_events = ["click", "view", "click", "purchase", "click"]

event_count={}

for event in user_events:
    if event in event_count:
        event_count[event]+=1
    else:
        event_count[event]=1
print("Aggregated result:", event_count)