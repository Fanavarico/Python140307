
"""
In The Name of GOD
Created on Sun Nov 24 17:32:12 2024

@author: Ali Pilehvar Meibody


L4_ADV_Attend




#--------python --> zaban beyne
ensan --> python --> machine

python mig eman 3 ta chiz msihnazsa
python mige man yeseri kalamato reserv daram k 3 bakhshe......



3 ghesmat
1--> python built in funciton (tabe haye dakhelie python) (print(),input(),len(),type())
2--->keywords---->dastoorat , logic (mantegh)--> if , else , for , while , def , class, ....
3----->variables


#harchi joz in do mored beman dadii--> man variable dar nazar migirm
moteghayer---> zarf

zarf --> zakhire

zarf--> esm --> mohtava dare

hala to tooye zarf chia mitoni brizi?



"""

#-------------(1)----------------------
print('salam man baraye namayesham')
a=input('salam man baraye gereftanam')

type()
len()
#dakhel man yechiz bzar man bht typesho ya andazasho migm


name='alipilehvarmeibody'
type(name) # str
len(name) #18
#space?
#hamechii
name='alipilehvarmeibody '

len(name) #19

#----
print()
type()

#ye esman ke reserve shdoe--> baraye hamast , adad, str, .....
#behet javab mdie, print namayehs
#**** yek amalkardi daran
#print-->nmayesh
#input-->vorodi
#len-->andaze
#tyep--.donestash


#-----------------(2)----------------------
if
else:
#mese ghabli --> amalkardi ndre
#balke--< sakhtare-->agar, tekrar , box
#*** boro khate 130 be bad bekhoneshg *********


#--------------(3)--------------------
a=4
#ye zarfe esme zarfe a e 4 ro toosh rikhti

#1-numebrs (int (0,1,2,3,4,...), float(1.32 , 1.4389347,1232.344),complex (1j ,1+3j))
#2-str (reshte ha , characterm harf , kalame, jomle)

#number--> operator --> ** tavan *zarb + - /
c=a*b

#str-->reshte
a='salam'
a[2] **

#function--> str functrion
name='ali'
#rooye zarfe noghte mizni
name.upper() # bozorg ALI
name.lower()
name.replace('a','b') # bli
name.find('a')

#3-bool
True
False


#---hame yedonas , yedoen adad, yedone harf, yedone kalame
#age man chanta zarf ro bkham yeja bzrem chi>?
#chanta value megdhar ro negah drm chi?
list, tuple, set , dictionary


#importance
#list> dictionary           >tuple>set

a=4
a=65
a=[4,56,2,4,6]
a=['salam','vahid',4334,34.4 ,True,1j]

#list functions
append()  a.append('reza')
pop() remove()



#=======================================
#=======================================
#=======================================
#=======================================
#=======================================
#=======================================
#=======================================
#=======================================
#=======================================
#=======================================
#----shoam vaghty mikhay ye skahtari estefasde koni miay az keywords ha estefade mikoni

#----sade tarin-->shart

'''

if shart:
    dastoor
    
agar in shart shod in kaor bokon


**noketye talaee--> 'agar'->if

shart chanta bashe , dastoor chnata bashe


and  har dota shart bayad ejra she
or hadeaghal yedone aazin shart ha




if shart1 and/or shart2 ,.....:
    dastoor1
    dastoor2
    dastooor3
    
    
#agar in shart anjam shod inakro kon
#agar nashdo??? hgichi

#dorahi dari-->agar shod inkaro kon(kare1) agar nashod bikhial na kare 2

#if else
if shart:
    dastoor1
else:
    dastoor2
  
agae shartet anajm shdoe dastoore 1 age nashod dastoore 2
'''

#-----------------------

answer=input('salam shoam aya confirm mikonid? y benevisid ya n')
#agar neevsht y mamnoon
#ag nevesht n begoo bebakhshid


#--------------IF STATEMENT----------
#y-->mamnoon
#n---->bebakhshid
#dhadkjdhsakdhaj --> bebakhshid
answer=input('salam shoam aya confirm mikonid? y benevisid ya n:')
if answer=='y':
    print('mamnooon')

#y---> mamnoon
#n---> hichi
#sjhsa--->hichi
#shart haye ye tarafe--> if --> be man rabt ndre --> if yedon ee mikhay



#dorahi koni
#shart mziari
#agar shdo inak rag nashod onkar

answer=input('salam shoam aya confirm mikonid? y benevisid ya n:')

