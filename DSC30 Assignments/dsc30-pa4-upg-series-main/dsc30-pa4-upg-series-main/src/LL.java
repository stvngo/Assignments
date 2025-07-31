public class LL<T> {
    private LLNode head;
    private LLNode tail;
    private int length;

    public LL() {
        LLNode dummyNode1 = new LLNode();
        LLNode dummyNode2 = new LLNode();
        this.head = dummyNode1;
        this.tail = dummyNode2;
        this.head.next = this.tail;
        this.length = 0;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("print the linked list ...\n==================\n");
        LLNode curr = this.head;
        while (curr != this.tail) {
            sb.append(curr.getIndex() + "\t: " + String.valueOf(curr.getData()) + "\n"); // instead of .toString()
            curr = curr.next;
        }
        sb.append("null\t: null\n");
        return sb.toString();
    }

    public int getLength() {
        return this.length;
    }

    public String[] getDataArray() { // use this method to test LL
        String[] data = new String[this.length];
        LLNode curr = this.head.next;
        for (int i = 0; i < this.length; i++) {
            data[i] = curr.getData().toString(); 
            curr = curr.next;
        }
        return data;
    }

    public String[] getIndexArray() { // use this method to test LL
        String[] indexes = new String[this.length];
        LLNode curr = this.head.next;
        for (int i = 0; i < this.length; i++) {
            indexes[i] = curr.getIndex();
            curr = curr.next;
        }
        return indexes;
    }

    public void appendNode(String _index, T _data) {
        if (_index == null || _index.isEmpty()) { // default to _index number if invalid _index passed
            _index = Integer.toString(this.length);
        }

        LLNode newNode = new LLNode(_index, _data);

        if (this.head.next == this.tail) { // if list is empty, place node btwn dummy nodes
            this.head.next = newNode;
            newNode.next = this.tail;
        } else {
            LLNode curr = this.head;
            while (curr.next != this.tail) {
                curr = curr.next;
            }
            curr.next = newNode;
            newNode.next = this.tail;
        }
        this.length++;
    }

    public LLNode searchNode(String _index) {
        LLNode curr = this.head.next; // skip dummy head
        while (curr != null && curr != this.tail) {
            if (_index.equals(curr.getIndex())) { 
                return curr;
            }
            curr = curr.next;
        }
        return null;
    }

    public void removeNode(String _index) throws IllegalArgumentException {
        LLNode curr = this.head;
        // LLNode<T> prevNode;
        LLNode nodeToRemove = searchNode(_index);
        if (nodeToRemove == null) {
            throw new IllegalArgumentException("removeNode(String _index): No node with an index " 
            + _index + " in the list"); // item not found
        }
        // } else if (this.length == 1) { // for one node case
        //     this.head.next = this.tail;
        //     this.length--;
        // } else if (this.head.next == nodeToRemove) { // nodeToRemove is first node in list
        //     this.head.next = nodeToRemove.next;
        //     nodeToRemove.next = null;
        //     this.length--;
        // } else if (nodeToRemove.next != null) { //nodeToRemove is not the last node
        //     while (!_index.equals(curr.next.getIndex())) {
        //         curr = curr.next;
        //     }
        //     prevNode = curr;
        //     prevNode.next = nodeToRemove.next;
        //     nodeToRemove.next = null;
        //     this.length--;
        // } 

        while (curr.next != null && curr.next != nodeToRemove) {
            // curr.next == null -> reached dummynode2
            // curr.next == nodeToRemove -> reached node before nodeToRemove
            curr = curr.next;
        }
        curr.next = nodeToRemove.next;
        nodeToRemove.next = null; 
        this.length--;
    }

    public void updateNode(String _index, T value) {
        LLNode nodeToUpdate = searchNode(_index);
        if (nodeToUpdate == null) {
            throw new IllegalArgumentException("updateNode(String _index, T value): No node with an index "
            + _index + " in the list");
        }
        nodeToUpdate.setData(value);
    }

    public class LLNode {
        private String index;
        private T data;
        private LLNode next;

        public LLNode() {
            this.index = null;
            this.data = null;
            this.next = null;
        }

        public LLNode(String _index, T _data) {
            this.index = _index;
            this.data = _data;
            this.next = null;
        }

        public String getIndex() {
            return index;
        }

        public T getData() {
            return data;
        }

        public void setData(T d) {
            this.data = d;
        }
    }
}