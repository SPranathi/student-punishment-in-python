"""
#Task to a student as Punishment

In a school, class teacher gives a task to a student as a punishment, 
teacher pronounces a sentence orally and ask the student to count number of charaters 
in initial-word or end-word in the sentence.

Initia-word is denoted by 'i' 
End-Word is denoted by 'e'

Input=
covid19 is a pandemic
i
Output=
covid19
-------------
Input=
covid19 is a pandemic
e
Output=
pandemic
""" 
import numpy
sentence=input().split(" ")
word=input()
if(word=='i'):
    print(sentence[0])
elif(word=="e"):
    print(sentence[-1])
