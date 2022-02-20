# The idea:
#       Skip the duplicate nodes in the list.

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def addNode(self, data):
        cur = self.head
        if cur is None:
            self.head = Node(data)
        else:
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def traverse(self):
        cur = self.head
        while cur and cur.next:
            print(cur.data, end=" -> ")
            cur = cur.next
        print(cur.data)


def arrayToLinkedList(arr : int) -> LinkedList:
    """
    Convert an array to a linked list
    """
    llist = LinkedList()
    for ele in arr:
        llist.addNode(ele)
    return llist


if __name__ == "__main__":

    arr = [1,1,2,2,3,3,4,4,4,4,5]

    llist = arrayToLinkedList(arr)
    
    print("Original Linked List: ")
    llist.traverse()

    ######### Solution starts #########
    
    def remove_duplicates(llist : LinkedList) -> LinkedList:
        """ 
        Remove duplicates from a linked list
        """
        cur = llist.head            # current node
        while cur and cur.next:     # while current node and next node are not None
            if cur.data == cur.next.data:       # if current node data is equal to next node data => duplicate node
                cur.next = cur.next.next        # remove the duplicate node
            else:                               # if current node data is not equal to next node data => no duplicate node
                cur = cur.next                  # move to next node
        return llist                            # return the linked list with no duplicates
    
    ######### Solution ends #########

    llist = remove_duplicates(llist)
    print("Linked List after removing duplicates: ")
    llist.traverse()

# Time complexity: O(n), with n is the number of nodes in the linked list.
            
    