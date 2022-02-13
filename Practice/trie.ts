class TrieNode{
    end:boolean;
    letter:string;
    
    constructor(letter:string,end:boolean=false){
        this.end = end;
        this.letter = letter; 
    }    
} 

class Trie{
    str:string; 
    dict:any;

    constructor(str:string){
        this.str = str; 
        this.formTrie(this.str); 
        
    } 

    private formTrie(input:string){
        const list:Array<string> = input.split(''); 
        let obj = {}  
        let temp = {}
        let prev = '';
        list.forEach((element,index) => {
            const node = new TrieNode(element); 
            // let temp = obj  
            temp = prev?temp[prev]:{}; 
            console.log("temp is", temp)
            temp[node.letter]={node}; 
            console.log("temp is", temp); 
            console.log("obj is", obj); 
            temp = temp[node.letter]
            prev = node.letter 
          
        });  
        this.dict = obj;
        console.log("Trie formed ",this.dict );
    }
} 

let sample = "kunal"; 
let sampleTrie:any = new Trie(sample); 
console.log("Sample trie", sampleTrie);