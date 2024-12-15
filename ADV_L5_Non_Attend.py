"""
In The Name of GOD

ADV_L5_Non_Attend

Created on Sun Dec 15 17:22:33 2024

@author: Ali Pilehvar meibody




    
    
    
    
"""


'''
Human -------- Machine interaction


Human (language: Fa, En , It,..)------Interface ------ Machine (Language: Binary 0,1)

Interface----> Python ......


python ---> 3 bakhsh tashkil shode



spyder--> safe chat --> az bala be paeen , az chap be rast mikhone
space haro rad mikoen # , qutation-->Comment kari ndre besh
harchize dg ee benevisi ro mikhone


Python --> har zane dg ghavanin , grammar , vocab ,.. 
ianro nafahme mige nafhmidm --> Error --> samte rast console 1/A



Python 3 bakhs tahskil shode ( az bala b paeen chap b rast k mikhone)
3 ta type kalame vasash vojod 3 ta haalt

1-python build in function ( tabe haye dakhelie python)--> yek akri mikonan
minevisi--> az gahbl sazandegane pyhton ianro 
print()  input() type()  len()  open() ,..... narenji 


2-Keywords --> logic (manteghi) --> if , else , while , for , def , class,.....
banafsh 

-----Farsi project --> python 
mikhonsih langauge (farsi)-->python
agar (shart) do rahi --> if 
agar , dota dastoor agar shod inakr agar nashdo oonkar -> if else
if elif elif elif else

for ,while --> tekrar 

for --> iteration , bazrresi -> too dele str, too dlee list, ....

for (if )--> iteration , too delsh check mikone coutn mishmore, append ezaf mikone

while--> zmaani hast k yek halgeh darim va shart mzirim baraye entehash

while true --> yekar ro ingahd anjam bde ta ...


mirftn too dele def --> BOX yekbar misakhtish vorod-->box-->khoroji

sedash koni 100 khat bnvisi






3--> un reserved --> variable (moteghayer) -->zarf --> mitoni chiz dakhelesh brizi
numebrs  ( int, float, complex)  + - * , reshte string, str --> (harf, character, jomle , yek ketab),
str function --> lower() upper() find() , bool ( True , false) 
= + - * ** / % alaemi k bahash mohasebati
moghayese gar --> == soale aya msoavi != aya msoavi nis
>  <  =>  =< ---> javab mdie python True False --> Boolean


changa moteghayer ro mikahsim baham zakhir ekonim --> iterable
list, tuple  , set , dictionary ,....


list fucntion --> append() .......



'''

#aslan mohem nis
open()
#type1-->python built in function 

'''

dade ha
matni --> .txt .doc .docx 
pdf--> .pdf
jadval .csv , .xlsx .xls
image --> .jpg .jpeg .png .gif .mp4 


varede spyder (IDE) 

tabe --> open()
be man enshoonisho bgo man miaramesh too mohite karet 

tooye yek zarf (variable)
adad, matn , ax ,.....
zakhriash koni


spyder ro baz mikoni --> koja dare run mishe???
too foldere C ? too folder D ? too desktop? 
installation path --> barname install
excution path --> run mishe

c:\user\aicoshop.ir

c:\user\name
c:\user\foldeC \prorgamm file \anaconda3 \
    
jaee hast k spyderet scripti k minevisi dare ejra mishe
va ag bzni control S --> save default

scriptet oonja save mishe


file ro baz koni

data_13dec.txt

myfriend.jpg



'''


print('salam')

#vorodii--> path 
#too qutation

open('data_13dec.txt')
#miagrde??
#baz mikone 
#ag nabashe baz nmikonee


#too desktop




#------------------------3 ta rah baray eopen kardn

#--------------------------1-------------------------------
#---sade tarine 
#daghighan oonjae k run mishe codet (in baal rast
#c\user\a
#datato oonja paste koni


a=open('data_13dec.txt')
b=open('myfriend.jpg')

#badam zkhiash too a ,

#------------------------2------------------------------
#dtaat yeja dg save desktop , .....
#biay path masire ejraye spyder ro avaz koni
#bebari hamoonjaee k filet has


