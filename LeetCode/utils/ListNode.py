

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_ListNode(arr: []):
    head = ListNode()
    tail = head
    for val in arr:
        t2 = ListNode(val)
        tail.next = t2
        tail = tail.next
    return head.next

def show_ListNode(root):
    node = root
    print("show list node")
    # while node:             # no nil no null,  use None, or just node
    while node != None:
        print(str(node.val) + ", ", end = '')
        node = node.next


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    node = make_ListNode(arr)
    show_ListNode(node)