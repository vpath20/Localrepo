if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


    def calculate_average_marks(student_marks, query_name):
        if query_name in student_marks:
            marks = student_marks[query_name]
            average_marks = sum(marks) / len(marks)
            return average_marks
        else:
            return "Student not found"


    result = calculate_average_marks(student_marks, query_name)
    print("{:.2f}".format(result))