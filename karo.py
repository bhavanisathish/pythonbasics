# -*- coding: utf-8 -*-
"""

python is both programming and scripting language. programming language is used to interact with
 machine and human. scripting language is also a programming language, it doesnot compile it undergo 
interpretation. python is also interpreted language beacuse it perform both compilation and execution

REASON FOR INVENTION
    --to avoid complexity in c and c++

WHY PYTHON NOW
    --machine learning,artifical intelligence,cloud computing etc

WHY PYTHON
    --flexible,begginer friendly, many pakages in repository.

FEATURES
    --simple,interactive,open,oop,portable,gui.

IMPORTANT LIBRARY
    --os,time,numpy,array,keras,sklearn,tkinter.

WEB develop
    --Django,flask

ANDROID app
    --kivy

DESKtop
    --tkinter

IDLE
    extension--->.py
    cd--> change directory
cd python
>> python sample.py
"""
#BASIC OPERATION and output

10/3  #3.33
10//3 #3
10*3 #30
2**3 #8
5+6 #11
'bhavani'+'sathish' #bhavanisathish
'python' #python
10*'python'  #'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
2+'6' #error
'2'+'6' #'26'
2+int('6') #8 the passing string should be in number format

#**********************************************************************

'''
Variables
    -- store something
    --no nees to specify the datatype
'''
a=10
print(a)    #10
print(type(a)) #<class 'int'>
b=type(a)
print(b)    #<class 'int'>

#addition
a=10
b=20
print(a+b)  #30
c=a+b
print(c)     #30

#char type variable
s='python'
print(s)
print(s[0])     #p forward and backward indexing is allowed
print(s[-1])    #n
s[2:5]          #'tho' 2-4
s.count('o')    #1
s.find('p')     #0 return the index else return -1(not found)
s.index('n')    #5
l=s.upper()
print(l)

#***************************************************************************

'''list
    -- collection of dissimilar elements,it is mutable(changable),it is denoted by[]
'''

l=[0,1,2,'ss']
print(l)    #[0, 1, 2, 'ss']
l[-1]   #'ss'
l.sort()    #'<' not supported between instances of 'str' and 'int'
l[0:2] # [0, 1]
l.append('pp')
print(l)   #[0, 1, 2, 'ss', 'pp']
l.insert(1,'ii')
print(l)   #[0, 'ii', 1, 2, 'ss', 'pp']
l.pop()    # 'pp' element and keys are allowed
l.pop(1)   #'ii'
l.remove(2) #elements only allowed
print(l)    #[0, 1, 'ss']
k=[5,6,'lol']
l.extend(k)
print(l) #[0, 1, 2, 'ss', 5, 6, 'lol'] extend is to add two list
l.clear()
print(l)    #[]

#****************************************************************************

'''
tuple
    --collection of similar elements amd immutable and denoted by ()'''

l=(0,1,2,3)
print(l)    #(0, 1, 2, 3)
l[0:4:2]    # (0, 2)
l.remove(0) #'tuple' object has no attribute 'remove' immutable

#*************************************************************************

'''dictionary
    --collection of keys and value
    --they are separated by semicolon
    --both pair are separated by comma
''' 

d={'name':'bhavani','nname':'crazy'}
print(d) #{'name': 'bhavani', 'nname': 'crazy'}
print(d['name'])   #'bhavani'
print(d.keys())    #dict_keys(['name', 'nname'])
print(d.values())#dict_values(['bhavani', 'crazy'])
d={'[1,23]':'crazy'}    #{'[1,23]': 'crazy'}
print(d)

#*******************************************************************************

#condition it is came like a choice if the user pass a condition they get the result based on it

#   :--> indicates the start of the condition

#   white space--> INdentation whick indicates the block of codes with in the condition

a=int(input("enter integer type value"))
if(a<6):
    print("good",a)         #good 2
elif(a>6 and a<20):
    print("average",a)  #average 7
else:
    print("excellent",a)    #excellent 44

#*************************************************************************************

#nested if

a=2
if(a<5):
    if(a==2):
        print('welcome')    #welcome
    else:
        print('warm welcome')
else:
    print("waiting")

#***********************************************************************************

"""loop
    --while and for looop are a entry control loop which chech the condition and then execute the block of codes
    --for is single line parameter and while is multiline
    --for i in range():
    //block of codes with automatic incrementer
while(condition):
    //block of codes
    incrementer
"""
a=0
while(a<11):
    print(a,end='')     #012345678910
    a=a+1       #a+=1
    
