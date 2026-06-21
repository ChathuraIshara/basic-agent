"""Safe calculator tool: evaluates arithmetic expressions using AST."""
import ast
import operator as op

# supported operators
_operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
    ast.Mod: op.mod,
}


def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        op_type = type(node.op)
        if op_type in _operators:
            return _operators[op_type](left, right)
        raise ValueError(f"Unsupported binary operator: {op_type}")
    if isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)
        op_type = type(node.op)
        if op_type in _operators:
            return _operators[op_type](operand)
        raise ValueError(f"Unsupported unary operator: {op_type}")
    raise ValueError(f"Unsupported expression: {node}")


def evaluate(expression: str) -> str:
    """Evaluate a safe arithmetic expression and return result as string.

    Examples:
        evaluate('2 + 3*4') -> '14'
    """
    try:
        parsed = ast.parse(expression, mode="eval")
        result = _eval(parsed)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"
