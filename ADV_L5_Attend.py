"""
L5
ADV_L5_Attend



In The Name of GOD

ALI PILEHVAR MEIBODY



Python built in function (print, input, len , type , ......)
keywords (logic---> if else , elif ,for , while)
Variable ( str, int, float , complex, bool), List , tuple, dictionary, set
def --> (review)--

CLASSS
CLASS OBJECT ORIENTED





"""

print()

print('salam khobi')
print('chetori')



print('salam khobi',end='*')
print('chetori')




#matne 
'''
txt --> notepad --> benevis
doc, docx --> word 
pdf --> pdf
csv , xlsx , xlx--> table --> excell
jpg, png, gif , mp4 --> ax , movie

koja zakhrie hast???

Folder C , ..../desktop/ documention , downloads and..
C-->  programm file , programm 86x , ...users 
desktop--> data --> dr. amiri 

user--> data --> dr.mousapour --> data file zakhir

#filet kojas


SPYDER--->  PYTHON -->SPYDER


AGAR 

open('data.txt')

dota rah


1---> b besmela beheshadress bdm 
C://users/a./desktop/data/dr./data.txt
open('C://users/a./desktop/data/dr./data.txt')


2-->jaee k spyder dare ejra mishe ro taghir bdm
open('data.txt')

open-->tabe --> mire (raho neshon ddim)-->dastrssi peyda mikone
bazsh mikone --> khrooji midd behet


shoam bayad yek zarf(variable)-->bezari jolosh va 
zkahriahs koni
ax , txt , excell, and......

txt --> 
bekhoonish (read)
benevisi (write)
be tahehs ezaf koni ( append)

open('data.txt','')

close

applicable 

ketabkhone ha --> pandas, numpy matplotlib 

tabe haee daran k az open dare stefad emikoen va open

xlsx --

pandas.open_excell('C://users/a./desktop/data/dr./data.txt')
jadval --> chanta list to dar too behet mdie ba formate ok




'''
open('C:')

open()




#-----------------------------------------------
#------------------------------------------------------
#-------


#-->tabe function


code=input('lotfan codetoon ro vared namaeed:')
text=f"""
product information

product code: {code}


PLUTUS @CO


"""

print(text)


#vorodi az karbar migire 
#Khoroji ro namayehs bmide


'''

application

web

telegram bot

bot

EBM --> ELECTRON BEAM MELTING

GUI --> Graphical user interface 


vorodii --> user side (input)dokme,neveshte , file
khoroji --> namayesh mide

mire dakheel console




******application 

vorodi , khorojit dg too consoel nis
be yejaee vasle

site 

teelgram









'''


code=input('lotfan codetoon ro vared namaeed:')
text=f"""
product information

product code: {code}


PLUTUS @CO


"""

print(text)

#bot --> toye tleegram--> API KEY 
#-->password


'''
API='djsadsjt6qdasjycast7dgeqewyg6cagfewquadbugs65cgcusdb'

#ketabkhoen telegram
#ketabkhoen koli tabe , class , def ,......

#application 

import telegram
telegram.application(API)



#telegram koliii tabe dare

#input -->
#inptu -->anamyesh mide migire 
#Print-->namayesh mide


#input-->console
telegram.update.message.reply_text('lotfan codet ro beman bede')
code=update.message.text


mytext=f"""
product information

product code: {code}


PLUTUS @CO


"""

telegram.update.message.reply_text(mytext)




#-------------------------------------------------------

code=input('lotfan codetoon ro vared namaeed:')
text=f"""
product information

product code: {code}


PLUTUS @CO


"""

print(text)



answer=input('sabtesh konam ya na? yes/no ')

if answer.upper().strip()=='yes':
    print('agah sabt shod')
    
else:
    print('agha sbar nashod')
    
    
#---------

keyword=[telegram.Inlinekeywords('yes'),
         telegram.Inlinekeywords('no')]
telegram.update.message.reply_text('sabtesh konam ya na?',reply_markup=keyword)

    
qu=query.callback_data

if qu=='yes':
    telegram.update.message.reply_text('agha save shod')
else:
    telegram.update.message.reply_text('agha sabt nashod')
 
#----QT --> ketabkhone kh bozorge application 

#--> C++

#-->python --> pyslide , pyqt

#----
    

pyslide.application()

pyslide.background().set_x(400)

pyslide.label('aya taed mikonid yta na')
pyslide.push_button('yes')
pyslide.push_button('no')

if push_button.answer()=='yes':
    pyslide.label('taeed shod')
else:
    pyslide.label('taeed nashod')
    
    
    
#web ----
'''


