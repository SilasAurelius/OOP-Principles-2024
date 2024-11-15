class Smartphone:
    def __init__(self, model, serial_number, operating_system):
        self.model = model # Public Attribute
        self.__serial_number = serial_number # Private Attribute
        self._operating_system = operating_system # Protected Attribute
        
    def show_info(self):
        # Accessing all attributes with the class
        print(f"Model: {self.model}")
        print(f"Serial Number: hidden for security.")
        print(f"Operating System: {self._operating_system}")
        
    def get_serial_number(self): # Getter for serial_number
        return self.__serial_number    

    def set_serial_number(self, new_number):
        self.__serial_number = new_number
# Creating a instance
my_phone = Smartphone("Pixel 5", "1234ABC", "Andriod")

# Accessing the public attriburte
print(my_phone.model)

# Trying to access the private and protected attributes
# print(my_phone.__serial_number) # This will raise an AttributeError
# print(my_phone._operating_system) # This is accessible but not recommended

# Accessing the private attribute using a getter
print(f"Serial Number: {my_phone.get_serial_number()}") # Safe Way

# Modifying the private attribute using a setter
my_phone.set_serial_number("9878564XYX")
print(f"Updated Serial Number: {my_phone.get_serial_number()}")
print()

class Personal_Info:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.__account_number = account_number  # Private attribute
        
    # Getter method for __account_number
    def get_account_number(self):
        return self.__account_number # Return the private attribute value
        
silas = Personal_Info("Silas", 10000000, 150908889)

print(f"Account name: {silas.name}")  # Prints: Silas
print(f"Account balance: ${silas.balance}.")   # Prints: 
print(f"Account number: {silas.get_account_number()}")  # Access the private account number using the getter method
