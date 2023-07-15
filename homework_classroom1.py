{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "241bab4d-5c5c-4bdf-8c72-9914ae9fd06a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "grade is set!\n",
      "Yu's is 100\n",
      "student name: Yu \n",
      "student_id: 12345 \n",
      "age: 15 \n",
      "gender: female\n"
     ]
    }
   ],
   "source": [
    "class Student() :\n",
    "    # 建構式\n",
    "    def __init__(self,name,student_id,age,gender):\n",
    "        self.name = name\n",
    "        self.student_id = student_id\n",
    "        self.age = age\n",
    "        self.gender = gender\n",
    "\n",
    "    # 方法(method)\n",
    "    def set_grade(self,grade):\n",
    "        self.grade = grade\n",
    "        print('grade is set!')\n",
    "              \n",
    "    def get_grade(self):\n",
    "        print(self.name+'\\'s is', self.grade)\n",
    "    \n",
    "    def display_student_info(self):\n",
    "        print('student name:',self.name,\n",
    "              '\\nstudent_id:',self.student_id,\n",
    "              '\\nage:',self.age,\n",
    "              '\\ngender:',self.gender)\n",
    "\n",
    "\n",
    "yu = Student('Yu','12345', 15, 'female')\n",
    "yu.set_grade(100)\n",
    "yu.get_grade()\n",
    "yu.display_student_info() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dabbbb2-19f3-4f2e-a5fe-10642f300d35",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