if answer=='y':
    print('mamnoon')
else:
    print('bebakhshidd')

#y-->mamnoooon
# n-->  bebakhshidd
#dfsfdd-->bebakhshid
 
 
 
#----------------
#-----
answer=input('salam shoam aya confirm mikonid? y benevisid ya n:')

if answer=='y':
    print('mamnoon')
elif answer=='n':
    print('bebakhshid')
else:
    print('vazhe ee k shoma ersal kardid yaft nashod')


#y-->mamnooon
#n-->bebakhshid
#sdkjsdh-->vazhe ee k shoma ersal kardid yaft nashod
#---------

#-----------------(FOR , WHILE)-------------------
#agar mididim 
#tekrarrr --> for, while (90% shabieh ham bdoonidesh)
#iteration 



#-------TEKRAR SOHBAT KONAM---------
#while

'''
4 ta chiz dare(joz)
#a-shomarande
#b-shart 
#c-dastooor
#d-afzayeshdahande



'''


#shomarande
#i , a , bv hame mitone
#kasaran
#aksaran 0 shorooo harchi bashe
#---a-----
i=0

#---b-----
while i<6:
    print('salam') #--c---
    i=i+1 #----d----
    
'''
chiakr mikone???
python--> az bala be paeen
az chap be rast


i ro mizare 0
while in yek skahtare --> ta zamani ke****
ta zamani ke i<6 hast dasstoorate zir ro anjam bde
i chande?-->0
dokhat 
khate vaakl-->salam --> print mikone salam
i=i+1 --> 1
halghe


i-->1
salam

i-->2
salam

i-->3
salam

i-->4
salam

i-->5
salam


'''

#khrooji chishdo??


'''
salam
salam
salam
salam
salam
salam

'''




#------berim naghsasho bbini

#----halgeh haye na shoroooo

'''

bargasht , khoroji , barmigardone--> return --> def (tabe)
sudocode --> shebhe code --.script-->  ejra mishe (run)


error va hich 
hich-->hamsieh gahalt nis--. shayad kari nmige anjambde
error-->yek kari 
print(zx) --> gahblkesh zx tarif nkrdi
NameError: name 'zx' is not defined



'''
    
    
#


print('') #ejra miseh hichi neshoon nemide namayesh nmide
print(zx) #NameError: name 'zx' is not defined



a=70
if a<50:
    print('salam')

#a=70
#hichi chap nmikone



if a=50:
    print('salam')

if a==50:
print('salam')

#IndentationError: expected an indented block

#a==50 a=50
#SyntaxError: invalid syntax





i=10

while i<6:
    print('salam')
    i=i+1

'''
i=10
ta zamani k i koochiktar az 6 hast in dastoor ra ejra kon
magar i kochiktar az 6 hast???
varede halghe nmishe


edame mide be karesh
chizi khoroji nmide



'''
    

#i ro
#a,b,c,d shomarande,sharft, dastoor, afzayehs

while i<6:
    print('salam')
    i=i+1

#ta zamani k i kochiktar az 6 bashad i ????
#error--> i defined nashode
#NameError: name 'i' is not defined




#dota ghalate ghabli ro anjam nmidim
#shoro konade, shart 
#

i=0
while i<6:
    print('salam')
    print('khdoafez')
    i=i+1
'''
salam
khdoafez
salam
khdoafez
salam
khdoafez
salam
khdoafez
salam
khdoafez
salam
khdoafez

'''




i=0
while i<6:
    #print('salam')


#whiel for halghan
#if , if else-->dpo rahi

'''

i=0 ta zmani k kochiktar az 6 hastr print kon salam
i=0 aya kochiktare az 6? bale salam
barmigrde-->halagahs dg
i=0 <6 bale print (salam)


'''

i=0
while i<6:
    print('salam')
    i=i+1

'''
i=0 while i<6 --> vase inke varede halgeh bshe
dastoor
too dele dastoor ye dastore afzayehs mdim
'''
#endless loop
#halgheye namahdood nareism

    
#--------SAKHTAR EASLIE YEK WHILE------   
i=0
while i<6:
    print('salam')
    i=i+1
    
    
#FOR?------
for i in range(0,6):
    print('salam')
    
    
#whiel o foro
    
'''

for-->
i=0 salam
i=1 salam
i=2 salam
i=3 salam
i=4 salam
i=5 salam
i=6 xxxx

default +1 
i=i+1

'''



