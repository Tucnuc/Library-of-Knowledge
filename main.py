# IMPORTS
import random
from data import booksList, visitorsList


#   VISITOR SECTION
# -------------------

# VISITOR CLASS
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
    borrowedBooks = []
    for book in self.books:
      borrowedBooks.append(book.name)
    print(f'Borrowed Books: {", ".join(map(str, borrowedBooks))}')
    if self.admin:
      print("")
      print("Rank: Administrator")

  def adminDisplayProfile(self):
    print(f"Name: {self.name}")
    print(f"ID: {self.id}")
    borrowedBooks = []
    for book in self.books:
      borrowedBooks.append(book.name)
    print(f'Borrowed Books: {", ".join(map(str, borrowedBooks))}')
    print(f"Password: {self.password}")

  def displayProfileList(self):
    print(f"ID: {self.id} | Name: {self.name}")

# VALUES FOR THE REGISTER AND LOGIN SYSTEM
visitorDatabase = []
takenIds = []
loggedIn = False
currentVisitor = ""

# LOGIN FUNCTION
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

# REGISTER FUNCTION
def registerVisitor():
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

  user = Visitor(generateId(), createName(), [], createPassword(), False)
  visitorDatabase.append(user)
  print("Registration successfull. Moving you to the login page..")
  print("")
  loginVisitor()

#ACCOUNT DELETING
def accountDeletion():
  global visitorDatabase
  name = input("Enter name of the account: ")
  for account in visitorDatabase:
    if account.name == name:
      print("Account found. Displaying details:")
      account.displayProfile()
      print("")
      def choice(account):
        decision = input("Do you want to delete this account? [1 - Yes, 2 - No]: ")
        print("")
        if decision == "1":
          visitorDatabase.remove(account)
          print("Account deleted successfully.")
          print("")
          print("Returning to the center..")
          print("")
          input("Press enter to continue..")
          print("")
          theHub()
        elif decision == "2":
          print("Returning to the center..")
          print("")
          input("Press enter to continue..")
          print("")
          theHub()
        else:
          print("Invalid choice. Please, try again.")
          print("")
          choice(account)

      choice(account)
      return
  print("Account not found. Please try again.")
  print("")
  accountDeletion()

#   BOOK SECTION
# ----------------

# BOOK CLASS
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

  def displayBookList(self):
    print(f"{self.name} | Author: {self.author}")

  def updateStatus(self, newStatus):
    self.status = newStatus

# BOOK ADDING
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
  input("Press Enter to continue: ")
  print("")
  theHub()

# BOOK REMOVING
selectedBookForRemoval = ""
def removeBook():
  global selectedBookForRemoval
  def choice():
    decision = input("Do you want to remove this book? [1 - Yes, 2 - No]: ")
    print("")
    if decision == "1":
      bookDatabase.remove(selectedBookForRemoval)
      print("Book removed successfully. Returning to the center..")
      print("")
      input("Press Enter to continue: ")
      print("")
      theHub()
    elif decision == "2":
      print("Returning to the center..")
      print("")
      input("Press Enter to continue: ")
      print("")
      theHub()
    else:
      print("Invalid choice. Please, try again.")
      print("")
      choice()

  name = input("Enter the name of the book you want to remove: ")
  print("")
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

