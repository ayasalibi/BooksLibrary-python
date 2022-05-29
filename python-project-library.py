class People :
    def __init__(self,id,full_name,age,id_no):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
   

      
class Client(People):
    def __init__(self,id,full_name,age,id_no,phone_number):
        super().__init__(id, full_name, age, id_no)
        self.phone_number = phone_number



clients = []
def client_id(c_id):
    available = False
    for i in range(0, len(clients)):
        if c_id == int(clients[i].id):
            available = True
            
    return available

class Librarian(People):
    def __init__(self, id, full_name, age, id_no,employee_type):
        super().__init__(id, full_name, age, id_no)
        self.employee_type = employee_type

librarian = [] 
librarian.append(Librarian(1,"aya",20,77878,"part"))  
librarian.append(Librarian(2,"asil",24,34670,"part"))    

class Book:
    def __init__(self,id,title,description,author,status):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.status = status
    def print(self):
        print(self.id, self.title, self.description, self.author, self.status)

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status


books = []
books.append(Book(1, "Jane eyre", "description1", "Charlotte Bronte","Active"))
books.append(Book(2, "The great gatsby", "description2", "F.Scott Fitzgerald","Active"))
books.append(Book(3, "title3", "description3", "author3","Active"))
books.append(Book(4, "title3", "description3", "author3","Active"))

def book_id(id):
    available = False
    for n in range(0, len(books)):
        if id == books[n].id:
            available = True
    return available


def get_book(book_id):
    for i in range(0, len(books)):
        if book_id == int(books[i].id):
            return books[i]
    



def borrow_book(book):
        if book.get_status()=="Active":
            book.set_status("Inactive")
            
            return  True
        else:
            
            return False
      


borrow_orders = []


class Borrowing_Order():
    def __init__(self,id, date, clint_id, book_id, status):
        self.id = id
        self.date = date
        self.clint_id = clint_id
        self.book_id = book_id
        self.status = status


while True:
    print( " 1- borrow a book\n 2- add new client\n 3- add new labririan\n 4- view list of books\n 5-total borrowed books\n 6-total available books\n 7-total borrowed orders")
    n = int(input())

    
    if (n) == 1:
        c_id = int(input("Enter client id: "))
        b_id = int(input("Enter book id: "))
        book = get_book(int(b_id))
        if client_id(c_id) == False:
            print("The client not found")

        elif book_id(b_id) != True:
            print("The book not found")

        elif borrow_book(book)== False:
            print("Sorry , The book is not active")


        else:
            borrow_orders.append(Borrowing_Order(0, "2022", c_id, b_id, "Active"))
            for i in range(0,len(books)):
                if b_id == int(books[i].id):
                    books[i].set_status("Inactive")
            print("Borrowing completed successfully")
               
           
        
    elif (n) == 2:
        print("add new clint")
        id = int(input("Enter id: "))
        full_name = input("Enter your full name: ") 
        age = input ("Enter your age: ")
        id_no = input("Enter your id number: ")
        phone_number = input("Enter your phone number: ")
        clients.append(Client(id,full_name,age,id_no,phone_number))

    elif (n) == 3:
        print("add new labririan")
        id = int(input("Enter id: "))
        full_name = input("Enter your full name: ")
        age = input("Enter your age: ")
        id_no = input("Enter your id_number: ")
        employee_type = input("Enter your employee_type: ")
        librarian.append(Librarian( id, full_name, age, id_no,employee_type))

    elif (n) == 4:       
        for i in books:
            i.print()


    elif (n) == 5:
        a = 0
        for i in range(0, len(books)):
            if books[i].status == "Inactive":
                a+=1
        print(a,"borrowed books")


    elif (n) == 6:
        a = 0
        for i in range(0, len(books)):
            if books[i].status == "Active":
                a+=1
        print(a,"available books")


    elif (n) == 7:
         print(len(borrow_orders),"borrowed orders")
    
    else:
        break

    