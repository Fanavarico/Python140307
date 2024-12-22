#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

In The Name of GOD


Created on Sun Dec 22 17:42:06 2024

@author: Ali Pilehvar Meibody


ADV_L6_Attend


"""


'''



CLASS -----------------


CLASS--> az dleesh object miekshim biroon


class---> 
1-properties ( values , dkaheel self --> ghafase ) object.value
2-methods (function ha hastan k kari mikonan) object.funciton()



jalaseye adv_l5_attend

BANK


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
        print(f'salam  moshtarie aziz , {thisname} khosh amadid b banke Plutus')

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
    



obj1=BANK('ali',30,1000,1234)



obj1.welcome()
#salam  moshtarie aziz , ali khosh amadid b banke Plutus

obj1.show_currency()
'''
Moshtarie aziz mojodie hesab shoma hast :
900
'''


obj1.deposit(1000)
'''
Variz ba moafaghiat anjam shod
Mojoodie shoma : 1900
'''

obj1.ATM(4000)
#mojodie shoam akfi nemibashad

obj1.ATM(1500)

'''
bardashte shoma ba moafaghiat anjam shod
mojodie shoam bad az bardahst hast:400

'''



#password ro avaz konim



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
        print(f'salam  moshtarie aziz , {thisname} khosh amadid b banke Plutus')

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
            
            
    def change_password(self):
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            new_password=input('ramze jadid ra vared konid:')
            
            if len(new_password)==4:
                new_new_password=input('ramze jadide khod ra baraye taeed dobare vared konid:')
                
                if new_password==new_new_password:
                    self.PIN=int(new_password)
                    print('ramze shoma ba moafaghiat taghir kard')
 
                else:
                    print('ramzha yeksna nis, mojadadan emtehan farmaeed')
                
            else:
                print('ramze shoam bish az 4 ragham hast, mojadad az aval emtehan konid')
            
            
        else:
            print('ramze vard shdoe doros nemibashad')
        
        
   
obj1=BANK('ali',30,3000,1234)
        

obj1.show_currency()    
'''
Moshtarie aziz mojodie hesab shoma hast :
2900

'''

obj1.change_password()


obj1.show_currency()
'''
Lotfan ramzetoon ro vared namaeed:1368
Moshtarie aziz mojodie hesab shoma hast :
2800

'''


#----FUNCTIONS HAEE K MSIHDO ADD KRD----

'''
1---> ramz ag bish az 3 bar vared she ghofl beshe account

2---> transfer history  (tarakonesh)


3--> khdoeton custom (change_password)


'''


#==============================================
#==============================================
#==============================================
#==============================================
#==============================================
#-------------TASK1 --> BISH AZ 3 BAR NATOONE VARED KONE---
#==============================================


obj1.show_currency()



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
        print(f'salam  moshtarie aziz , {thisname} khosh amadid b banke Plutus')

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
            
            
    def change_password(self):
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            new_password=input('ramze jadid ra vared konid:')
            
            if len(new_password)==4:
                new_new_password=input('ramze jadide khod ra baraye taeed dobare vared konid:')
                
                if new_password==new_new_password:
                    self.PIN=int(new_password)
                    print('ramze shoma ba moafaghiat taghir kard')
 
                else:
                    print('ramzha yeksna nis, mojadadan emtehan farmaeed')
                
            else:
                print('ramze shoam bish az 4 ragham hast, mojadad az aval emtehan konid')
            
            
        else:
            print('ramze vard shdoe doros nemibashad')
        
        
     
'''
import getpass
password=input('passwordeton ro vared konid')

password = getpass.getpass()
s
password=input('passwordeton ro vared konid')

print(password)
        


import pwinput
password=pwinput.pwinput()


pwinput.pwinput()
password=input('passwordeton ro vared konid')

# For Python 2:
from Tkinter import Entry, Tk
# For Python 3
from tkinter import Entry, Tk

master = Tk()

Password = Entry(master, bd=5, width=20, show="*")
Password.pack()

master.mainloop()




import getpass

# Prompt user to enter password
password = getpass.getpass("Enter your password: ")

# Now you can use the entered password
print("Password entered:", password)




Pyqt
pyslide


'''




#------------------------------------------------------

#----->


#beshmore --> talashe namovafagh ro 

ADMIN_PASSWORD=8000

class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        self.wrong_attempt=0
        
        
    def welcome(self):
        thisname=self.name
        print(f'salam  moshtarie aziz , {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
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
            self.wrong_attempt=self.wrong_attempt+1
            print('ramz doros nemibashad')
        
    def deposit(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.balance=self.balance + amount
            print('Variz ba moafaghiat anjam shod')
            print(f'Mojoodie shoma : {self.balance}')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vared shdoe doros nmiabshad')
        
    def ATM(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
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
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
    def change_password(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            new_password=input('ramze jadid ra vared konid:')
            
            if len(new_password)==4:
                new_new_password=input('ramze jadide khod ra baraye taeed dobare vared konid:')
                
                if new_password==new_new_password:
                    self.PIN=int(new_password)
                    print('ramze shoma ba moafaghiat taghir kard')
 
                else:
                    print('ramzha yeksna nis, mojadadan emtehan farmaeed')
                
            else:
                print('ramze shoam bish az 4 ragham hast, mojadad az aval emtehan konid')
            
            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')

    def unblock(self):
        
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
        


obj1=BANK('ali',30,1000,1234)

obj1.show_currency()

obj1.wrong_attempt #1

obj1.ATM(1000)

obj1.wrong_attempt #2

obj1.show_currency()

obj1.wrong_attempt #3


#hala k 3 shode harkair bkham konm
#oon if avalie true msihe
#kart masdood

obj1.show_currency()
#karte shoma masdood mibashad


obj1.ATM(1000)
#karte shoma masdood mibashad



#----BANK B TRF MIGAM AGHA LOTFAN OK KON


obj1.unblock()



obj1.show_currency()
'''
Lotfan ramzetoon ro vared namaeed:1234
Moshtarie aziz mojodie hesab shoma hast :
900

'''





#-----------bugf peyda krdm

obj1.show_currency()

#yek ba rghalat
#doi bar ghalat
obj1.wrong_attempt #2


obj1.show_currency()
'''
Moshtarie aziz mojodie hesab shoma hast :
800

'''

# 3 bar ejaze drm bznm 
obj1.show_currency()

obj1.wrong_attempt

#yani shoam har dafe doro sramzeto bzni 3 bar ejaze dri ghalat bzni
#wrfing attemp restart ishe



#===================================
ADMIN_PASSWORD=8000

class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        self.wrong_attempt=0

    def welcome(self):
        thisname=self.name
        print(f'salam  moshtarie aziz , {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            if self.balance-100>=0:
                self.balance=self.balance-100
                current=self.balance
                print('Moshtarie aziz mojodie hesab shoma hast :')
                print(f'{current}')
            else:
                print('shoma moojodoi mojoodi ham nadarid')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramz doros nemibashad')
        
    def deposit(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            self.balance=self.balance + amount
            print('Variz ba moafaghiat anjam shod')
            print(f'Mojoodie shoma : {self.balance}')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vared shdoe doros nmiabshad')
        
    def ATM(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            #if self.balance-amount>=5000:
            if self.balance-amount>=0:
                self.balance=self.balance-amount
                print('bardashte shoma ba moafaghiat anjam shod')
                print(f'mojodie shoam bad az bardahst hast:{self.balance} ')
            else:
                print('mojoodie shoma kafi nemibashad')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
    def change_password(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            new_password=input('ramze jadid ra vared konid:')
            
            if len(new_password)==4:
                new_new_password=input('ramze jadide khod ra baraye taeed dobare vared konid:')
                
                if new_password==new_new_password:
                    self.PIN=int(new_password)
                    print('ramze shoma ba moafaghiat taghir kard')
 
                else:
                    print('ramzha yeksna nis, mojadadan emtehan farmaeed')
                
            else:
                print('ramze shoam bish az 4 ragham hast, mojadad az aval emtehan konid')
  
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')

    def unblock(self):
        #------- if if if if 
        #local host
        #ip 
        #kodom computer
        #user pass
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
        
        
#========================================
#------TASK 2---> TRANSFER HISTORY BESAZ

# + - 
#yaddasht--> zakhire beshe

#shoam aval yechi niaz dari ye zarf k inaro toosh brizi



ADMIN_PASSWORD=8000

class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        self.wrong_attempt=0
        self.transfer_history=[]

    def welcome(self):
        thisname=self.name
        print(f'salam  moshtarie aziz , {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            if self.balance-100>=0:
                self.balance=self.balance-100
                current=self.balance
                print('Moshtarie aziz mojodie hesab shoma hast :')
                print(f'{current}')
            else:
                print('shoma moojodoi mojoodi ham nadarid')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramz doros nemibashad')
        
    def deposit(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            self.balance=self.balance + amount
            
            self.transfer_history.append(f'+ {amount}')


            print('Variz ba moafaghiat anjam shod')
            print(f'Mojoodie shoma : {self.balance}')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vared shdoe doros nmiabshad')
        
    def ATM(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            #if self.balance-amount>=5000:
            if self.balance-amount>=0:
                
                
                self.transfer_history.append(f'- {amount}')
                
                self.balance=self.balance-amount
                print('bardashte shoma ba moafaghiat anjam shod')
                print(f'mojodie shoam bad az bardahst hast:{self.balance} ')
            else:
                print('mojoodie shoma kafi nemibashad')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
    def change_password(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            new_password=input('ramze jadid ra vared konid:')
            
            if len(new_password)==4:
                new_new_password=input('ramze jadide khod ra baraye taeed dobare vared konid:')
                
                if new_password==new_new_password:
                    self.PIN=int(new_password)
                    print('ramze shoma ba moafaghiat taghir kard')
 
                else:
                    print('ramzha yeksna nis, mojadadan emtehan farmaeed')
                
            else:
                print('ramze shoam bish az 4 ragham hast, mojadad az aval emtehan konid')
  
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')

    def unblock(self):
        #------- if if if if 
        #local host
        #ip 
        #kodom computer
        #user pass
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
        
        
    def show_history(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            print('=========================')
            print('----Tarakonesh haye shoma-----')
            
            for i in self.transfer_history:
                print(i)
                print('----')
            
            print('=========================')
            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
    
        
      
obj1=BANK('ali',30,1000,1234)
        

obj1.show_currency()
'''
Moshtarie aziz mojodie hesab shoma hast :
900

'''



obj1.deposit(1000)


obj1.ATM(500)


obj1.deposit(10000)

obj1.ATM(3780)

obj1.ATM(2930)


obj1.ATM(2000)


obj1.deposit(10000)



#---------------

obj1.show_history()


#===============================================
#MORE ADVANCED==================================

ADMIN_PASSWORD=8000

class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        self.wrong_attempt=0
        self.transfer_history=[]

    def welcome(self):
        thisname=self.name
        print(f'salam  moshtarie aziz , {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            if self.balance-100>=0:
                self.balance=self.balance-100
                current=self.balance
                print('Moshtarie aziz mojodie hesab shoma hast :')
                print(f'{current}')
            else:
                print('shoma moojodoi mojoodi ham nadarid')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramz doros nemibashad')
        
    def deposit(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            self.balance=self.balance + amount
            
            self.transfer_history.append(f'+ {amount}')


            print('Variz ba moafaghiat anjam shod')
            print(f'Mojoodie shoma : {self.balance}')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vared shdoe doros nmiabshad')
        
    def ATM(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            #if self.balance-amount>=5000:
            if self.balance-amount>=0:
                
                
                self.transfer_history.append(f'- {amount}')
                
                self.balance=self.balance-amount
                print('bardashte shoma ba moafaghiat anjam shod')
                print(f'mojodie shoam bad az bardahst hast:{self.balance} ')
            else:
                print('mojoodie shoma kafi nemibashad')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
    def change_password(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            new_password=input('ramze jadid ra vared konid:')
            
            if len(new_password)==4:
                new_new_password=input('ramze jadide khod ra baraye taeed dobare vared konid:')
                
                if new_password==new_new_password:
                    self.PIN=int(new_password)
                    print('ramze shoma ba moafaghiat taghir kard')
 
                else:
                    print('ramzha yeksna nis, mojadadan emtehan farmaeed')
                
            else:
                print('ramze shoam bish az 4 ragham hast, mojadad az aval emtehan konid')
  
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')

    def unblock(self):
        #------- if if if if 
        #local host
        #ip 
        #kodom computer
        #user pass
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
        
        
    def show_history(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            
            
            if len(self.transfer_history)==0:
                print('shoma tarakoneshi nadashtid')
                
            else:
                print('=========================')
                print('----Tarakonesh haye shoma-----')
                
                for i in self.transfer_history:
                    print(i)
                    print('----')
                
                print('=========================')
                
            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
    
    def calculation(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:

            positive_values=[]
            negative_values=[]

            for i in self.transfer_history:
                
                pos_or_neg=i[0]
                

                if pos_or_neg=='+':
                    positive_values.append(int(i[2:]))

                if pos_or_neg=='-':
                    negative_values.append(int(i[2:]))
                    

                    
            all_deposition=sum(positive_values)
            all_atm=sum(negative_values)
            
            
            print('------------')
            
            print('Majmooe varize shoma : ',all_deposition)
            
            print('------------')
            
            print('Majmooe bardashte shoma:',all_atm)
            
            

        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
        
        

obj1=BANK('ali',30,10000,1234)

obj1.deposit(1000)


obj1.ATM(500)


obj1.deposit(10000)

obj1.ATM(3780)

obj1.ATM(2930)


obj1.ATM(2000)


obj1.deposit(10000)
    

#hame ina rftn too list --> transfer_history =[+ , - ,...]

#hame ye dakheel liste transfer_hsitory neshon mdie
obj1.show_history()
    
'''
=========================
----Tarakonesh haye shoma-----
+ 1000
----
- 500
----
+ 10000
----
- 3780
----
- 2930
----
- 2000
----
+ 10000
----

'''

obj1.calculation()

'''
------------
Majmooe varize shoma :  21000
------------
Majmooe bardashte shoma: 9210

'''


'''

Tamrin

#----LIMTI ROOZANE ----
#bardahstatm --> limtie roozane
#3 bar pool bardari , 1000 toman

#---Init---
#self.daily_number=0
#self.daily_amount=0

#tooye ATM --> amount+self.daily_amount
#number + self.daily__number

#if--->

'''



ADMIN_PASSWORD=8000

class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        self.wrong_attempt=0
        self.transfer_history=[]

    def welcome(self):
        thisname=self.name
        print(f'salam  moshtarie aziz , {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            if self.balance-100>=0:
                self.balance=self.balance-100
                current=self.balance
                print('Moshtarie aziz mojodie hesab shoma hast :')
                print(f'{current}')
            else:
                print('shoma moojodoi mojoodi ham nadarid')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramz doros nemibashad')
        
    def deposit(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            self.balance=self.balance + amount
            
            self.transfer_history.append(f'+ {amount}')


            print('Variz ba moafaghiat anjam shod')
            print(f'Mojoodie shoma : {self.balance}')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vared shdoe doros nmiabshad')
        
    def ATM(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            #if self.balance-amount>=5000:
            if self.balance-amount>=0:
                
                
                self.transfer_history.append(f'- {amount}')
                
                self.balance=self.balance-amount
                print('bardashte shoma ba moafaghiat anjam shod')
                print(f'mojodie shoam bad az bardahst hast:{self.balance} ')
            else:
                print('mojoodie shoma kafi nemibashad')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
    def change_password(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            new_password=input('ramze jadid ra vared konid:')
            
            if len(new_password)==4:
                new_new_password=input('ramze jadide khod ra baraye taeed dobare vared konid:')
                
                if new_password==new_new_password:
                    self.PIN=int(new_password)
                    print('ramze shoma ba moafaghiat taghir kard')
 
                else:
                    print('ramzha yeksna nis, mojadadan emtehan farmaeed')
                
            else:
                print('ramze shoam bish az 4 ragham hast, mojadad az aval emtehan konid')
  
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')

    def unblock(self):
        #------- if if if if 
        #local host
        #ip 
        #kodom computer
        #user pass
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
        
        
    def show_history(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            
            
            if len(self.transfer_history)==0:
                print('shoma tarakoneshi nadashtid')
                
            else:
                print('=========================')
                print('----Tarakonesh haye shoma-----')
                
                for i in self.transfer_history:
                    print(i)
                    print('----')
                
                print('=========================')
                
            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
    
    def calculation(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            

            positive_values=[]
            negative_values=[]

            for i in self.transfer_history:
                
                pos_or_neg=i[0]
                

                if pos_or_neg=='+':
                    positive_values.append(int(i[2:]))

                if pos_or_neg=='-':
                    negative_values.append(int(i[2:]))
                    

                    
            all_deposition=sum(positive_values)
            all_atm=sum(negative_values)
            
            
            print('------------')
            
            print('Majmooe varize shoma : ',all_deposition)
            
            print('------------')
            
            print('Majmooe bardashte shoma:',all_atm)
            
            

        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
#-------> inherent --> ers mibare


#hame ye bank ha --> miri --> hesabe arzi mitoni doros koni

#clase jadidet ro benevis too parnatez esme oon clas k mkikhay b ers bbri ro bnvis
class CURRENCY_BANK(BANK):
    #boro az bank yek class jadid bsaz
    #name,age,current,PIn chizae bode k too clas avali mikahste
    #behehs chizi ezafe koni
    #harchizi k hasto jadid mikhay ro too __init___
    #harchi kghadim boode ro to super()
    
    def __init__(self,name,age,current,PIN,currency_id):
        super().__init__(name,age,current,PIN)
        
        self.currency_id=currency_id
        
    def welcome_english(self):
        
        name=self.name
        print(f'Hello {name} Welcome to our Bank, PLUTUS, We appreciate your opening account')
        
        
        

obj1=CURRENCY_BANK('ali',30,10000,1377,500)

obj1.welcome_english()
#Hello ali Welcome to our Bank, PLUTUS, We appreciate your opening account

#malooem tabe hae k tooye currency_bank minevisi ro dare
#ama aya tabe haye gahbli ham dare?


obj1.welcome()
#salam  moshtarie aziz , ali khosh amadid b banke Plutus


#tabeye ghablio dare ejra mikoni
#ramzi alangozashti ro dre migire

obj1.show_currency()
#Moshtarie aziz mojodie hesab shoma hast :
#9900






class CURRENCY_BANK(BANK):
    #boro az bank yek class jadid bsaz
    #name,age,current,PIn chizae bode k too clas avali mikahste
    #behehs chizi ezafe koni
    #harchizi k hasto jadid mikhay ro too __init___
    #harchi kghadim boode ro to super()
    
    def __init__(self,name,age,current,PIN,currency_id):
        super().__init__(name,age,current,PIN)
        
        self.currency_id=currency_id
        
        self.currency_balance=0 #ppoole arzi
        
        
    def welcome_english(self):
        
        name=self.name
        print(f'Hello {name} Welcome to our Bank, PLUTUS, We appreciate your opening account')
        
    #amount-->chan  hezar toman mikhad b dolar tabdil kone
    def change_money(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0

            if self.balance>=amount:
                
                self.balance=self.balance - amount
                
                
                #---------tabe sedash mzine
                #hamoon rooz pole dollar ro dar miare
                
                usd=80000
                
                #----------
                self.currency_balance=amount/usd+self.currency_balance
                
                print(f'Ba moafaghiat {amount} toman b {amount/usd} dollar tabdil shod')
                print(f'mojodie arze shoma : {self.currency_balance} dollar')
                
            else:
                print('motasefane mojodi kafinemibashad')

            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
          
            
OBJ1=CURRENCY_BANK('ALI', 30, 2000000, 1377, 40)
        
OBJ1.welcome_english()        


OBJ1.show_currency()
#Moshtarie aziz mojodie hesab shoma hast :
#1999900

OBJ1.ATM(99800)

'''
bardashte shoma ba moafaghiat anjam shod
mojodie shoam bad az bardahst hast:1900000 

'''
#mikham az 1900000
#900 hezar toman brizam too account arzim

OBJ1.change_money(900000)

'''
Lotfan ramzetoon ro vared namaeed:1377
Ba moafaghiat 900000 toman b 11.25 dollar tabdil shod
mojodie arze shoma : 11.25

'''

OBJ1.show_currency()

OBJ1.currency_balance #11.25


#---------------


'''



#-----------
TAKLIF 1--> (ghesmate clas ro yad grfti ---> class BANK() to baayd class)
abrdahste poole arzi


currency_atm()

currency_deposition-->chaneg_money

show_transfer_history()

calculation()



#------------
TAKLIF ---> (inherent )
too clas ghabli tgahir ijad bdi 

show _currency ham dollar neshon bede ham arz




#----------
TAKLIF AKAHR
Yek hesab ramz arz besaze

change_money(amount)

10000 toman

input--> ch ramz arzi mikhay tabdilesh konam barat??
bitcoin
ether
....




'''


def crypto_update():
    return [96094, 3323.84, 182.73]
    
    
    
class CRYPTO_CURRENCY_BANK(CURRENCY_BANK):
    #boro az bank yek class jadid bsaz
    #name,age,current,PIn chizae bode k too clas avali mikahste
    #behehs chizi ezafe koni
    #harchizi k hasto jadid mikhay ro too __init___
    #harchi kghadim boode ro to super()
    
    def __init__(self,name,age,current,PIN,currency_id,crypto_id):
        super().__init__(name,age,current,PIN,currency_id)
        
        self.crypto_id=crypto_id
        
        self.crypto_balance=0 #ppoole arzi
        

    #amount-->chan  hezar toman mikhad b dolar tabdil kone
    #b dollar
    
    def change_crypto(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            

            if self.currency_balance>=amount:

                
                crypto_type=input('Shoma mikhahid b che ramz arzi pool tbaidl konid? :')
                
                
                crypto_list=crypto_update()
                
                if crypto_type=='bitcoin':
                    self.currency_balance=self.currency_balance - amount
                    crypto_amount=crypto_list[0]
                    
                elif crypto_type=='etherium':
                    self.currency_balance=self.currency_balance - amount
                    crypto_amount=crypto_list[1]
                    
                elif crypto_type=='solana':
                    self.currency_balance=self.currency_balance - amount
                    crypto_amount=crypto_list[2]
                    
                    
                    
                #-------
                
                
                else:
                    print('ramz arz mojod nemibashad')
                    
                    
                
                #----------
                self.crypto_balance=amount/crypto_amount+self.crypto_balance
                
                print(f'Ba moafaghiat {amount} dollar b {amount/crypto_amount} bitcoin tabdil shod')
                print(f'mojodie arze shoma : {self.crypto_balance} bitcoin')
                
                    
 
            else:
                print('motasefane mojodi kafinemibashad')

            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
            

        
              
            
obj1=  CRYPTO_CURRENCY_BANK('ali', 30, 300000000, 1234,10,3223239723)
            
      
obj1.welcome()
#salam  moshtarie aziz , ali khosh amadid b banke Plutus

#BANK

#crypto --> inehrent az currency --> bank


#YEK TABE AZBANK --> SHOW_CURRECNY
obj1.show_currency()

'''
Moshtarie aziz mojodie hesab shoma hast :
299999900

'''

obj1.deposit(1000000000000)

'''
Lotfan ramzetoon ro vared namaeed:1234
Variz ba moafaghiat anjam shod
Mojoodie shoma : 1000299999900

tomanieee

'''





#CURRENCY------->
obj1.change_money(100000000)

'''
Lotfan ramzetoon ro vared namaeed:1234
Ba moafaghiat 100000000 toman b 1250.0 dollar tabdil shod
mojodie arze shoma : 1250.0


1250 dollar


'''


#---crypto

obj1.change_crypto(1000)

'''
Ba moafaghiat 1000 dollar b 0.010410268689034864 bitcoin tabdil shod
mojodie arze shoma : 0.010410268689034864 bitcoin

'''




'''



YEK HESAB SAKHTAM--->


100 melyon dashtam

hesab arzi sakhtma 100 melyono --> 1250 dollar


1000 dolalr--> 0.01 bitcoin



'''







