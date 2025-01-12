
"""
In The Name Of GOD
Created on Sun Oct 27 15:36:49 2024

@author: apm

ADV_L2_Attend

"""

a='salam'

print(type(a))
#<class 'str'>






#---> str--> namayeshe matn


#----> koli function too deleshon has
#tabe -->function ......


#esme moteghayer (zarf) . esme tabe


name='ali'

#zarfi bename name
#toosh str (rehste) --> ali

print(name)
#ali



#--------
#upper
#lower
#isdigit
#replace
#split
#strip
#title



name.upper()
#'ALI'

name2='ALIPILEHVAR'

name2.lower()

#'alipilehvar'

name='batman'

name.replace('t','h')
# 'bahman'


#strip
#space chapo rasto hazf

code='  s15'
code.strip()
#'s15'



#split
text=' salam khobid, rooz bekheyr'
new=text.split(',')


text=' salam khobid, rooz bekheyr , man ali hastam'
new=text.split(',')



text=' salam khobid, rooz bekheyr , man ali hastam'
new=text.split('.')


text=' salam khobid. rooz bekheyr , man ali hastam'
new=text.split('.')

#----title
a='in the name of god'

a.title()
#'In The Name Of God'


#-----find
#horofe 
#a 

name='niaz'

name.find('a')
# 2



#---reshte ha (str)

#ali    index-->0 
#a-->indexe0
#l-->indexe 1
#i-->indexe 2

#-----------------------
#------
#nokte.....
print()
len()
type()
print(10) #10
print('salam') #salam


len('salam') #5

type(2) #int
type(True) # bool
type('salam') #: str

#--rangi--> hame chian, adad, list, str , ......


#--> upper, lower() ,find(),replace(),title(),....
#fgth baraye str *******



numb=20


numb.replace(0,1)
#AttributeError: 'int' object has no attribute 'replace'


#---> fght mokhtase strr hjastan

#rooye oon avriable dot . tabe ro benevis ()

name='ali'

name.upper()

name='alipilehvarmeibody'
name.count('a')
# 2

name.count('i')
# 3



#list functions-----

#tuple functions-----

#set functions-------




#--------*******
#function --> do daste
#1 datse --> kolian -->baraye haman--> python built in funciton (tabe haye dkaheli)
len()
type()
print()
input()

#esmesho minvisi () -->rangi 
#va mokhtase hamas



#dasteye 2--> function haee k fght baraye yekseri tyep hjasa
#str function
#llist function


#frgheshon ine-->ina mokhtase fght yek type hasan

#farghe mohem**
#rooye oon moteghyer dot bzni

upper(name) #in gahlateee

name.upper()

a='salam'

#in adade ya yek reshteye harfe


a=messsage.recieved

a.isdigit() #true #false


#if
if a.isdigit():
    #kareto anjam bdi
    
else:
    print('agha lotfan adad bezan')


#specifi va kahs --> l1 (ghabli)




#python built in function --> tabe haye dakhelie python -->




#-----------------
# 3 ta amsale hal str function
# 3 ta masale list function ha
# if , else , for --> pass, break , continiue



'''
Python






'''



#list--> [code , esm,price]
#namayesh--> mahsoole shoma : code , esm 



product1=['sh1','kiko lip2',40]
product1=['sh5','mac lip2',60]


'''
محصول شما :
    کد محصول : 
        نام محصول :
            قیمت :
                همین حالا میتوانید سفارش دهید

'''
code=product1[0]
name=product1[1]
price=product1[2]


text='''
محصول شما :
    کد محصول : code
        نام محصول :name 
            قیمت : price
                همین حالا میتوانید سفارش دهید

'''


print(text)




'''

product name : {esme_zarf}
{name}
{}


'''

text=f'''
محصول شما :
    کد محصول : {code}
        نام محصول :{name}
         قیمت : {price}
                همین حالا میتوانید سفارش دهید

'''


print(text)