#-------REVIEW-------------


'''

BOX --> VROODI KHOROJI



VORODII --> BOX --> KHOROJI



def name(vorodi1):
    dastoor1
    return khoroji



#call
#hamrogeh nai zdahsti

name(voorodit)





#geenrla form of function
def name(in1,in2,in3,...):
    order1
    order2
    .......
    ....
    ..
    return out1,out2,out3


'''

'''
Calculator

'''

#sedash mzianim anajm bde
#vodoirii--> dota adad --> khroji hesab kone


def jam(a,b):
    c=a+b
    return c



def jam(a,b):
    return a+b


jam(4,5)

#khoroji ba print frgh dre



def jam(a,b):
    c=a+b
    print(c)



jam(4,5) #9
#*** 9 ro neveshtttttt


zarf=jam(4,5)
#9 ro minvise

print(zarf)#None


#print fght namayehs mdie chizi pass nmide jaee k call (sedash mikonim)




def jam(a,b):
    c=a+b
    return c


zarf=jam(4,5)

print(zarf) #9
#khali nsi
#4 ,5 ro grfte --> too khdoehs jam krde 9 --> return dade
#bargardonde? koaj??? hamonjae k callesh (sedash krdim)




#-----------------------------------------------


#local global
#mahali , sarasari


def jam(a,b):
    c=a+b
    return c

jam(4,5)


#c nmisazim
#zarfe movagahat-->local


#biroon az tabe ina shekastan nisan


#c=4+5 --> 9

print(c)















c=10

def jam(a,b):
    c=a+b
    return(c)

d=jam(4,5)

print(c) #10









#agar ma bekhaym k yek chizi too yek tabe
#agha man bekahm in global brinam beshnasan



def tafrigh(numb1,numb2):
    h=numb1-numb2
    return h


d=tafrigh(10,5)

print(h)


#man bkham ychzii too yd ele tabe e bironesham beshansan
#local nabashe chiak rkonM???

#glbalesh kon


def tafrigh(numb1,numb2):
    global h
    h=numb1-numb2
    z=h*100
    t=z-100
    return h


d=tafrigh(10,5)

print(z) # z is not defined -->locale
print(t) #t is not defined-->locale
print(h) #globalesh krdm-->5


#-----------------------------------------------

c=10
def jam(a,b):
    global c
    c=a+b
    return c

d=jam(4,5)
print(c)#9



#-----------

#f = m* a
#nirooo vared koni b yek jesmi ba jerme m --> shetabesh a mishe 

def newton(mass,ac):
    force=mass*ac
    return force


#man yek jesm daram 10 kg 
#10 ta shetabesh bashe
#forc chgdh bznmbsh

newton(10,10) # 100


newton(10)
    
#ag kam bdi mige miss krde 
#ag ziad bdi additional postional were given


#too hale masaele physic

#a shetab ->geranehs migrian 9.8

#default --> 9.8 bashe a=9.8 

#vali 
#yeki fght mass -->5 kg darmorede a shetab hrf nzd
#eror nde ->khdoet a ro 9.8 bgir

#ag ham kasi kahs taghir bde tdast e baz bashe



def newton(mass):
    
    force=mass*9.8
    return force


newton(10)


