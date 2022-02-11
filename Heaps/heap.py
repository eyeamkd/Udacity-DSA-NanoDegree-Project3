class PriorityQueue:
    def __init__(self) -> None: 
        self.cbt= [] 
        pass 
    
    def insert(self, value:int, priority:int): 
        node = HeapNode(value, priority) 
        self.cbt.append(node) 
        self.heapify() 
        pass 
    
    def remove():
        pass 
    
    def front():
        pass 
    
    def size():
        pass 
    
    def is_empty():
        pass 
    
    def heapify(self): 
        if len(self.cbt)>=2:
            for node in reversed(self.cbt):
                element_index = self.cbt.index(node) 
                prev = self.cbt[element_index-1]
                if prev.priority < node.priority:
                    temp = node
                    node = prev 
                    prev = temp 
             
class HeapNode:
    def __init__(self, value, priority) -> None: 
        self.value = value
        self.priority = priority
        pass 
     
    