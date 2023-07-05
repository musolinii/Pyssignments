def grades(name, grade) :

    if grade < 40 :
        print(name + ' you got an E')
    elif grade > 39 and  grade < 44 : 
        print(name + ' you got a D')
    elif grade > 45 and grade < 50  :
        print(name + ' you got a C')
    elif grade > 49 and grade < 60 :
        print(name + ' you got a C')
    elif grade > 59 and grade < 90 :
        print(name + ' you got a B')
    else : print(name + ' you got an A!')

grades("Rick",10)