#kais dg nmitone shetab rotaghir bde


def newton(mass,acc=9.8):
    force=mass*acc
    return force

'''
***man yek tabe drm
dota vorodi dare
yeki mass yeki acc--> 
midi bshh mzire formol force ro hesba mikone pas smide


vorodi1 , vorodi 2--> box --> khrooji 

age vroodi 2 ro nadii -_> error nmdie
by default -->9.8 migire


ama toM mitoni tagireesham bdi






'''
newton(5,20) #100

newton(5)##errro missing 1   49.0


#---------------CLASS--------------------

#class

'''
CLASS->akarbordi tarin

C 
C++

c++ --> az class b
class bsazii 

object oriented 

Gahan shoam naiz darid k object (sheyt bsazid)





BANK ---> AFARD HESAB DOROS KONAN
VA POOL AVAL BRIZAN
VARDARAN
MOJODI BEGIRN

'''


def deposit(value):
    account=value
    print(f'varize {account} toman ba moaaghiat anajm shod')

deposit(400)



def current():
    print(account)


current()

#NameError: name 'account' is not defined


#function khali kar anjam bdi dar aksare jaha 70% moghiat ha



#niazmande class





'''

class name:
    
    def __init__(voroi hae migire)
    self. zakhriahs koni
    
self-->baarye inek yek megdhar ya harhcizio zakhie konim
k badanbdotim bahash bazi konim mohasebta



class--> too delesh koli tabe va adad

-----class-----
-----property (values)----
------method (fucntion)------


'''




class BANK:
    
    mojoodi=3203832727
    
    


mohsen=BANK()
    

#mohsen yek object az in clas hast

#too delesh --> proeprties (values) , tabe bashe
#kafie rooye mohsen dot bznm nogthe . behesh avsl sham


mohsen.mojoodi # 3203832727


#agah mohsen -->yek sheye az BANK


ali=BANK()

ali.mojoodi #3203832727


#tpod elsh tabe dahste bashe

class BANK:
    
    sen=18
    mojoodi=1000
    def welcome(self):
        print('salam khosh oomadid')


#yek calss --> properties  , method


#az in class koli object bsazi

#Obejcte 1


mohsen=BANK()
#agha az classe bank yek object bename mohsen bsaz

#kolan baraye dastresssi b attributes haye yek object
#bayad dot bzani


#class-->1-proeprties 2-methdos

#ag proeprties .esmesho 
#ag b tabe .esme tabe()

mohsen.mojoodi #1000
mohsen.sen #18

mohsen.welcome()


#-----------------------------------------
#in yek mesale bedoen kardbodz
#Mohsen ,a li , ......

#hamon b besmella vaghty yek object msiazm
#mikham bram va moshakhasat avalie behesh bdm
#k har object --> yek objecte khas (unqiue ) bashe


#class

mohsen=BANK()
#tooey giome , yekseri moshakahst bznm





class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.current=current





mohsen=BANK()

'''
TypeError: BANK.__init__() missing 3 required
 positional arguments: 'name', 'age', and 'current'

'''


obj1=BANK('mohsen',28,1000)



obj1.name #Mohsen
obj1.age
obj1.current



class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.current=current
    
    
    def welcome(self):
        print('salam khosh amadid')
        
obj1=BANK('mohsen',28,1000)

obj1.name

obj1.age
obj1.current

#() tabe

obj1.welcome()
#salam khosh amadid




obj2=BANK('ali',30,10000)

obj2.name
obj1.name
obj2.welcome()
obj1.welcome()



class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.current=current
    
    
    def welcome(self):
        thisname=self.name
        print(f'salam aghaye {thisname} khosh amadid b banke Plutus')



obj1=BANK('mohsen',28,1000)
obj2=BANK('ali',30,100000)



obj1.name #mohsen
obj2.name #ali



obj1.welcome()
#salam aghaye mohsen khosh amadid b banke Plutus

