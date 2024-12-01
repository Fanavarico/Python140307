#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In the nAME OF GOD
Created on Sun Dec  1 17:36:21 2024

@author: Ali Pilehvar Meibody

ADV_L4_Non_Attend

"""


'''

Review FAST

Python -->  human | computer

3 component 


1--> python built in function --> print() input() len() type() ,...
2--> keywords --> manteghi , structure --> if , else , while , for , def , ...
3--> Variable (zarf --> dakhelesh megdhar (value) zakhire koni)



variables --> zarf --> chan no?

1--> numebrs (int, float, complex) int 123 121  float --> ashari 2.43 2.43 i j
operations --> 
olaviateshon
**
* 
/
+
-
= 

a=2
c=a+b


% baghimande (zoj o fard)



c=10**2*3+4

aval 
10**2 -->100
100*3 = 300
300+4 --> 304



2--> Boolean Bool --> True False
amalgar haye moghayese
==
#miporsi 
a=b --> zarfe a ro , hrchi too b beriz to a

a==b --> dastoro nsit, porseseh aya a ba b barabar ast

>

<

=>
=<

soal porsidim -->montazerte javabim
javab-> True , False


3-->str --> horof, character, kalame, jomle , ketab --> STR string reshte

name='ali'
ali[1]
#index --> az 0 shoro mishod


str functions --> amalkardi baraye str ha anajm mide

name='ali'
name.upper()
name.lower()
name.replace('a','b')
name.find('a')


#-------done done , yedoen adad , yedoen horof 
#-->chanata chizi zkahire konm?---> 
list, tuple , dict , set
#---> mitone chantaa joz ra dakheel yek zarf zakhri ekone

a=[10,20,30,40]

b=[10, 'ali',True, 4.33 , 1j]

list function

b.append('vahid')
b.remove()
b.pop()

tuple , set--> tekrari nemigrfte, changable , 

dictionary --> key : value


'''


print('slaam man ali hastam 20 salame va avale esmam a hast')


#slaam man ali hastam 20 salame


#sen-->
a=20


print('salam man ali hastam a salame va avale harfam a hast')

#salam man ali hastam a salame va avale harfam a hast


# '' """ """

#dakheelsho hamaro horof ekeyborad
#a -->
#python --> ravesh f string


#---1--> poshte qout '' f''

a=20
print(f'salam man ali hastam a salame va avale harfam a hast')

#salam man ali hastam a salame va avale harfam a hast

#---2--
#oon variabli k mikhay seda koni ro tooye {}

print(f'salam man ali hastam {a} salame va avale harfam a hast')

#salam man ali hastam 20 salame va avale harfam a hast



a=40
print(f'salam man ali hastam {a} salame va avale harfam a hast')
#salam man ali hastam 40 salame va avale harfam a hast



#---------------------------------
#----------------------------------

'''
Programming 

Karfarma (too sherakat, porozhe, khodet yek idea, ostadi )

yek kari mikahd kone (yek chizi too zheneshe)

ye mahsin hesba mikham besazam 
yek product manager mikham besazam


yek chat bot ai-based (chatgpt)


dastoor---> zabane neglish (farsi) ensani ----> python 

keywords h hatsna k komakety mikonan



vaghty dari translate mikoni ag in kalamat omdn azin keyword ha estefade kon





#----------------------
begiree --> input()
namayesh bede --> print()

agar --> if 


'''

'''

if shart:
    dastooor

'''


'''

if shart1 and/or shart2 ......:
    dastooor1
    dastoor2 
    dastoor3



if --> yek shart darim
agar sharte--> anajm bde
ag nabood rrad kon


'''



a=20


if a>40:
    print('salam')
    print('khosh amadid')




#------



a=20


if a>40:
    print('salam')
    
    
    
print('khosh amadid')




#--------------------

'''
shart bzari yeja
kalamey e agar


senesh -->

agar bishtar az 40 bod --> bnego khosh amadid

shart --> yek kar


if



if shart:
    ........
    .....

'''


sen=int(input('salam senet chande?'))



if sen>18:
    print('mojaz hastid')
    

#ye tab --> 4 ta space 

#chanta?



    







sen=int(input('salam senet chande?'))



if sen>18:
    print('salam')
    print('mojaz hastid')
    print('khsoh amadid')






#-------------


sen=int(input('salam senet chande?'))



if sen>18:
    print('salam')
    print('mojaz hastid')
    
    
print('khsoh amadid')


#---agar , 



'''
#----------------------
begiree --> input()
namayesh bede --> print()

agar --> if 

agar (shart) yek dastoor --> if  [mesal: agar bala 18 -> mojaz]agar nabod? bemache


agar (shart) 

derakh do gehsmat 

bala 18 bdo bego mojazi paeen bod negoo mojaz nisis

shart dastoor (true) dastoor (false)

if else

'''


sen=int(input('salam senet chegahdre:'))


if sen>18:
    print('salam')
    print('khosh amadid')
    
else:
    print('salam')
    print('shoma mojaz nistid')
    


print('Shekate fanavari CO 2024')



#-------------------------
sen=int(input('salam senet chegahdre:'))
#shart --> badesham shart
#age naboood --> 

#ag bodo--> bala 18 ---> 
#else--> afaradi k zire 18

#---> age bala 15 ---> 18 - 15
#----> xzire 15

if sen>18:
    print('salam')
    print('khosh amadid')
    
elif sen>15:
    print('shoma nazdik b mojazi')
    
else:
    print('shoma aslanmojaz nisi')


print('Shekate fanavari CO 2024')



'''
Programmer Logic


begiree--> input()
namayesh--> print()
agar dastoro--> if
agar va do dastoro else --> if else
shart , badesh shart haye dg---> if elif else
tekrar ---> for , while

agar varresi --> iteration --> list, str --> for [ namayesh , shoamresdh, list]
ag mikhay yek kari ro ta zamanii anjam bde hey anajm ta zmani -> while true

'''


#10 salam
'''
while
shomarande tarifesh koni
shart --> while i<10
dastooor
dakhele dastoro afzayeshesh i=i+12

'''
i=0

while i<10:
    print('salam')
    i=i+1
    
    
    
for i in range(0,10):
    print('salam')
    
    
    
products=['zara','breshka','nike']

#be ezaye har jozi k tooye in liste maid i mizre

#i --> zara
#breshak
#nike

#to o i --> har kair bkhay koni

for i in products:
    print(i)
    
    
#--------------------------------



numbers=[10,123,234,42,343,22,232]

#for i in numbers:
    
    
#

#--------------
'''
liste numbrs darim

1--> adadi k zojan ro namayesh bde
2--> adadi k zojan ro beshmore
3--> adadi k zojan ro joda kone



varrwesi 3

namayesh bdee


'''


numbers=[10,11,20,23,30,35]


#varresii
#zoj


# % --> baghimande

#har adio % 2 --> 0 zoj
#fard





numbers=[10,11,20,23,30,35]

#baraye har joz k dar liste done doen biar biron
for i in numbers:
    #oon i ro boro taghsim bar 2 kon agar baghimondash 0 shod
    if i%2==0:
        #yani oon i zoje
        print(i)
        
'''
10
20
30

'''




#beshmoriiii

numbers=[10,11,20,23,30,35]


count=0

for i in numbers:
    if i%2==0:
        #print(i) bejaye print
        #count=count+1
        count+=1

print(count)
#3


#----ye list az zoj haro behem bede


numbers=[10,11,20,23,30,35]

mylist=[]

for i in numbers:
    if i%2==0:
        #bejaye inke print
        #bejaye inke beshmori
        mylist.append(i)


print(mylist) #[10, 20, 30]

print(numbers) #[10, 11, 20, 23, 30, 35]


#-------
#-----> ina tooye estekhdam 


numbers=[10,11,20,23,30,35]

mylist=[]
for i in numbers:
    if i%2==0:
        mylist.append(i) #yek list misaze
        numbers.remove(i)
        
print(mylist) #[10, 20, 30]
print(numbers) #[11, 23, 35]
        
        
        
        
#-----> yeklist daram fardaro too ye list zojaro ye klist edg

numbers=[10,11,20,23,30,35]

mylist=[]
mylist2=[]

for i in numbers:
    if i%2==0:
        mylist.append(i) #yek list misaze
    else:
        mylist2.append(i)
        


#-------shartesh sade nis--> zoj fard

numbers=[10,20,30,40,45,50,60,70]

shart=True

for i in numbers:
    if shart:
        print()
        #namayesh---> print()
        #beshmor---> count=count+1
        #list azash bsaz .append()
        #remove --> .remover()
        


#======================================


#------Sahebe foroshgah
#amazon -->tarahi amazonir

'''


karfaram zang mizane:
    agha ye site mikham mese amazon --> amazonir
    website baid az shaebe foroshagh
    name mahsol , code , gheymat ro begire
    bad behesh nehsoon bede
    bad ag taeed krd bege sabt shod
    
'''



'''

programmer

persian (fingilish) -->python language





'''

name=input('salam name mahsooleton ro bedid:')
code=input('lotfan code mahsoole morede nazar ro tarif konid:')
price=input('lotfan gheymate moshakahs shdoe ro tarif konid:')


text=f"""
-----*****------**-------
Product Informations


