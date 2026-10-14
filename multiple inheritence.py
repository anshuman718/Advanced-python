class Month:
    Year = 2025
    month_name = "September"
    major_days = (6, 7, 26, 15, 16)
    def show(self):
        print(f"The month is {self.month_name} and the major days are {self.major_days}.")
        

class Year_before:
    year_before = 2024
    def print_year_before(self):
        print(f"The year before is {self.year_before}.")

class Month_2(Month, Year_before):
    Year = 2025.9
    content = "Demon slayer"
    def showcontent(self):
          print(f" The month was {self.Year} and the content was {self.content}.")
a = Month()
b = Month_2()
b.show()
b.showcontent()


print(a.Year,b.Year)





class one:
    a = 39

class two(one):
    b =4

class three(two):
    c = 29853
    def print_age(self, years_passed):
        years_passed = 2039
        d = 4039
        print(f"The age is {years_passed} -{self.d}  years passed.")
    
    

    

   


        
    

v = three()
print(v.a,v.b,v.c,v.print_age)











class One: 
    a = 39 

class Two(One): 
    b = 4 

class Three(Two): 
    c = 29853 
    
    def print_age(self, years_passed): 
        years_passed = 2039 
        self.d = 4039 
        
        
        # Prints using the exact string format requested
        print(f"The age is {years_passed} - {self.d} years passed.") 
        print(f"{years_passed} - {self.d}")
        

        print(years_passed - self.d)  # This will print the difference in digits
v = Three() 

# Print the class attributes
print(v.a, v.b, v.c) 

# Run the method to see the formatting and difference
v.print_age(10)

