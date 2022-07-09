# Schedules

This project is the first attempt to solve a common problem on any organization that wants to *optimize* the schedule between teachers and students taking into account 
1. Teacher's availability and knowledge (subjects that can teach)
2. Student's needs (subjects that need to enroll)
3. Classrooms availability (hours and capacity)

based on the profit defined as

> PROFIT = INCOME - COST  

Where:  
> INCOME = SUM(students_payment)  
> COST = SUM(teacher_subject_cost) + SUM(classroom_total_hours_cost)  

This can be used not only for money but also for teachers acceptance by students changing the income that every teacher creates on a given subject. See more in [Example](#example)

### Assumptions
1. All students take the schedule purposed.
2. Quality on every teacher is the same, so student's preferences don't apply.


# Example

You can see the same example in Google Sheets here: [Schedules | Example tables](https://docs.google.com/spreadsheets/d/1sreTuAUG9ZhNeeUrbaPRySFlNXCtdgsaaKbC9FoxGHU/edit?usp=sharing)

### Student's needs
| student | subject 1 | subject 2 | subject 3 | subject 4 |
|---------|-----------|-----------|-----------|-----------|
| 1       | x         |           | x         |           |
| 2       | x         |           | x         | x         |
| 3       | x         | x         | x         |           |

Where:
* student 1 need to find a course for subject 1 and subject 3
* student 2 need to find a course for subject 1 and subject 3
* student 3 needs to find a course for subject 1, subject 2 and subject 3

### Teacher's knowledge
| teacher | subject 1 | subject 2 | subject 3 | subject 4 |
|---------|-----------|-----------|-----------|-----------|
| 1       | x         | x         | x         | x         |
| 2       | x         |           | x         | x         |
| 3       | x         | x         | x         |           |

Where:
* teacher 1 can teach subject 1, subject 2, subject 3, subject 4
* teacher 2 can teach subject 1, subject 3, subject 4
* teacher 3 can teach subject 1, subject 2, subject 3

### Subject hours per week
| subject | hours |
|---------|-------|
| 1       | 6     |
| 2       | 8     |
| 3       | 4     |
| 4       | 6     |

Where:
* subject 1 need 6 hours a week and cost 1 to the students
* subject 2 need 8 hours a week and cost 1 to the students
* subject 3 need 4 hours a week and cost 1 to the students
* subject 4 need 6 hours a week and cost 1 to the students

### Teacher cost per week
| teacher | subject | cost | income |
|---------|---------|------|--------|
| 1       | 1       | 6    | 3      |
| 2       | 1       | 8    | 4      |
| 3       | 1       | 4    | 2      |
| 4       | 1       | 6    | 3      |

Income means the payment per student. That also is usefull to measure student's happines in case the preference for some teachers is known.

### Classroom availability (weekly)
| classroom | cost | capacity | h2 | h3 | h4 | h5 | h6 | h7 | h8 |
|-----------|------|----------|----|----|----| ---|----|----|----|
| 1         | 5    | 10       | x  | x  | x  |    | x  | x  | x  |
| 2         | 7.5  | 15       |    | x  | x  | x  |    | x  | x  |
| 3         | 6    | 12       | x  | x  |    | x  | x  |    |    |

Where:
* classroom 1 can be used on hours 1,2,3,4,6,7,8 by a single teacher for a single subject and has capacity for 10 persons
* classroom 2 can be used on hours 2,3,4,5,7,8 by a single teacher for a single subject and has capacity for 15 persons
* classroom 3 can be used on hours 1,2,4,5 by a single teacher for a single subject and has capacity for 12 persons

### Teacher's availability
| teacher | schedule | h1 | h2 | h3 | h4 | h5 | h6 | h7 | h8 |
|---------|----------|----|----|----| ---|----|----|----|----|
| 1       | 1        |    | x  | x  | x  | x  | x  | x  | x  |
| 2       | 1        | x  | x  |    |    |    |    |    |    |
| 2       | 2        |    |    |    |    |    | x  | x  | x  |
| 3       | 1        | x  | x  |    | x  | x  |    | x  |    |

Teacher's can give multiple options for his own schedule. Example Teacher 2 can give 2 hours in the morning or 2 hours at night but 2 in the morning and 2 in the night.

Where:
* teacher 1, on schedule 1 can give class on hours 2,3,4,5,6,7,8 for a single subject
* teacher 2, on schedule 1 can give class on hours 1,2 for a single subject
* teacher 2, on schedule 2 can give class on hours 6,7,8 for a single subject
* teacher 3, on schedule 1 can give class on hours 1,2,4,5,7 for a single subject



## UNAM Scenario  
* Column "income" in "Teacher cost per week" table is 1
* Column "cost" in "Teacher cost per week" table is 0
* Column "cost" in "Classroom availability (weekly)" table is 0

# TO DO: 
## Students preference
Example: students with 100% credits can have preference over students with 90% credits and create an impact in the income.
