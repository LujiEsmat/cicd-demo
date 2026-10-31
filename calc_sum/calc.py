"""A simple calculator supporting four arithmetic operations."""[cite: 1]


def calculate(a, b, operation):
    """Calculate using addition, subtraction, multiplication, or division."""[cite: 1]
    if type(a) not in (int, float) or type(b) not in (int, float):[cite: 1]
        raise TypeError("Both operands must be numbers.")[cite: 1]

    if operation == "+":[cite: 1]
        return a + b[cite: 1]
    elif operation == "-":[cite: 1]
        return a - b[cite: 1]
    elif operation == "*":[cite: 1]
        return a * b[cite: 1]
    elif operation == "/":[cite: 1]
        return a / b[cite: 1]
    else:[cite: 1]
        raise ValueError("Unsupported operation. Use +, -, *, or /.")[cite: 1]


def main():[cite: 1]
    print("Python Calculator")[cite: 1]
    print("Supported operations: +, -, *, /")[cite: 1]
    print("Type 'exit' to quit.")[cite: 1]

    while True:[cite: 1]
        operation = input("Enter operation (+, -, *, /): ").strip()[cite: 1]

        if operation.lower() == "exit":[cite: 1]
            print("Goodbye!")[cite: 1]
            break[cite: 1]

        if operation not in ("+", "-", "*", "/"):
            print("Error: Unsupported operation. Use +, -, *, or /.")[cite: 1]
            continue[cite: 1]

        try:[cite: 1]
            a = float(input("Enter first number: "))[cite: 1]
            b = float(input("Enter second number: "))[cite: 1]
            result = calculate(a, b, operation)[cite: 1]
            print("Result:", result)[cite: 1]
        except (ValueError, TypeError, ZeroDivisionError) as error:[cite: 1]
            print("Error:", error)[cite: 1]


if __name__ == "__main__":[cite: 1]
    main()[cite: 1]