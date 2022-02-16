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

init for RouteTrieNode():
Time Complexity: O(1)
Space Complexity: O(1) 
The Time Complexity of O(1) is absolutely clear as there are no major computations happening, and I think this the same reason for the space complexity as we do not need any auxillary space here so the space complexity is also (1) 

init for Router():
Time Complexity: O(1)
Space Complexity: O(1) 
The Time Complexity of O(1) is absolutely clear as there are no major computations happening, and I think this the same reason for the space complexity as we do not need any auxillary space here so the space complexity is also O(1)

check_and_remove_trailing:
Time Complexity: O(n)
Space Complexity: O(1)

add_handler: 
Time Complexity: O(n), where n is the number of sub-paths in the path, i.e strings separated by "/" 
Space Complexity: O(n), where n is the number of sub-paths in the path, i.e strings separated by "/", as each sub-path needs to be added as a node 

lookup()
Time Complexity: O(n), where n is the number of sub-paths in the path, i.e strings separated by "/"
Space Complexity: O(1) 

return_404():
Time Complexity: O(1)
Space Complexity: O(1) 



## Overall Time Complexity Analysis 

Space Complexity of the solution is O(n): Because we use a key-value pair data structure and for each sub-path we add it as a key in the dictionary. Hence O(n), n- is the number of unique sub-paths