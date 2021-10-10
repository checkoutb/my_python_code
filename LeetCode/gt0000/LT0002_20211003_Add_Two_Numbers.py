

# import 
# import 
# import "../utils/ListNode"        ....md 也是错的，不过自动导入进去了，不知道什么原理。..kao  提示是vscode帮我的，但是执行的时候必须导入。
# import typing
import sys
sys.path.append("..")                   #...
from typing import Optional
from utils.ListNode import *        # .... .. not /

class LT0002:


# carry, val = divmod(v1+v2+carry, 10)

# py 整数没有上限，所以全部转为整数，然后相加，然后再转为ListNode
        # def toint(node):
        #     return node.val + 10 * toint(node.next) if node else 0
        # def tolist(n):
        #     node = ListNode(n % 10)
        #     if n > 9:
        #         node.next = tolist(n / 10)
        #     return node
        # return tolist(toint(l1) + toint(l2))

        # def toint(node):
        #     return node.val + 10 * toint(node.next) if node else 0            # 。。
        # n = toint(l1) + toint(l2)
        # first = last = ListNode(n % 10)               # = =
        # while n > 9:
        #     n /= 10
        #     last.next = last = ListNode(n % 10)           # 。。
        # return first

        # addends = l1, l2                      # ！！！
        # dummy = end = ListNode(0)
        # carry = 0
        # while addends or carry:
        #     carry += sum(a.val for a in addends)          # 。。。
        #     addends = [a.next for a in addends if a.next]         # 。。。
        #     end.next = end = ListNode(carry % 10)         # = =
        #     carry /= 10
        # return dummy.next




# Runtime: 64 ms, faster than 91.13% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.3 MB, less than 71.54% of Python3 online submissions for Add Two Numbers.

# Optional..
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        tail = ans
        carry = 0
        while l1 or l2 or carry:                 # 0 is true or false?      0 is false.
            carry = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(carry % 10)
            tail, carry = tail.next, carry // 10                # // != / ...
            l1, l2 = (l1.next if l1 else None), (l2.next if l2 else None)
        return ans.next


if __name__ == '__main__':
    sol = LT0002()
    arr1 = [9,9,9,9,9,9,9]
    arr2 = [9,9,9,9]
    l1 = make_ListNode(arr1)
    l2 = make_ListNode(arr2)

    l3 = sol.addTwoNumbers(l1, l2)

    show_ListNode(l3)

    