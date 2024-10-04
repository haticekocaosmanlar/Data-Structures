// Create Stack with Linked List
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    peek() {
        return this.top;
    }

    push(value) {
        const newNode = new Node(value);
        if (this.length === 0) {
            this.top = newNode;
            this.bottom = newNode;
        }
        else {
            newNode.next = this.top;
            this.top = newNode;
        }
        this.length++;
        return this;
    }

    pop() {
        if (this.length === 0) {
            return null;
        }
        if (this.length === 1) {
            this.bottom = null;
        }
        // const holdingPointer = this.top;
        this.top = this.top.next;
        this.length--;
        // return holdingPointer
        return this;
    }
}

const myStack = new Stack();
myStack.push('google');
myStack.push('udemy');
myStack.push('youtube');
myStack.pop();
myStack.pop();
console.log(myStack)
console.log(myStack.peek())

// ---------------------------------------------
// Create Stack with Array
class Stack {
    constructor() {
        this.stackArray = [];
    }

    peek() {
        return this.stackArray[this.stackArray.length-1];
    }

    push(value) {
        this.stackArray.push(value);
        return this;
    }

    pop() {
        this.stackArray.pop();
        return this;
    }
}

const myStack = new Stack();
myStack.push('google');
myStack.peek();
myStack.push('udemy');
myStack.push('youtube');
myStack.pop();