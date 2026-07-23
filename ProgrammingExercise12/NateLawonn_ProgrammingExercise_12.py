import numpy as np

def main():
    data = np.genfromtxt('grades.csv', delimiter=',', skip_header=1, dtype=None, encoding='utf-8')

    print("Array Shape:", data.shape)
    print("First 3 rows:\n", data[:3])

    all_grades = []
    name = data['f0']
    exam1_grades = data['f1']
    exam2_grades = data['f2']
    exam3_grades = data['f3']
    exam_1(exam1_grades)
    exam_2(exam2_grades)
    exam_3(exam3_grades)
    all_grades.append(exam1_grades)
    all_grades.append(exam2_grades)
    all_grades.append(exam3_grades)
    exam_totals(all_grades)
    return exam1_grades, exam2_grades, exam3_grades, all_grades

def exam_1(exam1_grades):
    passed = np.sum(exam1_grades >= 60)
    failed = len(exam1_grades) - passed
    print("Exam 1 Grades:", exam1_grades)
    print("Average for Exam 1:", np.mean(exam1_grades))
    print("Highest grade on Exam 1:", np.max(exam1_grades))
    print("Lowest grade on Exam 1:", np.min(exam1_grades))
    print("Median grade of Exam 1:", np.median(exam1_grades))
    print(f"Standard deviation of Exam 1: {np.std(exam1_grades):.2f}")
    print(f"Passed: {passed} students")
    print(f"Failed: {failed} students")
    print()
    return exam1_grades

def exam_2(exam2_grades):
    print("Exam 2 Grades:", exam2_grades)
    print("Average for Exam 2:", np.mean(exam2_grades))
    print("Highest grade on Exam 2:", np.max(exam2_grades))
    print("Lowest grade on Exam 2:", np.min(exam2_grades))
    print("Median grade of Exam 2:", np.median(exam2_grades))
    print(f"Standard deviation of Exam 2: {np.std(exam2_grades):.2f}")
    passed = np.sum(exam2_grades >= 60)
    failed = len(exam2_grades) - passed
    print(f"Passed: {passed} students")
    print(f"Failed: {failed} students")
    print()
    return exam2_grades

def exam_3(exam3_grades):
    print("Exam 3 Grades:", exam3_grades)
    print("Average for Exam 3:", np.mean(exam3_grades))
    print("Highest grade on Exam 3:", np.max(exam3_grades))
    print("Lowest grade on Exam 3:", np.min(exam3_grades))
    print("Median grade of Exam 3:", np.median(exam3_grades))
    print(f"Standard deviation of Exam 3: {np.std(exam3_grades):.2f}")
    passed = np.sum(exam3_grades >= 60)
    failed = len(exam3_grades) - passed
    print(f"Passed: {passed} students")
    print(f"Failed: {failed} students")
    print()
    return exam3_grades

def exam_totals(all_grades):
    all_grades_np = np.array(all_grades)
    print(f"Average of all exams: {np.mean(all_grades):.1f}")
    print("Highest grade of all exams:", np.max(all_grades))
    print("Lowest grade of all exams:", np.min(all_grades))
    print("Median grade of all exams:", np.median(all_grades))
    print(f"Standard deviation of all exams: {np.std(all_grades):.2f}")
    total_passed = np.sum(all_grades_np >= 60)
    total_grades_count = all_grades_np.size
    pass_percentage = (total_passed / total_grades_count) * 100
    print(f"Overall pass percentage across all exams: {pass_percentage:.1f}%\n")
    return all_grades

if __name__ == "__main__":
    main()