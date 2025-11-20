-- subqueries ,CTES  and  views in my sql 
-- Subqueries (Nested Query)
-- Subquery = ek query ke andar dusri query.
CREATE TABLE students(
 id INT PRIMARY KEY ,
 name VARCHAR(50),
 marks VARCHAR(50)

);
INSERT INTO students  VALUES
(1,'shashank',40),
(2,'ravi',50),
(3,'susuram',30),
(4,'kuko',10);
-- SUBQUERIES INSIDE THE ROUNDS MARKETS 
SELECT name,marks 
FROM students
WHERE marks =(SELECT MAX(marks) FROM students);

-- kya subquries ko  WHERE,SELECT,FROM se kar sakte hai ---answer hoga hai 
-- return values,list and tables 
-- subquery ke under ek aur subquery use kar sakte hai 

-- CTES 

WITH MaxMarks AS (
    SELECT MAX(marks) AS highest_marks
    FROM students
)
SELECT name, marks
FROM students
JOIN MaxMarks
ON students.marks = MaxMarks.highest_marks;

-- VIEW --VIRTUAL TABLES

-- ✔ A virtual table
-- ✔ Which does not store data
-- ✔ But shows data from other tables
-- ✔ You can use it like a normal table
-- A VIEW is used because we don't want to repeat the same complex query again and again.
CREATE VIEW top_student AS
SELECT name, marks
FROM students
WHERE marks = (SELECT MAX(marks) FROM students);

SELECT * FROM top_student;

-- You write one complex query → save it as VIEW
-- ✔ Next time, you just write → SELECT * FROM view_name;
-- ✔ View always shows latest / updated data
-- ✔ It saves time and reduces mistakes