#boro too file az samte files bri hamoonjae k filet has

#C:\Program Files (x86)\Common Files
#ejraye spyderam omde too program file
#ag datamam haminja bashe

a=open('data_13dec.txt')


#-------------------------3---------------------------------
#asan baram mohem nis k koja dare run mishe
#Miri rooye filet click rast mikni -->property

#Pat--> C://desktop/d.sd.sssdsssd


a=open('C:\users\apm\desktop\data_summer\data_13dec.txt')


b=open('C:\Users\Alcoshop.ir\Desktop\data_13dec.txt')
#=
#baraye man mohem nis k ejraye spyder kojas
#asan harja
#manmiam az b besmelal b spyder migm agahbor C / user /

#--------------------------------------------------
#---txt ---->
#a=open

#open (w , r , x )

#read only 
#write
#append



#--------ketabkhone ha omdn az hamin open 



#pandas---> ketabkhoen kar ba data --> data excell , csv

#radifo sootoon

#str , int ,...
#List --
#dataframe---
open()

#pandas.open_excell('C:\Users\Alcoshop.ir\Desktop\data_13dec.txt')


#opencv --> computer vision --> bianee machine
#ax film

#opencv.open_image('')




#--------------------------------------------------------
'''

Vorodii---> name BOX ---> khoroji
#100 , 50000




khoroji=name(vorodi)

'''



#-----LOCAL GLOBAL------

'''



1-->bdone khrooji borodi
2-->1 voorodi khroji ndsht (print)
3--> vorodi nadashte bash ekhoroji dahste bashe 
4-->ham vorodi ham khoroji

def name(input1,input2,input3,......):
    order1
    order2
    order3
    ....
    return output1,output2,output3,output4,.....




'''
def jam(a,b):
    c=a+b
    return c



# a, b ---> box ---> c



d=jam(4,5)



#-----Tamam emoteghayer haye dakheel yek tbae --> Local

#local --> mahali , 
#Global --> sarasari 


#esme moteghayer , a , b , c , name , numb umb2 ,...
#too dele yek tabe misazim fght too dle tabe hast 

#briona z on vojod ndre


#****zarf haye movaghatiii



def jam(a,b):
    c=a+b
    return c


d=jam(4,5)




print(c)
#NameError: name 'c' is not defined


#Locall
#taamme moteghayer haye dakhele yek tabe hame baham local hastand





c=40
def jam(a,b):
    c=a+b
    return c


d=jam(4,5)


print(c)



#--aga rma bkhaym yek moteghaye too dele tab ero global konim
#brionaz tabe ham beshnase
#global



def jam(a,b):
    global c
    c=a+b
    return c



d=jam(4,5)

#a,b,c --> zarf emovaghat 

#poshtesh nvshtm global c--> c zarfe movagaht nis
#yek zarfe daemi hast


#
print(c)


print(a) # a is not defined
print(b) #b is not dfineed

#c--> 9



#global , local


#-----------------default sazi



def jam(a,b):
    c=a+b
    return c



jam(4,5)


jam(4)
#kam bzni --> 2 ta mikhad --> 1 done kam dadi miss
#TypeError: jam() missing 1 required positional argument: 'b'
#ag ziad bzni --> 2 ta mikhad ---> given

jam(4,5,6)

#TypeError: jam() takes 2 positional arguments but 3 were given




def newton(mass,acc):
    
    
    
    
    
#-----jabe(jesm ) -->nirooe F vared koni , jabe jermesh M bashe 
#yek shetabi migire --> a 

#f=m*a


#mass -->jerm
#acc --> shetab

#force
def newton(mass,acc):
    force=mass*acc
    return force


newton(10,5) #50


newton(10)
#TypeError: newton() missing 1 required positional argument: 'acc'


#--gahan fefault




#----->
#-->zamina z bala chizi part koni paeen ->shetab bsoorate default 9.8


#10*9.8 --?98 

#tabe besazim

#agha ag trf fght jerm zad --.defaut acc-->9.8

#hamchin bshsh in ejaze ro ham bde k taghir bde shetab ag kahst



