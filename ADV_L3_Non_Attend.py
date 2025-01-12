#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In the name of GOD


Created on Sun Nov 17 17:39:06 2024

@author: Ali Pilehvar Meibody


ADV_L3_Non_Attend

"""


#------------
a=25

message='salam man a salame'
print(message)
#salam man a salame


#f string

message=f'salam man {a} salame'
print(message)
#salam man 40 salame
#salam man 25 salame

#---------------------


code=input('Salam code mahsool ra benevisid :')
name=input('lotfan esme mahsool ra benevisid : ')
price=int(input('lotfan gheymat ra benevisid: '))




message=f"""
Etelaate mahsooole shoma :
    
code mahsooletoon:  {code}
name mahsooletoon: {name}
gheymate kol: {price} toman
    
"""


print(message)



#----AGAR ---> if 


'''
#koja estefade mishe? harja haref agar omd

agar felan shod felan karo kon
agar shart1 shod dastoore 1 ro bokon

agar anshod nashod chi? velesh kon


if tak 




if shart1:
    dastoore1






'''



a=40

if a>20:
    print('bale')



a=10

if a>20:
    print('bale')

#hichiiiii


#2 ta nokte **** fght ye dastoor? sadta datso


a=40
if a>20:
    print('bale')
    b=a+20
    print(b)
    print('tabrik')
 
    
 
    
    
#4 ta dastoooor

#harchar ta dastoor bayad koja bashe?? tooye badaneye if




a=10
if a>20:
    print('bale')
    b=a+20
    print(b)
    print('tabrik')
 
    
 
    
 
    
 
a=40
if a>20:
    print('bale')
    b=a+20
    print(b)
    print('tabrik')
 
    
print('khodafez')
    
 
    
 
    
 
a=10
if a>20:
    print('bale')
    b=a+20
    print(b)
    print('tabrik')
 
    
print('khodafez') #biroonbe sharte yaniii 
#tab chra mohme
    
 
#---- 1* --. chanta dastoor mitonid ejr akonid
#-----2*-->chanta shart ro baham check koni

a=10
b=20

#ham a bayad bozorgtr az 5 abshe ham b ---> ha;a dastoor ro anjam bde
if a>5 and b>5:
    print('salam')
 
    
 
#haddeghal yekish y aa ya b ag joftesham bashe
    
if a>5 or b>5:
    print('salam')
    
    
'''

agar felan shod felan karo kon
ag sharte 1 shod dastoore 1 ro ejra kon

ag nashod chi? hich bma che


if shart1:
    dastooor1
    
    
#advanced
if shart1 and(or) shart2 and(or) shart3 .....:
    dastoor1
    dastoor2
    dastoorr.......



#else???
dorahiii doro skoni
agar shart1 shod dastore 1 ro anjam bde ag nashod dastore 2

ag shod inkaro agh nashod oonkaro
(2 shakhe , 2 rahi)

if else


if shart:
    inkaro
else:
    oonkaro


#if shart , 
#** if els ebayd zire ham abshan 
#karha dastoroat , inkaro (dastoroe true )  (false)
#too badane


'''
    
  #ghalat *******  
if a>20:
    print('salam')
    else

if a>20:
    print('salam')
else:
    print('khodafez')


#inja ham mitoni ham chanta shart bzari ham chanta dastoor
'''
advanced


if shart1 and(or) shart2 and(or) shart3.....:
    dstoor11
    dastoor2
    .....
else:
    dastoor1
    dastoor2
    ,......
    
    
   



'''

#print --> mige
#input --> migire


#----CODE , NAME , PRICE --> HAMEW INA RO BAHAM NAMAYEHS MDIAD
#be karbar bege confirm mikoni taewed mikone
#ma baya dbgirim az karbar yes no

code=input('Salam code mahsool ra benevisid :')
name=input('lotfan esme mahsool ra benevisid : ')
price=int(input('lotfan gheymat ra benevisid: '))




message=f"""
Etelaate mahsooole shoma :
    
