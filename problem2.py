# Check for an element in the rotated array 
def checkSorted(arr:list,index:int)->bool:
    if(index>=1):
        if(arr[index-1]<=arr[index]<=arr[index+1]):
            return True
        else:
            return False 
    else:
        if(arr[0]<=arr[index]):
            return True
        else:
            return False

    # find the pivot point 
    # divide the array by the pivot point 
    # binary search for the index
    # finding pivot point 

def binarySearchCheckSorted(arr:list,low:int,high:int)->int:
    while(low<high):
        mid = low+high//2  
        if(checkSorted(arr,mid)):
            binarySearchCheckSorted(arr,mid,high)
            binarySearchCheckSorted(arr,low,mid) 
        else:
            return arr.index(mid) 
    return -1 
    ## condition to handle, what if the element is not present at all? 

def binarySearchForIndex(arr:list,low:int,high:int,element:int)->int:  
    while(low<high):
        mid = low+high//2
        if(arr[mid]==element):
            return arr.index(mid) 
        else:
            binarySearchForIndex(arr,low,mid-1,element)
            binarySearchForIndex(arr,mid+1,high)
    return -1

def findIndex(arr:list,element:int)->int:  
    length = len(arr)
    pivot = binarySearchCheckSorted(arr,0,length-1)   
    if(pivot!=element):
        index = binarySearchForIndex(arr,0,pivot-1,element)
        if(index==-1):
            index = binarySearchForIndex(arr,pivot+1,element) 
        return index
    return pivot