def newton(mass):
    force=mass*9.8
    return force


newton(10) # 98.0

#taghir bdi shetab flexibl , 






def newton(mass,acc=9.8):
    force=mass*acc
    return force


#agha atbeye man dota vorodi dare , mass , acc
#zarb mikone


#ama age trf acc ndad --> shetabo pish farz --?9.8



#----2 point
#+ --> trf mitone fght y mass bzne va in by defualt 9.8
#ye vorodi ham ejra mishe


newton(10) # 98.0



#++-->flexible ->ag trf khas mitone voordi2 -->shetabam shetabe


newton(10,40)
#400

#----------------------------------------------------------

#-----10000 code application real world
#error 

'''

gahdm

kode man



try:
    kode man

except:
    print()


'''
def response_customer():
    a=10
    print('custoemre aziz gheymat hast:',a)
    pass


def handle_admin():
    try:
        b=100
        print(f'kalaye shoma ba gheymate{b} sabt shopd ')
        print(z)
        pass
    except:
        print('dar hale hazer moshkeli pish amade, chan daghigeh ye bad mojadadan talash farmaed')

def Bank_management():
    handle_admin()
    print('salam modire bank lotfan shoamre karte jadid ra ...')
    pass

def website_interface():
    pass

def applciation_API():
    pass

handle_admin()

response_customer()

Bank_management()
#NameError: name 'z' is not defined

#1-->koel abrname mikhabe

#2--> ag gtoo tbae haye dg ham estefade krd ebashi mikahbe 

#5ta hamzaman dare kar mikone

#Moshatri , admin ,bank , website , application 

#eroor admin --> error

#admin --> product error karesh anjam nmsihe




#motasfeane , application , website, bank , customer ,..


#real-world

#----10000

#100 ta tabe


#5 ta tabe

def response_customer():
    a=10
    print('custoemre aziz gheymat hast:',a)
    pass


def handle_admin():
    try:
        b=100
        print(z)
    except:
        print('moshkeli pish omde, lotfan daghayegeh dgar mojadadn taalsh farmaeed')
        

def send_message_to_dvlps(error):
    #telegram.send_message('apm',error)
    print(f'telergam mesage: {error}')
    
    
def handle_admin():
    try:
        b=100
        print(z)
    except Exception as e:
        print('moshkeli pish omde, lotfan daghayegeh dgar mojadadn taalsh farmaeed')
        
        send_message_to_dvlps(e)
        
        
handle_admin()
        
        
        
def Bank_management():
    handle_admin()
    print('salam modire bank lotfan shoamre karte jadid ra ...')
    pass

def website_interface():
    pass

def applciation_API():
    pass


#error --> ma nmitonim joloye error ro bgirm
#error 

#harja error okhroe kole barname maid paeen az run rdr maid

#yek rahi bood 
#k ag error khord --> baghei ro tahte shoa grar 
#Baghei ka rkonan


handle_admin()

#NameError: name 'z' is not defined

Bank_management()
#NameError: name 'z' is not defined



Bank_management()



#1--> error ndad
#2---> moshekli vghty pish maid --> behmon paaym mid emoshkel m
#3-->  baranme az run nmiofte


'''

kode shoam




try :
    kode man
    
except:
    error
    
age khaat dahst error , 

'''





'''
CLASS 
OBJECT



def --> BOX 


class 




Application --> local def


BANK --->


variz mikoni

yeja kam mikoni




CLASS ----> gahan toye application ( karbord)
shoam naiz darid az yek chzii biaid object shey besazid
shey haye mokhtalef




CLASSS ---> 2 TA CHIZ

1--> properties ( adad , adad toosh zakhrie  variable)
2--> methods ( fucntion )
'''




def variz(amount):
    balance=amount
    print('variz shod')
    
    
    
def mojoodi():
    print('mojdoie shoam hast:',balance)



variz(100)


mojoodi()



#----------------------------------------------
'''
CLASS ----> 1-properties(variables) 2-methdos(fucntion)


C 
C++

90% shabiahn 
c++ --> az class support 
def 

class --> object bekeshim biron

object _> properties , method mokhtase oon object hastan





'''