s="sathish"
for i in s:
    print(i,end="-") #s-a-t-h-i-s-h-
for i in s:
    print(s,end="") #sathishsathishsathishsathishsathishsathishsathish

#range specify the limit range(start,stop,step size)

for i in range(0,30,2):
    print(i,end="  ")   #0  2  4  6  8  10  12  14  16  18  20  22  24  26  28  

#********************************************************************************

#break

for i in range(0,10):
    if(i>5):
        break
    print(i,end=" ")    #0 1 2 3 4 5 

#***************************************************************************

#comment -----#single  '''multiline'''

#***************************************************************************

#type casting

a=10
float(a)    #10.0
a=10
id(a)   #gives the address
id('sathish')   #150482648
a=str(a)    #'10'
print(a)

#***************************************************************************

#functions in python

#it contain list of statements... execute again and again when it calls

#function without arguments

def display():
    print("python programming")     #python programming
display()

#function with single argument

def disp(s):
    print(s)        #sathish
disp('sathish')

#function with multiple argument

def di(s,l):
    k=s+l  
    print(k)        
di('sathish','franky')  #sathishfranky
di(10,20)               #30

#function with default arguments

def d(sat,rat=10):
    p=sat/rat
    print(p)
d(40,20)        #2.0
d(30)           #3.0

#return type

def de(a,b):
    return(a+b)
q=de(100,30)
print(q)        #130

#getting input from user

def disp(s):
    print(s)        #sathish
k=input("enter a value")
disp(k)

###lambda

#syntax---> lambda argument:expression

x=lambda a:a*25
print(x(5))         #125
k=lambda a,b:a+b+5
print(k(2,3))       #10

#variable length argument

def df(a,b,*c):     # *c is the variable length in the form of tuple  
    print(a,b,c)    #1 2 (3, 4, 5)
df(1,2,3,4,5)

#decalre variable length as dictionary

def dd(name,age,**add):
    print(name,age,add) #sathish 23 {'city': 'bodinayakanur', 'district': 'theni'}
dd('sathish',23,city='bodinayakanur',district='theni')

#recursion-- the set of codes which run repeatedly

def fact(n):
    if(n==0):
        return 1
    else:
        return(n*fact(n-1))
print(fact(5))      #120

#***************************************************************************

''' library        (site_packages contain all the library in python)

to import a library
    -->import library_name
    -->import library_name as new_name                  using alias(giving new name for easy usage)
    -->from library_name import *                        *--> denotes entire library or we specify any part from the library

to install library(command prompt)
    -->pip install lib_name                                  eg pip install tenserflow
    -->pip install lib_name==version                         eg pip install math==2.0
    -->pip install lib_name --upgrade                        eg pip install math --upgrade
'''

#example

import time
time.time() #1558759605.094906

#alias

import time as t
t.time()    #1558759605.094906

#***************************************************************************

#files in python

#file-->store something

#open has two argument 1...filename 2....mode,close-->close the file

file=open("data.txt","w")
file.write("sathishfranky") #open the file data.txt
file=open("data.txt","a")
file.write("sathishfranky") #open the file data.txt
file.close()

#read a file

file=open("data.txt","r")
print(file.read())  #sathishfranky
file.read()
file.close()

#rename the file

import os
os.rename("data.txt","sathi.txt")
file=open("data.txt","r")
print(file.read())  # No such file or directory: 'data.txt'
file=open("sathi.txt","r")
print(file.read())  #sathishfranky
file.close()

#***************************************************************************

#variable scope local and global

x=10    # global
def life():
    y=30    #local-->scope lost outside the block
    print(y)    #30
    print(x)    #10
life()
print(x)    #10
print(y)    #name 'y' is not defined

#declaring variable as global

x=10
def like():
    global x
    x=30
like()
print(x)    #30

#**********************************************/'*****************************

#raw string is used to print the directory with back slash character as same as user specified

print(r"c:\desktop")    #c:\desktop

#Exception handling

#exception means error

#the way to handle the error

#the key words are try,except,finally and else

try:
    a='data'
    int(a)
except:
    print('sting cant be converted into int')

#file specfic exception

try:
    file=open('karo.py','w')
except FileNotFoundError:
    print(" No such file or directory: '1.txt'")
else:
    print('no error') #no error if there is no error else part will executed
finally:    #the user is saved. this statement is executed at all time
    print('the user is saved')

#*****************************************************************************

