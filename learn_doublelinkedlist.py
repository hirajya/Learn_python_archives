class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def get_last_node(self):
        itr = self.head

        while itr.next:
            itr = itr.next
        return itr

    def print_forward(self):
        if self.head is None:
            print('Double linked list is empty')
            return

        itr = self.head
        dll = ''

        while itr:
            dll += str(itr.data) + ' --> '
            itr = itr.next
        print(f'Linked list in forward: {dll}')

    def print_backward(self):
        if self.head is None:
            print('Double linked list is empty')
            return

        dll = ''
        itr = self.get_last_node()

        while itr:
            dll += str(itr.data) + ' --> '
            itr = itr.prev
        print(f'Linked list in backwards: {dll}')

    def get_length(self):
        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node

        else:
            itr = self.head
            node = Node(data, itr, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node

        else:
            itr = self.get_last_node()
            node = Node(data, None, itr)
            itr.next = node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next = node
                if node.next:
                    node.next.prev = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        itr = self.head

        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next = node
                if node.next:
                    node.next.prev = node

            itr = itr.next

    def remove_by_element(self, element):
        if self.head is None:
            return

        itr = self.head
        if itr.data == element:
            self.head = self.head.next
            self.head.prev = None
            return

        while itr:
            if itr.data == element:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev

            itr = itr.next


if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_values(['rod', 'ara', 'love', 'joyce', 'lei'])
    print(ll.get_length())
    ll.print_forward()
