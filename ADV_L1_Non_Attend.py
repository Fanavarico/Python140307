"""
In The Name Of GOD
Created on Sun Oct 20 17:55:13 2024

@author: apm



"""



'''


Review------
machine (computer, laptob, mobile,...)--> 0,1 binary
human ( ensan) ---> English

Programming ---> ensan dastoro bede be machine
ertebat beyne machine human---> zabane vasete --> programming language


programming language( C, C++ ,JAVASCRIPT, PYTHON,....)-->
why python?--> website , security, narm afzar, hooshe masnoee, ......

python --> simple base-->



.....Python.....1-->aksare hite haro cover mikone 2-->xzabane base

1-->machine (yek fard --> faransavi (binary))
2-->ensan (human)--->(farsi)

programming goal--> ensan b machine dastoor bede

zabane vasete -->pythn (english)

2 ta chiz niaz
ham machinet --> python (install)
ham ensan -->python  (yad begirim)

--> yek narm afzar , interface --> bahash sohbat -->
IDE -->mohite toseye yekparche


wp,telegram, robika,....

IDE haye motefavet
vscode
spyder
jupyter
pycharm
atom
,.....

ANACONDA--> 3.11 python3
python4 -->
ANACONDA-->

hichi--> codamo (message)
run (send)




#---------focus-->zabane python----
zaban-->zaban-->farnsavi
vocab(kalamt)
grammar(dastoorat)

python built in function (tabe haye dekhaeli)
print() input() len() type() 
keywords
if else for while


kalamati k tarif shod ehast-->rangesh motefavet mishe
tarif nashode--> esme zarf -->esme variable


derakhte python --> 3 skahe
1--> python built in function (print,input,...)
2--->keywords --> if else elif for while ,....
3---> nemishanse reserved--> esme variable



3----> 3.1.int(10,20,30,23,33) 3.2.float(233.3443) 3.3.complex(1+j)
3.4str -----> (horof, character,akalme,jomle)

'''


print()
input()
for

ghad=3238
ghad=3238.4545
ghad='asahbak'

#------------------
#variable haro

#-------
'''
adad, horof -.zakhire
chanta hcizo zakhire konam chi>


'''



a=[10,20,30,40]
a=[10,'sds',True,1423.2 , 43j]

print(type(a))
#<class 'list'>

#----dastressi acess
#index
#az 0 --->
a=[10,20,30,40]

a[0] #10
a[1] #20

a[2:4] #akhariaro shamel nmishod

#---->tabe dasht



#=================================
#--->str string 

a='s'
a='salam'
a='salam khoobi'

#tabe ha darim k fght mokhtase strig ha hast
#va mityonim bahash manupulation ( string)

#upper

a='salam'
print(a) #salam

#a hameye horofo bozrog konm
a.upper()
#'SALAM'

b='SALAM'
b.lower()
# 'salam'

a='ali'
a.capitalize()
#'Ali'


#count

a.count('a') # 1


#find
a.find('i') #2


#replce

esm='batman'
#zarfet.replace(ghadimi,jadid)
esm.replace('t','h')
#'bahman'



#------strip()
#fasele ro hazf mikone az chap va rast

message=' salam khobi'
message.strip()
#'salam khobi'

's356'


message=' s356'


products=['s30','s32','s32']


print('s30' in products)
#True

print('s3024523432' in products)
#False

user_message=' s30'

print(user_message in products)
#False

user_message.strip()

#teelgram S30

user_message.lower()

#-----split()
jomle='salam man ali, hastam va kheyli khoshal, hastam'
b=jomle.split(',')


#---->
#------ format ostan, shahr, meydone, pelaket

user_message='tehran,tehran,felestin,40'
print(user_message)

address=user_message.split(',')
address[3]
#Out[28]: '40'


#rooye oon zarf, dot mziani esme tabe he()





'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''

#-------------
#int sahih
#float ashari
#complex 234j
#str reshte --> function (upper,lower, ...)



#lotfan ghadeton ro begid

ghad=input('lotfan ghadeton ro begid')
print(ghad) #180




#errror mide
ghad=int(input('lotfan ghadeton ro begid'))


#-------
print('lotfan adad vared kon')

#---str------

#az karbar ghadesho bgirm
#+100 --> ghade shoma dasr marikh

#irad
ghad=input('ghadetoon ro befarmaed:')
new_ghad=ghad+100
print('ghade shoma dar merikh:',new_ghad)

#tabeye input--> harchi bdi bsoorate str zakhire mikone


ghad=int(input('ghadetoon ro befarmaed:'))
new_ghad=ghad+100
print('ghade shoma dar merikh:',new_ghad)
'''
ghadetoon ro befarmaed:180
ghade shoma dar merikh: 280
'''

ghad=int(input('ghadetoon ro befarmaed:'))
new_ghad=ghad+100
print('ghade shoma dar merikh:',new_ghad)

#ValueError: invalid literal for int() with base 10: 'salam'



a=input('ghadetoon ro befarmaed:')

print(type(a))