'''

محصول شما :
    کد محصول : sh1
        نام محصول :kiko lip2
         قیمت : 40
                همین حالا میتوانید سفارش دهید
                
                '''


'''

محصول شما :
    کد محصول : sh5
        نام محصول :mac lip2
         قیمت : 60
                همین حالا میتوانید سفارش دهید


'''


a=20
a=40

text='salam man a salam has'
print(text)
#salam man a salam has

#f-string

text=f'salam man {a} salam hast'
print(text)

#salam man 20 salam hast
#salam man 40 salam hast



#--------pro
product1=['sh1','kiko lip2',40]


product1=['sh100','bmw',10000000]

product1=['sh29237809','bmw',10000000]


#name=
#nndsd
text=f'''
محصول شما :
    کد محصول : {product1[0]}
        نام محصول :{product1[1]}
         قیمت : {product1[2]}
                همین حالا میتوانید سفارش دهید


'''


print(text)


#--------

text='''
your product informations:
product code:
product name:
total price:
    
Now you can go for order

'''
print(text)




new_list=['sh1','dior','2123132']


text=f'''
your product informations:
product code: {new_list[0]}
product name: {new_list[1]}
total price: {new_list[2]}
    
Now you can go for order

'''

print(text)

'''
your product informations:
product code: sh1
product name: dior
total price: 2123132

Now you can go for order

'''


#-------
#benevise code
#name
#price
#KOJA BNVISE?

#--input
#tabe ee
code=input('lotfan code mahsool ra bede: ')
name=input('lotfan esme mahsool ro bede')
price=float(input('lotfan gheymat ro bede'))

text=f'''
Your product info:
    
product code: {code}
Product name : {name}
total price: {price}
 

'''
print(text)


#neshon bde
'''
Your product info:

product code: fan12
Product name : testa v100 Nvidia
total price: 11000.0
'''


#acccept mikoni ya reject?
code=input('lotfan code mahsool ra bede: ')
name=input('lotfan esme mahsool ro bede')
price=float(input('lotfan gheymat ro bede'))

text=f'''
Your product info:
    
product code: {code}
Product name : {name}
total price: {price}
 

'''
print(text)

answer=input('lotfan sefareshe bala ro accept ya rejetc kon: y / n')

#agar--> if 
#if else

if answer=='y':
    print('tabrik migooyam sefareshe hsoma sabt shod')
    
else:
    print('motasefam sefareshe shoma pak shod az tarikhche')
    
#==============
#beshedat pro benevisiiii
#----PRO------
code=input('lotfan code mahsool ra bede: ')
name=input('lotfan esme mahsool ro bede')
price=input('lotfan gheymat ro bede')


if price.isdigit():
    price=float(price)
    text=f'''
    Your product info:
        
    product code: {code}
    Product name : {name}
    total price: {price}
     

    '''
    print(text)
    answer=input('lotfan sefareshe bala ro accept ya rejetc kon: y / n')

    #agar--> if 
    #if else

    if answer=='y':
        print('tabrik migooyam sefareshe hsoma sabt shod')
        
    else:
        print('motasefam sefareshe shoma pak shod az tarikhche')
        

else:
    print('lotfan adad vared konid va dobare emtehan konid')


#------------------------------------------
#-----------------------------------------
#code,list,price, colors

product_list=['sh1','kiko',50,'red']

text=f'''
product info:
product code : {product_list[0]}
product name : {product_list[1]}
product color : {product_list[3]}


Total price : {product_list[2]}



'''

print(text)

#--------------
#yeseri mahosl arang daran yeseria nadaran

product_list=['sh1','kiko',50,'red']
product_list=['sh1','kiko',50,'0']

#---------
#--raveshe ghabli javab nmide

text=f'''
product info:
product code : {product_list[0]}
product name : {product_list[1]}
product color : {product_list[3]}


Total price : {product_list[2]}



'''

print(text)


#--jalse ye ayande------






#-----LISTESHOON------
#-----STR FUNCTIONS--------
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

