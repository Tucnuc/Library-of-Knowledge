import random

class Visitor:
  def __init__(self, id, name, books, password, admin):
    self.id = id
    self.name = name
    self.books = books
    self.password = password
    self.admin = admin

  def displayProfile(self):
    print(f"Name: {self.name}")
    print(f"ID: {self.id}")
    print(f"Borrowed Books: {self.books}")
    if self.admin:
      print("")
      print("Rank: Administrator")

  def adminDisplayProfile(self):
    print(f"Name: {self.name}")
    print(f"ID: {self.id}")
    print(f"Borrowed Books: {self.books}")
    print(f"Password: {self.password}")

visitorDatabase = []
takenIds = []
loggedIn = False
currentVisitor = ""

def loginVisitor():
  global currentVisitor, loggedIn
  print("Welcome to the Login Page.")
  print("")
  name = input("Enter your name: ")
  password = input("Enter your password: ")
  print("")
  for visitor in visitorDatabase:
    if visitor.name == name and visitor.password == password:
      print("Login successful. Moving to the center..")
      print("")
      currentVisitor = visitor
      loggedIn = True
      theHub()
      return
  print("Login failed. Try again.")
  print("")
  
  def choice():
    decision = input("Do you want to create a new account or try again? [1 - Create account, 2 - Another try]: ")
    print("")
    if decision == "1":
      registerVisitor()
    elif decision == "2":
      loginVisitor()
    else:
      print("Invalid choice. Try again")
      print("")
      choice()

  choice()


def registerVisitor():
  user = Visitor(generateId(), createName(), [], createPassword(), False)
  visitorDatabase.append(user)
  print("Registration successfull. Moving you to the login page..")
  print("")
  loginVisitor()

def createName():
  name = input("Enter your name: ")
  for visitor in visitorDatabase:
    if visitor.name == name:
      print("Name already taken.")
      print("")
      return createName()
  return name

def createPassword():
  password = input("Enter your password: ")
  password2 = input("Confirm your password: ")
  print("")
  if password == password2:
    return password
  else:
    print("Passwords do not match. Please try again.")
    print("")
    return createPassword()
    
def generateId():
  id = random.randint(1, 10000)
  if id in takenIds:
    return generateId()
  else:
    takenIds.append(id)
    return id

class Book:
  def __init__(self, name, author, isbn, status):
    self.name = name
    self.author = author
    self.isbn = isbn
    self.status = status

  def displayBook(self):
    print(f"Name: {self.name}")
    print(f"Author: {self.author}")
    print(f"ISBN: {self.isbn}")
    print(f"Status: {self.status}")
    print("")

  def updateStatus(self, newStatus):
    self.status = newStatus

bookDatabase = []
def createBook():
  name = input("Enter the name of the book: ")
  author = input("Enter the author of the book: ")
  isbn = input("Enter the ISBN of the book: ")
  status = "Available"
  book = Book(name, author, isbn, status)
  bookDatabase.append(book)
  print("")
  print("Book added successfully. Returning to the center..")
  print("")
  theHub()

selectedBookForRemoval = ""
def removeBook():
  global selectedBookForRemoval
  def choice():
    decision = input("Do you want to remove this book? [1 - yes, 2 - no]:")
    print("")
    if decision == "1":
      bookDatabase.remove(selectedBookForRemoval)
      print("Book removed successfully. Returning to the center..")
      print("")
      theHub()
    elif decision == "2":
      print("Returning to the center..")
      print("")
      theHub()
    else:
      print("Invalid choice. Please, try again.")
      print("")
      choice()
      
  name = input("Enter the name of the book you want to remove: ")
  for book in bookDatabase:
    if book.name == name:
      print("Book found successfully. Book details: ")
      print("")
      book.displayBook()
      selectedBookForRemoval = book
      choice()
  
  print("Book not found. Try again.")
  print("")
  removeBook()

def theHub():
  print("Welcome to the center of the library. Choose where you want to go from here.")
  print("")
  print("1. Look into the book list.")
  print("2. Find more information about a specific book.")
  print("3. Borrow a book.")
  print("4. Display account information.")
  print("5. Leave the library.")
  print("")
  if currentVisitor.admin:
    print("Administrator-exclusive options:")
    print("6. Add a book into the library.")
    print("7. Remove a book from the library.")
    print("8. Check a list of registered accounts.")
    print("9. Find more information about a specific account.")
    print("10. Delete an account from the database.")
    print("")
  
  def choice():
    global currentVisitor

    def pause():
      print("")
      input("Press Enter to continue: ")
      print("")
      theHub()

    decision = input("Choose an action. [number]: ")
    print("")
    if decision == "1":
      print("Here's the list of all books:")
      index = 1
      for book in bookDatabase:
        print(f"{index}. {book.name}")
        index += 1
      pause()
      return
    elif decision == "2":
      print("Info here..")
      pause()
      return
    elif decision == "3":
      print("Borrowing a book..")
      pause()
      return
    elif decision == "4":
      print("Here's your detailed account information:")
      currentVisitor.displayProfile()
      pause()
      return
    elif decision == "5":
      print(f"We wish you a safe journey, {currentVisitor.name}.")
      print("")
      currentVisitor = ""
      startingPoint()
      return
    elif decision == "6" and currentVisitor.admin:
      print("Starting the book adding procedure..")
      createBook()
      return
    elif decision == "7" and currentVisitor.admin:
      print("Starting the book removal procedure..")
      removeBook()
      return
    elif decision == "8" and currentVisitor.admin:
      print("Displaying the list of registered accounts:")
      for visitor in visitorDatabase:
        print(f"ID: {visitor.id} | Name: {visitor.name}")
      pause()
      return
    elif decision == "9" and currentVisitor.admin:
      print("Displaying..")
      pause()
      return
    elif decision == "10" and currentVisitor.admin:
      print("Deleting..")
      pause()
      return
    else:
      print("Invalid choice. Please, try again.")
      print("")
      choice()
    
  choice()


def startingPoint():
  print("Welcome, visitor. Before you can access all the knowledge on the continent, you need to verify yourself.")
  
  def choice():
    decision = input("Either login into an existing account or register a new one. [1 - Login, 2 - Registration]: ")
    print("")
    if decision == "1":
      print("Moving to the Login Page..")
      print("")
      loginVisitor()
    elif decision == "2":
      print("Moving to the Registration Page..")
      print("")
      registerVisitor()
    else:
      print("Invalid choice. Please, try again.")
      print("")
      choice()

  choice()

administrator = Visitor("1", "Adam", [], "1235", True)
visitorDatabase.append(administrator)
takenIds.append(administrator.id)

startingPoint()