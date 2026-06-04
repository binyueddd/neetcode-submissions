class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.val=value
        self.pre=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.head=Node()
        self.tail=Node()

        self.head.next=self.tail
        self.tail.pre=self.head

    def _remove(self, node):
        prev_node=node.pre
        nxt_node=node.next
        prev_node.next=nxt_node
        nxt_node.pre=prev_node

    def _add(self,node):
        prev_node=self.tail.pre
        prev_node.next=node
        self.tail.pre=node
        node.next=self.tail
        node.pre=prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node=self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value

            self._remove(node)
            self._add(node)
        
        else:
            node=Node(key,value)
            self.cache[key]=node
            self._add(node)
            if len(self.cache)>self.capacity:
                del_node=self.head.next
                self._remove(del_node)
                del self.cache[del_node.key]
