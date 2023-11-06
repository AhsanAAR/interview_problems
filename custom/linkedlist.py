class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next:Node = next

def linked_list_from_array(array: list) -> Node:
    temp = head = None
    for item in array:
        if head is None:
            head = temp = Node(item)
        else:
            temp.next = Node(item)
            temp = temp.next

    return head

def print_list(head: Node, end=' '):
    while head is not None:
        print(head.data, end=end)
        head = head.next

def length(head: Node) -> int:
    res = 0
    while head:
        res += 1
        head = head.next

    return res

def node_at(head: Node, index: int) -> Node :
    for _ in range(index):
        if head is None:
            break
        head = head.next

    if head is None:
        raise IndexError()
    
    return head

def insert(head: Node, index:int, data) -> Node:
    if index == 0:
        temp = Node(data)
        temp.next = head
        return temp
    
    prev_node = node_at(head, index-1)
    temp = prev_node.next
    prev_node.next = Node(data)
    prev_node.next.next = temp
    return head

def delete(head: Node, index:int) -> Node:
    if head is None:
        return Exception()
    
    if index == 0:
        temp = head.next
        del head
        return temp
    
    prev_node = node_at(head, index-1)
    curr = prev_node.next
    prev_node.next = curr.next
    del curr
    return head

arr = [2,3,4,5,5]
ll = linked_list_from_array(arr)

ll = delete(ll, 0)
print_list(ll)
