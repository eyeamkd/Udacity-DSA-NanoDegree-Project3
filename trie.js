var TrieNode = /** @class */ (function () {
    function TrieNode(letter, end) {
        if (end === void 0) { end = false; }
        this.end = end;
        this.letter = letter;
    }
    return TrieNode;
}());
var Trie = /** @class */ (function () {
    function Trie(str) {
        this.str = str;
        this.formTrie(this.str);
    }
    Trie.prototype.formTrie = function (input) {
        var list = input.split('');
        var obj = {};
        var temp = {};
        var prev = '';
        list.forEach(function (element, index) {
            var node = new TrieNode(element);
            // let temp = obj  
            temp = prev ? temp[prev] : {};
            console.log("temp is", temp);
            temp[node.letter] = { node: node };
            console.log("temp is", temp);
            console.log("obj is", obj);
            temp = temp[node.letter];
            prev = node.letter;
        });
        this.dict = obj;
        console.log("Trie formed ", this.dict);
    };
    return Trie;
}());
var sample = "kunal";
var sampleTrie = new Trie(sample);
console.log("Sample trie", sampleTrie);
