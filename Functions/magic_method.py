#magic methods - they are automatically called by many of pythons build-in operations
#like __ini__, __str__ and __eq__ 

# class Book:
#     def __init__(self,title,author,num_pages): # when we call class we are calling __init__
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

#     def __eq__(self, other): # we are examining two objects equality...
#         return self.title == other.title and self.author == other.author 

# book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
# book2 = Book("The Hobbit", "J.R.R Tolkien", 223) 

# book1 = Book("The Hobbit", "J.R.R Tolkien", 310 )
# book2 = Book("Harry Potter and the Philosopher's Stone", "J K Rowling", 223)
# book3 = Book("The Lion, the witch and the Wardrobe", "C.S Lewis", 172)

# print(book1)
# print(book2)
# print(book3)        

# print(book1 == book2)

#############################################
# to check built-in method __eq__...

# class Book:
#     def __init__(self,title,author,num_pages): # when we call class we are calling __init__
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __eq__(self, other): # we are examining two objects equality...
#         return self.title == other.title and self.author == other.author 

# book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
# book2 = Book("The Hobbit", "J.R.R Tolkien", 223) 

# print(book1 == book2)

#####################################

# to check built-in method __lt__...

# class Book:
#     def __init__(self,title,author,num_pages): # when we call class we are calling __init__
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __lt__(self,other): # Lets compare number of pages...between book2 to book3
#         return self.num_pages < other.num_pages
    
#     def __gt__(self,other): # Lets compare number of pages...between book2 to book3
#         return self.num_pages > other.num_pages
    
# book1 = Book("The Hobbit", "J.R.R Tolkien", 310 )
# book2 = Book("Harry Potter and the Philosopher's Stone", "J K Rowling", 223)
# book3 = Book("The Lion, the witch and the Wardrobe", "C.S Lewis", 172)


# print(book2 < book3)
# print(book2 > book3)    

#############################################
# # to check built-in method __add__...
# class Book:
#     def __init__(self,title,author,num_pages): # when we call class we are calling __init__
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __add__(self,other):  
#         return f"{self.num_pages + other.num_pages} Pages"    

# book1 = Book("The Hobbit", "J.R.R Tolkien", 310 )
# book2 = Book("Harry Potter and the Philosopher's Stone", "J K Rowling", 223)
# book3 = Book("The Lion, the witch and the Wardrobe", "C.S Lewis", 172)

# print(book1 + book2)
# print(book3 + book2)

#################################################
# TO search keyword within the book....

# class Book:
#     def __init__(self,title,author,num_pages): # when we call class we are calling __init__
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __contains__(self,keyword):
#         return keyword in self.title or keyword in self.author

# book1 = Book("The Hobbit", "J.R.R Tolkien", 310 )
# book2 = Book("Harry Potter and the Philosopher's Stone", "J K Rowling", 223)
# book3 = Book("The Lion, the witch and the Wardrobe", "C.S Lewis", 172)

# print("Lion" in book3)
# print("Lion" in book1)
# print("Lion" in book2)


# print("Rowling" in book3)
# print("Rowling" in book1)
# print("Rowling" in book2)

####################################
# search a key for given object...

class Book:
    def __init__(self,title,author,num_pages): # when we call class we are calling __init__
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __getitem__(self,key): # Lets compare number of pages...between book2 to book3
         if key == "title":
             return self.title
         elif key == "author":
             return self.author
         elif key == "num_pages":
             return self.num_pages
         else:
             return f"key {key} was not found"  
book1 = Book("The Hobbit", "J.R.R Tolkien", 310 )
book2 = Book("Harry Potter and the Philosopher's Stone", "J K Rowling", 223)
book3 = Book("The Lion, the witch and the Wardrobe", "C.S Lewis", 172)

print(book3["title"])
print(book1["title"])
print(book2["title"])         

print(book3["num_pages"])
print(book1["num_pages"])
print(book2["num_pages"])         

print(book3["audio"])
print(book1["vedio"])
print(book2["pizza"])         
