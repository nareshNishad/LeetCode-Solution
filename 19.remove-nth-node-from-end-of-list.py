#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Novice method
        """
        curr = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        if count == 1:
            return None
        if count == n:
            head.val = head.next.val
            head = head.next
            return head
        position_from_start = count - n -1
        curr = head
        while position_from_start !=0 :
            curr = curr.next
            position_from_start -=1
        curr.next = curr.next.next
        return head
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


        
# @lc code=end

