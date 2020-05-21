#import random module
#create a variable for first name
#create a variable that will load the 1st name tuple in random
#create a variable for last name
#create a variable that will load the 1st name tuple in random
#print the name in format mode.
#ask if user want to try again or quit.
#if quit stop
#else try again and print another funny alias.


import random


#tuple first and last name
first = ('jose', 'pedro', 'kantos', 'wally', 'timothy', 'clarence', 'bruce', 'arnold')
last = ('kasmot', 'little-mice', 'tortilla', 'cheese', 'doorknob', 'candy', 'sampalok', 'cremma')


while True:
    #choose a random first and last name.
    f_name = random.choice(first)
    l_name = random.choice(last)

    #print a formatted name
    full_name = f'{f_name} {l_name}'

    print('-------------------------------')
    print(f'Hello, {full_name.title()} !!!')

    #re-try or quit
    try_again = input("would you like to try again? (Press ENTER to try again or Q to quit): ")

    if try_again.lower() == 'q':
        print('-------------------------------')
        print('I hope you have fun, thank you!')
        break




