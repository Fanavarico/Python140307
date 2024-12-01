
"""
In The Name Of GOD

L2_NON ATTEND 


Created on Sun Nov  3 17:53:05 2024

@author: apm

"""


print()
#yek karaee dre

print('salam')



#input--> 

len('salam') #5


print('salam')

input('salam shomaratono benevisid:')

a=132234
type(a) #int

a=14.5
type(a) #float

a=1j
type(a) #float

a='ali'
b='salam arz shod'
type(a) #str
type(b) #str

#len andaze ye yek 

a='ali'
len(a) #3

name='alipilehvarmeibody'
len(name) #18


#hameye built in funciton
#https://docs.python.org/3/library/functions.html


#abs -->absolute -->motlagh

a=-10

abs(a) # 10



#------
#keywords----> manteghi agar , tekrar , halghe 

if

else:

for

while



#banafsha
#if --> agar
#for , while --> tekrar 




#harchize dg ee benevisi inaj --> yek zarf dar nazar migire
#sefides-->zarf -->variable (moteghayer) megdhar (value brizi)

#
'''
reserved --> python built in funciton ( print9) , keywords (if , else, for ,...)
not reserved --> 

dakhele in zarf ha (variable)

1.numbers (int,float , complex)
2.bool (True , False)
3. string --> reshte ( harf, character, kalame, jomle)


'''

numb=10

numb=10.145
ghad=180
vazn=86


#-->reshte string -> str
#tarkibi az horood, harchizi ktoo keyboardet
#space , chaartcter *  & 1 32 54

#yek note*** --> ' ' 

name=ali
#NameError: name 'ali' is not defined


#zarf bename name besaz , toosh 
name='ali'

name='ali '

name='ali* & '

sentence='salam doostan man ali hastam dar khedmate shoma hastam'


a=4
b='4'


#typeshon frgh dre 
#avali int has (sahih)
#dovomi str --> rehste

print(type(a)) #<class 'int'>
print(type(b)) #<class 'str'>




c=b+2

#operators --> amalgar
#+ jam
#- menha
#* zarb
#/ taghsim
#** tavan  2 be tavane 3   2**3

#()

#olaviat ha
'''
4*5**2-4+32

AVAL TAVAN
bad zarb | taghsim
bad jam | tafrigh


() parantez

(4*5)+ (3**4)

'''
#operator-->mohasebta beyne adad

#ina fght baraye adad
b='4' #keyworde 4 reshte e az 4

c=b+2


#-------


#vuilt in funciton
print()
input()
len()
type()

#****
#1*--> baraye hame type estefade mishe

print(14)
print('salam')


type(14)
type('salam')


#esme tabeye dkahel minevbisi parnatez ()

#print()





#==========****==========
#strr--.string (reshte)
#yekseri tabe daran k mokhtase khdoeshonan
#ber khdoeshon 
'''
capitalize()        	Converts the first character to upper case
casefold()	   Converts string into lower case
center()  	Returns a centered string
count()	     Returns the number of times a specified value occurs in a string
encode()   	Returns an encoded version of the string
endswith()   	Returns true if the string ends with the specified value
expandtabs()  	Sets the tab size of the string
find()    	Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	     Formats specified values in a string
index()	       Searches the string for a specified value and returns the position of where it was found
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
join()	Converts the elements of an iterable into a string
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
#----az bala mohem trina ro mig


#upper()


#print , .. python built in funciton (tab ehaye dakheli)
#upper, lower, find , --> str function (tabe haye str)

name='ali'


print(name)

#upper(name) ghalateeeee
#aval esme moteghaye
#dot mzini (nogthe )
#bad esme tabe


name.upper() # 'ALI'


name='ALI'

name.lower() #'ali'



name.replace('A','B') #'BLI'



#. 

#sklearn ------
#codi k minevisim migan scripts --> madule
#sklearn (lib) --> multiple madule --> tabe hast

#tabe --> MLP()

MLP()

#AVA

#ketabkhone-->madule --> class --> def 

#sklearn.neural_newtrok.MLP.


name='ali'

#str--clas
#koli tabe too delesh


name.upper()
#


#---inaro vel kon


#python buil in funciton
#tabe
#esme tabe () --> ********** call


print()
input()
len()


#str function ---> !** ina dfght baraye str hastan
#in shekli
#bayad biay 


#rooey variable . esme tabe ()



name='ali'

upper(name) #na naaaaaa

name.upper()

name.lower()

#replace

sentence='salam *  khobi * chetory'

a=sentence.split(',')

#a=sentence.split('*')

a=sentence.split('*')



#-----------
#index
a='ali'



#access dastressi

#esmo benevisi []

#kodom variable (zarf)
#chandomishhh

a[]

#3 nanevisi



#****** index ha az 0 shoro mishe



#a--> indexe 0
#l -->indexe 1
#i --> mishe indexe 2


name='alipilehvar'


name[0]  # 'a'

#charomin harf --> 4-1 = 3 vomin index

name[3] #'p'


#access by index


#slicing
#az ch indexi t ach indexi
#az 3 mikham 
#10 --> 10+1
#: ta
name[3:11]
 #'pilehvar'
 
 
name[3:11]

#az 3,4,5,6,7,8,9,10


#advanced-----
name[3:11]

name[3:11:1]
#start : end +1 : step

#3 , 5 , 7 , 9 ,
name[3:11:2]
#'plha'




#hosele nadari ta tah beshmori
#ya az aval bshmori


name[0:7]

#az aval 
name[:7]


name[4:]
#nanvisi mifhme k manzoret ta akahre




#str dfucntion
#upper
#lower
#split()
#find


name='ali'

name.find('a')


#Kdoom index , a hast

#0


name='alia'

name.find('a')

#0
#avalin jaee k oon horofo mibine bht idnexesho mide

#coutn


name.count('a')
# 2



message=' salam'

message2='salam'



print(message==message2)


#---- = ==


'''

