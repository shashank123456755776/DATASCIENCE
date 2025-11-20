SELECT SUM(Age) FROM students;
SELECT AVG(Age) FROM students;
SELECT COUNT(Age)  FROM students;
SELECT MIN(Age),MAX(Age) FROM students;
SELECT Name ,SUM(Age) FROM students GROUP BY NAME
HAVING SUM(Age)>56;