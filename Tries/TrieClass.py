
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