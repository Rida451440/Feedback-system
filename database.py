import sqlite3
from werkzeug.security import generate_password_hash

DB_NAME = "feedback.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section TEXT NOT NULL,
            text TEXT NOT NULL,
            q_type TEXT NOT NULL,
            is_active INTEGER DEFAULT 1
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            reg_no TEXT NOT NULL,
            course_id INTEGER NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            avg_rating REAL,
            sentiment TEXT,
            sentiment_reason TEXT,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            submission_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            answer TEXT,
            FOREIGN KEY (submission_id) REFERENCES submissions(id),
            FOREIGN KEY (question_id) REFERENCES questions(id)
        )
    """)

    conn.commit()
    conn.close()


def seed_data():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM admins")

    if cur.fetchone()[0] == 0:
        password_hash = generate_password_hash("admin123")

        cur.execute(
            """
            INSERT INTO admins
            (username, password_hash)
            VALUES (?, ?)
            """,
            ("admin", password_hash)
        )

    courses = [
        "Python Programming",
        "Web Development",
        "Artificial Intelligence",
        "Machine Learning",
        "Data Science",
        "Cyber Security",
        "Database Management",
        "Software Engineering",
        "Graphic Designing",
        "Digital Marketing",
        "Mobile App Development",
        "Cloud Computing"
    ]

    for course_name in courses:
        cur.execute(
            """
            INSERT OR IGNORE INTO courses (name)
            VALUES (?)
            """,
            (course_name,)
        )

    questions = [
        ("Section A: Instructor Evaluation", "The instructor has strong subject knowledge.", "rating"),
        ("Section A: Instructor Evaluation", "The instructor explains concepts clearly and effectively.", "rating"),
        ("Section A: Instructor Evaluation", "The instructor encourages questions and class participation.", "rating"),
        ("Section A: Instructor Evaluation", "The instructor is punctual and regular in classes.", "rating"),
        ("Section A: Instructor Evaluation", "The instructor provides helpful feedback on assignments and projects.", "rating"),
        ("Section B: Course Content and Curriculum", "The course content is relevant to current industry requirements.", "rating"),
        ("Section B: Course Content and Curriculum", "The course outline was clearly shared at the beginning.", "rating"),
        ("Section B: Course Content and Curriculum", "The balance between theory and practical work is appropriate.", "rating"),
        ("Section B: Course Content and Curriculum", "The course helped me build skills useful for jobs or freelancing.", "rating"),
        ("Section B: Course Content and Curriculum", "The projects and assignments improved my practical skills.", "rating"),
        ("Section C: Labs and IT Facilities", "Lab computers are in good working condition.", "rating"),
        ("Section C: Labs and IT Facilities", "The internet connection is reliable.", "rating"),
        ("Section C: Labs and IT Facilities", "Required software and tools are available in the lab.", "rating"),
        ("Section C: Labs and IT Facilities", "The classroom and lab environment is clean and comfortable.", "rating"),
        ("Section D: Administration and Support Staff", "The administration staff is professional and respectful.", "rating"),
        ("Section D: Administration and Support Staff", "My queries and issues are resolved in a timely manner.", "rating"),
        ("Section D: Administration and Support Staff", "The fee and admission process is clear and well managed.", "rating"),
        ("Section D: Administration and Support Staff", "Class schedules and announcements are communicated on time.", "rating"),
        ("Section E: Career Support", "The institute provides guidance on internships and career opportunities.", "rating"),
        ("Section E: Career Support", "I feel confident about my career prospects after this course.", "rating"),
        ("Section F: Overall Satisfaction", "Overall, I am satisfied with my experience at Corvit Institute of Information Technology.", "rating"),
        ("Section F: Overall Satisfaction", "I would recommend Corvit to others.", "yesno"),
        ("Section G: Open-Ended", "What do you like most about Corvit?", "text"),
        ("Section G: Open-Ended", "What problems have you faced, and what should be improved?", "text")
    ]

    for section, text, q_type in questions:
        cur.execute(
            """
            SELECT id
            FROM questions
            WHERE section = ?
            AND text = ?
            """,
            (section, text)
        )

        if cur.fetchone() is None:
            cur.execute(
                """
                INSERT INTO questions
                (section, text, q_type, is_active)
                VALUES (?, ?, ?, 1)
                """,
                (section, text, q_type)
            )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    seed_data()
    print("Database created and updated successfully.")