class James_Bond:
    Recent_actor = "Daniel Craig"

    @classmethod
    def show_actor(cls):
        print(f"The recent actor who played James Bond is {cls.Recent_actor}.")

    @property
    def hair(self):
        return f"Hair length: {self.length_hair}, Hair color: {self.color_hair}"


    @hair.setter
    def hair(self,value):
        self.length_hair = value.split(" ")[0]
        self.color_hair = value.split(" ")[1]


j = James_Bond()
j.Recent_actor = "Pierce Brosnan"


j.hair = "short blonde"
print(j.hair) # This will raise an AttributeError since 'hair' is not defined as a class or instance attribute. But in this case we have used the property decorator to define a getter and setter for the 'hair' attribute, so it will work as expected.


j.show_actor()


