#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

TASK1--------------------------
POROZHE K NAHAEE SHDO SHOMA HAM PRINT HARO BENEVISID 
MASALAN FELAN DEVCIE SAKHTE SHDO ..
FELAN DEVCIE ADD SHDO ....



TASK2---------------------------------
khate 1054 ->tabe haro takmil koniud


TASK3-----
FEKRE KHDOETON 2 TA TABE BEZARID









Created on Sat Feb  1 18:00:27 2025

@author: apm


class BANK


--> 
deposit()
atm()
show_balance()



a1=BANK()

a.deposit()



GUI---> Graphical user interface -> desktop application

tkinter , pyqt , pyslide --> 3 ketyabkhone-->GUI on the python





mesh()

def slicer(number):
    
    mesh ----> slice
    
    show()
    
    
    
def hatch(number):
    
    slice haro mgiire port mikone
    
    show()
    
    
    
#-------KHOLASE------

Backend ( CORE) --> IN PYTHON minevisim
WE HAVE SOME FUNCTIONS

input --> BOX (DEF) ---> Output
vorodi---> box ---> khorojii

rooye CORE ---> GUI (C++ , Python pyslide,pyqt,tkinter / WEBSITE (html,css,javascript)
                      
FRONT ---->(API) ---> CORE


#--------------------------
objective of the advanced classs---> writing the CORE Programmm (product management / Bank management , Final project)

CORE---> Baraye yek application benevisim



----final project idea-------
IDEA---> IoT ---> 

Internet of Things --> 

Things --> all --> (electronic, house , medical , ....)

connection of the things ( hamaro beham vasl konim)

---> modiriatesh (amnagementesho bedim be khdoemon)



Things ---> do category
device ---> ma beheshon dastoor mdiim . lamp (mikhaym roshan she), dar (baz she)
sensor---> yechizaee hast k va ma bshho , information,signal pass mdian bema

#----------
example--> Smart house (khaneye hooshmand)

In one house we have a lot of things ---> (things--> device / sensor)

Device-->Lamp , Tv , Pc , microwave , Door
Sensor--> temperature, gas sensor,........


IOT --> ma betoonim modiriat konim device sensor haroo

PANEL --> toosh b devcie ha dastoro bedim , az sensor ha information begirim


sole asli --> panel (computere man) chijori dastor bde be yek devcie??


device -> chip --> ina mitonan b wifi (internet vasl shan)

pc --> computere --> barenamamone --> b wifi wasl she


pc -> device (niaz dare ye vasete beynesh bashe)


shekati k devcie hooshmand misaze --> roosh chip mizare




device (lamp ) wifi ------> SHERKAT   <--------agar shoamre device , ramzesho , az tarighe pc





#======
device
sensor


panel --> dastoro bedam be device sensor

--->

lamp, door , fan --> DEVICE

yek shey (object) az yek class 

lamp1,lamp2,door1,door2,fan1 --> objects from Device class


NIAZ DARAM B CLASS


class Device():

device()


a1=Device(....)
a1.name
a1.number
a1...
#function 

a1.turn_on()
a1.tun_off()
.....

"""

#DEVICE YEK CLASS HAST 

#mikhaym doen doen azash object bekeshim

#a1=device()
#too pareantez baraye har devcie ychizi minvisim (moshakhate avalie)
#avalie--> initial --> init

'''

Khane (home)
otagh --> living_room , room , WC , kitchen,....

lamps -->lamp ha
lamp1 lamp2 lamp3
fan1 fan2




beyne lamp ha , lampe shoamre 8 tooye otaghe living__room tooye khoone

laptab --> folder --> C://user/amirpc/desktop/folder87/data.csv
shabieh in address bdim



home/living_room/lamps/lamp1

-->topic









'''

#a=Device(topic='home/living_room/lamps/lamp1)


class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        pass
  
        
b='home/living_room/lamps/lamp1'

c=b.split('/')

a1=Device('home/living_room/lamps/lamp1')


class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        
        self.topic=topic
        
        self.topic_list=topic.split('/')
        
        self.location=self.topic_list[0]
        
        #group--->kojas kojaye khone
        self.group=self.topic_list[1]
        
        self.device_type=self.topic_list[2]
        
        self.name=self.topic_list[3]
        
        


#lamp besazam , tooye home 
#tooye parking 
#lamp9


a1=Device(topic='home/parking/lamps/lamp9')

a1.topic #'home/parking/lamps/lamp9'
a1.name #'lamp9'
a1.device_type #lamps
a1.group # 'parking'
a1.location #'home'


#device---
#sensor--> chizi hats k behet data pas middee


'''
import Adafruiy_DHT

class Sensor:
    def __init__(self,name,group,unit,pin):
        self.name=name
        self.group=group
        self.pin=pin #sensor pin
        self.unit=unit #C , ....
        self.current_value=None
        
    def read_sensor(self):
        humidity,temperature=Adafruiy_DHT.read_retry(Adafruiy_DHT.DHT22,self.pin)
        
        if self.unit=='C':
            self.current_value=temperature
        elif self.unit=='%':
            self.current_value=humidity
            
        return self.current_value    
      
a1=Sensor('s4','living_room','C',2721313297612937)
'''
#2721313297612937
a1.name

a1.read_sensor() #--->

#in too delesh read_sensor()

#Adafruiy_DHT.

#yek tabe ee dare
#read_retry

#too dlee tabe mige agha behem PIN bde pine sewnsoreto bdi

#pin ---> LIB ADAFRUIY --> DATA

#pin , 


import numpy as np


class Sensor:
    def __init__(self,name,group,unit,pin):
        self.name=name
        self.group=group
        self.pin=pin #sensor pin
        self.unit=unit #C , ....
        self.current_value=None
        
    def read_sensor(self):
        #bejaye inke bere vasl she va az sensor datya begire
        #behemonr andom data mdie --> simualtion
        
        return np.random.uniform(20,25)
        
    
t1=Sensor('t1','living_room','C',32198723498)


t1.name #t1
t1.group #living_room
t1.unit #C


#yek tabeye mohem dare

t1.read_sensor() # 21.1997404859644

t1.read_sensor()  #20.514981030744128





#================================================
#================================================
#----. DOTA CLASS --> DEVICE 
#SENSOR



class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        
        self.topic=topic
        
        self.topic_list=topic.split('/')
        
        self.location=self.topic_list[0]
        
        #group--->kojas kojaye khone
        self.group=self.topic_list[1]
        
        self.device_type=self.topic_list[2]
        
        self.name=self.topic_list[3]




#lamp --> lamp6 , lamp , living__room --> home

#home/living_room/lamps/lamp1

class name:
    
    def __init__(self,moshakhaste1,moshakahse2,moshakahsate3):
        
        self.moshakhaste1=moshakhaste1
        self.mo2=moshakahse2
        self.mo3=moshakahsate3
        
#a1=name(mo1,mo2,mo3) 
#a1.dsakj




class Device():
    #group-->kojaye khone
    def __init__(self,location,group,device_type,name):
        
        self.location=location
        self.group=group
        self.device_type=device_type
        self.name=name
        
a1=Device('home','living_room','lamps','lamp1')     
        
#shey msiaze lamp1 --> lamp hast , tooye yek khone too otaghe living__rom hast

#ingahd salkt

#a1=Device(yek_voordi)

#computer

#c/user/dekstop/


#home/living_room/lamps/lamp1

a='home/living_room/lamps/lamp1'
        

a1=Device('home','living_room','lamps','lamp1')     
 
a1=Device('home/living_room/lamps/lamp1')     


class Device():
    #group-->kojaye khone
    def __init__(self,topic):
        self.topic=topic
        
        self.topic_list=topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        

#dar besazam dare shomare 8 troo parking

#../.../../..
a1=Device('home/parking/doors/door4')    
        
a1.topic 

# 'home/parking/doors/door4'


a1.topic_list

#['home', 'parking', 'doors', 'door4']




a1=Device('home/parking/doors/door4')    

a1.name# 'door4'

a1.device_type #'doors'


#---> hadafe ma ine ke 
#betoonim behesh yekseri tabe ezafe konim



#yek devcie besazim

#hadafemon ine ke yekseri funciton--. turn_on, turn_off



class Device():
    #group-->kojaye khone
    def __init__(self,topic,pin):
        self.topic=topic
        
        self.topic_list=topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
        
    def turn_on(self):
        #intern betonam vasl sham
        
        #dargahi -_> general electric 
        
        #betonaam b general electric vbasl sham
        
        #begam agah lotfan roshan kon devicamo
        
        
        #general --> library 
        
        #mige azin function
        
        #PIN --> shoamre devcieto bgooo
        
        
        
        
        
        print('yes it is on')
        
        
        
        
#fan3 --> Wc , khoone

a1=Device('home/wc/fans/fan3')

#moshakhasat
a1.name

a1.device_type

a1.group



#roshanesh konm

a1.turn_on()
#yes it is on



#object --> function (turn_)on -->click mikoni

#bayad vasl beshe be devciue vagehi va roshanehs kone




#man too ye functioen turn_on --> b yek chizi niaz drm
#k biad b devcie vageh e vasl she


#Pin -->rooye lamp --> 43093202382309

a1=Device('home/living__room/lamps/lamp1',42329803928)

a1.trun_on()


#==================================================
#-----alaghe mandan----------------

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO  # For controlling GPIO pins

'''
az cokmputer --> device connection bezani


mqtt befresiii
GPIO ----->


turn_on()
1--> mqtt bdfrxsi b devicet
2--> GPIO bfresi b devciet 
roshan msihe


a1=Device()


a1.turn_on()




'''


#a1=Device(topic,)


class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]



        self.port=port
        self.mqtt_broker=mqtt_broker
        
        
        
        
        self.connect_mqtt()
        self.setup_gpio()
        
        
        
    def connect_mqtt(self):
        self.mqtt_client.connect(self.mqtt_broker,self.port)
        

        
    def setup_gpio(self):
        
        #Light ba signal
        #doors --> motor
        #fans --> motor 
        
        #PIN -->
          
        if self.device_tye=='lights':
            GPIO.setup(17,GPIO.OUT)

        elif self.device_type=='doors': 
            GPIO.setup(27,GPIO.OUT)
            
        elif self.device_type=='fans':
            GPIO.setup(22,GPIO.OUT)
            

    def tunr_on(self):
        self.send_command('TURN_ON')
        
        
    def send_command(self,command):
        self.mqtt_client.publish(self.topic,command)
        
      
        
      
#-------
a1=Device('home/living_room/lamps/lamp1')

a1.name
a1.group
a1.device_type
a1.location


a1.turn_on()




#---sade sazi

class Device:
    #def __init__(self,topic,pin):
    def __init__(self,topic):
        
        
        self.topic=topic
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
        self.status='off'

        #self.pin=pin

       

    def turn_on(self):
        
        self.status='on'
        #yadet bashe ino k seda mziani
        #ba dota chiz --> gpio / mqtt vasl msihe b server
        #pino mdie behesh k shenasaee she
        #va too donayye vaghey oon server ba wifi
        #vasl msieh be device to ba in pini k dadi
        #va roshanehs mikone
        print('now it is turned on')
        
        
    def turn_off(self):
        self.status='off'
        
        #dksjlizjlajsdkdad
        
        print('now it is turned off')
        
    def get_status(self):
        return self.status
        
        
        
a1=Device('home/living_room/lamps/lamp1')    
        
a1.name        

a1.device_type

a1.group

a1.location


a1.turn_on()

a1.turn_off()

#a1 roshane ya khamosh?
#a1.get_status --> on off


a1=Device('home/parking/doors/door6')
a2=Device('home/living_room/lamps/lamp7')



a1.device_type#'doors'
a1.name

 
a2.device_type # 'lamps'


a1.turn_on()



a1.get_status() #'on'

a2.get_status() #'off'

a2.turn_on()

a2.get_status() # 'on'

a2.turn_off()

a2.get_status() #'off'

#=====electronics va fahme masale

#ma mikonim b onvane kasi k core


#ADMIN_PANELO BESAZIIII



#KHOONE DARIII
#LIVING ROM , WC , PARKING  , KITCHEN 

#HARKODOM 10 TA LAMP DARE

#2 TA DAR PAKRING , 1DAR WC , 1 DAR KITCHEN


#50 device


a1=Device('home/living_room/lamps/lamp1')

a2=Device('home/living_room/lamps/lamp2')
a3=Device('home/living_room/lamps/lamp3')
#...........
a1=Device('home/parking/doors/door6')
a1=Device('home/parking/doors/door6')



#ADMIN_PANEL --> INKARARO RAHAT KONE POROZHE SHOMA INJAS 




class admin_panel():
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        self.groups[group_name]=[]
        
        
    
        
#a1=Admin_panel()

#khonam --> chanta ghesmat dare -> living_rom ,.. ,....  
        
        
a1=admin_panel()

a1.groups # {}

#creat_group --> mitoni bakhsh haye khoanto nbesazi


a1.create_group('living_room')


a1.groups

#{'living_room': []}


a1.create_group('wc')

a1.groups

#{'living_room': [], 'wc': []}


a1.create_group('parking')
a1.groups
#{'living_room': [], 'wc': [], 'parking': []}

a1.create_group('wc')
a1.groups




class admin_panel():
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'group {group_name} is created')
            
        else:
            print('your name is dublicated')
        
        
    def add_device_to_group(self,group_name,device):
        
        if group_name in self.groups:
            self.groups[group_name].append(device)
   
        else:
            print('your group is not created')
            
            
        
    
a=admin_panel()   
a.groups  #{}
a.create_group('living_room')        
        
a.groups        
#{'living_room': []}



d1=Device('home/living_room/lamps/lamp1')


a.add_device_to_group('living_room',d1)

b=a.groups

#'living_room': [<__main__.Device at 0x163850f20>]}
d2=Device('home/living_room/lamps/lamp2')

a.add_device_to_group('living_room', d2)
b=a.groups





class admin_panel():
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'group {group_name} is created')
            
        else:
            print('your name is dublicated')
        
        
    def add_device_to_group(self,group_name,device):
        
        if group_name in self.groups:
            self.groups[group_name].append(device)
            

        else:
            print('your group is not created')
            
            
            #d1=Device('home/group/device_type/name')
            
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            #F'DEVICE IS CREATE'
           # F'device {device.name} is created'
            
        else:
            print('your group is not created')
            

a1=admin_panel()
            
a1.groups    


a1.create_group('living_room')


a1.create_device('living_room', 'lamps', 'lamp7')

b=a1.groups
print(b)
#{'living_room': [Device('home/living__rom/lamps/lamp7)]}






class admin_panel():
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'group {group_name} is created')
            
        else:
            print('your name is dublicated')
        
        
    def add_device_to_group(self,group_name,device):
        
        if group_name in self.groups:
            self.groups[group_name].append(device)
            

        else:
            print('your group is not created')
            
            
            #d1=Device('home/group/device_type/name')
            
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            #F'DEVICE IS CREATE'
           # F'device {device.name} is created'
            
        else:
            print('your group is not created')
            
            
            
    def create_multiple_devices(self,group_name,device_type,number_of_devcies):
        
        if group_name in self.groups:
            
            for i in range(1,number_of_devcies+1):
                #number=10 -> 1,2,3,4,5,6,7,8,9,10 -->i
                
                device_name=f'{device_type}{i}'
                
                topic=f'home/{group_name}/{device_type}/{device_name}'
                
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)

            
        else:
            print('')





a2=Device('home/living_room/lamps/lamp1')
#lamp2,........



a=admin_panel()

a.groups #{}

a.create_group('living_room')
a.groups
# {'living_room': []}


#a1.create_device -->besazam
#a1.add_devcie_in_group -->yek device berizam too groh

#Multilple devcie to ye grop

#20 ta lamp mikham tooye living_room



a.create_multiple_devices('living_room', 'lamps', 20)

a.groups
'''
{'living_room': [<__main__.Device object at 0x163853020>,
                 <__main__.Device object at 0x163853230>,
                 <__main__.Device object at 0x163920ec0>,
                 <__main__.Device object at 0x1639201a0>,
                 <__main__.Device object at 0x1639201d0>,
                 <__main__.Device object at 0x1639203b0>, 
                 <__main__.Device object at 0x163920470>, 
                 <__main__.Device object at 0x163920530>,
                 <__main__.Device object at 0x1639205f0>, 
                 <__main__.Device object at 0x163920710>, 
                 <__main__.Device object at 0x163920860>, 
                 <__main__.Device object at 0x163920980>,
                 <__main__.Device object at 0x163920ad0>, <__main__.Device object at 0x163920bc0>, <__main__.Device object at 0x163920cb0>, <__main__.Device object at 0x1639200b0>, <__main__.Device object at 0x163920dd0>, <__main__.Device object at 0x163920fb0>, <__main__.Device object at 0x163920fe0>, <__main__.Device object at 0x1639210a0>]}

yek devicean --> DEVICE --> name .dhsskasjaljs


'''


#****************************
#****************************
#****************************
#****************************
#****************************
#****************************
#****************************
#****************************
#****************************
#****************************
#****************************
#****************************
#****************************

#----------------------nemoneye akahri
class admin_panel():
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'group {group_name} is created')
            
        else:
            print('your name is dublicated')
        
        
    def add_device_to_group(self,group_name,device):
        
        if group_name in self.groups:
            self.groups[group_name].append(device)
            

        else:
            print('your group is not created')
            
            
            #d1=Device('home/group/device_type/name')
            
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            #F'DEVICE IS CREATE'
           # F'device {device.name} is created'
            
        else:
            print('your group is not created')
            
            
            
    def create_multiple_devices(self,group_name,device_type,number_of_devcies):
        
        if group_name in self.groups:
            
            for i in range(1,number_of_devcies+1):
                #number=10 -> 1,2,3,4,5,6,7,8,9,10 -->i
                
                device_name=f'{device_type}{i}'
                
                topic=f'home/{group_name}/{device_type}/{device_name}'
                
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)

            
        else:
            print('')
            
            
            
    def get_devices_in_groups(self,group_name):
        if group_name in self.groups:
            return self.groups[group_name] #listi az device
            
            
        else:
            print('')
            
            
            #tamame device haye yek grooh ro roshan koen
    def turn_on_all_in_groups(self,group_name):
        
        devices=self.get_devices_in_groups(group_name)
        #list 
        #{'living_room'}:[d1,d2,d3,df34,....]
        #devices=[d1,d2,d3,df34,....]
        
        for device in devices:
            #DEVICE() class
            #in class --> .location .name .group .device__type
            #.turn_on turn_off
            device.turn_on()
            
            
            
    def turn_off_all_in_groups(self,group_name):
        '''
        yek group name begire mesle living_room
        tamame device haro khamosh kone
        
        
        '''


        pass
    
    

    def turn_on_all_devices(self):
        '''
        tamam device haro roshan kone
        **na fghht vase ye goroh
        '''            
        pass
    
    def turn_off_all_devices(self):
        '''
        tamam device haro khamoosh kone
        **na fghht vase ye goroh
        '''            
        pass
    
    def get_status_in_group(self,gorup_name):
        
        '''
        
        group_name bdi
        bege device ha done done roshanan ya kahmoosh
        
        print kone
        device {esme} --> on
        devcie {} --> off
        
        
        '''
    
        pass
    
    
    def get_status_in_device_type(self,device_type):
        
        '''
        device_type-->masalan lamp
        
        name , too kodom goroh on off
        
        lamp2 in living_room is off
        lamp3 in wc is on
        
        '''
        
        
    #Sensor --> a1=Sensor(...)
    #def create_device
    
    def create_sensor(self):
        pass
    
    def add_sensor_in_group(self,group_name):
        #yek group name bede va to sensor ro tooye oon list ezaf koni
        
        #add_devcie_in_group
        
        pass
    
    
    def get_data_from_sensor_in_group(self,group_name):
        
        '''
        
        lkiving__room --> tamame sensor haro mire behet 
        datasho pas mide
        '''
        pass
    
    
    

            
            
