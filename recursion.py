# Fibonacci
# F(0) = 0
# F(1) = 1
# n > 1: F(n) = F(n-1) + F(n-2)

# Time: O(2^n), Space: O(n)
def f(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return f(n-1)+f(n-2)
    
print(f"this is the ans of fibo:{f(12)}")


# Linked Lists

class SinglyNode:

  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    return str(self.val)

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

# Time: O(n), Space: O(n)
def reverse(node):
  if not node:
    return

  reverse(node.next)
  print(node)


reverse(Head)

# reverse array
def array_reverse(arr):
  start = 0
  end = len(arr)-1

  while start < end:
    arr[start],arr[end] = arr[end],arr[start]

    start +=1
    end -=1
  
  return arr

arr = [10,20,30,40,50]
print(array_reverse(arr))

arr2 = [1, 2, 3, 4, 5]
rev = list(reversed(arr2))
print(rev)