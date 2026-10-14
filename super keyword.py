class One: 
    def __init__(self): # This will be called automatically when an object of the class is created
        print("constructor of class One")
    a = 39 

class Two(One): 
    def __init__(self):
        print("constructor of class Two")
    b = 4 

class Three(Two): 
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Two)
        print("constructor of class Three")

    c = 29853 

k = Three()
print(k.a)

