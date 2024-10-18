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

    
