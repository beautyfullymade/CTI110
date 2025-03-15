#Toni Bethune

#03152025

#P2HW2

#Write a program that allow users to enter grades for test.



#Pseudocode:
#Initialize an empty list named grades_list.
#Prompt the user to enter grades for six modules, one by one.
#Store each entered grade in the grades_list.
#Convert each input into a floating-point number before storing.
#Calculate:
#The lowest grade using the min() function.
#The highest grade using the max() function.
#The sum of all grades using the sum() function.
#The average by dividing the sum of grades by the number of grades.
#Display the results with correct formatting:
#"Lowest Grade:" followed by the lowest grade.
#"Highest Grade:" followed by the highest grade.
#"Sum of Grades:" followed by the total sum.
#"Average:" followed by the calculated average formatted to 2 decimal places.
#Ensure output matches the given formatting.

# Initialize an empty list to store grades
grades_list = []

# Requesting grades from user
grades_list.append(float(input("Enter grade for Module 1: ")))
grades_list.append(float(input("Enter grade for Module 2: ")))
grades_list.append(float(input("Enter grade for Module 3: ")))
grades_list.append(float(input("Enter grade for Module 4: ")))
grades_list.append(float(input("Enter grade for Module 5: ")))
grades_list.append(float(input("Enter grade for Module 6: ")))

# Calculate required values
lowest_grade = min(grades_list)
highest_grade = max(grades_list)
sum_of_grades = sum(grades_list)
average_grade = sum_of_grades / len(grades_list)

# Display the results with correct formatting
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest_grade:.1f}")
print(f"Highest Grade:     {highest_grade:.1f}")
print(f"Sum of Grades:     {sum_of_grades:.1f}")
print(f"Average:           {average_grade:.2f}")
print("--------------------------------")
