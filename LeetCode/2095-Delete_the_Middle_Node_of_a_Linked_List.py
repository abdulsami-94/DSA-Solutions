from helpers import ListNode, make_linked_list

head = make_linked_list([1, 3, 5, 7, 2, 4],-1)

def solve(head):
    if not head or not head.next:
        return None

    prev = None
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head



print(solve(head))