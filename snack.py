# # import random

# # snacks = ['chips', 'popcorn', 'candy', 'nuts', 'jerky']

# # def snack_game():
# #     print("Welcome to the Snack Game!")
# #     print("You will be given a random snack.")
# #     print("If you like the snack, type 'yum'. If you don't like it, type 'yuck'.")
# #     print("Let's begin!")
# #     print("")
    
# #     random_snack = random.choice(snacks)
# #     response = input(f"Your snack is {random_snack}. Yum or yuck? ")
    
# #     if response == 'yum':
# #         print("Great! Enjoy your snack!")
# #     elif response == 'yuck':
# #         print("Oh no! Better luck next time.")
# #     else:
# #         print("Invalid response. Please try again.")
# #         snack_game()

# # snack_game()





# # Working Calculator

# # class Calculator:
# #     def add(self, a, b):
# #         return a + b

# #     def subtract(self, a, b):
# #         return a - b

# #     def multiply(self, a, b):
# #         return a * b

# #     def divide(self, a, b):
# #         if b == 0:
# #             return "Error! Division by zero."
# #         return a / b

# # # Example usage
# # if __name__ == "__main__":
# #     calc = Calculator()
# #     print("Addition:", calc.add(5, 3))
# #     print("Subtraction:", calc.subtract(5, 3))
# #     print("Multiplication:", calc.multiply(5, 3))
# #     print("Division:", calc.divide(5, 0))





# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, x, y):
#         self.result = x + y
#         return self.result

#     def subtract(self, x, y):
#         self.result = x - y
#         return self.result

#     def multiply(self, x, y):
#         self.result = x * y
#         return self.result

#     def divide(self, x, y):
#         if y != 0:
#             self.result = x / y
#             return self.result
#         else:
#             return "Error! Division by zero."

#     def clear(self):
#         self.result = 0
#         return self.result

# def main():
#     calc = Calculator()
#     while True:
#         print("Options: add, subtract, multiply, divide, clear, exit")
#         operation = input("Select operation: ")

#         if operation == "exit":
#             break
#         elif operation == "clear":
#             print("Result cleared:", calc.clear())
#             continue

#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if operation == "add":
#             print("Result:", calc.add(num1, num2))
#         elif operation == "subtract":
#             print("Result:", calc.subtract(num1, num2))
#         elif operation == "multiply":
#             print("Result:", calc.multiply(num1, num2))
#         elif operation == "divide":
#             print("Result:", calc.divide(num1, num2))
#         else:
#             print("Invalid operation. Please try again.")

# if __name__ == "__main__":
#     main()
