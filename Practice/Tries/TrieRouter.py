# from TrieClass import Trie 
# from TrieClass import TrieNode

from email.mime import base
from re import sub


def check_and_remove_trailing(path:str):
    if path[0] == '/' and path[-1] == '/':
        return path[1:-1] 
    elif path[0] == '/':
        return path[1:]

class RouteTrieNode:
    
    def __init__(self, path) -> None:
        self.children = {} 
        self.route = False 
        self.route_path = path 


class RouteTrie:
    def __init__(self, handler:str, not_found_handler:str) -> None:
        root_node = RouteTrieNode('root')
        self.root = root_node 
        self.handler = handler
        self.not_found_handler = not_found_handler 
    
    
    def insert(self, path:str)-> None:  
        path = check_and_remove_trailing(path)
        paths = path.split('/') 
        #print("paths are ", paths)
        base_node = self.root 
        for sub_path in paths: 
            if(len(sub_path)>0):
                if sub_path in base_node.children:
                    base_node = base_node.children[sub_path]
                else:
                    new_node = RouteTrieNode(sub_path)
                    base_node.children[sub_path] = new_node
                    base_node = base_node.children[sub_path]
        base_node.route = True 
                    
    
    def find(self, path): 
        base_node = self.root
        if path =='/':
           return self.return_handler(path, base_node.route_path  )
        path = check_and_remove_trailing(path)
        paths = path.split('/') 
        for sub_path in paths:
            if(len(sub_path)>0):
                if sub_path in base_node.children:
                    base_node = base_node.children[sub_path]
                else: 
                  return self.return_404(path)
                      
        print("Paths are ", paths) 
        print("base_node is", base_node.children.keys()) 
        if base_node.route:
           return self.return_handler(path,base_node.route_path ) 
        
    def return_handler(self,route_name:str,sub_path:str):
       return "Handler for the Route {} is {}".format(route_name,sub_path + " " +self.handler) 
        
    
    def return_404(self, route_name:str):
       return "Oops! for the given route {} is {}".format(route_name, self.not_found_handler)
         


# testing 

new_trie = RouteTrie("handler","404 handler")
new_trie.insert("/about") 
new_trie.insert("/about/cv")
new_trie.insert("/about/portfolio")
new_trie.insert("/ideas") 
new_trie.insert("/goals")

print(new_trie.find('/')) 

#edge cases 
# /empty trail 
# ///// ..n slashes of string 