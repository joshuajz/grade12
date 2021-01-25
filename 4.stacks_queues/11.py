def ask_course():
    return input("Course: ")


def main():
    courses = []
    for i in range(5):
        courses.append(ask_course())

    print(courses)
    popped = courses.pop()
    print(courses)
    return popped


main()
