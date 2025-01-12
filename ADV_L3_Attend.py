
"""
In The Name Of GOD

Created on Sun Nov 10 17:49:33 2024

@author: apm

Python --->  3 bakhsh
1-python built in function (print, input, len ,...)
2-keywords (if , else, for , while , break, continue , pass)
3-variables ( int, float, str)
str , fdunction ( upper, lower , find)



"""

a='salam'
len(a) # 5


b='alipilehvarmeibody'
len(b) #18


c='ali '
len(c) #4
#product = []

text='''
your product informations:
product code:
product name:
total price:
    
Now you can go for order

'''
print(text)



#f string

product=['l123','nike',420]
product=['l200','adidas',600]


text=f'''
your product informations:
product code: {product[0]}
product name: {product[1]}
total price: {product[2]}
    
Now you can go for order

'''
print(text)



#f --> string {} 
'''
your product informations:
product code: l123
product name: nike
total price: 420

Now you can go for order

'''


'''

your product informations:
product code: l200
product name: adidas
total price: 600

Now you can go for order
'''




text=f'''
your product informations:
product code: product[0]
product name: product[1]
total price: product[2]
    
Now you can go for order

'''
print(text)


'''
your product informations:
product code: product[0]
product name: product[1]
total price: product[2]

Now you can go for order

'''



a=20

text='salam man ali hastam va man a salame'

print(text)

#salam man ali hastam va man a salame

text=f'salam man ali hastam va man {a} salame'
print(text)
#salam man ali hastam va man 20 salame


a=40
text=f'salam man ali hastam va man {a} salame'
print(text)
#salam man ali hastam va man 40 salame


#dynamic akridm yek string ro




#-------application-----------------
#az karbar beporse bege code mahsooleton ro begoo
#bad bege esmesho begoooo
#bad bege gheymato begoooo
#bad namayesh bedeee bege taeed mikoni ya reject mikoni


code=input('salam code mahsooleton ro begid:')
name=input('lotfan esme mahsooleton ro begid:')
price=input('lotfan gheymate mahsooleton ro begid')


text=f"""
Product information:
product code: {code}
    
product name: {name}
    
total price: {price} 
    
    
Plutus .co 2024

"""
print(text)

answer=input('age taeed mikoni benevis yes age na benevis no:')

if answer=='yes':
    print('mamnoon mahsoole shoam sabt shod')
else:
    print('motasefane mahsoel shoma sabt nashod va cancel shod')
    
    
    
    
    
    
    
a='yes'
b='Yes'

print(a==b)
#False


'''
= assign (megdhardehi)
a barabar hast ba 10
a=10


besanji , soali , beporsi 
aya a ba 10 
a==10



'''







#sade tarin rah or


#str function .......
'''
upper()
lower()


'''


code=input('salam code mahsooleton ro begid:')
name=input('lotfan esme mahsooleton ro begid:')
price=input('lotfan gheymate mahsooleton ro begid')


text=f"""
Product information:
product code: {code}
    
product name: {name}
    
total price: {price} 
    
    
Plutus .co 2024

"""
print(text)

answer=input('age taeed mikoni benevis yes age na benevis no:')
#Yes YES yEs
#yes
new_answer=answer.lower()
if new_answer=='yes':
    print('mamnoon mahsoole shoam sabt shod')
else:
    print('motasefane mahsoel shoma sabt nashod va cancel shod')
    



#---HERFE EE---

code=input('salam code mahsooleton ro begid:')
name=input('lotfan esme mahsooleton ro begid:')
price=input('lotfan gheymate mahsooleton ro begid')


text=f"""
Product information:
product code: {code}
    
product name: {name}
    
total price: {price} 
    
    
Plutus .co 2024

"""
print(text)

answer=input('age taeed mikoni benevis yes age na benevis no:')

if answer.lower() =='yes':
    print('mamnoon mahsoole shoam sabt shod')
else:
    print('motasefane mahsoel shoma sabt nashod va cancel shod')
    



##---alternative -_>jaygozin
answer=input('age taeed mikoni benevis yes age na benevis no:')

if answer.upper() =='YES':
    print('mamnoon mahsoole shoam sabt shod')
else:
    print('motasefane mahsoel shoma sabt nashod va cancel shod')
    
    

a='yes'
b=' yes'

print(a==b)
#False  

print(len(a)) #3 y e s
print(len(b)) #4 space y e s


#------
code=input('salam code mahsooleton ro begid:')
name=input('lotfan esme mahsooleton ro begid:')
price=input('lotfan gheymate mahsooleton ro begid')


text=f"""
Product information:
product code: {code}
    
product name: {name}
    
total price: {price} 
    
    
Plutus .co 2024

"""
print(text)

answer=input('age taeed mikoni benevis yes age na benevis no:')

