class stringmethods():
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = str(input("Enter a string: "))

    def print_String(self):
        print(self.string.upper())

string = stringmethods()
string.get_String()
string.print_String()