"""
oops-object oriented programming
    --class- group of variable(properties) and function(methods)
    --like a blueprint,info,living
    --no memory allocated,code space like text space
    --object- physical representation of class instance,memory can be allocated
    --built a house of flat with 5 room with same blueprint

adv
    reusability like whatsapp

application
    job because max in oop
"""

class like:
    def life(self):  #object is passed as a argument
        print('make code easy')
l=like()
l.life() #make code easy

## class with in class

class a:    
    def lie(self):  #object is passed as a argument
        print('make code easy')
    class b:
        def life(self):
            print('python code')
s=a()
s.lie()        #s.life() o/p 'a' object has no attribute 'life'
k=s.b()
k.life() #python code

#****************************************************************************

"""constructor
    --used for initailisation purpose 
    --it is called at the time of object creation
    --default constructor
            -- with out arguments
    --parameterized construction
        -- with passing parameters
"""

class a:
    def __init__(self):
        print('inheritance')
    def life(self):
            print('python code')
s=a()   #inheritance
s.life()    #python code

#parameterized

class a:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        return c
s=a(10,20)
c=s.add()
print(c)    #30

#*****************************************************************************

"""Iheritance
    --the class which uses the properies of another class is called child class,another class is parent class
"""

class a:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a,b)
    def add(self):
        print(self.a+self.b)
    def life(self):
        print('python code')
class b(a):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(a,b,c)
    def add1(self):
        print(self.a+self.b+self.c)
    def life(self):             #1 23 4
        print('my code')        #24
s=b(1,23,4)                     #28
s.add()                 #my code
s.add1()
s.life()

#******************************************************************************

"""numpy
    --numerical python
    --It is used for performing numerical operations 

functions
    --array(),linspace,logspace,zeros,ones()
"""

#from numpy import *

#linspace which split the elements with in the range depend on count

import numpy as a
s=a.linspace(0,10,5)    #[ 0.   2.5  5.   7.5 10. ]
print(s)    
print(s.ndim)   #1
print(s.size)   #5

#****************************************************************************

#logspace which split the elements with in the range depend on log value

import numpy as a
s=a.logspace(0,10,10)    #[ 0.          1.11111111  2.22222222  3.33333333  4.44444444  5.55555556
                          #6.66666667  7.77777778  8.88888889 10.        ]
print(s)    
print(s.ndim)   #1
print(s.size)   #10

#***************************************************************************

#ones

import numpy as a
#l=(2,2)
s=a.ones((2,2)) #[[1. 1.]
#s=a.ones(5,int)                    # [1. 1.]]
print(s)        #[1 1 1 1 1]
print(s.ndim)   #1
print(s.size)   #5

#******************************************************************************

#zeros

import numpy as a
#s=a.ones((2,2)) 
s=a.zeros(5,int)
print(s)        #[0 0 0 0 0]
print(s.ndim)   #1
print(s.size)   #5

#**********************************************************************************

#array single dimensions

import numpy as a
s=a.array([1,2,3,4])    #array([1, 2, 3, 4])
print(s)  #[1, 2, 3, 4]
type(s)    #numpy.ndarray
print(s.ndim)   #1
print(s.size)   #4
l=a.array([2,3,4,5])    # array size must be same
print(s+l)  #[3 5 7 9]

#***********************************************************************************

#two dimensional array

import numpy as a
s=a.array([[1,2,3],[3,4,5]])   
print(s) #[[1 2 3]
            # [3 4 5]]
print(s.ndim)   #2
print(s.size)   #8
l=s=a.array([[6,7,8],[8,9,10]]) 
print(s+l)  #[[ 4  4  6  8]
 #[ 4  6  8 10]]
print(s*l) #[[ 4  4  9 16]
 #[ 4  9 16 25]]

 #******************************************************************************************

 #three dimensional array

import numpy as a
s=a.array([[[1,2,3],[3,4,5],[5,6,7],[7,8,4],[8,9,7]],[[1,2,3],[3,4,5],[5,6,7],[7,8,4],[8,9,7]]])
print(s)  
'''
[[[1 2 3]
  [3 4 5]
  [5 6 7]
  [7 8 4]
  [8 9 7]]

 [[1 2 3]
  [3 4 5]
  [5 6 7]
  [7 8 4]
  [8 9 7]]]
'''

 #**************************************************************************** 

 '''matplotlib
     --it is used for data visualization
     --pictoraial representation of data

   It has two packages 
        1...pyplot-It imports the matplotlib library
        2...pylab-It is a mixture of pyplot and numpy
 '''

import matplotlib.pyplot as p
x=[1,2,3,4,5]
y=[6,7,8,9,10]
p.plot(x,y)
p.title('karo')
p.xlabel('life')
p.ylabel('like')
p.show()

