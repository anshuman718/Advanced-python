class Batman():
    Height = 6.1
    @classmethod
    def show_height(cls):
        print(f"The height of Batman played by Christian bale is {cls.Height} feet.")

s = Batman()
s.Height = 6.4

s.show_height() # Output: The height of Batman played by Christian bale is 6.4 feet.