code mahsooletoon:  {code}
name mahsooletoon: {name}
gheymate kol: {price} toman
    
"""


print(message)


answer=input('aya confirm mikoni ? yes or no :')

if answer=='yes':
    print('sabt shod')
else:
    print('motasefane sabt nashod')



a='Yes'
b='yes'
print(a==b)
#False

#Yes yes




#---------------



#yES
#YES
#Yes
#yes

answer=input('aya confirm mikoni ? yes or no :')

if answer.upper()=='YES':
    print('sabt shod')
else:
    print('motasefane sabt nashod')



#----moshekle badi -->  yes

a=' yes'
b='yes'


len(a) #4 space y  e  s
len(b) #3 y e s
print(a==b)
#False


#str --> strip()


a='    salam'

b=a.strip()

print(b)
#salam

#faseley ghabl va bad 




answer=input('aya confirm mikoni ? yes or no :')

if answer.upper().strip()=='YES':
    print('sabt shod')
else:
    print('motasefane sabt nashod')
    
    
    

    
#----------------final from previous lecture (L2)-----
code=input('Salam code mahsool ra benevisid :')
name=input('lotfan esme mahsool ra benevisid : ')
price=int(input('lotfan gheymat ra benevisid: '))


message=f"""
Etelaate mahsooole shoma :
    
code mahsooletoon:  {code}
name mahsooletoon: {name}
gheymate kol: {price} toman
    
"""

print(message)

answer=input('aya confirm mikoni ? yes or no :')

if answer.upper().strip()=='YES':
    print('sabt shod')
else:
    print('motasefane sabt nashod')
    



#------------doostan
adad=input('adade avalo bzn:')

print(adad)

new_adad=adad.strip()

new_new_adad=int(new_adad)



adad=input('adade avalo bzn:')
new_adad=int(adad.strip())

#----do adad va yek amalgar az karbar bgire

adad1=input('adade 1 ro vared konid:')
adad2=input('adade 2 ro vared konid:')
amalgar=input('amalgare more nazar ro vared konid')


if amalgar.strip()=='+':
    result=int(adad1.strip()) + int(adad2.strip())
    print(' natiej :',result)
    
    
elif amalgar.strip()=='-':
    result=int(adad1.strip()) - int(adad2.strip())
    print(' natiej :',result)
    



#----AVANCED
#BA YEKBAR FGHT AZ KARBAR BGIRE 4+6....... jalase ayande

javab=input('maodelat ro benevis:')



#-------------------
adad1=input('adade 1 ro vared konid:')
adad2=input('adade 2 ro vared konid:')
amalgar=input('amalgare more nazar ro vared konid')


if amalgar.strip()=='+':
    result=int(adad1.strip()) + int(adad2.strip())
    print(' natiej :',result)
    
    
elif amalgar.strip()=='-':
    result=int(adad1.strip()) - int(adad2.strip())
    print(' natiej :',result)
    
#----> ta jaee ke shoam exit
#-----------------------------

    
    
    
    
    
    
code=input('Salam code mahsool ra benevisid :')
name=input('lotfan esme mahsool ra benevisid : ')
price=input('lotfan gheymat ra benevisid: ')

#tabe e bename isdigit()

#tabe --> str upper lower find isdigit
#agar adad bashe --> true , false



message=f"""
Etelaate mahsooole shoma :
    
code mahsooletoon:  {code}
name mahsooletoon: {name}
gheymate kol: {price} toman
    
