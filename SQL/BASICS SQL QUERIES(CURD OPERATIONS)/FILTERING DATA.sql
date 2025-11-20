# FILTERING THE  PARTICULAR DATA

-- use of where clause in filtering of particular row data
#LIKE ka use tab hota hai jab aap column me pattern, partial text, ya starting/ending characters ke base par filtering karna chahte ho.
SELECT * FROM  students WHERE CITY LIKE '%PATNA%';
SELECT * FROM students WHERE Name="shashank" AND CITY LIKE '%bihar%';
SELECT * FROM  students WHERE CITY NOT LIKE '%PATNA%';