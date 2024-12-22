task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

importance = ""
time_sensitive = ""

match priority:
    case "high" if time_bound == "no":
        importance = "is a high priority task."
    case "high" :
        importance = "is a high priority task"
    case "medium" if time_bound == "no":
        importance = "is a medium priority task."
    case "medium":
        importance = "is a medium priority task"
    case "low":
        importance = "is a low priority task."

if time_bound == "yes":
    time_sensitive = "that requires immediate attention today!"
else:
    time_sensitive = "Consider completing it when you have free time."

print(f"{task} {importance} {time_sensitive}")

