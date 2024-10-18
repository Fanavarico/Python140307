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