#pie chart
 
import matplotlib.pyplot as p
x=[1,2,3,4,5]
y=[6,7,8,9,10]
p.pie(x)
p.show()

import matplotlib.pyplot as p
x=[1,2,1.5]
l=['tea','boost','coffee']
c=['red','green','blue']
p.pie(x,labels=l,colors=c)
p.show()

#scatter

import matplotlib.pyplot as p
x=[1,2,3,4,5]
y=[6,7,8,9,10]
p.scatter(x,y,label='life',color='blue')
p.show()
 
#bar cahrt

import matplotlib.pyplot as p
x=[1,2,3,4,5]
y=[6,7,8,9,10]
p.bar(x,y,label='life',color='blue')
p.show()

#****************************************************************************

""" 
artificial intelligence
    ---machine think like human

machine learning
    it involves 2 parts deep learning and predictive analysis..
    deep learning involves neural network
    predictive analysis-- predict the performance of the machine

natural language processing
    --understand the language spoken by human invole in speech to text and text to speech conversion
    eg--google assistant     

RGB
red[255 0 0]
green[0 255 0]
blue[0 0 255]
"""

#****************************************************************************

#opencv(open computer vision)

'''
    --it is one of the library in python
    --it is installed by using the command {pip install opencv / conda install -c conda-forge opencv}
    --it uses numpy with matlab way syntax

applications
    image processing
    building gui
    video analysis
    object detection
    machine learning
    etc
'''

#read and show the image

import cv2
img=cv2.imread(r"C:\Users\lenovA\Desktop\1.jpg")
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)         
cv2.waitKey(0)
cv2.destroyAllWindows() 

''' read is used to read the image
    --show-->display the image
    --im-->image
    --namedwindow-->is used to fit the image to the size of the window and contain all the properties of the normal window
    --waitkey-->is the time to show the image
'''

#write the gray scale image

#[0 0 0]--white

#[255 255 255] black


import cv2
img=cv2.imread(r"C:\Users\lenovA\Desktop\1.jpg")
g=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
cv2.imshow("gray",g)
cv2.waitKey(0)
cv2.imwrite(r"C:\Users\lenovA\Desktop\123.png",g)   

#blur the image

import cv2
image=cv2.imread(r"C:\Users\lenovA\Desktop\1.jpg")
img=cv2.blur(image,(5,5))
cv2.imshow("blured image",img)
cv2.namedWindow("blured image",cv2.WINDOW_NORMAL)
cv2.waitKey(0)
cv2.destroyAllWindows()

#edge the image

import cv2
img=cv2.imread(r"C:\Users\lenovA\Desktop\1.jpg")
g=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("edge",g)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
morphological operation are a set of operation based on shapes of image 
    --erosion and dilation to remove the noise
'''

import cv2
import numpy as np
img=cv2.imread(r"C:\Users\lenovA\Desktop\1.jpg")
kernel=np.ones((3,3),np.uint16)
erosion=cv2.erode(img,kernel,iterations=0)
dilate=cv2.dilate(img,kernel,iterations=0)
while True:
    cv2.imshow("image",img)
    cv2.imshow("erosion",erosion)
    cv2.imshow("dilation",dilate)
    k=cv2.waitKey(33)
    if(k==27):
        cv2.destroyAllWindows()
        break

'''video processing
     --the argument in videocaptue 
         0-->local camera
         1-->external camera
         url-->captured video
   ''' 

import cv2
vdo=cv2.VideoCapture(0)
while True:
    ret,fame=vdo.read()
    print(fame)
    cv2.imshow("video",fame)
    cv2.resizeWindow("video",600,600)
    k=cv2.waitKey(33)
    if(k==27):
        cv2.destroyAllWindows()
        vdo.release()
        break
    
#object detection
     
from imageai.Detection import VideoObjectDetection
import os
import cv2
execution_path=os.getcwd()
cam=cv2.VideoCapture(0)
while True:
    k=cv2.waitKey(33)
    if(k==27):
        cv2.destroyAllWindows()
        vdo.release()
        break
    else:
          detector=VideoObjectDetection()
          detector.setModelTypeAsYOLOv3()
          detector.setModelPath(os.path.join(execution_path,'yolo.h5'))
          detector.loadModel()
          video_path=detector.detectObjectsFromVideo(camera_input=cam,output_file_path=os.path.join(execution_path,"camera_detected_1"),frames_per_second=29,log_progress=True)
          print(video_path)