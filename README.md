# CISC 217 Week 3 Lab: Course Enrollment Tracker

## Weekly Topic

Dictionaries and nested collections.

## Lab Summary

In this lab, you will implement a small course enrollment tracker. You will use dictionaries to look up students and courses, lists to store enrolled courses and rosters, and nested dictionaries to represent related records.

You will complete the code in:

```text
src/cisc217_week3/enrollment_tracker.py
```

Do **not** change function names, parameter names, file names, or test file names unless your instructor tells you to. The tests and Classroom50 autograder import these exact functions.

## Learning Goals

By the end of this lab, you should be able to:

- Create and update Python dictionaries.
- Use dictionary keys for fast lookups.
- Store nested records using dictionaries inside dictionaries.
- Store lists inside dictionary records.
- Check membership before adding duplicate values.
- Return useful summary dictionaries.
- Run `pytest` before committing and pushing your work.
- Submit a clear Canvas lab post with GitHub evidence.
- Complete peer review through a GitHub pull request.

## Development Workflow: Classroom50 + GitHub + NRP JupyterHub

Use the table below as a checklist. Some steps happen in GitHub or Classroom50 in your browser; other steps use shell commands in the NRP JupyterHub terminal.

| Step Description | Shell Command or Browser Action |
|---|---|
| Open the Classroom50 assignment link from this Canvas module and accept the assignment. | Use the Classroom50 assignment link in Canvas. |
| Open your assignment repository. After accepting the assignment, click **Go to your GitHub repository** and keep that browser tab open. | Browser action: **Go to your GitHub repository** |
| Open NRP JupyterHub. | Browser action: open <https://sdccd-jupyterhub.nrp-nautilus.io/> |
| Start your JupyterHub server using the course settings. | Browser settings: **0 GPUs, 2 CPU cores, 4 GB Memory, Stack Minimal** |
| If you have not already connected JupyterHub to GitHub with SSH, generate an SSH key in a JupyterHub terminal. Press **Enter** three times to use the default location and skip a passphrase. | `ssh-keygen -t ed25519` |
| Print and copy your SSH public key. Copy the full line that starts with `ssh-ed25519`. | `cat ~/.ssh/id_ed25519.pub` |
| Add the SSH public key to your GitHub account. | Browser action: GitHub **Settings → SSH and GPG keys → New SSH key** at <https://github.com/settings/keys> |
| Copy the SSH clone URL from your assignment repository. Make sure you choose **SSH**, not HTTPS. | Browser action: GitHub repo **Code → SSH → Copy URL** |
| Clone your Classroom50 assignment repository into JupyterHub. Replace `PASTE_YOUR_SSH_CLONE_URL_HERE` with the SSH URL copied from GitHub. | `cd ~/`<br>`git clone PASTE_YOUR_SSH_CLONE_URL_HERE`<br>`cd REPOSITORY_FOLDER_NAME` |
| Confirm that you are in the repository root folder. You should see files such as `README.md`, `pyproject.toml`, `src`, and `tests`. | `pwd`<br>`ls` |
| Create and activate a virtual environment. | `python -m venv .venv`<br>`source .venv/bin/activate` |
| Install the project and test tools. | `python -m pip install -e .[test]` |
| Run the tests before editing so you can see what currently fails. | `python -m pytest -q` |
| Edit only the permitted source file for this lab. | `src/cisc217_week3/enrollment_tracker.py` |
| Run tests repeatedly until they pass. | `python -m pytest -q` |
| Check which files changed before committing. | `git status` |
| Stage and commit your completed source file. | `git add src/cisc217_week3/enrollment_tracker.py`<br>`git commit -m "Complete week 3 course enrollment tracker lab"` |
| Push your completed work to GitHub. | `git push origin main` |
| Check the autograder result after it runs. | Browser action: GitHub repository **Actions** tab |
| Grant the GitHub Team `classroom50-cisc217-inter-python-programming` the role **Read** on your repository if peer review access is not already available. | Browser action: GitHub repo **Settings → Collaborators and teams** |
| Post your GitHub repository link and required evidence in the Canvas lab discussion. | Browser action: reply to the Week 3 Lab Discussion in Canvas. |