if answer.lower() =='yes':
    print('mamnoon mahsoole shoam sabt shod')
else:
    print('motasefane mahsoel shoma sabt nashod va cancel shod')
    
    
    
    
#=======================
#=======================
#======================
code=input('salam code mahsooleton ro begid:')
name=input('lotfan esme mahsooleton ro begid:')
price=input('lotfan gheymate mahsooleton ro begid')


text=f"""
Product information:
product code: {code}
    
product name: {name}
    
total price: {price} 
    
    
Plutus .co 2024

"""
print(text)

answer=input('age taeed mikoni benevis yes age na benevis no:')

if answer.strip().lower() =='yes':
    print('mamnoon mahsoole shoam sabt shod')
else:
    print('motasefane mahsoel shoma sabt nashod va cancel shod')
    
    
a='  yes'
    
b='yes  '
    

a.strip() #'yes'
b.strip() #'yes'


c='  y es '
c.strip() # 'y es'



c.replace(' ','') #'yes'

#----if --> shart 
#agar kard inkaro kon ag nakrd bvel kon


#---if else-->
#if-->agar inshart ok inkaro kon
#agar nashod kare 2vomo kon (else)



#for , while --> tekrar , iteration
#list, str

for i in range(0,10):
    print('salam')
    
for i in range(0,10):
    print(i)


#---LOGIC for ......

a='salam'

for i in a:
    print(i)
    



#while --> 




#=================================
code=input('salam code mahsooleton ro begid:')
name=input('lotfan esme mahsooleton ro begid:')
price=input('lotfan gheymate mahsooleton ro begid')

#'1200'

price_list=[]
for i in price:
    price_list.append(i)
    
    
#1 2 0 0 
# 0 1 2 3 
#
#0 1 2 3 


for i in range(0,len(price_list)):
    if price_list[i]=='۰':
        price_list[i]='0'
    if price_list[i]=='۱':
        price_list[i]='1'
    if price_list[i]=='۲':
        price_list[i]='2'
    if price_list[i]=='۳':
        price_list[i]='3'
    if price_list[i]=='۴':
        price_list[i]='4'
    if price_list[i]=='۵':
        price_list[i]='5'
    if price_list[i]=='۶':
        price_list[i]='6'
    if price_list[i]=='۷':
        price_list[i]='7'
    if price_list[i]=='۸':
        price_list[i]='8'
    if price_list[i]=='۹':
        price_list[i]='9'
    
final_price=''.join(price_list)
    

 


text=f"""
Product information:
product code: {code}
    
product name: {name}
    
total price: {final_price} 
    
    
Plutus .co 2024

"""
print(text)

answer=input('age taeed mikoni benevis yes age na benevis no:')




if answer.strip().lower() =='yes':
    print('mamnoon mahsoole shoam sabt shod')
else:
    print('motasefane mahsoel shoma sabt nashod va cancel shod')
    




'''

1--> tashkhis bede bebine farsie ya englisi
2--> badesh bayad farsio--> englisi 0 farsi --> 0 englisi

'''




#niaz daram bala copy paste konam heyt?
'''
FUNCTION????


box besaz toosh karo bego
sedash bzn
tabe --> fucntion



input ---> BOX (FUNCTION) -->output

vorodii--> box---> khoroji 

1-->tarif koni
2--> call (sedash bzn)-->hadafe nahaee




'''

'''
def esme tabe(vorodi, , , ,):
    #daastsoor
    #......
    

esme tabe --> esme moteghayer

'''

ali=
name=
2name= #adad nemsihe aval gzoash
21232=
print #esme reser, if else, input
convert to persdian
# 
'''
convert to persian XXXXXXX
converttopersian

ConvertToPersian

convert_to_persian

'''
#tabe bensvisam dota vorodi yek khoroji

# input --> BOX --> khoroji

#**2 --> khrooji ba print motefavete


def jam(a,b):
    c=a+b
    


#1-na vorodi na khoorji
#---tabe ee drim k vorodi nadahste bashe va khroji ham ndshte bashe


def welcome():
    print('khosh oomadid')
    
welcome()





#2-->vorodi nadahste bashe ama khoroji dahst ebashe
#---tabe e dirm vodoi nadahst ebahs amna khorji dashte bashe?

def pi():
    return 3.14


b=pi()


#3-0->vorodi dahste bashe ama khoroji dashte bashe
#vorodi dare va khoroji ham dare
def jam(a,b):
    c=a+b
    return c


result=jam(4,5)



#4--> ham vorodi ham khoroi
#----tabe miton eham khoroji ham print dashte bashe?
def jam(a,b):
    c=a+b
    print(c)
    return c






#----------aval misazish badan sedash mikoni
#vaghty seda



result=jam(5,6)

#NameError: name 'jaaaaam' is not defined


