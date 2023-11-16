def recur(sum):
    if sum:
        return sum + recur(sum - 1)
    else:
        return 0


print(recur(10))
