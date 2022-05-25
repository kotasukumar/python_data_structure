class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next

    def remove(self, remove_key):
        head_value = self.head

        if head_value is not None:
            if head_value.data == remove_key:
                self.head = head_value.next
                head_value = None
                return
        while head_value is not None:
            if head_value.data == remove_key:
                break
            prev = head_value
            head_value = head_value.next

        if head_value is None:
            return

        prev.next = head_value.next
        head_value = None


if __name__ == "__main__":
    my_llist = Linkedlist()
    file_open_write = open("example.txt", 'w')
    file_open_write.write('hi all good morning')
    file_open_write.close()

    data = open("example.txt", 'r')
    data_store = data.read().split()
    for i in range(len(data_store)):
        my_llist.append(data_store[i])
    data.close()
    print('The linked list: ', end=' ')
    my_llist.display()
    word = str(input("\nEnter a word to search: "))
    if word in data_store:
        my_llist.remove(word)
    else:
        my_llist.append(word)
    my_llist.display()

    file = open("example.txt", 'w')
    curr = my_llist.head
    while curr is not None:
        file.write(curr.data, end=' ')
        curr = curr.next
    file.close()

