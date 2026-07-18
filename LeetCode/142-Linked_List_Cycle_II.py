from helpers import ListNode, make_linked_list

head = make_linked_list([3, 2, 0, -4], 1)

def solve(head):
    slow = head
    fast = head 

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            ptr = head
            while ptr != slow:
                ptr = ptr.next
                slow = slow.next
            return ptr

    return None

print(solve(head))