"""

print(message)



answer=input('aya confirm mikoni ? yes or no :')

if answer.upper().strip()=='YES':
    print('sabt shod')
else:
    print('motasefane sabt nashod')
    



#eroor kole barnamato mikhabone
#ahrchi joz adad zad
#behesh bege 
#fingilish--> lotfan adad vared konid


#----------

price=input('lotfan gheymat ra benevisid: ')

#tabe e bename isdigit()

#tabe --> str upper lower find isdigit
#agar adad bashe --> true , false


new_price=price.isdigit()
#print(new_price)


#agar if #agar adad bood 

if new_price==True:
    price=int(price)
else:
    print('lotfan adad vared konid')


#ta zamani ke 
#while
#for


#----if
#agar......




#---------for

#----> for 
#1--> tekrar -> 100 bar , 1 ta 100 , 1ta100 ,....
#2---> beri tooye iterable (list, str) begardi doone dooen ozver --> iteration 


'''




for yekchiz in yek baze:
    dastooor (dastoor)



'''



for i in range(0,10):
    print('salam')



'''
i
range
i=0 dastoro ejr amikone
i=1 dastoora ejra mikone
i=2 dastooro ejra mikone
......



'''


for i in range(0,10):
    print(i)

'''
0
1
2
3
4
5
6
7
8
9
'''



#---range 0 -- > 10-1 =9

#while ---> payanesh maloom nis fixed 
#balke shart payan bzarim




#-------------
#aval
'''
sakhatresh

shoamrande = adade avalie


while shart:
    dastoooor
    shoamrande ro ziad mikoni



az 0 ta zamani k i <6 --> dastoori ejra kon







'''
i=0


while i<6:
    print('salam')
    i=i+1


#endless ->halgheye bi payan
#



i=0


while i<6:
    print(i)
    i=i+1



#--------------------------
#dar asl --> for o while shabihan

i=0
while i<6:
    print('salam')
    i=i+1



for i in range(0,6):
    print('salam')










i=0
while i<6:
    print(i)
    i=i+1


for i in range(0,6):
    print(i)




#khoobie while 
#fixed range
#ta zamani k masalan 



#khobie while zamani hast k shomaa 
#shoooma shart mitoni bzari baraye ekhtetame looop 
#barae payane loooppp

code=input('Salam code mahsool ra benevisid :')
name=input('lotfan esme mahsool ra benevisid : ')
price=input('lotfan gheymat ra benevisid: ')

price_is_digit=price.isdigit()
#agar true
#age na false mide


#ta zamani k in digit nis hey azash bpor hey azash bepors
#ag bod bia biron 


while price_is_digit==False:
    price=input('lotfan adad vared kon : ')
    price_is_digit=price.isdigit()
    
    
    


message=f"""
Etelaate mahsooole shoma :
    
code mahsooletoon:  {code}
name mahsooletoon: {name}
gheymate kol: {price} toman
    
"""

print(message)

answer=input('aya confirm mikoni ? yes or no :')

if answer.upper().strip()=='YES':
    print('sabt shod')
else:
    print('motasefane sabt nashod')
    




#-----------nokte

#--->while se ghesmat dare

'''

a)shomarande ro tarif koni
b)shart bezari
c)afzayesh bdish


i=0
while shart:
    
    i=i+..




'''

#behtarin halat

i=0
while i<10:
    print('salam')
    i=i+1







#----i ro nnvisim
#step a ro ejra nkonim
while i<10:
    print('salam')
    i=i+1
#NameError: name 'i' is not defined
#start





#-----gehsmat b 
#sharteto joori bnvisi k asan shoro nashe
#while varede halgeh nmishiiiii

i=20
while i<10:
    print('salam')
    i=i+1
    


#ghesae c shoamrande n
#endless looop

'''
XXXXXXXXXXXXX

i=0
while i<10:
    print('salam')
    



ENDLESSS looop
'''




#------3 ta chiz hayatie
i=0 #a)aval bsaz i ro

while i<6 : #B0 shart bzar bre dakhelsh
    print('salam')
    i=i+1 #i ro afzayehs bde ta enlss nashe
    
    
    
#-----------------------------------

code=input('Salam code mahsool ra benevisid :')
name=input('lotfan esme mahsool ra benevisid : ')
price=input('lotfan gheymat ra benevisid: ')

price_is_digit=price.isdigit()
#agar true
#age na false mide


#ta zamani k in digit nis hey azash bpor hey azash bepors
#ag bod bia biron 


while price_is_digit==False:
    price=input('lotfan adad vared kon : ')
    price_is_digit=price.isdigit()
    
    



message=f"""
Etelaate mahsooole shoma :
    
