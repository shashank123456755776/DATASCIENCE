
-- JOIN  TABLES USE KARO 

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);
INSERT INTO Students VALUES
(1, 'Rahul', 'Delhi'),
(2, 'Priya', 'Mumbai'),
(3, 'Amit', 'Delhi'),
(4, 'Sneha', 'Kolkata');
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    student_id INT     -- foreign key referring to Students.student_id
);
INSERT INTO Courses VALUES
(101, 'Math', 1),
(102, 'Science', 2),
(103, 'English', 2),
(104, 'History', 5);   -- student_id does NOT exist in Students
-- INNER JOIN IS USED TO ONLY MATCHING DATA FROM BOTH THE TABLES
-- Shows only matching data from both tables. 
SELECT s.student_id,s.name,c.course_name
FROM Students s
INNER JOIN courses c
ON s.student_id = c.student_id;

-- Shows all students, and matching courses.
-- If course not found → NULL.
-- LEFT JOIN
SELECT s.student_id, s.name, c.course_name
FROM Students s
LEFT JOIN Courses c
ON s.student_id = c.student_id;

-- Shows all courses, and matching students.
-- If student missing → NULL.
-- RIGHT JOIN
SELECT s.student_id, s.name, c.course_name
FROM Students s
RIGHT JOIN Courses c
ON s.student_id = c.student_id;

-- FULL OUTER JOIN or union (MySQL does NOT support directly)
-- Shows all rows from both tables—matching or not.
SELECT s.student_id, s.name, c.course_name
FROM Students s
LEFT JOIN Courses c
ON s.student_id = c.student_id

UNION

SELECT s.student_id, s.name, c.course_name
FROM Students s
RIGHT JOIN Courses c
ON s.student_id = c.student_id;

-- CROSS JOIN

-- Creates Cartesian product (every student × every course).

SELECT s.name, c.course_name
FROM Students s
CROSS JOIN Courses c;

-- Table joins with itself.
-- Example: Find students from the same city.
-- example same city se persoon ko fimd karne ke liye us ekarte hai SELF JOIN KA 
SELECT A.name AS Student1, B.name AS Student2, A.city
FROM Students A
JOIN Students B
ON A.city = B.city
AND A.student_id <> B.student_id;


-- INNER JOIN	Matching rows only
-- LEFT JOIN	All from left + matches
-- RIGHT JOIN	All from right + matches
-- FULL JOIN	All rows (match + no match)
-- CROSS JOIN	Every row × every row
-- SELF JOIN	Join table with itself
