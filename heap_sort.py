class Heap():
    def __init__(self) -> None: 
        self.cbt = []
        self.current_index = 0
        pass
    def insert(self,value:int):
        self.cbt.append(value)  
        self.heapify(self.current_index) 
        self.current_index+=1
    
    def remove(self):
        max_element = self.cbt[0]
        current_element = self.cbt[self.current_index] 
        temp_index = self.current_index 
        
        while(temp_index >= 0):
            parent_index =  self.get_parent_index(temp_index)
            parent = self.cbt[parent_index] 
            self.swap(temp_index,parent_index) 
            temp_index = self.get_parent_index(temp_index) 
        self.cbt.remove(self.current_index)
        self.current_index -=1 
        return max_element 
    
    def print_heap(self): 
        count = 0 
        index = 0
        while(index < len(self.cbt)):
            for i in range(pow(2,count)):
                if index < len(self.cbt):
                    print(self.cbt[index],end=" ")
                    index+=1
                else:
                    break 
            count+=1 
            print("")  
            
    
    def swap(self,index_1, index_2):
        temp = self.cbt[index_1]
        self.cbt[index_1] = self.cbt[index_2]
        self.cbt[index_2] = temp  
        
    def get_parent_index(child_index):
        if child_index%2==0:
            return child_index//2
        else:
            return (child_index-1)//2
        
        
     
    def heapify(self,current_index): 
        if current_index==0:
            return   
        if current_index%2 == 0:
            parent_index = current_index//2
        else:
            parent_index = (current_index-1)//2
        if self.cbt[current_index] > self.cbt[parent_index]:
            self.swap(current_index,parent_index)
            self.heapify(parent_index) 
        else:
            return
    
    def reverse_heapify(self, limit): 
        index = 0  
        # check if the node is a leaf node
        while(2*index+2 < limit): 
            index_child1 = 2*index + 1
            index_child2 = 2*index + 2
            child1 = self.cbt[index_child1]
            child2 = self.cbt[index_child2]  
            if self.cbt[index] < child1 or self.cbt[index] < child2 :
                if child1 > child2:
                    self.swap(index, index_child1) 
                    index = index_child1
                else:
                    self.swap(index,index_child2)  
                    index = index_child2 

            
            
            

        
def heap_sort(arr:list)->list: 
    heap = Heap()
    
    # convert the array into a max_heap 
    for element in arr:
        heap.insert(element) 
    heap.print_heap() 
    # re-arrange the elements of the array in order to sort them out 
    pointer1 = 0;
    pointer2 = len(heap.cbt) - 1
    while(pointer2 >= 0):
        heap.swap(pointer1,pointer2) 
        heap.reverse_heapify(pointer2)
        pointer2-=1 # locking the array position 
        
    print(heap.cbt)
          
        
        
heap_sort([8,9,4,5,6,7,2,3,1,0])