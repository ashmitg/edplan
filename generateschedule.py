import math


def create_balanced_schedule(courses, qmax, smax):
    average_difficulty = calculate_average_difficulty(courses)*qmax
    course_size = [2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3] #example schedule
    course_size = [qmax if value == 3 else smax for value in course_size]

    chosen_courses = set()

    courses.sort(key=lambda x: (x.category, x.name))
    #sort the courses alphabetically since I assume courses are in order such as Math 1A, Math 1B, Math 1C

    
    num_quarters = len(course_size)

    quarters = [[] for _ in range(num_quarters)]

    for i, course in enumerate(courses):
        for t, quarter in enumerate(quarters):
            if course in chosen_courses:
                continue
            if len(quarter) < course_size[t] and sum(c.difficulty for c in quarter) + course.difficulty <= average_difficulty:
                if not any(c.category == course.category for c in quarter):
                    if course_size[t] == 2 and course.difficulty > 1:
                        continue

                    quarter.append(course)
                    chosen_courses.add(course)
                    break
                elif course.category == "Arts" or course.category == "Humanities" or course.category == "Social Science": #optimization to allow multiple elective classes in a quarter
                    quarter.append(course)
                    chosen_courses.add(course)
                    break

    return quarters

#calculate a total difficulty to ensure courses are maintaned under this threshold
def calculate_average_difficulty(courses_data):
    total_difficulty = 0
    total_courses = len(courses_data)

    for course in courses_data:
        total_difficulty += course.difficulty

    average_difficulty = total_difficulty / total_courses
    return math.ceil(average_difficulty)


