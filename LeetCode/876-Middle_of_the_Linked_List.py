from helpers import make_linked_list, ListNode

head = make_linked_list([1, 2, 3, 4, 5, 6], -1)

def solve(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next
    return slow

print(solve(head))