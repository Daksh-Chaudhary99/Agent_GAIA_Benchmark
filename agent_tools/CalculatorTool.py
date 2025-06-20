import numexpr
from llama_index.core.tools import FunctionTool

def calculate(expression: str) -> str:
    """
    A safe calculator that evaluates a mathematical string expression.
    This tool can handle complex expressions with parentheses, addition,
    subtraction, multiplication, and division.
    Args:
        expression (str): The mathematical expression to evaluate (e.g., "2 * (3 + 4)").
    """
    print(f"Calculating expression: {expression}")
    try:
        # Use the numexpr library to safely evaluate the string.
        result = numexpr.evaluate(expression).item()
        
        # Return the result as a string for the agent to process.
        return str(result)
    except Exception as e:
        # If the expression is invalid, return a descriptive error.
        return f"Error: Invalid mathematical expression. Please check your syntax. Details: {e}"

def get_calculator_tool() -> FunctionTool:
    """Initializes and returns our custom-built, safe calculator tool."""
    return FunctionTool.from_defaults(
        fn=calculate,
        name="calculator",
        description="A tool for evaluating mathematical expressions. Use this for any math calculations, like addition, subtraction, multiplication, division, etc. Example input: '(25 * 4) + 15 - 5'"
    )