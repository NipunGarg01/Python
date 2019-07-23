import pdb
class Book():
    def __init__(self, name, author, pages):
        self.name=name
        self.author=author
        self.pages=pages

    def __str__(self):
        return ("This {} is written by {} and contains {} pages".format((self.name),self.author,self.pages))

    def __len__(self):
        return self.pages

    def __del__(self):
        print(" Book object has been deleted")


B=Book("Networking fundamentals", "Nipun Garg", 200)
print(B)                        #------------------------------> string is printed and we have used __str__ inside class

print(len(B))

del B                           # To delete the object






































