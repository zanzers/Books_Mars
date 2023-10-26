# Marc START HERE!!!!!!!!!!!!!!
import json

class Mars_Books:
    def __init__(self,json_file):
    
        self.json = json_file
        
    def read_book(self):
        try:
            with open('books.json','r') as file:
                book = json.load(file)
            return book
        
        except FileNotFoundError:
            return[]
        
    def write_book(self,book):

        with open('books.json', 'w') as file:
            json.dump(book, file, indent=4)
            
    def addBook(self, new_book):
            book = self.read_book()
            book.append(new_book)
            self.write_book(book)

    def remove(self, remove_bookNumber):
            book = self.read_book()
            update_book = [book for book in book if book.get("ISBN") != remove_bookNumber]
            self.write_book(update_book)



# Marc PART END HERE!!!!!!!!!!!!!!

# MIC PART END HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!
     
#   NOWELL PART START HERE!!!!!!!!!!!!
class Book(Mars_Books):
     def __init__(self, json_file):
          super().__init__(json_file)

     def display(self):

          books = list_book.read_book()
          for book in books:
               print("----------------------------")   
               for key, value in book.items():
                    print(f"{key}: {value}")  
# NOWELL PART END HERE!!!!!!!!!!!!!!!!!!!!!!!!!!

# MARK & Marcelot PART START HERE!!!!!!!!!!!!!!!!!!!!!!!!!!

     
# MARK & Marcelot PART END HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# MARK VEL START HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

     
# MARK VEL START END HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# DREWW START HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Shipping (Customer):

    def __init__ (self, json_file, customer_json, customer_id, customer_name, customer_address, payment_method):
        super().__init__(json_file, customer_json, customer_id, customer_name, customer_address)
        self.payment = payment_method


    def payment_display(self):
        print(f"Your Order is Shipping")
        print(f"Name: {customer1_name}")
        print(f"Address: {customer_address}")
        print(f"Patment method: {self.payment}")

        super() .Checkout()

# DREWW START END HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
list_book = Mars_Books('books.json')
new_book = {
        "Title": "Marcelo: The Baho Boy",
        "Author": "Marcelo Mabaho",
        "ISBN": "978-0316769488",
        "Genre": "Fiction",
        "Price": "2560"
}
list_book.addBook(new_book)
book_in = Book('book.json')
book_in.display()