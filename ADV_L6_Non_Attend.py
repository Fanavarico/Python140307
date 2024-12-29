#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:37:44 2024

@author: apm
"""



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
        
        #liste khaliiiiii
        self.transfer_list=[]
        
        
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
        
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
            

        
        
        
        
#transection --> history 


#def --> az avlin timi k hesabo sakhti ta alan
#tarakonesh 


#+1000
#-500
#+800


'''
INFRUSTRUCTURE
ZIRSAKHT minevisim



#-----------------------------
Persian ---> Python ---> binary



tarakonesh--> mabaleghi k ezaf shode, kam shdoe ro 
biad done done neshon bede


ezaf --> deposite --> (amount) 
kam --> atm --> (AMOUNT)

berizam too ye list???
list mikahm






'''




class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        self.wrong_attempt=0
        
        #liste khaliiiiii
        self.transfer_list=[]
        
        
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
            
            
            self.transfer_list.append(f'+ {amount}')
            
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
                
                self.transfer_list.append(f'- {amount}')
                
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
        
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
            
            
            
    def transfer_history(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            
            #core--------------------------
            
            print('tarakoneshate shoma :')
            
            


        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')




obj1=BANK('ali',30,1000,1234)




obj1.deposit(2000)

'''

Variz ba moafaghiat anjam shod
Mojoodie shoma : 3000

'''

obj1.transfer_list
#['+ 2000']


obj1.ATM(1000)
'''
bardashte shoma ba moafaghiat anjam shod
mojodie shoam bad az bardahst hast:2000 

'''


obj1.transfer_list
#['+ 2000', '- 1000']

#farsi---> python



'''

beshkonesh

agha aval + - ha ro too ye ye list brizimmmmm
badesh namayesh bdim



'''



class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        self.wrong_attempt=0
        
        #liste khaliiiiii
        self.transfer_list=[]
        
        
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
            
            
            self.transfer_list.append(f'+ {amount}')
            
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
                
                self.transfer_list.append(f'- {amount}')
                
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
        
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
            
            
            
    def transfer_history(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            
            #core--------------------------
            
            print('tarakonesh haye shoma :')
            
            print('------------------------')
            for i in self.transfer_list:
                print(i)
                print('---')
                
            print('------------------------')
                
            
                
 

        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
            
obj1=BANK('ali',30,1000,1234)

obj1.deposit(2000)
obj1.deposit(1000)


obj1.ATM(1500)

obj1.deposit(3000)


obj1.ATM(2100)
obj1.ATM(2200)

#har dafe k man  deposit ya ATM kardm ina + - tooye transfer_list rikth eshdoe

#yek tabe darim bname transfer_hisutory

obj1.transfer_history()

'''
tarakonesh haye shoma :
------------------------
+ 2000
---
+ 1000
---
- 1500
---
+ 3000
---
- 2100
---
- 2200
---
------------------------

'''


#tabeye dg --> mohasebe kone + - haye mano

#shoam kolan 4000 ezaf krdin 6000 kahrj krdid

#def claculation



class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        self.wrong_attempt=0
        
        #liste khaliiiiii
        self.transfer_list=[]
        
        
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
            
            
            self.transfer_list.append(f'+ {amount}')
            
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
                
                
                #self.transfer_list.append(-amount)
                self.transfer_list.append(f'- {amount}')
                
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
        
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
            
            
            
    def transfer_history(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            
            #core--------------------------
            
            print('tarakonesh haye shoma :')
            
            print('------------------------')
            for i in self.transfer_list:
                print(i)
                print('---')
                
            print('------------------------')
                
            
                
 

        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
            
    def calcualtion(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            
            #-----core------
            
            
            
            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
mylist=obj1.transfer_list


print(mylist)


#+amount
#-amount

a='200'
int(a)
a='+ 200'
int(a)
#jami az keybordet


mylist=obj1.transfer_list

print(mylist)



positive_list=[]
negative_list=[]

for i in mylist:
    if i[0]=='+':
        positive_list.append(i)
        
    if i[0]=='-':
        negative_list.append(i)
#toonestam manfio mosbat ro jdoa konam ammaaaa
 
    
    

positive_list=[]
negative_list=[]

for i in mylist:
    if i[0]=='+':
        positive_list.append(int(i[2:]))
        
    if i[0]=='-':
        negative_list.append(int(i[2:]))




class BANK:
    #chizhaee k vaghty yek obejct gharar hast sakhet ebshe
    #taraf baayd vared kone ke objectesbh ba baghie frgh kone
    
    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        self.wrong_attempt=0
        
        #liste khaliiiiii
        self.transfer_list=[]
        
        
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
            
            
            self.transfer_list.append(f'+ {amount}')
            
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
                
                
                #self.transfer_list.append(-amount)
                self.transfer_list.append(f'- {amount}')
                
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
        
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
            
            
            
    def transfer_history(self):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            
            #core--------------------------
            
            print('tarakonesh haye shoma :')
            
            print('------------------------')
            for i in self.transfer_list:
                print(i)
                print('---')
                
            print('------------------------')
                
            
                
 

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
            
            #-----core------
            
            
            pos_list=[]
            neg_list=[]
        
            for i in self.transfer_list:
                
                if i[0]=='+':
                    pos_list.append(int(i[2:]))
                    
                if i[0]=='-':
                    neg_list.append(int(i[2:]))
                    
            #neg_list
            #pos_list
            
            sum_pos_list=sum(pos_list)
            sum_neg_list=sum(neg_list)
            
            
            print('---------------')
            
            print('majmooe varize shoma :',sum_pos_list)
            print('majmooe bardashte shoma:',sum_neg_list)
            
            print('------------------')                
            

        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            


obj1=BANK('ali',30,1000,1234)

obj1.deposit(2000)
obj1.deposit(1000)


obj1.ATM(1500)

obj1.deposit(3000)


obj1.ATM(2100)
obj1.ATM(2200)


obj1.transfer_history()

'''
Lotfan ramzetoon ro vared namaeed:1234
tarakonesh haye shoma :
------------------------
+ 2000
---
+ 1000
---
- 1500
---
+ 3000
---
- 2100
---
- 2200
---
------------------------

'''

obj1.calculation()

'''
---------------
majmooe varize shoma : 6000
majmooe bardashte shoma: 5800
------------------

'''




#------------------------------------
#------------------------------------

#ag man yek hesabe arzi bekham besazam
#bayad beram dobare az aval ye bank besazam????
#yek class??

#Nmeishe yek clas bsazam k yek shobe ee bashe azin 





#method ezafe koanm beehsh?



#ers bordan inherent

#YEK CLASS bname currency_bank k az class bank sakhte shdoe

class CURRENCY_BANK(BANK):
    #yani name,age,dcurrenct,pin tamame chizaee k bank mikahste bayad inam bkhad
    #mitonei chzie jadid ham ezaf koni
    
    def __init__(self,name,age,current,PIN,currency_id):
        #super--> iino b oon vasl kon
        super().__init__(name,age,current,PIN)
        
        
        self.currency_id=currency_id
        
        
    def welcome_english(self):
        name=self.name
        
        print(f'Hello {name} , welcome to plutus Bank , we appreciate your opening account')
        
        
        
        
obj1=CURRENCY_BANK('ali',30,1000,1234,191919)

obj1.welcome_english()
#Hello ali , welcome to plutus Bank , we appreciate your opening account


#tamame tavabeye BANK ham dare

obj1.show_currency()
'''
Moshtarie aziz mojodie hesab shoma hast :
900

'''


class CURRENCY_BANK(BANK):
    #yani name,age,dcurrenct,pin tamame chizaee k bank mikahste bayad inam bkhad
    #mitonei chzie jadid ham ezaf koni
    
    def __init__(self,name,age,current,PIN,currency_id):
        #super--> iino b oon vasl kon
        super().__init__(name,age,current,PIN)
        
        
        self.currency_id=currency_id
        
        self.currency_balance=0
        #in tomani nis
        
        #slef.balance -->tomani
        
    def welcome_english(self):
        name=self.name
        
        print(f'Hello {name} , welcome to plutus Bank , we appreciate your opening account')
        
        
        
        
    def exchange_money(self,amount):
        
        password=int(input('passwordeton ro bezanid:'))
        
        if password==self.PIN:
            
            
            if self.balance>=amount:
                self.balance=self.balance-amount
                
                us=80000
                
                self.currency_balance=self.currency_balance+amount/us
                
                
                print('hesabe shoam hast:')
                print(f'{self.balance} toman')
                print(f'{self.currency_balance} dollar')
                
            else:
                print('mojodi kafi nemibashad')
            

        else:
            #+ wrong attemp
            print('passworde shoam doros nis')


    def dollor_show_currency(self):
        
        print(f'mojodie shoam hast : {self.currency_balance}')


obj1=CURRENCY_BANK('ali',30,2000000,1234,191919)

obj1.welcome_english()
#Hello ali , welcome to plutus Bank , we appreciate your opening account

obj1.welcome()
#salam  moshtarie aziz , ali khosh amadid b banke Plutus


obj1.show_currency()
'''
Moshtarie aziz mojodie hesab shoma hast :
1999900

'''

obj1.deposit(100)
'''
Variz ba moafaghiat anjam shod
Mojoodie shoma : 2000000
'''


obj1.exchange_money(160000)
'''
hesabe shoam hast:
1840000 toman
2.0 dollar

'''


obj1.show_currency()

'''
Lotfan ramzetoon ro vared namaeed:1234
Moshtarie aziz mojodie hesab shoma hast :
1839900

'''



#-------Barname revolet




#banke majaziie


#hesabbb 
#hesab arzi

#ramz arz 
#hesabe ramz arz


#hesab tomani 
#hesab dolalri 

#aramz arz


class CRYPTO_BANK(CURRENCY_BANK):
    
    def __init__(self,name,age,current,PIN,currency_id,crypto_id):
        
        super().__init__(name,age,current,PIN,currency_id)
        
        self.crypto_id=crypto_id
        
        #hesabe bitcoin
        #hesabe teter
        #solana
        
        self.crypto_balance=0
        
        
        
    def welcome_crypto(self):
        
        print('Helloo , welcome to the wrold of traid')





obj1=CRYPTO_BANK('ali',30,1000000,1234,1919,'bitcoin')

obj1.welcome_crypto()

obj1.welcome_english()

obj1.welcome()




#request API


def update_crypto():
    
    #ami=request(API=28237398273932732)
    #response =[bitcoin, teter, solana]
    #adad gozashtam
    
    
    bitcoin=89818
    teter=1
    solana=192
    
    
    cyrpto_list=[bitcoin,teter,solana]
    return cyrpto_list
    


class CRYPTO_BANK(CURRENCY_BANK):
    
    def __init__(self,name,age,current,PIN,currency_id,crypto_id):
        
        super().__init__(name,age,current,PIN,currency_id)
        
        self.crypto_id=crypto_id
        
        #hesabe bitcoin
        #hesabe teter
        #solana
        
        self.crypto_balance=0
        
        
        
    def welcome_crypto(self):
        
        print('Helloo , welcome to the wrold of traid')



    def exchange_crypto(self,amount):
        #dollari
        
        #dollari 
        
        
        #if wrong.attemp>3
        
        password=int(input('passwordeton ro bezanid:'))
        
        if password==self.PIN:
            
            if self.currency_balance >=amount:
                
                
                
                
                self.currency_balance=self.currency_balance-amount
                
                
                list_crypto_price=update_crypto()
                
                if self.crypto_id=='bitcoin':
                    crypto_price=list_crypto_price[0]
                    
                elif self.crypto_id=='teter':
                    crypto_price=list_crypto_price[1]
                    
                elif self.crypto_id=='solana':
                    crypto_price=list_crypto_price[2]
                    
                
                
                self.crypto_balance=self.crypto_balance+ amount/crypto_price
                
                
                print('mojodie hesabe shoma:')
                
                print(f'{self.balance} toman')
                print(f'{self.currency_balance} dollar')
                print(f'{self.crypto_balance} {self.crypto_id}')
                
                
            else:
                print('you dont have enough money for crypto ')
                
                
        else:
            print('your password is incorrect')
                
            
            
        
obj1=CRYPTO_BANK('ali',30,20000000,1234,1919,'solana')

obj1.welcome()
#bank
#salam  moshtarie aziz , ali khosh amadid b banke Plutus


obj1.welcome_english()
#Hello ali , welcome to plutus Bank , we appreciate your opening account

obj1.welcome_crypto()
#Helloo , welcome to the wrold of traid


obj1.show_currency()
'''
Moshtarie aziz mojodie hesab shoma hast :
19999900

'''


obj1.deposit(100)

'''
Lotfan ramzetoon ro vared namaeed:1234
Variz ba moafaghiat anjam shod
Mojoodie shoma : 20000000

'''

#200 dollar

#200 dolar
#az hesabe tomani (BANK) --> hesabe azri (CURRENCY_BANK)
obj1.exchange_money(16000000)

'''
hesabe shoam hast:
4000000 toman
200.0 dollar

'''


obj1.exchange_crypto(160)
#160 solana
'''
passwordeton ro bezanid:1234
mojodie hesabe shoma:
4000000 toman
40.0 dollar
0.8333333333333334 solana

'''