Product Name:{name}
product Code:{code}
Total:{price}
    
    
    
Plutus Co. 2024

"""

print(text)

answer=input('aya etelaate bala ra taed mikonid (yes/no) :')
#real world --> input --> 
#telegram bot --> 

'''
inlinekeywords=[INLINEKEYWORDS['YES'],INLINEKEYWORDS['NO']]
await update.message.send_message('Aya etelaate bala ra teed mikonid?',user_kyword=inline)



pyslide pyqt 
Tkinter 
#-->desktop app
#QT --> bozorgi C++

#GUI --> graphical user interface

pyslide.label('aya eteallate bala ra taeed mikonid?')
button_yes=pyslide.push_button('yes')
button_no=pyslide.push_button('no')
button_yes.style('Blue',40,)

'''



name=input('salam name mahsooleton ro bedid:')
code=input('lotfan code mahsoole morede nazar ro tarif konid:')
price=input('lotfan gheymate moshakahs shdoe ro tarif konid:')


text=f"""
-----*****------**-------
Product Informations


Product Name:{name}
product Code:{code}
Total:{price}
    
    
    
Plutus Co. 2024

"""

print(text)

answer=input('aya etelaate bala ra taed mikonid (yes/no) :')

if answer=='yes':
    print('sabt shod')



#age nevesht yes benevis sabt shdo ag nevehst no --> benevis motasefam




name=input('salam name mahsooleton ro bedid:')
code=input('lotfan code mahsoole morede nazar ro tarif konid:')
price=input('lotfan gheymate moshakahs shdoe ro tarif konid:')


text=f"""
-----*****------**-------
Product Informations


