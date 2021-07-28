def isBalanced(s):
    # {{[[(())]]}}
    # {[(])}
    stack = []
    bracket = {"{": "}", "[": "]", "(": ")"}

    for char in s:
        if char in bracket.keys():
            stack.append(char)
        else:
            if len(stack) != 0:
                top = stack.pop()
                if bracket[top] != char:
                    return "NO"
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
print(isBalanced("}][}}(}][))]"))
print(isBalanced("[](){()}"))
print(isBalanced("()"))
print(isBalanced("({}([][]))[]()"))
