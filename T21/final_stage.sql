SELECT s.email
FROM Student s
INNER JOIN Course c ON s.stu_subject_code = c.course_code
WHERE c.course_level = 3;