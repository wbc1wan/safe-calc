# safe_calculator.py
from simpleeval import SimpleEval, FunctionNotDefined, InvalidExpression

def evaluate_expression(expr: str):
    """
    Pure function that evaluates a single expression.
    Safe to test without mocking I/O.
    """
    se = SimpleEval()
    return se.eval(expr)

def main():
    print("Safe Calculator — type 'exit' to quit.")

    while True:
        expr = input("Enter an expression: ").strip()

        if expr.lower() in ('exit', 'quit'):
            print("Goodbye!")
            break

        try:
            result = evaluate_expression(expr)
            print("Result:", result)
        except (FunctionNotDefined, InvalidExpression, ZeroDivisionError) as e:
            print("Error: Invalid expression or operation —", e)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
