def ReverceString(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


strin1 = ["h", "e", "l", "l", "o"]
print(ReverceString(strin1))