'''

class Name:
    variable (properti)
    
    def () -->method
    
'''




class BANK:
    
    amount=40000
    name='ali'
    
    
    
    
    
#step1--->class ro bszi
#step2-->obejct az class bekshi biron


obj1=BANK()

obj2=BANK()

new_customer=BANK()



#too deleshoon
#ag noght ebezani mitoen b proeprty , methdo ha dastresi peyd akoni



obj1.name

#'ali'


obj1.amount
#40000

#properties?
#methdo-->fucntion




class BANK:
    amount=1000
    name='ali'
    
    def welcome():
        print('salam arz shod')


#tabe misazi too delshe




'''

az dele yek classs koli object bekeshi biroooon

in obejct ha proeprties

obj1.amount
obj1.name


#methdo tabe

obj1.welcome()
#paranetz yadet nre

#choon tabe ast


'''


#harchi man msiazam
#10000 ta obejct ham azin clas bsazam
#proeprti moshakahsat yeksane


#customization -->skahsi sazi tar konam


#vaghty mikahm object bsazam az yek class --> yekseri chziaro khodam
#mokhats bzaram




#obj1 
#obj2 
#Obj3

#amouunt

#vaghty mikhay obejct bsaz

#bj1=BANK()
#obj1=BANK(polesh, sen , ghad, esm)
#tooye init


class BANK:
    
    #khate 870 -->mige ke vaghty pbject msiazi chia bhsh bdiii
    def __init__(self,name,sen,amount):
        self.name=name 
        self.sen=sen
        self.amount=amount
        
        


#object misazam



obj1=BANK()

#vorodi mikahd --> __init___

#shakhsi sazi konam



obj1=BANK('ali',30,1000)

obj1.name# 'ali'
obj1.sen #30
obj1.amount

new=BANK('MOHSEN',30,40000)

new.name # 'MOHSEN'


#too self too dele class 
#
class BANK:
    
    #__init__ chia ro mikhay bgire
    #in setaro Nam,sen,meghdar az object mikahd a bhsh namayehs mdie
    
    def __init__(self,nam,sen,meghdar):
        #boro vase in class y ghafase baz kon esmesho bzar name
        self.name=nam
        self.age=sen
        self.amount=meghdar
        self.new=0
        self.pi=3.14
        
obj1=BANK('ali',30,1000)


obj1.sen
#AttributeError: 'BANK' object has no attribute 'sen'

#object fght chizaee dare k b self vasle
     
obj1.age   
        
obj1.new
    

        
        
        
#kh sade
class BANK:
    #init---> miay bahash migi vaghty yeki khas obejct bsazd
    #ch vorodi haee bayad bde elzami
    def __init__(self,nam,sen,meghdar):
        #self yejas hey to toosh gghafase besaz va chizi toosh zakhrir kon
        self.name=nam
        self.age=sen
        self.amount=meghdar

    #har tabe k b
    #hatman too delesh vorodi mitone
    #self--> k 
    def welcome(self):
        print('salam khosh amadid')


new1=BANK('ali',30,1000)

new1.name
new1.age
new1.amount

#hamchenin

#yek atbe hast
new1.welcome()
#mitone vorodi ham bkhad
#salam khosh amadid

new2=BANK('mohsen',40,0)

new2.name

new2.age
new2.welcome()


#shakhsi sazi yani chi



class BANK:
    #init---> miay bahash migi vaghty yeki khas obejct bsazd
    #ch vorodi haee bayad bde elzami
    def __init__(self,nam,sen,meghdar):
        #self yejas hey to toosh gghafase besaz va chizi toosh zakhrir kon
        self.name=nam
        self.age=sen
        self.amount=meghdar

    #har tabe k b
    #hatman too delesh vorodi mitone
    #self--> k 
    def welcome(self):
        esm=self.name
        print(f'salam jenabe {esm} b banke Plutus khosh amadid')

        

obj1=BANK('ali',30,1000)
obj2=BANK('mohsen',40,10000)
obj3=BANK('vahid',50,1000000)  
        
        

