SELECT * FROM patients;

SELECT name, bmi
FROM patients
WHERE bmi >= 30;

SELECT name, bmi
FROM patients 
ORDER BY bmi DESC;

SELECT AVG(bmi) AS average_bmi
FROM patients;