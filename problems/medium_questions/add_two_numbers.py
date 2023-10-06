# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
                                                            Optional[ListNode]:

        number_1 = self.computeValueOfListNode(l1)
        number_2 = self.computeValueOfListNode(l2)

        summation_number = number_1 + number_2

        return self.convertNumberToListNode(summation_number)

    def convertNumberToListNode(self, number: int) -> Optional[ListNode]:
        # Converting the number to string
        str_number = str(number)

        # Reversing as the values go in reverse order in the listnode
        reversed_str_number = str_number[::-1]

        num_of_digits = len(reversed_str_number)


        # Saving base node to return
        base_l = ListNode()

        # Creating a cursor variable
        temp_l = base_l

        for i in range(num_of_digits):
            # converting the character into digit
            digit = int(reversed_str_number[i])

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