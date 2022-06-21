def main():
    nums = int(input(
        "Введите '2', чтобы посчитать среднее арифметическое без самой плохой оценки: "))
    student = 1
    while nums == 2:
        get_mark(student=student)
        student += 1
        nums = int(input(
            "Введите '2', чтобы посчитать среднее арифметическое без самой плохой оценки, '6' - Чтобы выйти с программы: "))
        if nums == 6:
            break


def get_mark(student):

    total = 0

    marks_of_student = []

    mark = int(input("Введите оценку студента: "))
    marks_of_student.append(mark)

    index_while = int(input("'1' - Введите, чтобы добавить ещё: "))

    while index_while == 1:
        mark = int(input("Введите оценку студента: "))
        marks_of_student.append(mark)
        index_while = int(input("'1' - Введите, чтобы добавить ещё: "))

    marks_of_student.sort()
    # print(marks_of_student)

    if marks_of_student[0] < 3:

        marks_of_student.pop(0)

    print(marks_of_student)

    for marking in marks_of_student:
        total += marking

    length_list = len(marks_of_student)

    average = total / length_list

    print(f"Average of {student} student: {average}")


main()