#tekrar .............

#fargh--->
#tekrar shabieh ham bodan



#----> while true --->
#too ghablia hsarte while hey chekc mishod
#ta zamani k true bod hey mirft too halghe
#ag false msihdo miomd biroon


#while true--> hamishe shart true hast
#hamishe too halghas
#break mzirn k bepare biroon


#hey mikhay tekrar she
#inghd tekrar kon magvar inek exit ro bzne
#ingdhr tekrar kon hey bgo numebreto englisi bnvis , ta zamni k englis nvsht
#ingdh tekrar kon tas taraf adad avreed kone


while True:
    input('salam benevis')
    break




#--->for--->iteration
#beri done done begrdiii




#done done inaro bekeszhi birooon

for i in range(0,6):
    print('salam')
#baraye har i=0 , 1 ,2,3,4,5
#rasnge(0,6)   0 1 2 3 4 5  hey doen done i mizree

a=[10,20,30,40,50,60]

for i in a

#i=10 , 20 , 30 ,40 ,50 ,60

users=['ali','vahid','hamid','reza']

for i in a:
    
#i= 'ali' , ;vahid , hamid , reza


#harfe nahae--> done doanshono az khoone mikeshe biron
#varresi , bazzressis

#@yechizi cehck joni


a=[10,20,30,40,50,60]

for i in a:
    print(i)
    
    
    
for i in a:
    print(i*5)
    
    
#----------------\
a=[10,20,30,40,50,60]

'''
yek barname benvisid ke biad
#yek list bedim behesh
#tedasde zojaro beshmoree
(TASK1)



(TASK2)
yek liste jadid doros kone az zoj ha



'''
#---> dorahi , shart?
#shart mikham --> if 
#iteration

'''
shart dorahi-->if else
tekrar--> for , while
hey tekrar beshe ta --> while true
bazrresi, varresi--> for
'''
#done done

a=[10,20,30,40,50,60]

#aval baayd doen donashono bekeshim biron


for i in a:
    print(i)


#done done 
#shart --> if
#agar zoj bood?

#** * + - / %

a=20%2
#baghimoonde

#% -->baghimond

#har adadi %2 --> baghimodmnash roye taghsime2
#age 0 --> zoje
#ag nash enis

#ag zoje
#shart ->
a=[10,20,30,40,50,60]
#i=10 ,20
for i in a:
    if i%2==0:
        #ta injaaaaa
        
        
#for , if
#for-->donme doen miekshe biron
#if --.check mikone zoje ya na
#dastoor?

#begam print kon
a=[10,13,20,30,33,50,51,60]

for i in a:
    print(i)
'''
10
13
20
30
33
50
51
60
'''

a=[10,13,20,30,33,50,51,60]

#i=10 ,20
for i in a:
    if i%2==0:
        print(i)
        
'''
10
20
30
50
60
'''


#kolan 3 ta ka rmikoni?? varresi 1-->print sade

#2 ta kar mohem tr

#2---> beshmoori -->chnat adari

a=[10,13,20,30,33,50,51,60]
k=0 #shomarande
for i in a:
    if i%2==0:
        k=k+1
        #k+=1
#msihoamresh
#YCHIZI BENAM K dari

print(k) #5


#3-->jdoashon koni      
#jdo akonm?koja berizm?
#yedonas-->ye zarf

#chanta --> list

a=[10,13,20,30,33,50,51,60]
k=[]
for i in a:
    if i%2==0:
        k.append(i)
    
print(k)
#[10, 20, 30, 50, 60]



#---3 ta akrie hatman anjam mishe
#pass, break ,continue

'''
vaghty tooye for , if 
'''


#----------
'''

if---> yek shart
if else---> do rahie shart
if elif else--> yek do rahi dorahi  (shakeh shakhe)
for , while--> tekrar
for-->iteration
while true--> yek kar hey anjam bshe taa....



----> iteration
for....
if....

#3 no kar
print --> zojareo print mikrd
behsmori--> k=0 k=k+1 
joda koni brizi toye ye liste jadi--> k=[] k.append(i)
3 ta kare dg
pass
continue
break



'''


a=[10,20,30,40,50,60,70,80,90]

#70-->


for i in a:
    print(i)
#baraye har i dar inja iteration
#fdone done ro print kon

#yej mikham bgam agah
#age 70 bood rad sho

#ag ag felan chzi shod anajm nde 
#halgeh nis?
#halgeh ro edame bde
#edsme-->continue

