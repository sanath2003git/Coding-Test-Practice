def minimum_squares(n):

    dp = [0] * (n + 1)

    for i in range(1 ,n + 1):

        dp[i] = i
        j = 1

        while j * j <= i:

            dp[i] = min(dp[i], 1 + dp[i - j * j])
            j += 1

    return dp[n]

n = 12

result = minimum_squares(n)

print(result)