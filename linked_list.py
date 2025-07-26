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
  curr = head  # curr ->it is a pointer that store the val of head 
  elements = []
  while curr:
    elements.append(str(curr.val))
    curr = curr.next
  print(' -> '.join(elements))

# display(Head)

# Search for node value - O(n)

def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            print(True)

        curr = curr.next
    return False

# print('this is search')
# search(Head, 4)

# Doubly Linked Lists
class DoublyNode:
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev

  def __str__(self):
    return str(self.val)

head1 = tail = DoublyNode(1)
print(tail)

# Display - O(n)
def display(head):
  curr = head
  elements = []
  while curr:
    elements.append(str(curr.val))
    curr = curr.next
  print(' <-> '.join(elements))

display(head1)

# Insert at beginning - O(1)
def insert_at_beginning(head, tail, val):
  new_node = DoublyNode(val, next=head)
  head.prev = new_node
  return new_node, tail

head2, tail = insert_at_beginning(head1, tail, 3)
display(head2)