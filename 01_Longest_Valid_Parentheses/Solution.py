def longest_valid_parentheses(s):
    stack = []
    stack.append(-1)
    max_length = 0
    for i in range(len(s)):
        if(s[i] == "("):
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                length = i - stack[-1]
                max_length = max(max_length, length)
    return max_length

s = ")()())"
result = longest_valid_parentheses(s)
print(result)