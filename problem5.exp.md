# Idea 
This problem was pretty straight forward and helped me to know the implementation of Trie in real life use cases 

I built each node of the Trie, to have the letter and the end result if it's a word or not, also a children={} property to contain the nodes below it 

With each letter that typed into the text box, the function traverses through the children of the node containing the sequence in the input box and returns all the results ( node that have end result as true) 

## Modular Time and Space Complexity  


functions in TrieNode: 


init():
Time Complexity: O(1)
Space Complexity: O(1) 
These are O(1) because they don't have a direct correlation with the input size, i.e they are independent of the input size

insert():
Time Complexity : O(1) 
Space Complexity: O(1)

suffixes():
not used in the functionality 


functions in Trie: 

init():
Time Complexity: O(1)
Space Complexity: O(1) 
These are O(1) because they don't have a direct correlation with the input size, i.e they are independent of the input size

add():
Time Complexity: O(k), 'k' is the number of characters in the word being added 
Space Complexity: O(k), 'k' is the number of unique characters in the word being added to the trie


exists():
Time Complexity: O(k), 'k' is the number of characters in the word being checked 
Space Complexity: O(1)

find():
Time Complexity: O(k), 'k' is the number of characters in the word being checked
Space Complexity: O(1)

get_trie_node():
Time Complexity: O(k), 'k' is the number of characters in the word being checked
Space Complexity: O(1)

get_suffixes():
Time Complexity: O(K*L), where 'K' is the number of keys present in the trie and 'L' is the length of average key, because of the recursion involved for each key 
Space Complexity: O(k), where 'k' is the number of matching suffixes


recursive_suffix_search():
The time complexity of recursive_suffix_search is same as that of get_suffixes() function, if you observe carefully, the structure of these functions are almost similar, the only difference is that the former calls the later and the later calls itself
Space Complexity: O(k), where 'k' is the number of matching suffixes 

## Overall Time Complexity

The above approach is quite costly ( atleast seems to be), and it depends on the depth and children of the of the Trie, hence a Time Complexity is O(N) where there are 'N' elements
I think it's because of this massive complexity that services like Algolia Search don't display the results until unless atleast 3-4 characters are typed. Which decreases the possible chances by "D" times.

The Space Complexity is O(ALPHABET_SIZE), which is the number of unique character present