for i in a:
    if i==70:
        continue
    print(i)
    
#na mikham detection
#agh ressidi b 70 bia biron
#edame nadeee -->ghat kon-->break

for i in a:
    if i==70:
        break
    print(i)





#--pass
#karbordi nadree magar dar code zani haye ziadd
#agar 70 sh#mikham 70 ro taghsim bar 8 kone
#+132
#bad chekc kone farde
#ag fard ......
#+10000
#-23234342

for i in a:
    if i==70:
        pass

    print(i)


#IndentationError: expected an indented block


def english_to_persian(vorodi1):
    pass

    

'''

for ,if --> iteration -->varresi va yek shart ro check mikone
print-->namayesdh
k=k+1 -->mishamre
listi -->k.append(i)
bepari az roosh (nadid begirish) -->continiue
behehs beresi ghat koni-->break
alan hal ndri-->pass


'''
    
#yek rah

if a%2==0:
    print('zoj')
else:
    print('fard')

a=23
if a%2!=0:
    print('fard')
    
#fard




#------------------------------------
#------------------------------------
#------------------------------------
#az L3_ADV_ATTEND varesh dashtam

code=input('salam code mahsooleton ro begid:')
name=input('lotfan esme mahsooleton ro begid:')
price=input('lotfan gheymate mahsooleton ro begid')

#'1200'

price_list=[]
for i in price:
    price_list.append(i)
    
    
#[1, 2, 0 ,0] 


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




#---yekam bzoorge mitonim???
#tabe besazimmm?
#tabe-->BOX



'''

vorodiii----> BOX ---> khrooji
'''


#sudocode
#shebhe code
#sabte mahsol az shop owner (sahebe foroshgah)
#digickala, amazon



#side --> customer (msohtari)
#code--> code ->farsdi





#copy paste

'''

BOX


voroodi-->BOX___>khoroji

sedash konm

tabe persian_to_english


pesian

'''

#print , khorojhi frgh
#1-na vorodi na khoorji
#---tabe ee drim k vorodi nadahste bashe va khroji ham ndshte bashe


def welcome():
    print('khosh oomadid')
    
    
    
    
welcome()

a=welcome()

print(a)
#None




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


result=jam(4,5)




#-------vorodi , khoroji daran
#price--> fard user-->mizane


price_list=[]
for i in price:
    price_list.append(i)
    
    
#[1, 2, 0 ,0] 


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



#price----> amaliat --> final_price

'''

price----> box --> FINAL_PRICE

'''




def persian_to_english(price):
    price_list=[]
    for i in price:
        price_list.append(i)
        
        
    #[1, 2, 0 ,0] 


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
    return final_price


    

#============
#ghablie


price=input('salam lotfan gheymat ra bedahid: ')

#for i in price
   
final_price=persian_to_english(price) 
print(final_price)

#10000
#customer



print('salam moshjtartie gerami khosh amadid')
code=input('lotfan code mahsooeltan ra ersal konid')

#motmane codam--> engliusi

english_code=persian_to_english(code)

print(english_code)
#400


for i in anbar:
    if code in anbar:
        print('mojkod hast')
        
        
        
        
#==========================================
#-------------------------------------------

product_codes=['a1','a2','a4','a5']
'''
admin

bege salam khosh amadid code mahsol ra bgiid

user-->code bzne
aval chekc kone bebine vojod dare ya na 
#badesh bege 
#hala gheymato bego
#name
#gheymat farsi-->englis

#confim kon
#
#ag y --> confirm
#ag n --> baregarde az aval 
#ta zamanii k na na edame dashte bashe





hamechi mesle gahble
code, price, name --> (price--> englisish) --> y , n --> y mamnoon , n -> barmigahst aghab


fargh-->1--> vaghty product code mide bere begarde bbine hast ya na
ag bodo edame bede (name , pricxe) ag nabod mojod nist , dobare vared kon

fargeh2 --> y , n --> y zad trf ok , n process 
#agha etelaat ro taeed mikoni ya mikhay tagghir bdi
y --> taeed mamnon sabt shod
n--> dobare 




'''



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
        #dobare tekrar kone
        #hey tekrar hey tyekrarr
        #while true



code=input('salam code mahsooleton ro begid:')
#*****

name=input('lotfan esme mahsooleton ro begid:')
price=input('lotfan gheymate mahsooleton ro begid')
#***1
#product_codes=['a1','a2','a4','a5']


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
#***










