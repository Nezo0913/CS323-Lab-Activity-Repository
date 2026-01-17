def simple_calculator():

    def apply_op(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b
        
    def calculate(expr):
        expr = expr.replace(' ', '')
        nums, ops = [], []

        def prec(o): return 1 if o in '+-' else 2

        def run():
            b, a = nums.pop(), nums.pop()
            nums.append(apply_op(a, b, ops.pop()))

        i = 0
        while i < len(expr):
            if expr[i].isdigit() or expr[i] == '.':
                n = ''
                while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                    n += expr[i]; i += 1
                nums.append(float(n)); continue

            if expr[i] == '(':
                ops.append('(')
            elif expr[i] == ')':
                while ops[-1] != '(':
                    run()
                ops.pop()
            else:
                while ops and ops[-1] != '(' and prec(ops[-1]) >= prec(expr[i]):
                    run()
                ops.append(expr[i])
            i += 1

        while ops: run()
        r = nums[0]
        return int(r) if r.is_integer() else r

    while True:
        s = input(">>> ")
        if s.lower() in ('q','x'): break
        print("Result:", calculate(s))


if __name__ == "__main__":
    simple_calculator()