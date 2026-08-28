def distinct_passwords(n, k):
    answer = 1
    if n > k:
        answer = 0
    else:
        for i in range(n):
            answer *= k 
            k -=1
    return answer
n = int(input("password length: "))
k = int(input("number of available characters: "))
result = distinct_passwords(n,k)
print(result)