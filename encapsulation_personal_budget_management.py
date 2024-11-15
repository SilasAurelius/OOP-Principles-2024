# Problem Statement: You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

# Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. - Initialize these attributes in the constructor.

# - Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).

# - Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

# Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. - Validate the expense amount before making deductions from the budget.

# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

# Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

class BudgetCategory:
    def __init__(self, category_name, allocated_budget=1000):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
 
    # Getters and setters for category name and budget
    # ...

    def add_expense(self, expense):
        # Method to add an expense to the category
        if expense <= 0:
            print("Cannot be a negative number.")
        else:
            self.__allocated_budget -= expense
            return f"New budget: {self.__allocated_budget}"
            
            
    def display_category_summary(self):
        # Method to display the budget category details
        return (f"Category name: {self.__category_name}\nBudget: {self.__allocated_budget}")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
print(food_category.display_category_summary())

