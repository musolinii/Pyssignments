def grades(grade) :

    if grade < 40 :
        print('You got an E')
    elif grade > 39 and  grade < 44 : 
        print('You got a D')
    elif grade > 45 and grade < 50  :
        print('You got a C')
    elif grade > 49 and grade < 60 :
        print('You got a C')
    elif grade > 59 and grade < 90 :
        print('You got a B')
    else : print('You got an A!')

grades(97)