#TypeError: jam() missing 1 required positional argument: 'b'


#TypeError: jam() takes 2 positional arguments but 3 were given

def persian_to_english_numb(persian_numb):
    price_list=[]
    for i in persian_numb:
        price_list.append(i)
    
    #price_list = ['' , '' , '' , '']
    
    for i in range(0,len(price_list)):
        if price_list[i]=='۰':
            price_list[i]='0'
        if price_list[i]=='۱':
            price_list[i]='1'
        if price_list[i]=='۲':
            price_list[i]='2'
        if price_list[i]=='۳':
            price_list[i]='3'
        if price_list[i]=='۴':
            price_list[i]='4'
        if price_list[i]=='۵':
            price_list[i]='5'
        if price_list[i]=='۶':
            price_list[i]='6'
        if price_list[i]=='۷':
            price_list[i]='7'
        if price_list[i]=='۸':
            price_list[i]='8'
        if price_list[i]=='۹':
            price_list[i]='9'
    #list --> be str
    final_price=''.join(price_list)
    return final_price
    


#persian_to_english_numb('۱۴۰۰')

#1 vorodi migie --> 1 khorji mide



def confirmation(answer):
    if answer.strip().lower() =='yes':
        print('mamnoon mahsoole shoam sabt shod')
    else:
        print('motasefane mahsoel shoma sabt nashod va cancel shod')
    


#-----code nahaeee------------

code=input('salam code mahsooleton ro begid:')
name=input('lotfan esme mahsooleton ro begid:')
price=input('lotfan gheymate mahsooleton ro begid')
#******man dar inja yek box (def , functiojn) mikham ke
#yek adad begire (vorodi) ( farsie)
#yek khoroji bde neglisi



'''

input ( ۱۲۰۰)  ---> box ---> ouytput (1200)


'''


new_price=persian_to_english_numb(price)

text=f"""
Product information:
product code: {code}
    
product name: {name}
    
total price: {new_price} 
    
    
Plutus .co 2024

"""
print(text)

answer=input('age taeed mikoni benevis yes age na benevis no:')



confirmation(answer)








#-------======*********NAHAEEEE--------------
#==========================
#========================== 
#==========================

#==========================
#========================== 
#==========================#==========================
#========================== 
#==========================#==========================
#========================== 
#==========================#==========================
#========================== 
#==========================#==========================
#========================== 
#==========================#==========================
#========================== 
#==========================#==========================
#========================== 
#==========================#==========================
#========================== 
#==========================
def persian_to_english_numb(persian_numb):
    price_list=[]
    for i in persian_numb:
        price_list.append(i)
    
    #price_list = ['' , '' , '' , '']
    
    for i in range(0,len(price_list)):
        if price_list[i]=='۰':
            price_list[i]='0'
        if price_list[i]=='۱':
            price_list[i]='1'
        if price_list[i]=='۲':
            price_list[i]='2'
        if price_list[i]=='۳':
            price_list[i]='3'
        if price_list[i]=='۴':
            price_list[i]='4'
        if price_list[i]=='۵':
            price_list[i]='5'
        if price_list[i]=='۶':
            price_list[i]='6'
        if price_list[i]=='۷':
            price_list[i]='7'
        if price_list[i]=='۸':
            price_list[i]='8'
        if price_list[i]=='۹':
            price_list[i]='9'
    #list --> be str
    final_price=''.join(price_list)
    return final_price
    

def confirmation(answer):
    if answer.strip().lower() =='yes':
        print('mamnoon mahsoole shoam sabt shod')
    else:
        print('motasefane mahsoel shoma sabt nashod va cancel shod')
    



code=input('salam code mahsooleton ro begid:')
name=input('lotfan esme mahsooleton ro begid:')
price=input('lotfan gheymate mahsooleton ro begid')
#***1
new_price=persian_to_english_numb(price)

text=f"""
Product information:
product code: {code}
    
product name: {name}
    
total price: {new_price} 
    
    
Plutus .co 2024

"""
print(text)

answer=input('age taeed mikoni benevis yes age na benevis no:')

#2**
confirmation(answer)




#----size ro beporsam



name=input('brande kafgsehj shoma chand ast?')
size=input('salam size kafshe shoma chand ast ')
new_size=persian_to_english_numb(size)

text=f'''

shooes information
shooes name : {name}
shooes size : {new_size}
'''

print(text)

answer=input('age taeed mikonid yes age na no ro bezani')

confirmation(answer)




#----yechize dg
'''
az msohtari
code product 
name
price (b rial) 10 000 farsi
size --> farsi

text : product code , name price b toman  , size

aya taeed mikoni ya na -->yes no

#azash beporsi aya mikhahi taghuir bdi? yes az aval
#ag gofi na --> mamnoon omidvaram baz be ma sar bezanid

'''






