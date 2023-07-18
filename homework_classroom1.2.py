#!/usr/bin/env python
# coding: utf-8

# In[80]:


class Student() :
    # 建構式
    def __init__(self,name,student_id,age,gender):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.gender = gender

    # 方法(method)
    def set_grade(self,grade):
        self.grade = grade
        print('grade is set!')
                      
    def get_grade(self): # 改用return
        return self.grade
    
    def display_student_info(self):
        print('student name:',self.name,
              '\nstudent_id:',self.student_id,
              '\nage:',self.age,
              '\ngender:',self.gender,
              '\ngrade:',self.get_grade())


# In[ ]:




