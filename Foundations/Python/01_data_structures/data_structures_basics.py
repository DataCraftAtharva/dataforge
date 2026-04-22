# -------------------------------
# LIST OPERATIONS (REAL USAGE)
# -------------------------------
print("--LIST OPERATIONS (REAL USAGE)--")
user_events = ["click", "view", "click"]
#Access
print("First event:",user_events[0])

#Add
user_events.append("purchase")

#Remove
user_events.remove("click")

#Iterate

for event in user_events:
    print("Event:",event)

print("Final List",user_events)


# -------------------------------
# DICTIONARY OPERATIONS
# -------------------------------
print("--DICTIONARY OPERATIONS--")
event_count = {}
# Add / update
event_count["click"] = 1
event_count["view"] = 2

# Access
print(event_count["click"])

#Iterate

for key,value in event_count.items():
    print(key,value)