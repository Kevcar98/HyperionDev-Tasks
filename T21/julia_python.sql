SELECT s.mark
FROM Student s
INNER JOIN Course c ON s.stu_subject_code = c.course_code
WHERE c.teacher_name = 'Julia Python';