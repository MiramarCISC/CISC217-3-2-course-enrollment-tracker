"""Course enrollment tracker functions.

Complete the functions below for the Week 3 lab.

This lab practices dictionaries, nested dictionaries, lists stored inside
records, membership checks, dictionary lookups, and returning summary values.
Do not rename the functions or parameters. The tests import these exact names.
"""


def create_tracker():
    """Return a new empty enrollment tracker.

    The tracker should be a dictionary with two top-level keys:
    - "students": maps student IDs to student records
    - "courses": maps course codes to course records
    """
    # TODO: Replace with your implementation.
    return None


def add_student(tracker, student_id, name):
    """Add or update a student record and return the tracker.

    Student records should be stored under tracker["students"].
    Each student record should contain:
    - "name": the student's name
    - "courses": a list of course codes for the courses the student is taking

    If the student already exists, update only the name and keep the course list.
    """
    # TODO: Replace with your implementation.
    return tracker


def enroll_student(tracker, student_id, name, course_code, course_title):
    """Enroll a student in a course and return the tracker.

    This function should:
    - ensure the student exists
    - ensure the course exists
    - add the course code to the student's course list if not already present
    - add the student ID to the course roster if not already present

    Course records should be stored under tracker["courses"].
    Each course record should contain:
    - "title": the course title
    - "roster": a list of student IDs enrolled in the course
    """
    # TODO: Replace with your implementation.
    return tracker


def drop_student(tracker, student_id, course_code):
    """Drop a student from a course and return the tracker.

    Remove the course code from the student's course list and remove the
    student ID from the course roster if those records exist. Missing students
    or courses should not cause an error.
    """
    # TODO: Replace with your implementation.
    return tracker


def get_roster(tracker, course_code):
    """Return a sorted list of student names enrolled in a course.

    If the course does not exist or has no students, return an empty list.
    The returned names should be sorted alphabetically.
    """
    # TODO: Replace with your implementation.
    return []


def find_courses_for_student(tracker, student_id):
    """Return a sorted list of course codes for one student.

    If the student does not exist or has no courses, return an empty list.
    """
    # TODO: Replace with your implementation.
    return []


def student_summary(tracker, student_id):
    """Return a dictionary summary for one student.

    Return a dictionary with these keys:
    - "student_id"
    - "name"
    - "course_count"
    - "courses"

    The "courses" value should be a sorted list of course codes.
    If the student does not exist, return an empty dictionary.
    """
    # TODO: Replace with your implementation.
    return {}


def course_summary(tracker):
    """Return a dictionary mapping course codes to enrollment counts.

    Example return value:
    {
        "CISC217": 3,
        "MATH150": 2,
    }

    The dictionary keys should be course codes and the values should be roster
    counts. Return an empty dictionary if there are no courses.
    """
    # TODO: Replace with your implementation.
    return {}
