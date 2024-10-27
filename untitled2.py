r=float(input('enter a number : '))
p=3.14
a=p*r*r
c=2*p*r
print('mohit',c)
print('masahat',a)

bmi=w/(h**2)
bim<15   سو<تغذیه
15<=bmi<16 لاغر
16<=bmi<18.5 کمبود وزن
18.5<=bmi<25 نرمال
25<=bmi<30 اضافه وزن
bmi>30 چاق

#==========================================
#==========================================
w=float(input('enter your weight (KG) : '))
h=float(input('enter your hight (M) : '))
bmi=w/(h**2)

if bmi<15:
    c='سوءتغذیه'
elif 15<=bmi<16:
    c='لاغر'
elif bmi>=16 and bmi<18.5:
    c='کمبود وزن'
elif bmi>=18.5 and bmi<25:
    c='نرمال'
elif bmi>=25 and bmi<30:
    c='اضافه وزن'
elif bmi>=30:
    c='چاق'
    

    
    
print('your bmi is : ',bmi,' and you are :',c)




#==========================================
#==========================================
a=int(input('enter age : '))
g=input('select m for male or f for female : ')
if a<18:
    if g=='m':
        print('son')
    elif g=='f':
        print('girl')
    else:
        print('not valid')
        
        
elif a>=18 and a<=65:
    if g=='m':
        print('father')
    elif g=='f':
        print('mother')
    else:
        print('not valid')

elif a>65:
    if g=='m':
        print('grandpa')
    elif g=='f':
        print('grandma')
    else:
        print('not valid')


#==========================================
#==========================================
a=int(input('enter age : '))
g=input('select m for male or f for female : ')

if a<18 and g=='m':
    print('son')
elif a<18 and g=='f':
    print('girl')
elif a>=18 and a<=65 and g=='f':
    print('mother')
elif a>=18 and a<=65 and g=='m':
    print('father')
elif a>65 and g=='f':
    print('grandma')
elif a>65 and g=='m':
    print('garndpa')



#==========================================
#==========================================
a=int(input('enter age : '))
g=input('select m for male or f for female : ')

if g=='m':
    if a<18:
        print('son')
    elif a>=18 and a<=65:
        print('father')
    elif a>65:
        print('grandpa')
elif g=='f':
        
     if a<18:
         print('girl')
     elif a>=18 and a<=65:
         print('mother')
     elif a>65:
         print('grandma')



#==========================================
#==========================================
for i in range(-10,1):
    print(i)
