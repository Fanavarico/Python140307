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