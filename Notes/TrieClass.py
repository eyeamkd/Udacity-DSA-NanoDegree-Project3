
from asyncio.windows_events import NULL
from mimetypes import init


class TrieNode(): 
    def __init__(self) -> None:
        self.children = { } 
        self.word = False

class Trie():  
    def __init__(self):
        self.root = TrieNode()
        
    def add(self,word): 
        base_node = self.root
        for char in word:
            if(char not in base_node.children):
                base_node.children[char] = TrieNode()
                base_node = base_node.children[char] 
            else:
                base_node = base_node.children[char] 
        base_node.word = True
    
    def exists(self,word): 
        base_node = self.root
        for char in word: 
            if(char in base_node.children ):
                base_node = base_node.children[char] 
            else:
                return False
        return base_node.word 

trie = Trie()
trie.add('Kunal')
trie.add('Dubey')

print(trie.exists('Kunal')) 



from collections import defaultdict 

class NewTrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.word = False
        
class NewTrie:
    def __init__(self) -> None:
        self.root = NewTrieNode()
    
    def add(self,word:str)->None: 
        base_node = self.root;
        for letter in word: 
            base_node.children[letter] = NewTrieNode() 
            base_node = base_node.children[letter] 
        base_node.word = True 
    
    def exists(self,word:str)->bool: 
        base_node = self.root
        for letter in word: 
            if(letter in base_node.children): 
                base_node = base_node.children[letter] 
            else:
                return False 
        return base_node.word 
    
    def print_node(self)->None:
        print(self.root) 
        
    def __repr__(self) -> str:
        return self.root
                
            
#test 
new_trie = NewTrie() 

new_trie.add("kunal")
new_trie.add("dubey") 
new_trie.print_node() 
result = new_trie.exists("kunal") 
print(result)
