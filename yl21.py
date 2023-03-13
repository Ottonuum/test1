import random

arvuti = random.randrange(0,100)

while(True):
    text = int (input('Arva ära number 1-100: '))

    if arvuti == text:
        print('Õige')
        guess = int ()
    elif arvuti < text:
        print('Paku väiksem')
    else :
        print('suurem')