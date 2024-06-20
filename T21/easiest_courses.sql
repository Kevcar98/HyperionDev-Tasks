SELECT s.first_name, c.course_name
FROM Student s
INNER JOIN Course c ON s.stu_subject_code = c.course_code
WHERE s.mark >= 70;