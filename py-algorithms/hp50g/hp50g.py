import operator

valid_operations = ['+', '-', '*', '/']
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
opposites_ops = {'-': operator.add, '+': operator.sub, '/': operator.mul, '*': operator.truediv}

def operation(formula):
    sides_formula = formula.split("=")
    for op in valid_operations:
        right_side_values = sides_formula[1].split(op)
        if len(right_side_values) > 1:
          operator_value = op
          break
    
    V = sides_formula[0]
    D = right_side_values[0]
    T = right_side_values[1]

    values = [V, D, T]

    try:
      if float(values[0]):
         pass
    except ValueError:
        total = ops[operator_value](float(values[1]),float(values[2]))
        print(f"V = {total}")
        return
    
    try:
      if float(values[1]):
         pass
    except ValueError:
        total = opposites_ops[operator_value](float(values[0]),float(values[2]))
        print(f"D = {total}")
        return

    try:
      if float(values[2]):
         pass
    except ValueError:
        if operator_value == '/' or operator_value == '-':
          total = ops[operator_value](float(values[1]),float(values[0]))
          print(f"T = {total}")
          return
        
        elif operator_value == '*' or operator_value == '+':
          total = opposites_ops[operator_value](float(values[0]),float(values[1]))
          print(f"T = {total}")
          return

