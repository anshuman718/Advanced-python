class Month:
    Year = 2025
    def show(self):
        print(f"The month is {self.month_name} and the major days are {self.major_days}.")
        self.month_name = "September"
        self.major_days = 6,7,26,15,16


 # class Month_2:
 #   Year = 2025.9
  #  def show(self):
   #         print(f"The month is {self.month_name} and the major days are {self.major_days}.")
   # def showcontent(self):
   #      print(f" The month was {self.month_name} and the content was {self.content}.")


# The two clases are similar and if we change something in one we will have to change in all so we can't simply copy paste for multiple classes or larger files.

# Instead of that we can use inheritance to avoid code duplication and make our code more maintainable.

class Month_2(Month):
    Year = 2025.9
    def showcontent(self):
         print(f" The month was {self.month_name} and the content was {self.content}.")
a = Month()
b = Month_2()
print(a.Year,b.Year)




