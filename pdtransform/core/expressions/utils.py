from . import expressions


def iterate_over_expr(expr):
    """
    Iterate in depth-first preorder over the expression and yield all components.
    """

    yield expr
    if isinstance(expr, expressions.FunctionCall):
        for child in expr.iter_children():
            yield from iterate_over_expr(child)