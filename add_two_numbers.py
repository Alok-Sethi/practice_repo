"""
This program adds two numbers.
"""

def add_two_numbers(num1, num2):
    """
    This function adds two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """

    # Add the two numbers.
    sum = num1 + num2

    # Return the sum.
    return sum


# Get the two numbers from the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Add the two numbers.
sum = add_two_numbers(num1, num2)

# Print the sum.
print("The sum of the two numbers is:", sum)