class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node

        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        node.prev.next =  node.next
        node.next.prev = node.prev

    def add(self,node):
        prevEnd = self.right.prev
        prevEnd.next = node
        node.prev = prevEnd
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            oldNode = self.cache[key]
            self.remove(oldNode)
        
        node = Node(key,value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            nodeToDelete = self.left.next
            self.remove(nodeToDelete)
            del self.cache[nodeToDelete.key]
        