= --> felan chiz ba felan chiz barabrehs kon ddastoor midi


== --> miporsi --> aya flean chiz ba felan chiz barabare?
!=
<
>
amalgar haye ghiasi
'''



#yes 
message=input(' aghaye user confirm mikoni?')

message=message.lower()


if message=='yes':
    print('kharide shoma sabt shod')

else:
    print('motasefane sabt nashod')
    
    
#kharide shoma sabt shod
    

#2 rah dari

#for ,k ......
#str function... lower() upper()


#koochik
message=input(' aghaye user confirm mikoni?')

message=message.lower()


if message=='yes':
    print('kharide shoma sabt shod')

else:
    print('motasefane sabt nashod')
    



#bozorg

message=input(' aghaye user confirm mikoni?')

message=message.upper()


if message=='YES':
    print('kharide shoma sabt shod')

else:
    print('motasefane sabt nashod')





message=input(' aghaye user confirm mikoni?')

message=message.upper()


message=message.strip()

#space ebtedaee , entehasee hazf mikone

if message=='YES':
    print('kharide shoma sabt shod')

else:
    print('motasefane sabt nashod')



#herfe ee ta rbenevisim

 
a=' salam'
b=a.strip()
print(b)

#-------------------------
#Q1--->  yes   yes  with space
#kharide sat shod



#Q2--->


product=['sh2','mac',1000]


product=['sh3','apple',1000]

#product --> ['code','name',price]

message='''
Your product information:
    
product code:
    
product name:
    
product price:


'''


print(message)



'''
Your product information:
    
product code: sh1
    
product name: mac
    
product price: 1000


'''


product=['sh2','mac',1000]

print('product code:',product[0])

print('product name:',product[1])

print('product price:',product[2])









product=['sh2','mac',1000]



message='''





'''


print(message)



#f string



sen=30


print('salam man ali hastram man 30 salame')



sen=10

print(f'salam man ali hastam man {sen} salame')


#f string + {}


print('salam man ali hastam man sen salame')


print(f'salam man ali hastam man {sen} hastam')





product=['sh2','mac',1000]

product=['sh10','nvidia',11000]


code=product[0]
name=product[1]
price=product[2]


message=f"""
product informations:

    
product code : {code}
product name : {name}
product price : {price}


You can order now...


"""


print(message)






'''
product informations:


product code : sh2
product name : mac
product price : 1000


You can order now...

'''



'''
product informations:


product code : sh10
product name : nvidia
product price : 11000


You can order now...

'''


#--advanced
product=['sh2','mac',1000]

product=['sh10','nvidia',11000]




message=f"""
product informations:

    
product code : {product[0]}
product name : {product[1]}
product price : {product[2]}


You can order now...


"""


print(message)


#===================
#application
# codesho bgo
#emesho bego
#gheymatesho bgfoo

#agha jan aya taeed mikoni etalt vase kharid




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

answer=input('Aya mahsoole kharidari shdoe ra taeed mikonid? ba yes ya no javab dahid')

if answer.upper().strip()=='YES':
    print('tabrik migam kharide shoma sbat shod')
    
else:
    print('motasefane kharide shoma sabt nashod')


#framwork -->ssite, application ,.....


#------------------------
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

answer=input('Aya mahsoole kharidari shdoe ra taeed mikonid? ba yes ya no javab dahid')

if answer.upper().strip()=='YES':
    print('tabrik migam kharide shoma sbat shod')
    
else:
    print('motasefane kharide shoma sabt nashod')
    
   
    
#str , str function
#built in fucntion , .....
#list.....


#------LIST, 10 min tabe hash append,...
#IF , ELSE, FOR
#def --> tabe 








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

answer=input('Aya mahsoole kharidari shdoe ra taeed mikonid? ba yes ya no javab dahid')

if answer.upper().strip()=='YES':
    print('tabrik migam kharide shoma sbat shod')
    
else:
    print('motasefane kharide shoma sabt nashod')
    


#ValueError: invalid literal for int() with base 10: 'sad toman'

#aval input grft
#check krd did adade ya na
#ag adad bood --> int
#ag nabood userpayam bde bege adad vared kon

#--QUIZ JALASE BADET

#adado fartsi bezanam chi????
#yes --> تایید


#



#a A .
#farsi support mikone




'''
Q1--> adad ag vared nakard --Price -_>bege lotfan adad vared kon (hint --> isdigit())

Q2--> age bejaye gheymjat --> farsi vared krd ? --> tabdil b englisi

Q3--> process--> persian (parsi benevisid)





'''








