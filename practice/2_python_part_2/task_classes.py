"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime 
from datetime import date


class Homework:
    def __init__(self, task, deadline,created):
        self.task = task
        self.deadline = deadline
        self.created=created
    def is_active(self): 
        
        date_now=datetime.datetime.now()
        if((date_now-self.deadline)==0):
            print( "Task closed")
        else:
            print("Task Active")
        
    
class Teacher:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
    def create_homework(self,task_text,days_to_complete):
        created_date=datetime.datetime.now()
        deadline=created_date+datetime.timedelta(days=days_to_complete)
        return Homework(task_text,created_date,deadline)
  

class Student:
     def __init__(self, task, deadline,created, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
        Homework.__init__(self, task, deadline,created)

     def do_homework(homework):
       if homework.is_active():
           print(f'Doing Homework')
       else:
           print("you are late")    

            
    

    
            





if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
