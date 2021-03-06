class TrieNode(): 
    def __init__(self) -> None:
        self.children = { } 
        self.word = False
    
    def insert(self, char): 
        self.children[char] = {}
        pass 

    def suffixes(self, suffix=""):
        if self.word:
            return suffix 
        keys = self.children.keys() 
        for char in keys: 
            node = self.children[char]
            node.suffixes(suffix+char)
        

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
    
    def find(self, prefix): 
        ## Find the Trie node that represents this prefix 
        current_node = self.root
        for char in prefix:
            if current_node.children[char] is not None:
                current_node = current_node.children[char] 
        return current_node.word
    
    def get_trie_node(self, word): 
        base_node = self.root
        for char in word: 
           if char in base_node.children :
               base_node = base_node.children[char] 
        return base_node; 
             
    
    def get_suffixes(self, word):
        suffixes = [] 
        node = self.get_trie_node(word) 
        keys = node.children.keys() 
        #print("keys for the word", word, "are ", keys)
        for char in keys:
            self.recursive_suffix_search(node.children[char],word+char, suffixes)
        return suffixes 
        
             
    def recursive_suffix_search(self, node, suffix, suffixes):  
        keys = node.children.keys()
        for char in keys: 
            if char in node.children:
                if node.children[char].word == True:
                    suffixes.append(suffix+char)
                self.recursive_suffix_search(node.children[char],suffix+char, suffixes)
             
         

trie = Trie()
trie.add('Kunal')
trie.add('Dubey')
trie.add('Kushal') 
trie.add('Kruti') 
trie.add('Kruthi')


print(trie.get_suffixes('D')) 

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
] 

for word in wordList:
    MyTrie.add(word) 

print(MyTrie.get_suffixes('a'))
print(MyTrie.get_suffixes('an'))
print(MyTrie.get_suffixes('f'))
print(MyTrie.get_suffixes('tr'))
print(MyTrie.get_suffixes('fa'))
print(MyTrie.get_suffixes('anto'))

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
