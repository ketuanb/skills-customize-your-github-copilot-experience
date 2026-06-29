# 📘 Assignment: SQL Foundations for Student Data

## 🎯 Objective

Practice beginner SQL skills by creating a small student database and writing queries to answer real classroom questions. You will use SQL to filter, sort, and summarize data.

## 📝 Tasks

### 🛠️	Task 1: Create and Populate a Student Table

#### Description
Set up a SQLite database with one table named `students` and insert sample rows for at least 8 students.

#### Requirements
Completed program should:

- Create a `students` table with columns: `id`, `name`, `grade_level`, `club`, and `math_score`.
- Insert at least 8 records using `INSERT INTO`.
- Use realistic values (for example: grade levels 9-12, clubs like Robotics/Art/Math).
- Print all rows to confirm the data was added correctly.

### 🛠️	Task 2: Query, Filter, and Sort Data

#### Description
Write SQL queries to answer questions about student records.

#### Requirements
Completed program should:

- Use `SELECT` to show all student names and math scores.
- Use `WHERE` to filter students with `math_score >= 85`.
- Use `ORDER BY` to list students from highest to lowest score.
- Use `LIMIT` to show only the top 3 scores.

### 🛠️	Task 3: Summarize with GROUP BY

#### Description
Use aggregation to understand trends in the class data.

#### Requirements
Completed program should:

- Use `GROUP BY` to count how many students are in each club.
- Use `AVG` to compute average math score by grade level.
- Display query results clearly with labels.
- Include at least one short reflection sentence in a comment explaining one trend you noticed.
