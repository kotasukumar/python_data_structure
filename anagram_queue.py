def prime(palindrome_list):
    dummy_list = []
    for number in palindrome_list:
        for j in range(2, number):
            if number % j == 0:
                break
        else:
            dummy_list.append(number)
    return dummy_list


def reverse(num):
    return num[::-1]


def anagram(lower, upper):
    anagram_list = []
    for i in range(lower, upper):
        if str(i) == reverse(str(i)):
            anagram_list.append(i)
    prime_list = prime(anagram_list)
    return prime_list


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = Node(data, None)

    def remove(self, data):
        if self.head is None:
            return "list is empty"
        if self.head.data == data:
            self.head = self.head.next

        first = self.head
        while first.next is not None:
            if first.next.data == data:
                first.next = first.next.next
                break
            first = first.next

    def print(self):
        if self.head is None:
            return "It is empty"

        first = self.head
        string = ''
        while first is not None:
            string += str(first.data) + ' '
            first = first.next
        return string


if __name__ == "__main__":
    anagram = anagram(0, 1000)
    my_linked_list = linked_list()
    my_linked_list.append(anagram)
    print(my_linked_list.print())
