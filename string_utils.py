def split_before_each_uppercases(formula):
    if len(formula) <= 1:
        return [formula] if formula else []
    start = 0
    split_formula = []
    for end in range(1, len(formula)):
        char = formula[end]
        if char.isupper():
            split_formula.append(formula[start:end])
            start = end
    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    digit_location = 1
    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula) and not formula[-1].isdigit():
        return formula, 1
    else:
        prefix = formula[:digit_location]
        numeric_part = int(formula[digit_location:])
        
        return prefix, numeric_part
