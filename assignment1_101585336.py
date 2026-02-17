"""
Author: Rene Vincent Quiambao
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" # str
preffered_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # bool

# Step c: Create a dictionary named workout_stats
# This is a dictionary containing strings(names) mapped to tuples(time spent on exercises)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (50, 20, 30),
    "Taylor": (15, 45, 35)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for member in list(workout_stats):
    total = sum(workout_stats[member])
    workout_stats[f"{member}_Total"] = total

# Step e: Create a 2D nested list called workout_list
# This is a list that will have lists appended to it (making a 2D list)
workout_list = []

for times in workout_stats.values():
    if isinstance(times, tuple):
        workout_list.append(list(times))

# Step f: Slice the workout_list
for times in workout_list:
    yoga_run = times[0:2]
    print(yoga_run)

for times in workout_list[-2:]:
    weightlifting = times[2]
    print(weightlifting)

# Step g: Check if any friend's total >= 120
for member in workout_stats:
    if isinstance(workout_stats[member], int) and workout_stats[member] >= 120:
        print(f"Great job staying active, {member}!")

# Step h: User input to look up a friend
search = input("Please enter a name to search: ")

if search in workout_stats:
    print(f"Minutes per activity: {workout_stats[search]}")
    print(f"Total time: {workout_stats[f'{search}_Total']}")
else:
    print(f"Friend {search} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
min = 1000
min_name = ""
max = -1
max_name = ""

for member, time in workout_stats.items():
    if isinstance(time, int):
        if time > max:
            max = time
            max_name = member
        if time < min:
            min = time
            min_name = member

print(f"Member with highest total workout minutes: {max_name.replace('_Total', '')}")
print(f"Member with lowest total workout minutes: {min_name.replace('_Total', '')}")