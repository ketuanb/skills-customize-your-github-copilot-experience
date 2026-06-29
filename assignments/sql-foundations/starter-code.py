"""
Starter Code: SQL Foundations for Student Data

Run with:
python3 starter-code.py
"""

import sqlite3


def main() -> None:
    # Creates a local SQLite database file in the assignment folder.
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # Task 1: Create table and insert sample data.
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            grade_level INTEGER NOT NULL,
            club TEXT NOT NULL,
            math_score INTEGER NOT NULL
        )
        """
    )

    # TODO: Replace or expand this sample data to include at least 8 students.
    sample_students = [
        (1, "Ava", 9, "Robotics", 91),
        (2, "Liam", 10, "Art", 84),
        (3, "Noah", 11, "Math", 88),
        (4, "Mia", 12, "Robotics", 95),
    ]

    cursor.executemany(
        """
        INSERT OR REPLACE INTO students (id, name, grade_level, club, math_score)
        VALUES (?, ?, ?, ?, ?)
        """,
        sample_students,
    )

    connection.commit()

    print("All students:")
    for row in cursor.execute("SELECT * FROM students"):
        print(row)

    print("\nTODO Task 2: Students with score >= 85")
    # Example:
    # for row in cursor.execute(
    #     "SELECT name, math_score FROM students WHERE math_score >= 85 ORDER BY math_score DESC"
    # ):
    #     print(row)

    print("\nTODO Task 3: Count students by club")
    # Example:
    # for row in cursor.execute(
    #     "SELECT club, COUNT(*) AS total FROM students GROUP BY club ORDER BY total DESC"
    # ):
    #     print(row)

    connection.close()


if __name__ == "__main__":
    main()