#az yek calss 3 ta object 
#properties , methods

obj1.name
obj2.name


#az tabe estefade
#welcome
obj1.welcome()

obj2.welcome()

obj3.welcome()



#------------------------------------------------------


#BANK ----> 
'''
def ? class?

bank-->moshtari --> object 

classs bzoorg besazim koli object azash bekeshim biroon

CLASS bsazim


har kas k mikhad y obejct bshe yek seri moshakhast mikahd

object vorodi ---> __init__

karbord dre , mojodi , variz , khosh amadi , ...__. methods






__init___

BANK()

name





'''



#yek class bename BANK misazam
class BANK:
    #__init__ yek self dre
    #va vroodi haee k yek frd bekhad obejct bsaze bayad hatman bzane
    #esmesham azadam harchi mikham bzaram
    #suggestion--> chizi bzar k trf befahme
    def __init__(self,nam,sen,moojoodie_avalie):
        #ta inaj az taraf migirim
        #zakhriash nabayad konim?
        #badan 
        
        #self --> gahfase hey bsaz tosh briz
        #esmesh fght 
        
        #tooye self yek gahfase bename name (proeprty bename name)
        #nam 
        self.name=nam
        self.age=sen
        self.balance=moojoodie_avalie
        
    
customer1=BANK('ali',30,5000)
        

customer1.name
customer1.age
customer1.balance



#yek class bename BANK misazam
class BANK:

    def __init__(self,nam,sen,moojoodie_avalie):
        self.name=nam
        self.age=sen
        self.balance=moojoodie_avalie
        
    def welcome(self):
        esm=self.name
        print(f'salam jenabe {esm} , b banke Plutus khsoh amadid')
        
c1=BANK('ali',30,5000)
c2=BANK('mohsen',40,0)


c1.name
c2.name

c1.welcome()
c2.welcome()




class BANK:

    def __init__(self,nam,sen,moojoodie_avalie):
        self.name=nam
        self.age=sen
        self.balance=moojoodie_avalie
        
    def welcome(self):
        esm=self.name
        print(f'salam jenabe {esm} , b banke Plutus khsoh amadid')
        
    def show_current(self):
        
        print('mojodie hesabe shoam hast :')
        print(self.balance)        
        
c1=BANK('ali',30,5000)
c2=BANK('mohsen',40,0)


c1.name

c1.welcome()

c2.welcome()

c1.show_current()
'''
mojodie hesabe shoam hast :
5000
'''

c2.show_current()
'''
mojodie hesabe shoam hast :
0

'''



class BANK:

    def __init__(self,nam,sen,moojoodie_avalie):
        self.name=nam
        self.age=sen
        self.balance=moojoodie_avalie
        
    def welcome(self):
        esm=self.name
        print(f'salam jenabe {esm} , b banke Plutus khsoh amadid')
        
    def show_current(self):
        
        print('mojodie hesabe shoam hast :')
        print(self.balance)  
        
        
    #oon frdi k objecte bayad megdharo bege
    
    #c1.deposit(poolo)
    #yek vorodi 
    def deposit(self,amount):
        
        self.balance=self.balance+amount
        print('varize shoam anjam shod')
        
        
    #c1.ATM(pool)
    def ATM(self,amount):
        self.balance=self.balance - amount
        print('bardasht ba moafaghiat anjam shod')
        
        


c1=BANK('ali',30,10000)

#1-properties
c1.name
c1.age



#2-->methods

c1.welcome()
#salam jenabe ali , b banke Plutus khsoh amadid

c1.show_current()
'''
mojodie hesabe shoam hast :
10000

'''

c1.deposit(5000)
#variz anjam shod

c1.show_current()
'''
mojodie hesabe shoam hast :
15000

'''


c1.ATM(7000)


c1.show_current()
'''
mojodie hesabe shoam hast :
8000

'''



#--------Real world
'''




'''


c1.show_current()


c1.ATM(20000)

c1.show_current()
'''
mojodie hesabe shoam hast :
-12000
'''




