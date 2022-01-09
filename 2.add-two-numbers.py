#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            SUM = l1.val if l1 else 0
            SUM += l2.val if l2 else 0

            carry, val = divmod(SUM + carry, 10)
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return out.next


        
# @lc code=end

