class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    curr = dummy
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 if list1 else list2
    return dummy.next


def deleteDuplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == slow: # исправлено для проверки
            if slow == fast:
                return True
    return False


def reorderList(head):
    if not head or not head.next:
        return
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


def doubleIt(head):
    def helper(node):
        if not node:
            return 0
        carry = helper(node.next)
        total = node.val * 2 + carry
        node.val = total % 10
        return total // 10

    carry = helper(head)
    if carry > 0:
        head = ListNode(carry, head)
    return head


import heapq

def mergeKLists(lists):
    dummy = ListNode()
    curr = dummy
    heap = []
    
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.val, i, l))
            
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
            
    return dummy.next


def reverseKGroup(head, k):
    curr = head
    count = 0
    while curr and count < k:
        curr = curr.next
        count += 1
        
    if count == k:
        curr = reverseKGroup(curr, k)
        while count > 0:
            nxt = head.next
            head.next = curr
            curr = head
            head = nxt
            count -= 1
        head = curr
    return head


def partition(head, x):
    before_head = ListNode(0)
    before = before_head
    after_head = ListNode(0)
    after = after_head
    
    curr = head
    while curr:
        if curr.val < x:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next
        curr = curr.next
        
    after.next = None
    before.next = after_head.next
    return before_head.next


# Вспомогательные функции для перевода списка в массив и обратно (для удобства тестов)
def list_to_array(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

def array_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


if __name__ == "__main__":
    # Тест 1: Об'єднати два списки
    l1 = array_to_list([1, 2, 4])
    l2 = array_to_list([1, 3, 4])
    print("Task 1:", list_to_array(mergeTwoLists(l1, l2)))

    # Тест 2: Видалити дублікати
    l3 = array_to_list([1, 1, 2, 3, 3])
    print("Task 2:", list_to_array(deleteDuplicates(l3)))

    # Тест 3: Цикл (створимо цикл вручную)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node1.next = node2
    print("Task 3 (False):", hasCycle(node1))

    # Тест 4: Перевпорядкувати список
    l4 = array_to_list([1, 2, 3, 4])
    reorderList(l4)
    print("Task 4:", list_to_array(l4))

    # Тест 5: Видалити вузол
    l5 = array_to_list([4, 5, 1, 9])
    # удалим узел со значением 5 (это второй элемент)
    deleteNode(l5.next) 
    print("Task 5:", list_to_array(l5))

    # Тест 6: Подвоїти число
    l6 = array_to_list([1, 8, 9])
    print("Task 6:", list_to_array(doubleIt(l6)))

    # Тест 7: Об’єднати k списков
    lists7 = [array_to_list([1, 4, 5]), array_to_list([1, 3, 4]), array_to_list([2, 6])]
    print("Task 7:", list_to_array(mergeKLists(lists7)))

    # Тест 8: Розвернути в k-групі
    l8 = array_to_list([1, 2, 3, 4, 5])
    print("Task 8:", list_to_array(reverseKGroup(l8, 2)))

    # Тест 9: Розділити список
    l9 = array_to_list([1, 4, 3, 2, 5, 2])
    print("Task 9:", list_to_array(partition(l9, 3)))