def longest_valid_parentheses(s):
    stack = []
    stack.append(-1)
    max_lenght = 0
    for i in range(len(s)):
        if(s[i] == "("):
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                lenght = i - stack[-1]
                max_lenght = max(max_lenght, lenght)
    return max_lenght

s = ")()())"
result = longest_valid_parentheses(s)
print(result)