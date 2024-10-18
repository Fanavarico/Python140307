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