Product Name:{name}
product Code:{code}
Total:{price}
    
    
    
Plutus Co. 2024

"""

print(text)

answer=input('aya etelaate bala ra taed mikonid (yes/no) :')

if answer.strip().upper()=='YES':
    print('tabrik migam , sabt shod')
else:
    print('motasefane sabt nashod')
    
  
answer='yes'

answer.upper() # 'YES'


answer='     yes  '
len(answer) #10
new_answer=answer.strip()
print(new_answer)  #yes
len(new_answer) #3


#=======================================





name=input('salam name mahsooleton ro bedid:')
code=input('lotfan code mahsoole morede nazar ro tarif konid:')
price=input('lotfan gheymate moshakahs shdoe ro tarif konid:')


text=f"""
-----*****------**-------
Product Informations


Product Name:{name}
product Code:{code}
Total:{price}
    
    
    
Plutus Co. 2024

"""

print(text)

answer=input('aya etelaate bala ra taed mikonid (yes/no) :')

if answer.strip().upper()=='YES':
    print('tabrik migam , sabt shod')
else:
    print('motasefane sabt nashod')
    
    
    
    
    
    
#_----------------------------------------
    
    
name=input('salam name mahsooleton ro bedid:')
code=input('lotfan code mahsoole morede nazar ro tarif konid:')
price=input('lotfan gheymate moshakahs shdoe ro tarif konid:')






text=f"""
-----*****------**-------
Product Informations


Product Name:{name}
product Code:{code}
Total:{price}
    
    
    
Plutus Co. 2024

"""

print(text)

answer=input('aya etelaate bala ra taed mikonid (yes/no) :')

if answer.strip().upper()=='YES':
    print('tabrik migam , sabt shod')
else:
    print('motasefane sabt nashod')
    
    
    
    
    
    
price=input('lotfan gheymate moshakahs shdoe ro tarif konid:')
 
   
price='۱۲۴'
    
print(price)    #۱۲۴


#i--> adade
for i in price:
    print(i)
    
    
    
    
price='۰۱' 


price='۱۰'



price='۱۲۴'

new_number=[]

for i in price:
    if i=='۰':
        new_number.append('0')
    elif i=='۱':
        new_number.append('1')
    elif i=='۲':
        new_number.append('2')
    elif i=='۳':
        new_number.append('3')
    elif i=='۴':
        new_number.append('4')
    elif i=='۵':
        new_number.append('5')
    elif i=='۶':
        new_number.append('6')
    elif i=='۷':
        new_number.append('7')
    elif i=='۸':
        new_number.append('8')
    elif i=='۹':
        new_number.append('9')


print(new_number)

#['1', '2', '4']

#list---> str

#'124'


final_price=''.join(new_number)



    
    
print(final_price)

#124

    
   
    
   
    
   
    
   
    
#----------------
    #------**************************************
    
    
name=input('salam name mahsooleton ro bedid:')
code=input('lotfan code mahsoole morede nazar ro tarif konid:')
price=input('lotfan gheymate moshakahs shdoe ro tarif konid:')

new_number=[]

for i in price:
    if i=='۰':
        new_number.append('0')
    elif i=='۱':
        new_number.append('1')
    elif i=='۲':
        new_number.append('2')
    elif i=='۳':
        new_number.append('3')
    elif i=='۴':
        new_number.append('4')
    elif i=='۵':
        new_number.append('5')
    elif i=='۶':
        new_number.append('6')
    elif i=='۷':
        new_number.append('7')
    elif i=='۸':
        new_number.append('8')
    elif i=='۹':
        new_number.append('9')

final_price=''.join(new_number)

#pirce--->persian number
#final_price-->english number


text=f"""
-----*****------**-------
Product Informations