class BANK:

    def __init__(self,nam,sen,moojoodie_avalie):
        self.name=nam
        self.age=sen
        self.balance=moojoodie_avalie
        
    def welcome(self):
        esm=self.name
        print(f'salam jenabe {esm} , b banke Plutus khsoh amadid')
        
    def show_current(self):
        
        print('mojodie hesabe shoam hast :')
        print(self.balance)  
        

    def deposit(self,amount):
        
        self.balance=self.balance+amount
        print('varize shoam anjam shod')

    #self.balance-amount>0
    
    #amount < self.balance
    #0<self.balance-amount
    
    def ATM(self,amount):
        if self.balance - amount>0:

            self.balance=self.balance - amount
            print('bardasht ba moafaghiat anjam shod')
        else:
            print('mojodie shoam kafi nmibashad')
        
        
        
c1=BANK('ali',30,10000)


c1.show_current()

c1.ATM(20000)

#mojodie shoam kafi nmibashad


class BANK:

    def __init__(self,nam,sen,moojoodie_avalie):
        self.name=nam
        self.age=sen
        self.balance=moojoodie_avalie
        
    def welcome(self):
        esm=self.name
        print(f'salam jenabe {esm} , b banke Plutus khsoh amadid')
        
    def show_current(self):

        self.balance=self.balance-100
        print('mojodie hesabe shoma hast :')
        print(self.balance)  
        

    def deposit(self,amount):
        
        self.balance=self.balance+amount
        print('varize shoam anjam shod')
        print(f'Mojodie hesabe shoma : {self.balance}')

    def ATM(self,amount):
        if self.balance - amount>0:

            self.balance=self.balance - amount
            print('bardasht ba moafaghiat anjam shod')
            print(f'mojodie hesabe shoma: {self.balance}')
        else:
            print('mojodie shoam kafi nmibashad')
            
     
c1=BANK('ali',30,10000)

#properties    
c1.name  
  
#method
c1.welcome()      
        
c1.show_current()  
'''
mojodie hesabe shoma hast :
9900
'''

  
c1.deposit(5000)   
'''
varize shoam anjam shod
Mojodie hesabe shoma : 14900

'''
c1.ATM(20000)
#mojodie shoam kafi nmibashad

c1.ATM(4000)
'''
bardasht ba moafaghiat anjam shod
mojodie hesabe shoma: 10900

'''

c1.show_current()
'''
mojodie hesabe shoma hast :
10800

'''

#-----------
      

c1.ATM(10750)
'''
bardasht ba moafaghiat anjam shod
mojodie hesabe shoma: 50
'''

c1.show_current()

'''
mojodie hesabe shoma hast :
-50

'''


class BANK:

    def __init__(self,nam,sen,moojoodie_avalie):
        self.name=nam
        self.age=sen
        self.balance=moojoodie_avalie
        
    def welcome(self):
        esm=self.name
        print(f'salam jenabe {esm} , b banke Plutus khsoh amadid')
        
    def show_current(self):
        
        if self.balance>=100:
            

            self.balance=self.balance-100
            print('mojodie hesabe shoma hast :')
            print(self.balance)  
        else:
            print('motasfeane shoam mojodie mojodie hesba ham nadard')
        
    def deposit(self,amount):
        
        self.balance=self.balance+amount
        print('varize shoam anjam shod')
        print(f'Mojodie hesabe shoma : {self.balance}')
        
        

    def ATM(self,amount):
        if self.balance - amount>0:

            self.balance=self.balance - amount
            print('bardasht ba moafaghiat anjam shod')
            print(f'mojodie hesabe shoma: {self.balance}')
        else:
            print('mojodie shoam kafi nmibashad')
            
            
      
#-------------------------PIN code-------

