"""
    THIS IS NOT FOR BEGINNER, PLEASE IGNORE THIS TASK IF YOU ARE
    NEW TO PROGRAMMING.

    Complete the folllowing function that takes a mathematical expression
    as a string and evaluates it. This function allows for an arbitrary number
    of keyword arguments using **kwargs, and provide default values for
    variable x, and y if they are not provided.
"""

"""
Evaluates a mathematical expression with arbitrary variables.
- expression: A string representing the mathematical expression.
- x, y: Default values for 'x' and 'y' if not provided.
- **kwargs: Arbitrary additional variables for the expression.

Example usage:
    evaluate_expression('x + y + z', x=1, y=2, z=3) -> 6
    evaluate_expression('a * b + c', a=5, b=3, c=10) -> 25

To get started with this task, you can have a look at Python built-in
function eval that will return the results of an evaluated expression.
"""

import ast
import operator


# ast = Abstract Syntax Tree
def evaluate_expression(expression, **vars):
    def evaluate(node):
        if isinstance(node, ast.Expression): return evaluate(node.body)
        if isinstance(node, ast.Constant): return node.value

        if isinstance(node, ast.Name):
            if node.id not in vars: raise ValueError
            return vars[node.id]

        if isinstance(node, ast.BinOp) and type(node.op) in (ops := {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
        }):
            left, right = evaluate(node.left), evaluate(node.right)
            return ops[type(node.op)](left, right)

    return evaluate(ast.parse(expression, mode = "eval"))

print(evaluate_expression('x + y + z', x = 1, y = 2, z = 3)) # 6
print(evaluate_expression('a * b + c', a = 5, b = 3, c = 10)) # 25