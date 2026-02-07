from typing import Callable, Dict
def add(a: float, b: float) -> float:
    return a + b
def subtract(a: float, b: float) -> float:
    return a - b
def multiply(a: float, b: float) -> float:
    return a * b
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
OPERATIONS: Dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def run_calculator() -> None:
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    print("Type 'q' to quit\n")
    while True:
        operator = input("Enter operation: ").strip()
        if operator.lower() == "q":
            break
        if operator not in OPERATIONS:
            print("Invalid operation\n")
            continue
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = OPERATIONS[operator](a, b)
            print(f"Result: {result}\n")
        except ValueError:
            print("Invalid number input\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
if __name__ == "__main__":
    run_calculator()
