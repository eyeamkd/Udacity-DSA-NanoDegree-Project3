trie = {
    'k': {
        'u': {
            'n': {
                'a': {
                    'l': {
                        'end': True
                    },
                    'end': False
                },
                'end': False
            },
            'end': False
        },
        'end': False
    },
    'end': False
}

word = 'kun'

for char in word:
    if(not trie['end']):
        trie = trie[char]

if(trie['end']):
    print("Word found")
else:
    print("Word not found")


another_trie = {'k': {
    'u': {
        'n': {
                'a': {
                    'l': {
                        'end': True
                    },
                    'end': False
                },
                'end': False
                },
        'end': False
    },
    'end': False
},
    'end': False
} 

class Trie_node:{
    letter,
    end
}
