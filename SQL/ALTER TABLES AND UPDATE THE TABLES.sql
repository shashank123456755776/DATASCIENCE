#how to add new columns 
ALTER TABLE students
ADD COLUMN CITY VARCHAR(50);
INSERT INTO students(ID,CITY)
VALUES("PATNA");
# ager hmm new column add karte hai aur id mera auto increment hai and if we wants to add data in new column in specific rows or any rows 
#then use below commands  
UPDATE students
SET CITY = 'PATNA'
WHERE Id = 1;
# ek sath paricular rows mai sare column kaise bahrenge 
UPDATE students
SET CITY ='PATNA'
WHERE id=2;

UPDATE students
SET NAME='shashank',
    Age=25,
    EMAIL='shashank6712456@gmail.com',
    CITY='bihar',
    joinDate='2026-08-12'
Where id =3;
# how  to change the datetypes of any colums  
ALTER TABLE students  MODIFY Age SMALLINT;

#how to Rename the any columns  name  
ALTER TABLE students RENAME  COLUMN EMAIL  To StudentEmail;
#how to delete the tables 
# DROP TABLES students(name of the table)
# how to reset the tables--
#TRUNCATE TABLE  students   
SELECT * FROM students 

 