code mahsooletoon:  {code}
name mahsooletoon: {name}
gheymate kol: {price} toman
    
"""

print(message)

answer=input('aya confirm mikoni ? yes or no :')

if answer.upper().strip()=='YES':
    print('sabt shod')
else:
    print('motasefane sabt nashod')
    
    
#---while


#---for #shart ndsht




for i in range(0,10):
    print(i)

'''

0
1
2
3
4
5
6
7
8
9

'''



#gahan

#3 ta kar konm
pass
break
continue



#yek sharti bzari too dele for 
#yek shart bzariii
#halgeh --> 10 ba ryekair
#agar i=4 
#agar felan shod 

for i in range(0,10):
    
    if i==5:
        pass
        
        
    
    print(i)
    print('salam')


#az 0 ta 9 10 bar slaam bnvise
#io=5 ye kare dg kone

#continue
#break




#yechizio behsmori ta yeja
#age shod 5 break koni biay bironnn


#for 2 ta dalil
#1----> tekrar
#2---> varresi iteration


a=[10,20,30,40,50,60]



for i in a :
    print(i)
    
    
'''
10
20
30
40
50
60
'''



a=[10,20,-30,40,50,60]

len(a) #6


#0 1 2 3 4 5 
for i in range(0,len(a)):
    if a[i]<0:
        print('manfi')
        
    else:
        print('mosbat')
    
'''
mosbat
mosbat
manfi
mosbat
mosbat
mosbat

'''
    

#asan edame nadee bia birooon
#halgeh ro vel kon


a=[10,20,-30,40,50,60]


for i in range(0,len(a)):
    if a[i]<0:
        break
    else:
        print('mosbat')
    
    
    
#continue
#fght mosbataro print kon



a=[10,20,-30,40,50,60]
for i in range(0,len(a)):
    print(a[i])
    
'''
10
20
-30
40
50
60

'''

a=[10,20,-30,40,50,60]
for i in range(0,len(a)):
    if a[i]<0:
        break
    print(a[i])

'''
10
20
'''
    
    

a=[10,20,-30,40,50,60]
for i in range(0,len(a)):
    if a[i]<0:
        continue
    print(a[i])
    
'''
 10
 20
 40
 50
 60
 
'''



code=input('Salam code mahsool ra benevisid :')
name=input('lotfan esme mahsool ra benevisid : ')


#ta abad maid hey mige
#Lotfan gehymat ra benevisid
#
while True:
    price=input('lotfan gheymat ra benevisid (adad bezanid): ')
    price_is_digit=price.isdigit()
    if price_is_digit==True:
        break
    





message=f"""
Etelaate mahsooole shoma :
    
code mahsooletoon:  {code}
name mahsooletoon: {name}
gheymate kol: {price} toman
    
"""

print(message)

answer=input('aya confirm mikoni ? yes or no :')

if answer.upper().strip()=='YES':
    print('sabt shod')
else:
    print('motasefane sabt nashod')
    


#================================================

#================================================

#================================================

#================================================
#-----JALASE BADI--------
#================================================

#================================================

#================================================


#agar taraf farsi zad 
#englisi namayesh bde


code=input('Salam code mahsool ra benevisid :')
name=input('lotfan esme mahsool ra benevisid : ')

price=input('lotfan gheymat ra benevisid (adad bezanid): ')


message=f"""
Etelaate mahsooole shoma :
    
code mahsooletoon:  {code}
name mahsooletoon: {name}
gheymate kol: {price} toman
    
"""

print(message)

answer=input('aya confirm mikoni ? yes or no :')

if answer.upper().strip()=='YES':
    print('sabt shod')
else:
    print('motasefane sabt nashod')
    
    
#adade farsi ro --> englisish kone

'''


for , if 


'''

    
    
