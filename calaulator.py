import re

def main():
    """Main program flow"""
    operands = get_operands()
    result = perform_operation(operands)
    print(f"Result: {result}")

def get_operands():
    """Collect and validate user inputs for calculation"""
    return {
        "num1": validate_number(input("Enter first number: ")),
        "operator": validate_operator(input("Enter operator (+, -, *, /): ")),
        "num2": validate_number(input("Enter second number: "))
    }

def validate_number(num):
    """Convert input to float with validation"""
    while True:
        try:
            return float(num)
        except ValueError:
            print("Invalid number. Please enter a numeric value")
            num = input("Enter number again: ")

def validate_operator(operator):
    """Validate and extract arithmetic operator from input string"""
    while True:
        match = re.search(r'^\s*([+\-*/])\s*$', operator)
        if match:
            return match.group(1)  # Return validated operator
        print("Invalid operator. Please use +, -, *, or /")
        operator = input("Enter a valid operator: ")

def perform_operation(operands):
    """Execute arithmetic operation based on validated inputs"""
    operator_map = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else "Error: Division by zero"
    }
    return operator_map[operands["operator"]](operands["num1"], operands["num2"])

if __name__ == "__main__":
    main()