# BOOK BORROWING/RETURNING
def bookAction():
  def choice():
    decision = input("Do you want to borrow or return a book? [1 - Borrow, 2 - Return]: ")
    print("")
    if decision == "1":
      borrowBook()
    elif decision == "2":
      returnBook()
    else:
      print("Invalid choice. Please, try again.")
      print("")
      choice()

  def borrowBook():
    def choice():
      name = input("Enter the name of the book you want to borrow: ")
      print("")
      for book in bookDatabase:
        if book.name == name:
          print("Book found successfully. Book details: ")
          book.displayBook()
          if book.status != "Available":
            print("This book is not available at the moment. We're sorry for the incovenience.")
            print("")
            print("Returning to the center..")
            print("")
            input("Press enter to continue: ")
            print("")
            theHub()
            return
          def choice2(book):
            decision = input("Do you want to borrow this book? [1 - Yes, 2 - No]: ")
            print("")
            if decision == "1":
              book.updateStatus("Borrowed")
              currentVisitor.books.append(book)
              print("Book borrowed successfully. Returning to the center..")
              print("")
              input("Press Enter to continue: ")
              print("")
              theHub()
              return
            elif decision == "2":
              print("Returning to the center..")
              print("")
              theHub()
              return

          choice2(book)
          return
      print("Book not found. Please, try again.")
      print("")
      choice()

    choice()

  def returnBook():
    if len(currentVisitor.books) == 0:
      print("You've got no books to return. Returning to the center..")
      print("")
      input("Press Enter to continue: ")
      print("")
      theHub()
      return

    def choice():
      name = input("Enter the name of the book you want to return: ")
      print("")
      for book in currentVisitor.books:
        if book.name == name:
          currentVisitor.books.remove(book)
          book.updateStatus("Available")
          print("Book found. Return succesfull.")
          print("Time limit hasn't been violated, free of charge.")
          print("")
          print("Returning to the center..")
          print("")
          input("Press Enter to continue: ")
          print("")
          theHub()
          return
      print("Book not found. Please, try again.")
      print("")
      choice() 

    choice()

  choice()


#   LOCATIONS SECTION
# ---------------------

# CENTER OF THE LIBRARY
def theHub():
  print("Welcome to the center of the library. Choose where you want to go from here.")
  print("")
  print("1. Look into the book list.")
  print("2. Find more information about a specific book.")
  print("3. Borrow or return a book.")
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

  def choiceMain():
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
      for book in bookDatabase:
        book.displayBookList()
      pause()
      return
    elif decision == "2":
      def choice():
        def nameSearch():
          name = input("Enter the name of the book: ")
          print("")
          for book in bookDatabase:
            if book.name == name:
              print("Book found successfully. Book details: ")
              book.displayBook()
              print("Returning to the center..")
              pause()
              theHub()
              return
          print("Book not found. Please, try again.")
          print("")
          nameSearch()

        def authorSearch():
          name = input("Enter the name of the author: ")
          print("")
          index = 0
          for book in bookDatabase:
            if book.author == name:
              print("Book found successfully. Book details: ")
              book.displayBook()
              index += 1
          if index != 0:
            print("Returning to the center..")
            pause()
            theHub()
            return
          print("No books found. Please, try again.")
          print("")
          authorSearch()

        decision = input("Do you want to search by name or by author? [1 - Name, 2 - Author]: ")
        print("")
        if decision == "1":
          nameSearch()
          return
        elif decision == "2":
          authorSearch()
          return
        else:
          print("Incorrect choice. Please, try again.")
          print("")
          choice()
          return

      choice()
      return
    elif decision == "3":
      bookAction()
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
      input("Press enter to continue: ")
      print("")
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
        visitor.displayProfileList()
      pause()
      return
    elif decision == "9" and currentVisitor.admin:
      def choice():
        name = input("Enter the name of the account: ")
        for account in visitorDatabase:
          if account.name == name:
            account.adminDisplayProfile()
            print("")
            print("Returning to the center..")
            pause()
            theHub()
            return
        print("Account not found. Please, try again.")
        print("")
        choice()

      choice()
      return
    elif decision == "10" and currentVisitor.admin:
      print("Welcome to the Account Deletion Page.")
      accountDeletion()
      return
    else:
      print("Invalid choice. Please, try again.")
      print("")
      choiceMain()

  choiceMain()

# OUTSIDE OF THE LIBRARY
def startingPoint():
  print("Welcome, visitor. Before you can access all the knowledge on the continent, you need to verify yourself.")
  print("")

  def choice():
    decision = input("Either login into an existing account or register a new one. [1 - Login, 2 - Registration]: ")
    print("")
    if decision == "1":
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


#   OTHER
# ---------

# ADDING INITIAL ACCOUNTS, BOOKS
for visitor in visitorsList:
  visitorDatabase.append(visitor)
  takenIds.append(visitor.id)

for book in booksList:
  bookDatabase.append(book)

# STARTING THE APPLICATION
startingPoint()