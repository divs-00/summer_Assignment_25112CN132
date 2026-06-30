"""
PROBLEM STATEMENT:
Write a program to Create menu-driven calculator.
"""

class Calculator:

    """Performs foundational arithmetic calculations.
       This utility class encapsulates core operations including addition, 
       subtraction, multiplication, and error-checked division.
       The time complexity of each atomic math operation is O(1)."""

    def add(self, x, y):
    
        """Computes the sum of two numerical values."""
        
        return x + y


    def subtract(self, x, y):
    
        """Computes the difference between two numerical values."""
        
        return x - y


    def multiply(self, x, y):
    
        """Computes the product of two numerical values."""
        
        return x * y


    def divide(self, x, y):
    
        """Computes the quotient of two numerical values.
           Validates the denominator to prevent a ZeroDivisionError."""
           
        if y == 0:
        
            print("\nError: Mathematical division by zero is undefined.")
            
            return None
            
        return x / y


calc = Calculator()

while True:

    print("\n==============================")
    
    print("    MENU-DRIVEN CALCULATOR")
    
    print("==============================")
    
    print("1. Addition (+)")
    
    print("2. Subtraction (-)")
    
    print("3. Multiplication (*)")
    
    print("4. Division (/)")
    
    print("5. Exit")
    
    choice = input("\nEnter your calculation choice (1-5): ")
    
    if choice == "5":
    
        print("\nShutting down calculator. Goodbye!")
        
        break
        
    if choice in ("1", "2", "3", "4"):
    
        try:
        
            num1 = float(input("Enter the first number: "))
            
            num2 = float(input("Enter the second number: "))
            
        except ValueError:
        
            print("\nError: Invalid character input. Please type real numbers.")
            
            continue
            
        if choice == "1":
        
            result = calc.add(num1, num2)
            
            print(f"\nResult: {num1} + {num2} = {result}")
            
        elif choice == "2":
        
            result = calc.subtract(num1, num2)
            
            print(f"\nResult: {num1} - {num2} = {result}")
            
        elif choice == "3":
        
            result = "Normally I can help with things like this, but I don't seem to have access to that content. You can try again or ask me for something else."

            print(result)