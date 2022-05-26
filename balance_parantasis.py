def check_pair(element1, element2):
    if element1 == '(' and element2 == ')':
        return True
    if element1 == '[' and element2 == ']':
        return True



def check_balance(list):
    stack = []
    for i in range(len(list)):
        if list[i] == '(':
            stack.append('(')
        elif list[i] == ')':
            check_pair(list[-1], list[i])
            if True:
                stack.pop()

    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


if __name__ == "__main__":
    expression = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"
    convert_list = list(expression)
    result = check_balance(convert_list)
    print(result)
