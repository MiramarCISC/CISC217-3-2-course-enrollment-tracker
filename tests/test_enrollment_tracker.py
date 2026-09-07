from cisc217_week3.enrollment_tracker import (
    add_student,
    course_summary,
    create_tracker,
    drop_student,
    enroll_student,
    find_courses_for_student,
    get_roster,
    student_summary,
)


def test_create_tracker_has_students_and_courses():
    tracker = create_tracker()

    assert isinstance(tracker, dict)
    assert tracker == {"students": {}, "courses": {}}


def test_add_student_creates_nested_student_record():
    tracker = create_tracker()
    add_student(tracker, "s001", "Ada Lovelace")

    assert tracker["students"]["s001"]["name"] == "Ada Lovelace"
    assert tracker["students"]["s001"]["courses"] == []


def test_add_student_updates_name_without_erasing_courses():
    tracker = create_tracker()
    enroll_student(tracker, "s001", "Ada", "CISC217", "Intermediate Python")
    add_student(tracker, "s001", "Ada Lovelace")

    assert tracker["students"]["s001"]["name"] == "Ada Lovelace"
    assert tracker["students"]["s001"]["courses"] == ["CISC217"]


def test_enroll_student_creates_student_and_course_records():
    tracker = create_tracker()
    enroll_student(tracker, "s001", "Ada Lovelace", "CISC217", "Intermediate Python")

    assert tracker["students"]["s001"] == {
        "name": "Ada Lovelace",
        "courses": ["CISC217"],
    }
    assert tracker["courses"]["CISC217"] == {
        "title": "Intermediate Python",
        "roster": ["s001"],
    }


def test_enroll_student_does_not_duplicate_course_or_roster_entry():
    tracker = create_tracker()
    enroll_student(tracker, "s001", "Ada Lovelace", "CISC217", "Intermediate Python")
    enroll_student(tracker, "s001", "Ada Lovelace", "CISC217", "Intermediate Python")

    assert tracker["students"]["s001"]["courses"] == ["CISC217"]
    assert tracker["courses"]["CISC217"]["roster"] == ["s001"]


def test_get_roster_returns_sorted_student_names():
    tracker = create_tracker()
    enroll_student(tracker, "s002", "Grace Hopper", "CISC217", "Intermediate Python")
    enroll_student(tracker, "s001", "Ada Lovelace", "CISC217", "Intermediate Python")
    enroll_student(tracker, "s003", "Linus Torvalds", "CISC217", "Intermediate Python")

    assert get_roster(tracker, "CISC217") == [
        "Ada Lovelace",
        "Grace Hopper",
        "Linus Torvalds",
    ]


def test_get_roster_returns_empty_list_for_missing_course():
    tracker = create_tracker()

    assert get_roster(tracker, "DOESNOTEXIST") == []


def test_find_courses_for_student_returns_sorted_course_codes():
    tracker = create_tracker()
    enroll_student(tracker, "s001", "Ada Lovelace", "MATH150", "Calculus")
    enroll_student(tracker, "s001", "Ada Lovelace", "CISC217", "Intermediate Python")

    assert find_courses_for_student(tracker, "s001") == ["CISC217", "MATH150"]


def test_find_courses_for_student_returns_empty_list_for_missing_student():
    tracker = create_tracker()

    assert find_courses_for_student(tracker, "missing") == []


def test_drop_student_removes_both_sides_of_enrollment():
    tracker = create_tracker()
    enroll_student(tracker, "s001", "Ada Lovelace", "CISC217", "Intermediate Python")
    enroll_student(tracker, "s001", "Ada Lovelace", "MATH150", "Calculus")

    drop_student(tracker, "s001", "CISC217")

    assert tracker["students"]["s001"]["courses"] == ["MATH150"]
    assert tracker["courses"]["CISC217"]["roster"] == []


def test_drop_student_ignores_missing_records():
    tracker = create_tracker()

    assert drop_student(tracker, "missing", "CISC217") == tracker


def test_student_summary_returns_expected_dictionary():
    tracker = create_tracker()
    enroll_student(tracker, "s001", "Ada Lovelace", "MATH150", "Calculus")
    enroll_student(tracker, "s001", "Ada Lovelace", "CISC217", "Intermediate Python")

    assert student_summary(tracker, "s001") == {
        "student_id": "s001",
        "name": "Ada Lovelace",
        "course_count": 2,
        "courses": ["CISC217", "MATH150"],
    }


def test_student_summary_returns_empty_dictionary_for_missing_student():
    tracker = create_tracker()

    assert student_summary(tracker, "missing") == {}


def test_course_summary_maps_course_codes_to_counts():
    tracker = create_tracker()
    enroll_student(tracker, "s001", "Ada Lovelace", "CISC217", "Intermediate Python")
    enroll_student(tracker, "s002", "Grace Hopper", "CISC217", "Intermediate Python")
    enroll_student(tracker, "s001", "Ada Lovelace", "MATH150", "Calculus")

    assert course_summary(tracker) == {
        "CISC217": 2,
        "MATH150": 1,
    }
