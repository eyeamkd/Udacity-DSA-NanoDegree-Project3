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
    
    def __init__(self, path, handler) -> None:
        self.children = {} 
        self.route = False 
        self.route_path = path  
        self.handler = handler


class Router:
    def __init__(self, handler:str, not_found_handler:str) -> None:
        root_node = RouteTrieNode('root','root handler')
        self.root = root_node 
        self.handler = handler
        self.not_found_handler = not_found_handler 
    
    
    def add_handler(self, path:str, handler:str)-> None:  
        path = check_and_remove_trailing(path)
        paths = path.split('/') 
        #print("paths are ", paths)
        base_node = self.root 
        for sub_path in paths: 
            if(len(sub_path)>0):
                if sub_path in base_node.children:
                    base_node = base_node.children[sub_path]
                else:
                    new_node = RouteTrieNode(sub_path,handler)
                    base_node.children[sub_path] = new_node 
                    base_node = base_node.children[sub_path]
        base_node.route = True 
                    
    
    def lookup(self, path): 
        base_node = self.root
        if path =='/':
           return base_node.handler
        path = check_and_remove_trailing(path)
        paths = path.split('/') 
        for sub_path in paths:
            if(len(sub_path)>0):
                if sub_path in base_node.children:
                    base_node = base_node.children[sub_path]
                else: 
                  return self.return_404(path)
                      
        #print("Paths are ", paths) 
        #print("base_node is", base_node.children.keys()) 
        if base_node.route:
           return base_node.handler 
        else:
            return self.return_404(path)
            
    def return_404(self, route_name:str):
       return "Oops! for the given route {} is {}".format(route_name, self.not_found_handler)
         


# testing 
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

#edge cases 
# /empty trail 
# ///// ..n slashes of string 