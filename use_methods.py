class User:
    '''The clas defining a user'''  
    def __init__(self, fname, birthyear):
        
        '''Initialises the class User'''
        self.fname = fname
        self.birthyear = birthyear


    def welcome(self):
        '''Greet the user'''
        if(self.birthyear <= 2000):
            print(f"Wecome {self.fname} you were born during 20th century")

        else:
            print(f"Welcome {self.fname} you were born during 21st century")

nancy = User("Nancy", 2005)
nancy.welcome()
roma = User("Roma", 1982)
roma.welcome()