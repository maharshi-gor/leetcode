# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Author: Maharshi Gor
    Date: 2023-10-06
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
                                                            Optional[ListNode]:
        """
        You are given two non-empty linked lists representing two non-negative
        integers. The digits are stored in reverse order, and each of their
        nodes contains a single digit. Add the two numbers and return the sum as
        a linked list.

        You may assume the two numbers do not contain any leading zero, except
        the number 0 itself.

        Explanation
        -----------
        It is very simple problem we need to collect the digits from the linked-
        list and create a number. We will be doing the same thing for both l1 &
        l2.

        One more thing is the linked-list is reversed so we will encounter the
        digit at the unit's place first. We will multiply that digit with its
        place value i.e; unit's place with 1, ten's place with 10 and so on.

        Example:
        input: 2 -> 4 -> 3
        number: 2*1 + 4*10 + 3*100 = 342

        Once we extract both number we will simply add them.

        After that we convert that number to string, that will give us the
        flexibility to iterate over digits to split them.

        We will be accessing them in the reverse order as the node list starts
        from unit's place.
        """

        number_1 = self.computeValueOfListNode(l1)
        number_2 = self.computeValueOfListNode(l2)

        summation_number = number_1 + number_2

        return self.convertNumberToListNode(summation_number)

    def convertNumberToListNode(self, number: int) -> Optional[ListNode]:
        # Converting the number to string
        str_number = str(number)

        num_of_digits = len(str_number)

        # Saving base node to return
        base_l = ListNode()

        # Creating a cursor variable
        temp_l = base_l

        for i in range(num_of_digits):
            # converting the character into digit
            digit = int(str_number[num_of_digits - i - 1])

            # Assigning value to list node
            temp_l.val = digit

            if i != num_of_digits - 1:
                # create next list node
                next_l = ListNode()

                # set next node of the current node
                temp_l.next = next_l

                # move the pointer to next node
                temp_l = temp_l.next

        return base_l

    def computeValueOfListNode(self, l: Optional[ListNode]) -> int:
        value = 0
        digit_position = 1
        while True:
            value += l.val * digit_position

            if l.next:
                l = l.next
                digit_position *= 10
            else:
                break
        return value