obj2.welcome()
#salam aghaye ali khosh amadid b banke Plutus




class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
    def welcome(self):
        thisname=self.name
        print(f'salam aghaye {thisname} khosh amadid b banke Plutus')

    
obj1=BANK('ali',30,10000)

obj1.name
obj1.age
obj1.current

#self--> ahrchizio dare ke dot khrode roosh
obj1.balance # 10000



'''
FARSI ---> PYTHON

trf besaze hesb 

ye tabe dahste bashe mojodi bgire -->show

ye tabe variz kone --> vorodi yedoen -_> pool chghd 1000 200000

atm -->pool bgire --> vorodi -->cheghad mikhad bgire




'''


class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
    def welcome(self):
        thisname=self.name
        print(f'salam aghaye {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        current=self.balance
        print('Moshtarie aziz mojodie hesab shoma hast :')
        print(f'{current}')
        
    def deposit(self,amount):
        self.balance=self.balance + amount
        print('Variz ba moafaghiat anjam shod')
        
    def ATM(self,amount):
        
        self.balance=self.balance-amount
        print('bardashte shoma ba moafaghiat anjam shod')
        
        
        
        




#besaziiiii

#0---> class BANK ro skahtam
#1---> object bsazam 
#obejct chia mikhad vroodi--> hamonae k too __init__


obj1=BANK('ali',30,1000)

#ccla-ss---> proeprties (values) / methods ( functions)

#-------properties-------
obj1.name #ali
obj1.age #30

#---------methods-------
obj1.welcome()
#salam aghaye ali khosh amadid b banke Plutus

obj1.show_currency()
#Moshtarie aziz mojodie hesab shoma hast :1000


#pool brizam
#deposit

obj1.deposit(2000)
#Variz ba moafaghiat anjam shod

obj1.show_currency()
#Moshtarie aziz mojodie hesab shoma hast : 3000


obj1.ATM(1500)
#bardashte shoma ba moafaghiat anjam shod


obj1.show_currency()
#Moshtarie aziz mojodie hesab shoma hast :
#1500


obj1.ATM(400000)
#bardashte shoma ba moafaghiat anjam shod

obj1.show_currency()
#Moshtarie aziz mojodie hesab shoma hast : -398500


#----------------------------------


class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        
    def welcome(self):
        thisname=self.name
        print(f'salam aghaye {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        current=self.balance
        self.balance=self.balance-100
        print('Moshtarie aziz mojodie hesab shoma hast :')
        print(f'{current}')
        
    def deposit(self,amount):
        self.balance=self.balance + amount
        print('Variz ba moafaghiat anjam shod')
        print(f'Mojoodie shoma : {self.balance}')
        
        
    def ATM(self,amount):
        if self.balance-amount>=0:
            self.balance=self.balance-amount
            print('bardashte shoma ba moafaghiat anjam shod')
        else:
            print('mojoodie shoma kafi nemibashad')
        
        
    
        
#more advanced--------

class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        
    def welcome(self):
        thisname=self.name
        print(f'salam aghaye {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        if self.balance-100>=0:
            current=self.balance
            self.balance=self.balance-100
            print('Moshtarie aziz mojodie hesab shoma hast :')
            print(f'{current}')
        else:
            print('shoma moojodoi mojoodi ham nadarid')
        
        
    def deposit(self,amount):
        self.balance=self.balance + amount
        print('Variz ba moafaghiat anjam shod')
        print(f'Mojoodie shoma : {self.balance}')
        
        
    def ATM(self,amount):
        #if self.balance-amount>=5000:
        if self.balance-amount>=0:
            self.balance=self.balance-amount
            print('bardashte shoma ba moafaghiat anjam shod')
        else:
            print('mojoodie shoma kafi nemibashad')
        
#--->class sakhtim 

#Object msiazim vroodi hamonas k to __init__    
        
obj1=BANK('ali',30,1000)

#---class---> 1-properties 2- methods


#-----properties--------

obj1.name
obj1.age


#------methods--------
obj1.welcome()

obj1.show_currency()

obj1.show_currency()



class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        
    def welcome(self):
        thisname=self.name
        print(f'salam aghaye {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        if self.balance-100>=0:
            self.balance=self.balance-100
            current=self.balance
            print('Moshtarie aziz mojodie hesab shoma hast :')
            print(f'{current}')
        else:
            print('shoma moojodoi mojoodi ham nadarid')
        
        
    def deposit(self,amount):
        self.balance=self.balance + amount
        print('Variz ba moafaghiat anjam shod')
        print(f'Mojoodie shoma : {self.balance}')
        
        
    def ATM(self,amount):
        #if self.balance-amount>=5000:
        if self.balance-amount>=0:
            self.balance=self.balance-amount
            print('bardashte shoma ba moafaghiat anjam shod')
            print(f'mojodie shoam bad az bardahst hast:{self.balance} ')
        else:
            print('mojoodie shoma kafi nemibashad')
        


        
obj1=BANK('ali',30,1000)

#---class---> 1-properties 2- methods


#-----properties--------

obj1.name
obj1.age
obj1.balance

#------methods--------
obj1.welcome()

obj1.show_currency()
#900
#ham namayehs dad 
#ham 100 tomanam kam krd


obj1.deposit(2000)
'''
Variz ba moafaghiat anjam shod
Mojoodie shoma : 2900

'''



obj1.ATM(1000)
'''
bardashte shoma ba moafaghiat anjam shod
mojodie shoam bad az bardahst hast:1900

'''


obj1.ATM(7000)
#mojoodie shoma kafi nemibashad


obj1.ATM(1900)
'''
bardashte shoma ba moafaghiat anjam shod
mojodie shoam bad az bardahst hast:0 
'''


obj1.show_currency()
#shoma moojodoi mojoodi ham nadarid


obj1.deposit(10000)
'''
Variz ba moafaghiat anjam shod
Mojoodie shoma : 10000

'''



'''

RAMZ

obj1=BANK('ali',30,1000,'a2983832')

'''

class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        
        
    def welcome(self):
        thisname=self.name
        print(f'salam aghaye {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            if self.balance-100>=0:
                self.balance=self.balance-100
                current=self.balance
                print('Moshtarie aziz mojodie hesab shoma hast :')
                print(f'{current}')
            else:
                print('shoma moojodoi mojoodi ham nadarid')
        else:
            print('ramz doros nemibashad')
        
    def deposit(self,amount):
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.balance=self.balance + amount
            print('Variz ba moafaghiat anjam shod')
            print(f'Mojoodie shoma : {self.balance}')
        else:
            print('ramze vared shdoe doros nmiabshad')
        
    def ATM(self,amount):
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            #if self.balance-amount>=5000:
            if self.balance-amount>=0:
                self.balance=self.balance-amount
                print('bardashte shoma ba moafaghiat anjam shod')
                print(f'mojodie shoam bad az bardahst hast:{self.balance} ')
            else:
                print('mojoodie shoma kafi nemibashad')
        else:
            print('ramze vard shdoe doros nemibashad')
    



obj1=BANK('ali',40,4000,1234)

obj1.name
obj1.welcome()



obj1.show_currency()

'''
Moshtarie aziz mojodie hesab shoma hast :
3900

'''

obj1.deposit(6100)




'''

TASK1
taraf 3 bar vared kone ramzo eshtebah
dg aslan natoen az hich goone tabe ha estefad kone

hint--> aval too init bayad yechi bsazi bsazi 





TASK2

Transfer history dashte bashe


transfer_history()
#done done transfer haro neshon bde
+ 100
-5000
+233
-3233
tarikhche 

hint--> init--> self.transfer=[]


TASK3 --> OPTIONAL

KHODET EZAFE KON .... (MOHEM TARIN TASK)

bashgah ---> ghad vazn ,.....



'''