## Required Data Structure

Your tracker should be a dictionary with this overall shape:

```python
{
    "students": {
        "s001": {
            "name": "Ada Lovelace",
            "courses": ["CISC217"]
        }
    },
    "courses": {
        "CISC217": {
            "title": "Intermediate Python",
            "roster": ["s001"]
        }
    }
}
```

The `students` dictionary maps student IDs to student records. The `courses` dictionary maps course codes to course records.

## Required Functions

Complete all functions in `enrollment_tracker.py`.

### `create_tracker()`

Return a new empty enrollment tracker.

Rules:

- Return a dictionary.
- Include a `"students"` key mapped to an empty dictionary.
- Include a `"courses"` key mapped to an empty dictionary.

Example:

```python
create_tracker()
# returns {"students": {}, "courses": {}}
```

### `add_student(tracker, student_id, name)`

Add or update a student record and return the tracker.

Rules:

- Store the student record under `tracker["students"]`.
- Each student record should include `"name"` and `"courses"`.
- If the student is new, create an empty course list.
- If the student already exists, update the name but keep the existing course list.

### `enroll_student(tracker, student_id, name, course_code, course_title)`

Enroll a student in a course and return the tracker.

Rules:

- Ensure the student exists.
- Ensure the course exists.
- Add the course code to the student's course list if it is not already present.
- Add the student ID to the course roster if it is not already present.
- Do not create duplicate course entries or duplicate roster entries.

Example:

```python
tracker = create_tracker()
enroll_student(tracker, "s001", "Ada Lovelace", "CISC217", "Intermediate Python")

# tracker now contains Ada under students and CISC217 under courses
```

### `drop_student(tracker, student_id, course_code)`

Drop a student from a course and return the tracker.

Rules:

- Remove the course code from the student's course list if present.
- Remove the student ID from the course roster if present.
- Missing students or courses should not cause an error.

### `get_roster(tracker, course_code)`

Return a sorted list of student names enrolled in a course.

Rules:

- Return student names, not student IDs.
- Sort the names alphabetically.
- If the course does not exist or has no students, return an empty list.

### `find_courses_for_student(tracker, student_id)`

Return a sorted list of course codes for one student.

Rules:

- Return course codes, not course titles.
- Sort the course codes alphabetically.
- If the student does not exist or has no courses, return an empty list.

### `student_summary(tracker, student_id)`

Return a dictionary summary for one student.

Return a dictionary with these keys:

```python
{
    "student_id": "s001",
    "name": "Ada Lovelace",
    "course_count": 2,
    "courses": ["CISC217", "MATH150"]
}
```

Rules:

- Use a sorted list of course codes.
- If the student does not exist, return an empty dictionary.

### `course_summary(tracker)`

Return a dictionary mapping course codes to enrollment counts.

Example:

```python
{
    "CISC217": 3,
    "MATH150": 2,
}
```

Rules:

- The keys should be course codes.
- The values should be the number of students on each course roster.
- Return an empty dictionary if there are no courses.

## Running the Tests

Run:

```bash
python -m pytest -q
```

A passing run should show output similar to:

```text
14 passed
```

The exact number of tests may change if your instructor updates the assignment, so pay attention to whether all tests pass.

## Canvas Initial Lab Post

After your tests pass and you push your work to GitHub, post in the Week 3 Lab Discussion.

Your initial post should include:

1. A link to your GitHub/Classroom50 repository.
2. Test evidence showing that you ran the tests, such as the command `python -m pytest -q` and the passing result.
3. A short explanation of how your tracker uses dictionaries. For example, describe the top-level `students` and `courses` keys or how student IDs and course codes are used as dictionary keys.
4. A short explanation of one nested collection in your solution. For example, `tracker["courses"]["CISC217"]["roster"]` stores the student IDs enrolled in a course.
5. One example of how your code prevents duplicate course or roster entries.
6. One question, challenge, or debugging issue you encountered.

Example initial post:

> My repository is here: PASTE_LINK_HERE. My tests passed after I ran `python -m pytest -q`. In my solution, I used a top-level dictionary with `students` and `courses` keys. Each student record is also a dictionary, and the `courses` field stores a list of course codes. One nested collection in my solution is `tracker["courses"]["CISC217"]["roster"]`, which stores the student IDs enrolled in that course. To prevent duplicates, I checked whether the course code or student ID was already in the list before appending it. One issue I had was remembering when to use dictionary keys and when to use list membership checks.

## Peer Review Pull Request

Your peer review is completed through a GitHub pull request and a Canvas reply in the same lab discussion board.

The peer review is due one week after the initial lab post is due.

For this lab, your pull request should make a small, helpful contribution to a classmate's repository. Usually this should be a documentation improvement, clearer code comment, or small test/comment clarification. Do **not** rewrite your classmate's solution or make unrelated changes.

The example below uses `kanika` as the classmate and `kanikasPR` as the peer review branch name. Replace those names with your classmate's GitHub username, repository name, and your own branch name.

| Step Description | Shell Command or GitHub Action |
|---|---|
| Fork your classmate's repository on GitHub. This creates your own copy of their repository under your GitHub account. | Use GitHub in your browser: click **Fork** on your classmate's repository. |
| Copy the SSH clone URL from **your fork**, not from your classmate's original repository. | Use GitHub in your browser: **Code → SSH → Copy URL**. |
| Clone your fork into NRP JupyterHub. | `cd ~/`<br>`git clone PASTE_YOUR_FORK_SSH_URL_HERE`<br>`cd REPOSITORY_FOLDER_NAME` |
| Create and switch to a new peer review branch. Do not work directly on `main`. | `git checkout -b kanikasPR` |
| Make your peer review changes. For Week 3, make a small helpful change, such as a documentation improvement, a clearer comment, or a note that explains a dictionary or nested collection. Do not rewrite your classmate's solution. | Edit the file in JupyterHub. Good choices are `README.md`, files in `docs/`, or a small explanatory comment in `src/cisc217_week3/enrollment_tracker.py`. |
| Check which files you changed. | `git status` |
| Run the tests so your peer review does not break the project. | `python -m pytest -q` |
| Commit your peer review change. | `git add .`<br>`git commit -m "Peer review feedback"` |
| Push your peer review branch to your fork on GitHub. | `git push -u origin kanikasPR` |
| Check the autograder or GitHub Actions result on your fork. Your peer review should not break your classmate's project. | Use GitHub in your browser: **your fork → Actions**. |
| Create a pull request from your fork's peer review branch back into your classmate's original repository. | Use GitHub in your browser: **Compare & pull request**. Base repository: your classmate's repository. Base branch: `main`. Head repository: your fork. Compare branch: `kanikasPR`. |
| In the pull request description, explain what you changed and why it is helpful. Ask one useful question connected to dictionaries, nested collections, duplicate prevention, or test evidence. | Example: "I added a short comment to clarify how the course roster dictionary is organized. One question I had: how does your code prevent the same student from being enrolled twice in the same course?" |
| Copy the pull request link and submit it in your Canvas peer review reply. | Copy the pull request URL from GitHub. |
| After the pull request is created and your Canvas reply is posted, you may delete the cloned copy from your JupyterHub account if you no longer need it. | `cd ~/`<br>`rm -rf REPOSITORY_FOLDER_NAME` |

### Canvas Peer Review Reply

In the same Canvas discussion board, reply to your classmate with:

1. A link to the pull request you opened.
2. One specific comment about their code, documentation, test evidence, or weekly concept.
3. One specific suggestion or question connected to their repository.

Replies such as "Good job," "I agree," or "Looks good" by themselves are not substantial enough for credit.

Example peer review reply:

> Hi Kanika, here is the pull request I opened on your repository: PASTE_PULL_REQUEST_LINK_HERE. I noticed that your enrollment tracker uses a dictionary to connect course names with student lists. I added a small documentation comment to make that structure easier to understand. One question I had was how your code prevents duplicate enrollments if the same student is added to the same course more than once.

## Academic Integrity

You may discuss setup steps, error messages, and general Python concepts with classmates. Your submitted code must be your own work. Do not copy another student's solution. Peer review pull requests should be small, helpful improvements rather than replacement solutions.