#<class 'str'>
#<class 'str'>

#flashback
#180  adade sahihe type 
#'180'  str 180  + - ,....




a=180
b='180'
a+2
b+2 #TypeError: can only concatenate str (not "int") to str

#@tabeye input()-->hamvare str 12349843 ashasd

ghad=int(input('ghadetoon ro befarmaed:'))
new_ghad=ghad+100
print('ghade shoma dar merikh:',new_ghad)






ghad=input('gahdetoon chande')

if type(ghad)==str:
    print('lotfan adad bezanid')
    ghad=input('gahdetoon chande')
else:
    new_ghad=ghad+100
    print('ghade shoma dar merikh:',new_ghad)


#--------------
#tabe haye str --> daste kam migirim



ghad=input('adad begoooo')
print(type(ghad))
#salam--> <class 'str'>
#18--><class 'str'>
#adad ki zazsde nazade?

#str function --> isdigit()



ghad=input('adad begoo')
print(ghad.isdigit())

#salam --> False
#180-->True


ghad=input('ghadeto begooo:')

if ghad.isdigit():
    new_ghad=100+ int(ghad)
    print('gahde shoma dar merikh hast:',new_ghad)
    
else:
    print('lotfan adad vared kon')
    

#-------------------
#---str -->
#list---> 
#toosh zakhire koni
a=[10,20,30,40]
a=[10,'salam',True]

users=['user1','admin','user2']

users[0] # 'user1'

users=['user1','admin','user2','user3','user4']

users[1:4]
#['admin', 'user2', 'user3']

#nokteye index
#**1---> AZ0 SHORO MISHE
#**2--->AKAHRIARO SHAMEL NMISHE



#-------------list
#taber hayee
#list function


#append
users=['user1','admin','user2','user3','user4']


users.append('user8')

print(users)
#['user1', 'admin', 'user2', 'user3', 'user4', 'user8']

#insert
users.insert(3,'admin2')
print(users)

#['user1', 'admin', 'user2', 'admin2', 'user3', 'user4', 'user8']

#append miad b tahe list ezafemikone
#insert miad ye index ezzafe mikone


#---> remove
users.remove('admin2')
print(users)
#['user1', 'admin', 'user2', 'user3', 'user4', 'user8']

#esmo nmidoni

#indexe 3
users.pop(3)

#-----------------------
#---list----- 1
#1.1. access
mylist=[10,20,30,40]
mylist[0] #10
mylist[2:4] # [30, 40]

#1.2.add
#b tahesh
mylist.append(80)
print(mylist)
#[10, 20, 30, 40, 80]

#bgi felan idnex felan adad
mylist.insert(2,100)
print(mylist)
#[10, 20, 100, 30, 40, 80]


#1.3.remove
mylist.remove(40)
print(mylist)
#[10, 20, 100, 30, 80]

#indexi
mylist.pop(0)
print(mylist)
#[20, 100, 30, 80]


#1.4.change
mylist=[20, 100, 30, 80]

mylist[2]=200 #change
print(mylist)
#[20, 100, 200, 80]

#clear -->pak sazi kardan
#delete --> hazf kardan


#------clear
mylist.clear()

print(mylist) #[]
#vojod dare ama toosho khali krdim

mylist.append(200)
print(mylist)

#-----delete

del mylist
#del -->

print(mylist)
#NameError: name 'mylist' is not defined


#----------------------------
#list-->chanta ajza ro dar dele khodesh zakhir ekone

#list
#--> ordered , changable , allow duplicated
#--->inndex nazm , ghabele taghire , tekrari ham mitoni
mylist=[100,100,100,100]


#tuple-->
#---> ordered, unchangable, allow duplicated
a=(10,20,30)

b=(12)
print(type(b)) #<class 'int'>

b=(12,)
print(type(b)) #<class 'tuple'>


a=(10,20,30)
#20--80

b=list(a)

#b.append()
#b.remove()
b[1]=600
print(b)
#[10, 600, 30]

a=tuple(b)
print(a)
#(10, 600, 30)

#tuple-->list (taghir) -->tuple


#-
del a
#delete shod



#set------>
#unordered, unchanbgable ( add, rmeove), not allow duplicated

myset={'ali','vahid','reza'}
print(type(myset))
#<class 'set'>

#add
#index

#index

mylist=['ali','vahid','reza']


for i in mylist:
    print(i)
    


myset={'ali','vahid','reza'}
for i in mylist:
    print(i)

#index
#.pop()-->random pak mikone




myset={'ali','vahid','reza','reza'}

#------------------
#dictionary


#keys , values


a={ 'brand' : 'benz' ,
   'year': 1998 ,
   'city' : 'newyork'}

a.keys()
#: dict_keys(['brand', 'year', 'city'])

a.values()
#: dict_values(['benz', 1998, 'newyork'])

a.items()
#dict_items([('brand', 'benz'), ('year', 1998), ('city', 'newyork')])


a['city']='sanfransisco'

a['year']=1800

#add

a['color']='blue'


#=========================================
