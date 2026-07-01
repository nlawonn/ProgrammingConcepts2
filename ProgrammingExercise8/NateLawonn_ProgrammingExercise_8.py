import os
import csv

HISTORY_FILE = "grades.txt"
CSV_FILE = "grades.csv"

def main():
    students = int(input("How many students are in the class? "))
    
    #Initialize the CSV file with headers before the loop starts
    with open(CSV_FILE, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Exam 1", "Exam 2", "Exam 3"])

    #Loop through each student, get inputs, and immediately write them
    for x in range(students):
        name = input("\nPlease enter the student's name: ")
        exam1 = int(input("Please enter the student's first exam score: "))
        exam2 = int(input("Please enter the student's second exam score: "))
        exam3 = int(input("Please enter the student's third exam score: "))
        
        #Pass the data to save_grades for each student
        save_grades(name, exam1, exam2, exam3)

def save_grades(name, exam1, exam2, exam3):
    #Writes Name and exam scores from main to file
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Exam 1: {exam1}\n")
        f.write(f"Exam 2: {exam2}\n")
        f.write(f"Exam 3: {exam3}\n")
        f.write("-" * 20 + "\n") # Added a separator line for readability

    #Use append so previous students aren't overwritten
    with open(CSV_FILE, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, exam1, exam2, exam3])

if __name__ == "__main__":
    main()