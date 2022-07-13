def evaluate(expr):
    operators = {"+": lambda x , y : x + y,
                        "-" : lambda x , y : y - x,
                        "*": lambda x , y : x*y,
                        "/" : lambda x , y : y/x}
    stack = []
    for s in expr.split():
        if s in operators:
            s = operators.get(s)(stack.pop() , stack.pop())
        stack.append(float(s))
    assert len(stack) == 1 or len(stack) == 0
    return stack[0] if stack else 0

def main():
    evaluation = evaluate("1 2 + 2 3 * -")
    print(evaluation)

if __name__ == "__main__": main()
