class library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displaybooks(self):
        print(f"we have following books in our library:{self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book Database has been updated.you can take book now")

        else:
            print(f"Book is already being used by{self.lendDict[book]}")

    def addBook(self,book):
           self.booklist.append(book)
           print("the book has been added to the book list")

    def returnBook(self,book):
        self.booklist.remove(book)

if __name__=='__main__':
    lib = library(['Python','c++',"Harry Potter",'rich Dad Poor dad'],"CodeExpert")

    while(True):
        print(f"welcome to the {lib.name} library.Enter your choice to continue")
        print("1.Display Books")
        print("2.Lend a Book")
        print("3.Add Book")
        print("4.Return Book")
        user_choice = int(input())

        if user_choice==1:
            lib.displaybooks()

        elif user_choice ==2:
            book = input("enter the name of tbook you want to lend")
            user = input("enter the your name")
            lib.lendBook(user,book)

        elif user_choice == 3:
            book=input("enter the name of book you want to add:")
            lib.addBook(book)

        elif user_choice == 4:
            book = input("enter the name of book you want to return")
            lib.returnBook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue

