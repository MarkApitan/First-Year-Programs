# Practical Exam #1
# June 1, 2024

# Suppose that a text file contains a list of integer scores.
# Write a program that reads the scores from the file and calculates the total and the average score.
# Note that the user should be able to enter the filename of the text file.
# Sample Run:
# There are 3 scores
# The total is 297
# The average is 99

# Get the filename from the user
filename = input("Enter a filename: ")

# Open the file
with open(f"{filename}") as f:
    scores = f.read().split()
    total = 0
    count = 0
    # Iterate over each score in the list
    for score in scores:
        total += int(score)
        count += 1

    # Calculate the average by dividing the total by the count
    average = total / count

# Print the number of scores, the total, and the average
print(f"There are {count} scores")
print(f"The total is {total}")
print(f"The average is {average}")