class BANK:

    def __init__(self,nam,sen,moojoodie_avalie,password):
        self.name=nam
        self.age=sen
        self.balance=moojoodie_avalie
        self.PIN =password
        
    def welcome(self):
        esm=self.name
        print(f'salam jenabe {esm} , b banke Plutus khsoh amadid')
        
    def show_current(self):
        password=int(input('lotfan ramze kart ro vared konid:'))
        if password==self.PIN:
        
            if self.balance>=100:
                
    
                self.balance=self.balance-100
                print('mojodie hesabe shoma hast :')
                print(self.balance)  
            else:
                print('motasfeane shoam mojodie mojodie hesba ham nadard')
        else:
            print('ramze shoma doros nemibashad')
            
            
    def deposit(self,amount):
        password=int(input('lotfan ramze kart ro vared konid:'))
        if password==self.PIN:
            self.balance=self.balance+amount
            print('varize shoam anjam shod')
            print(f'Mojodie hesabe shoma : {self.balance}')
        else:
            print('ramze shoam sahih nemibashad')
        
        

    def ATM(self,amount):
        password=int(input('lotfan ramze kart ro vared konid:'))
        if password==self.PIN:
        
            if self.balance - amount>0:
    
                self.balance=self.balance - amount
                print('bardasht ba moafaghiat anjam shod')
                print(f'mojodie hesabe shoma: {self.balance}')
            else:
                print('mojodie shoam kafi nmibashad')
        else:
            print('ramze vared shode shaih nemibashad')
            
            
        
c1=BANK('ali',30,10000,1234)
            
c1.show_current()


c1.ATM(5000)
        
     
        
class BANK:

    def __init__(self,nam,sen,moojoodie_avalie,password):
        #if len(password)==4:
        self.name=nam
        self.age=sen
        self.balance=moojoodie_avalie
        self.PIN =password
      
        
    def welcome(self):
        esm=self.name
        print(f'salam jenabe {esm} , b banke Plutus khsoh amadid')
        
    def show_current(self):
        password=int(input('lotfan ramze kart ro vared konid:'))
        if password==self.PIN:
        
            if self.balance>=100:
                
    
                self.balance=self.balance-100
                print('mojodie hesabe shoma hast :')
                print(self.balance)  
            else:
                print('motasfeane shoam mojodie mojodie hesba ham nadard')
        else:
            print('ramze shoma doros nemibashad')
            
            
    def deposit(self,amount):
        password=int(input('lotfan ramze kart ro vared konid:'))
        if password==self.PIN:
            self.balance=self.balance+amount
            print('varize shoam anjam shod')
            print(f'Mojodie hesabe shoma : {self.balance}')
        else:
            print('ramze shoam sahih nemibashad')
        
        

    def ATM(self,amount):
        password=int(input('lotfan ramze kart ro vared konid:'))
        if password==self.PIN:
        
            if self.balance - amount>0:
    
                self.balance=self.balance - amount
                print('bardasht ba moafaghiat anjam shod')
                print(f'mojodie hesabe shoma: {self.balance}')
            else:
                print('mojodie shoam kafi nmibashad')
        else:
            print('ramze vared shode shaih nemibashad')
            
    def set_password(self):
        password=int(input('lotfan ramze kart ro vared konid:'))
        if password==self.PIN:
            
            new_password=int(input('lotfan ramze jadide khdo rad vared konid:'))
            
            #if len(new_passwor)
            
            confirm_password=int(input('lotfan dobare passworde jadide khdo ra avred konid:'))
            
            if new_password==confirm_password:
                self.PIN=new_password
                print('passworf ba moafghiat anjam shod')
            else:
                print('motasefane dota ramzbaham barbad nist')
                
        else:
            print('ramze shoam doro snmibashad')
        
        
        
        
c1=BANK('ali',30,10000,1234)
        
       
c1.show_current()#9900

c1.set_password()

 

c1.show_current()
#ramze shoma doros nemibashad


c1.show_current()




    
    
    
'''

TASK1---> 
taraf too ahrja har vaght 3 bar ramz ro eshtebah zad kartesh ban bshe

#ban kone kole kart ro

hint--> __init__ --> self.ban =off


TASK2--->transfer history()

#clcik koni

+1000
-500
+300
-6000

hint--> list --> self.transfer=[]

deposit , atm --> append()


TASK3---> (optional)

mohem tarin task

Bug haro bartarf kon
tabe ye jadid behesh ezafe kon
(kahlaghiat)







'''



