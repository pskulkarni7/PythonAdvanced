class User:
    '''The clas defining a user'''  
    def __init__(self, fname, lname):
        
        '''Initialises the class User'''
        self.name = ""
        self.fname = fname
        self.lname = lname

        print("Hello from the user class")

    def full_name(self):
        '''Prints full name of the user'''
        self.name = self.fname + " " + self.lname


pallavi = User("Pallavi" , "Kulkarni")
pallavi.full_name()
print(pallavi.name)
matt = User("Matt" , "Delac")
matt.full_name()
print(matt.name)
pallavi.lname = "Deshpande"
pallavi.full_name()
print(pallavi.name)

