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

  def displayProfileName(self):
    return self.name

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
      print("Login successful. Moving to the hub..")
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
      createName()
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
    createPassword()
def generateId():
  id = random.randint(1, 10000)
  if id in takenIds:
    generateId()
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

  def displayBookName(self):
    return self.name

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
  print("Book added successfully. Returning to The Hub..")
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
      print("Book removed successfully. Returning to The Hub..")
      print("")
      theHub()
    elif decision == "2":
      print("Returning to The Hub..")
      print("")
      theHub()
    else:
      print("Invalid choice. Try again.")
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
  print("Welcome to The Hub. Choose where you want to go from here.")
  return



print("Welcome to the Royal Library. Please login or register.\n")
loginVisitor()
print(currentVisitor.displayProfile())