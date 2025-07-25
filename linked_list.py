class singelNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = singelNode(1)
A = singelNode(2)
B = singelNode (3)
C = singelNode(4)

Head.next = A
A.next =B
B.next =C

# print(Head)

# Treverse the list - O(n)
# curr = Head

# while curr:
#     print(curr)
#     curr = curr.next

# Display linked list -> O(n)
def display(head):
    curr = head # curr ->it is a pointer that store the val of head 
    element =[]
    while curr:
        element.append(str(curr.val))
        curr = curr.next()
    print(' -> '.join(element))

display(Head)

