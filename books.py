import csv

with open('books.csv', 'r') as file:
    reader = csv.DictReader(
        file, fieldnames=['Title', 'Author', 'ISBN', 'Price'])
    data = list(reader)

    print("How do you want to search for a book ? Pick one of the choices below.")
    print("1.By Authors name\n2.By ISBN \n3.By price range")
    
    choice = input(":")

    def search_author(data, name):
        result = []
        for item in data:

            if name in item.values():
                result.append(item)
        print(result)

    def search_ISBN(data, ISBN):
        for item in data:

            if ISBN in item.values():
                print("Title: "+item['Title']+" Price: "+ str(item['Price'])) 

    def search_diff(data, min_price,max_price):
        result = []
        for item in data:
            if float(item['Price']) > float(min_price) and float(item['Price']) < float(max_price):
                print(item)

    try:
        if int(choice) == 1:
            name = input("Enter Authors name : ")
            search_author(data,name)

        elif int(choice) == 2:
            ISBN = input("Enter the ISBN : ")
            search_ISBN(data,ISBN)
        
        elif int(choice) == 3:
            min_price = input("Enter the minimum price : ")
            max_price = input("Enter the maximum price : ")
            search_diff(data, min_price,max_price)
        
        else:
            print("Enter one of the three choices above.")
    
    except:
        print("Please enter numbers")
        
file.close()