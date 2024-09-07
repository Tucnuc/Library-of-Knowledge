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

# LIST OF BOOKS
booksList = [
    Book("History of the Empire", "A.R. Tolkien", "8-384-93823-6", "Available"),
    Book("The Dragon's Tale", "L.R. Silverleaf", "4-926-83752-1", "Available"),
    Book("Whispers of the Ancients", "M.K. Stormrider", "3-587-19284-7", "Borrowed"),
    Book("Chronicles of the Forgotten Realm", "E.J. Nightshade", "1-834-72836-2", "Available"),
    Book("Mysteries of the Moonstone", "G.D. Starfall", "6-219-59384-0", "Available"),
    Book("The Shadow King's Curse", "T.H. Ravencloak", "9-103-49832-5", "Borrowed"),
    Book("The Elven Prophecy", "C.F. Sunblade", "7-847-26395-4", "Available"),
    Book("Tales of the Frost Giants", "R.K. Frostbeard", "5-721-37482-8", "Available"),
    Book("The Wizard's Grimoire", "B.N. Spellweaver", "2-664-84930-9", "Borrowed"),
    Book("The Blood of the Phoenix", "S.J. Emberheart", "0-382-10394-6", "Available"),
    Book("Legends of the Darkwood", "D.C. Shadowwalker", "8-748-18273-3", "Available"),
    Book("Secrets of the Enchanted Forest", "V.L. Moonwhisper", "3-938-67284-1", "Borrowed"),
    Book("The Cursed Amulet of Drakoria", "H.G. Ironfist", "7-194-48753-2", "Available"),
    Book("The Last Sorceress", "A.L. Thornrose", "9-582-29473-8", "Borrowed"),
    Book("Vortex of the Shadow Realm", "K.M. Blackwind", "2-783-93821-7", "Available"),
    Book("Swords of the Fallen Heroes", "P.T. Stormblade", "1-387-28492-4", "Available"),
    Book("Riders of the Stormpeak", "E.J. Windrider", "3-128-84537-5", "Borrowed"),
    Book("The Eternal Flame", "L.V. Firebrand", "6-492-57381-9", "Available"),
    Book("Echoes of the Lost City", "B.C. Graymist", "0-837-28194-3", "Available"),
    Book("The Crystal of Aether", "S.K. Skygazer", "8-394-19284-7", "Borrowed"),
    Book("The Alchemist's Secret", "J.M. Goldleaf", "5-183-62948-2", "Available"),
    Book("Warlocks of the Abyss", "T.R. Netherbane", "4-583-74829-1", "Available"),
    Book("The Siege of Evernight", "M.D. Starborn", "9-462-82719-0", "Borrowed"),
    Book("Runes of the Dreadlands", "N.S. Frostflame", "1-649-38572-8", "Available"),
    Book("The Lost Lore of Eldoria", "C.G. Whisperwind", "2-982-67238-5", "Available"),
    Book("The Titan's Wrath", "O.W. Stoneshield", "7-572-38472-3", "Borrowed"),
    Book("The Veil of Midnight", "R.P. Nightbloom", "6-103-57821-6", "Available"),
    Book("Tales of the Crimson Seas", "V.R. Bloodwave", "3-948-27364-7", "Borrowed"),
]


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

# LIST OF VISITORS
visitorsList = [
    Visitor("1", "Adam", [], "12345", True),
    Visitor("2982", "Eve", [], "pw1234abc", False),
    Visitor("396", "John", [], "qwerty789", False),
    Visitor("4369", "Sophia", [], "password567", False),
    Visitor("5259", "Michael", [], "hello123!", False),
    Visitor("61", "Olivia", [], "abcxyz7890", False),
    Visitor("722", "James", [], "mypassword", False),
    Visitor("1596", "Emily", [], "securepass1", False),
    Visitor("2959", "Daniel", [], "hunterx12", False),
    Visitor("9853", "Mia", [], "letmein456", False),
    Visitor("1058", "Noah", [], "supersecret", False),
    Visitor("1298", "Isabella", [], "123secure", False)
]

# ADDING BORROWED BOOKS
visitorsList[1].books.append(booksList[25])
visitorsList[3].books.append(booksList[27])
visitorsList[3].books.append(booksList[5])
visitorsList[4].books.append(booksList[22])
visitorsList[6].books.append(booksList[2])
visitorsList[6].books.append(booksList[11])
visitorsList[7].books.append(booksList[19])
visitorsList[8].books.append(booksList[8])
visitorsList[9].books.append(booksList[13])
visitorsList[11].books.append(booksList[16])