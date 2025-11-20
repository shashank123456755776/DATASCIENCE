CREATE TABLE student(
  Id INT AUTO_INCREMENT PRIMARY KEY,
  Name VARCHAR(100),
  Age TINYINT,
  EMAIL VARCHAR(100),
  joinDate DATE
);


-- SELECT * FROM student
-- if we wants to reset teh data in tables 
-- TRUNCATE TABLE student;
INSERT INTO student(Name,Age,EMAIL,joinDate)
VALUES('shashanksuman',54,'shashank78@gmail.com','2025-05-12');
SELECT * FROM student
