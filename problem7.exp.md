# Idea 

I found this problem to be the most interesting ones

Code-wise explanation 

function check_and_remove_trailing 
Wrote this to extract the route name from the url 

RouteTrieNode: 
Node present in the Trie, has the properties of 
children = {} --> To adhere and facilitate the Trie DataStructure 
rote --> To specify whether the route is true or false 
route_path to store the url path 
handler --> name of the handler, which is supposed to handle this path 

Route: 

init --> takes in "root handler" and "not found handler" 

add_handler --> takes the url path, and the handler name to initialize a TrieNode with a handler and add it to the Trie 

lookup --> used to search through the dictionary trie structure and find out if the path is actually a route

return_404(): returns a message along with the not found handler
## Modular Time and Space Complexity: 

Time Complexity of lookups and add_handler : O(n), n is the number of sub-paths  

Space Complexity of the solution is O(n): Because we use a key-value pair data structure and for each sub-path we add it as a key in the dictionary. Hence O(n), n- is the number of unique sub-paths