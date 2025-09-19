# hash set
s = set()
print(s)

# add item into set - O(1)
s.add(1)
s.add(2)
s.add(3)
s.add(5)

print(s)
for i in s:
    if i==5:
        s.pop()
        s.add(4)

