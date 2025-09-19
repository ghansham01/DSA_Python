def reverse(n):
    ans =0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while n!=0:
        digit =n%10
        if ans> (2**31 - 1) // 10:
            return 0
        
        ans = ans *10+digit
        x//=10

    ans *= sign
    if ans < -2**31 or ans > 2**31 - 1:
        return 0
    return ans