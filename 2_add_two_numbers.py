# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode()
        answer_iter = answer
        carry = 0
        while True:
            if l1 != None:
                answer_iter.val += l1.val
            if l2 != None:
                answer_iter.val += l2.val

            if answer_iter.val >= 10:
                answer_iter.val -= 10
                carry = 1
            else:
                carry = 0

            if (l1 != None and l1.next != None) or (l2 != None and l2.next != None) or carry == 1:
                answer_iter.next = ListNode(carry)
                answer_iter = answer_iter.next
            else:
                break

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        return answer
