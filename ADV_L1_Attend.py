

"""
In The Name Of GOD
Created on Sun Oct 13 18:36:10 2024

@author: Ali Pilehvar Meibody   Linkdin

email: --> telegram

emergency --> alipilehvar1999@gmail.com

"""

'''

Review-----
Python---> yek zabane beyne ensan va mashin

--> zabane -->mesle zabane italiee , faransavi

Vocab (kalamat)
Grammar (dastoor, mantegh)

** harchi benevisi hich etefaghi nmiofte
ta send ro nazani
send zade she--> run bshe

#
-->python nemikhone

comment , khodeton, modares


# 

vocab 
grammar

---> reserv shodan 
rangi mishan
esme zarf

'''

#Jalase ye avale advanced--------


print()
input()
#if

#ino man nmiushasa
#esme zarf
#zarf-->adad , horod , kalame , zakhire konam
#-------------
#moteghayer variable
'''
1---> adad sahih (1,3,300,400) int 
ashari bashe (3.453) (45.645) float
complex --> i + j  1+2j

2--> reshte --> string --> harf, kalame, jomle


berizi tooye yek zarf

'''

#agar kalamey haye python bashe tarif shode-->rangi mishe
#ag nabashe--> reserve nashode--> esme zarf


#yek zarf daram, inam esmeshe, tosh

name=45

adad=45.6


#jomle , character, kalame , harf --> quot 
# ' '
jomle=' salam arz shod'

jomle= 'salam arz shod'


#---------- tooye zarf zakhire koni
#reserve shdoe ha

'''
1-unreserved --> nemishanse---> esme zarf
2-reserv (python mishanse) --> built in funciton (tabe haye dakheli) , dastoorat (keywords)

#yek karaee dare



'''
print()
input()
type()
len()
#.........


#vaghy mikhay yechizi ro namayehs bdi aaz print estefade mikone


print(4)


print('salam arz shod')


#ghalaat XXXXX
print(salam arz shod)



salam= 45
print(salam)


#type --> 
a=45
b=45.5
c=1j
d='salam'
e='s'
f='@'

type(a) # int adade sahih
type(b) # float ashari
type(c) #complex i + j
type(d) #str
type(e)
type(f)
#str-->reshte --> jomle , kalame va va va...


#======================================
'''
Python ---> another language (yek zabane)
1-unreserved---> esme zarf
2- python built in function ( print, input , len , type), keywords ( if , for , else , ....)

1-----> zarf --> 1.1 adad (int,float,complex)  1.2str (kalame, harf , jomle)

'''
#1--->adad
a=20
b=3

'''
+ jam
- menha
/ taghsim
* zarb
** tavan


'''

#a+b=c

#aval zarfeto besazi 

c= a+b
print(c) #23


c= a-b
print(c) #17

c= a*b
print(c) #60

c= a/b
print(c) #6.666666666666667


c= a**b
print(c) ###8000

#20 ** 3   --> 20 be tavane 3 --> 20 * 20 * 20


#--------1.2 str (reshte ha , horof, kalame , jomle)
#kh sade

#esme zarfeto bdi badesh dakheelsh rehsatto ba quota

a=ali
#zarfi drm b esm,e a
#ali ro tosh mikham

a= 'ali'

#------chandta horof dare str e ma?
#az koja bfhmim

b='alipilehvarmeibody'

len(b) #18


#---input
#print()


#print()
#namayehs mide

print('salam') #salam

#vorodi bgrim?

#tabe ee input
#$skaheleam chizi k mikhay b karbar namayesh bdi ro bgooo bnvis namayehs
#az karbar ychizi migire
#va in pass mide
#jolosh y zarf bzari zakhirash koni

input('salam seneton cheghadre:')


sen=input('salam seneton cheghadre:')

print(sen) #40

#----**** tabreye input --> harchizi bgire be soorate str zakhire mikone

print(type(sen))
#<class 'str'>

#moshkel?
#shoam dg nmitoni azash darm mohasebat estefade koni


jadid=sen+10

a=40
b='40'
#a--> type int --.adade
#b-->yek rehste hast ke az keyboard adade 4 + adade 0 40


#jae k mikhay adad bgfuri poshtesh int ya float

sen=int(input('seneto begoo:'))
print(sen) #40
print(type(sen)) #<class 'int'>

#float
#vazn mishe

#ghalate 
vazn=int(input('vazneto begoo:'))
print(vazn)


vazn=float(input('vazneto begoo:'))

print(vazn) #45.5 40.0



#--------
print()
input()
len()
type()



#_---nokate print
#ag bkham chantaaa chizi ro print konam chi?

a=20


print(a)

a=20
b=40
#20 40

#ya fght virgooL?
print(a , b) #20 40
print(a and b) #40 XXXX
print(a or b) #20 XXXXXX
#tabeye print(sdjdsh)
#ag bishtar az 1 --> + ,

print(a+b) #60

a='salam'
b='khoobi'
print(a,b)
#salam khoobi

print(a + b)
#salamkhoobi


#default--> pish farz--> az gamma estefade koni


#dakhelesh yechize ghashangi dare

a='salam'
b='khoobi'
print(a,b)
#a ro jchap kon virgool , kalamey badi 

#salamkhoobi chra?
#salam khoobi

print(a,b,sep=' ') #pishfarz

#taghir bdi

#beyen salam o khoobi setare bzne

print(a,b,sep='*')

#salam*khoobi

c='ali'
d='hastam'

print(a,b,c,d)
#salam khoobi ali hastam
print(a,b,c,d,sep='*')
#salam*khoobi*ali*hastam
print(a,b,c,d,sep='@')
#salam@khoobi@ali@hastam


print(a)
print(b)
'''
salam
khoobi
'''
print(a,end='')
print(b)
#salamkhoobi


print(a,end='*')
print(b)
#salam*khoobi


print()
#print yektabe ye pishe pa oftade
#tabe haye pishrafte dakhele giome kh dastressi bht midan





#------------str------------
a='salam'

#access
#dovomi dastresi peyda konm
#index --> shoamresh
#adad az 0 shor mishan

#esme zarfano breeraket bznm
a[0] # 's'
a[3] # 'a'

#yerdone??



#az 0 ta 3 sala
a[0:4] #0 1 2 3 'sala'

#--------koli tabe dakhele str vojod dasre k mitoni estefade koni
#kafie rooye zrafet dot bzni
#upper()
#lower()
#.......


a='salam'

#bozorg konam

#dot esme tabe () esme tae
#*****esme tabe omd -->parantez

a.upper() #'SALAM'

a='SALAM'
a.lower() # 'salam'


a='salam'

a.find('m') #: 4
#mige harfe m dar indexe 4 hast

#a aro bokon d
a.replace('a','d')
#'sdldm'

#fasele ghablo bado hazf mikone

a='  salam'
print(a) #  salam
len(a) #7


b=a.strip()

print(b) #salam
len(b) #5


#split --> mige behemk ye character bde harjha didamehs nesf mikonam 

a=' salam arz shod , khob hasti , man ali hastam'

b=a.split(',')

#TAMAME IN TBE HA makhsooose str (string ha hastan)
#va karbiord haye kahs ro daran


'''
estefade--> rooye zrafet dot mizani esmesho mibis

.upper()
.lower()
.find()
.replace()
.strip()
.split()



LIST , IF , ESLE ,FOR ...........
+ EZAF EZAFE KONIM
masaelio hal konim ---> applicable --> karbodi hast


'''





'''

Applications-----

1---> bot -->telegram bot ---> kharid ro bsoorate automat anjam bde





'''






