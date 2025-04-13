#Toni Bethune

#03152025

#P4HW1

#User enters grades and createa loop to collect the number of scores user want to enter.
#Evaluating if the score is valid. Provides an average of the scores and a letter grade. 





# Create an empty list to store scores
scores = []

# Ask how many scores to enter
num = int(input("How many scores do you want to enter? "))

# Loop to collect valid scores
for i in range(1, num + 1):
    score = float(input(f"Enter score #{i}: "))
    while score < 0 or score > 100:
        print("Invalid score! Enter a value between 0 and 100.")
        score = float(input(f"Enter score #{i} again: "))
    scores.append(score)

# Drop the lowest score
lowest = min(scores)
scores.remove(lowest)

# Calculate average
average = sum(scores) / len(scores)

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n---- Results ----")
print("Lowest Score:", lowest)
print("Scores After Drop:", scores)
print("Average Score:", round(average, 2))
print("Letter Grade:", grade)
