def gcd_of_string(str1, str2):
    right = str1+str2
    lift = str2+str1

    if lift != right:
        return ""
    
    def gcd(len1, len2):
        while len2:
            len1, len2 = len2, len1 % len2
    
        return len1

    return str1[:gcd(len(str1), len(str2))]


s1 = 'ABCABC'
s2 = 'ABCABCABC'

print(gcd_of_string(s1, s2))