Product Name:{name}
product Code:{code}
Total:{final_price}
    
    
    
Plutus Co. 2024

"""

print(text)

answer=input('aya etelaate bala ra taed mikonid (yes/no) :')

if answer.strip().upper()=='YES':
    print('tabrik migam , sabt shod')
else:
    print('motasefane sabt nashod')
    
    
#side saheb owner shop owner

#moshatri 


    
#def-->tabve
#box -->vorodi --> box --> khoroji
    
    #yek ba rmano tarifr kon , dafe badi beja neveshtan sedam bzn
    
    
#

'''


persian_price --> BOX --> english

vorodii--> box --> khoroji



def name(vorodi1)


def name(vorodi1,vorodi2,....):
    dastooooor1
    dastoor2
    return khoroji

name(vrodoi)

'''
    
    
    

def persian_to_english_numb(price):
    new_number=[]

    for i in price:
        if i=='۰':
            new_number.append('0')
        elif i=='۱':
            new_number.append('1')
        elif i=='۲':
            new_number.append('2')
        elif i=='۳':
            new_number.append('3')
        elif i=='۴':
            new_number.append('4')
        elif i=='۵':
            new_number.append('5')
        elif i=='۶':
            new_number.append('6')
        elif i=='۷':
            new_number.append('7')
        elif i=='۸':
            new_number.append('8')
        elif i=='۹':
            new_number.append('9')

    final_price=''.join(new_number)
    return final_price

#sakhjtaro msiaze k hatja benevisi persian_to_english_numb


def confirmation(answer):
    if answer.strip().upper()=='YES':
        print('tabrik migam , sabt shod')
    else:
        print('motasefane sabt nashod')
    





#--------****----------------
#-----------**----------------


name=input('salam name mahsooleton ro bedid:')
code=input('lotfan code mahsoole morede nazar ro tarif konid:')
price=input('lotfan gheymate moshakahs shdoe ro tarif konid:')
final_price=persian_to_english_numb(price)
text=f"""
-----*****------**-------
Product Informations


Product Name:{name}
product Code:{code}
Total:{final_price}
    
    
    
Plutus Co. 2024

"""
print(text)
answer=input('aya etelaate bala ra taed mikonid (yes/no) :')
confirmation(answer)






#------

product_codes=['a1','a2','a4','a5']

'''
TASK 1-----------------------
name ro migire mese ghabl
code ro migire mese ghable
*** code ro mibien too product-codes hast ya na 

agar nabood--> bege motasefam
agar bood --> price ro bgire va edameeee



TASK2------------
Hamin task1 hast fght 
agar bood--> price ro nbegire
age nabood--> hey beporse m,, lotfan code jadid bedid , exit kharej she

'''






#------- ejaze nadari esm haye resrv shdoe bzri

#list=[]
#open=  

listt=[]
mylist=[]
openn=10


#adad

mylist2=[]

#2mylist=[]


#my house=100

#my_list


#Name not found

mylistt=[]

print(mylisttt)
#*** NameError: name 'mylisttt' is not defined

#harchi k sedsa mizni bayad ghablesh tarif shode bashe


print(z)
#*** NameError: name 'z' is not defined



yekish havasewt nist horofo



mylist=[10,20,300]
print(mylst)


print(z)
z=10

#tabe

print(persian_to_english)

def persian_to_english(text):
    new_text=f'translated from{text}'
    return new_text


#------- whi

while k<30:
    print('salam')
    k=k+1
    
'''