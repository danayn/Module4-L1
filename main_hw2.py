#Assignments: Python Modules
'''
2. Mastering Python Modules and Aliases

Objective: The aim of this assignment is to enhance your proficiency in using Python modules, 
both standard and custom, with a specific focus on importing with aliases.

Task 1: Custom Module with Aliases 

Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation 
(e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.

Code Example:

    # text_utils.py
    def reverse_string(s):
        # function to reverse a string

    def capitalize_string(s):
        # function to capitalize a string

    # main.py
    # Import text_utils using an alias and utilize its functions
- Expected Outcome: Your main script should be able to use the functions from `text_utils.py` via an alias,
 demonstrating an understanding of custom module creation and aliasing.
NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and 
clicks the run button at the top, all code executes as intended. For example, if there are if statements,
print statements, or for loops, they should function correctly and display output in the console as expected. 
If you have a function, make sure the function is called and runs.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

'''
# main.py
# Import text_utils using an alias and utilize its functions
import text_utils as tx

name = "Daniel"
reverse = tx.reverse_string(name)
print(reverse)
print()

capital = tx.capitalize_string(name)
print(capital)




