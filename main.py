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
     
# NOWELL PART START HERE!!!!!!!!!!!!

class Book(Mars_Books):
     def __init__(self, json_file):
          super().__init__(json_file)

     def display(self):          
          books = list_book.read_book()
          for book in books:
               print("----------------------------")   
               for key, value in book.items():
                    print(f"{key}: {value}")  
                            


          books = list_book.read_book()
          for book in books:
               print("----------------------------")   
               for key, value in book.items():
                    print(f"{key}: {value}")  
# NOWELL PART END HERE!!!!!!!!!!!!!!!!!!!!!!!!!!

    
# MARK & Marcelot PART START HERE!!!!!!!!!!!!!!!!!!!!!!!!!!
class Customer(Book):
    def __init__(self, json_file, customer_json,customer_id, customer_name, customer_address):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_jason = customer_json
        self.cart = []

    def customer_info(self):
        print(f"Your ID: {self.customer_id}")
        print("----------------------------")
        print(f"Welcome: {self.customer_name}")
        print("----------------------------")
        print(f"home Address: {self.customer_address}")
        print("----------------------------")

    def add_cart(self, book_title):
        self.cart.append(book_title)
        print(f"You add {book_title} in your cart")
        print("----------------------------")

    def sava_customer(self):
        customer_data ={
            "id": self.customer_id,
            "Name": self.customer_address,
            "Address": self.customer_address,
        }
        with open(self.customer_jason, 'w') as file:
            json.dump(customer_data, file, indent=4)

    def view_cart(self):
        print("Shopping List")
        for item in self.cart:
            print(item)
            print("----------------------------")

    def remove(self, book_title):
        if book_title in self.cart:
            self.cart.remove(book_title)
            print(f"The Book {book_title} are been remove in your cart.")
        else:
            print(f"The {book_title} was not found in your cart!")

    def calculate_total_price(self):
        books = self.read_book()
        total_price = 0
        for title in self.cart:
            for book in books:
                if title == book.get('Title'):
                    price = float(book.get('Price', 0))
                    total_price += price
        return total_price

    def empty_cart(self):
        return not bool(self.cart)

    def checkout(self):
        if not self.empty_cart():
            print("Checkout Details")
            for item in self.cart:
                print(item)
            total_price = self.calculate_total_price()
            print("----------------------------")
            print(f"Total Price: {total_price:.2f}")
            print(f"Matamang Salamat")
        else:
            print("Your cart is empty")


# MARK & Marcelot PART END HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Seller(Mars_Books): 
    def __init__(self, json_file,seller_name, title,author,isbn,genre,price):
      super().__init__(json_file)
      self.seller = seller_name 
      self.title = title
      self.author = author 
      self.isbn = isbn 
      self.genre = genre
      self.price = price
    def seller_add(self):
      new_add_book ={ "Seller": self.seller, 
                     "Title": self.title, 
                     "Author": self.author , 
                     "ISBN": self.isbn, 
                     "Genre": self.genre,
                     "Price": self.price, }
      self.addBook(new_add_book)
    def removeSeller_book(self, remove_isbn_num): 
      self.remove(remove_isbn_num) 
    def seller_display(self):
      print(f"Seller Name: {self.seller}")
      books = self.read_book() 
      seller_book = [book for book in books if book.get("Seller") == self.seller] 
      for book in seller_book:
       book_info = f"Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Price: ${book['Price']}"
      print(book_info)
     
# MARK VEL START END HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# DREWW START HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Shipping (Customer):
    def __init__ (self, json_file, customer_json, customer_id, customer_name, customer_address, payment_method):
        super().__init__(json_file, customer_json, customer_id, customer_name, customer_address)
        self.payment = payment_method

    def payment_display(self):
        print(f"Your Order is Shipping")
        print(f"Name: {customer1_name}")
        print(f"Address: {customer1_address}")
        print(f"Payment method: {self.payment}")

# DREWW START END HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



list_book = Mars_Books('books.json')
customer_json = "customer.json"
#new_book = {
        #"Title": "Marcelo: The Baho Boy",
        #"Author": "Marcelo Mabaho",
        #"ISBN": "978-0316769488",
        #"Genre": "Fiction",
        #"Price": "2560"
#}
#list_book.addBook(new_book)
book_in = Book('book.json')
book_in.display()

customer1_id = '1'
customer1_name = 'Nowell'
customer1_address = 'BBx Sky at Night Magazine, Eagle House, Bristol, BS1 4ST, United Kingdom'
customer1 = Customer(list_book, customer_json, customer1_id, customer1_name, customer1_address)

customer1.customer_info()
customer1.add_cart("To Kill")
customer1.view_cart()
customer1.sava_customer()

# customer1.remove("The Catcher in the Rye")


payment = "COD"
ship = Shipping(list_book, customer_json,customer1_id, customer1_name, customer1_address, payment)
ship.payment_display()
customer1.checkout()


seller1 = Seller('book.json',"Nowell","The One","nowellss","978-00000","Fantasy","2000" )
seller1.seller_add()
seller1.seller_display()
