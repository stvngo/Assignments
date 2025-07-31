public class BST<I extends Comparable<? super I>, T>{

    class BSTNode {
        private I index;
        private T data;
        private BSTNode left;
        private BSTNode right;

        /**
         * Default constructor. Sets all instance variables to be null.
         */
        public BSTNode() {
            this.index = null;
            this.data = null;
            this.left = null;
            this.right = null;
        }

        /**
         * Constructor. Sets data and index to be _data and _index respectively.
         */
        public BSTNode(I _index, T _data) {
            this.index = _index;
            this.data = _data;
        }

        /**
         * Returns the index stored in this node.
         */
        public I getIndex() {
            return this.index;
        }

        /**
         * Returns the data stored in this node.
         */
        public T getData() {
            return this.data;
        }

        /**
         * Updates the data in this node to the specified value.
         */
        public void setData(T d) {
            this.data = d;
        }

        /**
         * Returns a string representation of the node, indicating its index and data.
         */
        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("index:\t" + this.index.toString() + ",\tdata:\t" + this.data.toString() + "\n");
            return sb.toString();
        }

        // NOT SPECIFIED BY WRITEUP
        public int compareTo(I i) {
            int cmp = this.index.compareTo(i);
            return cmp;
        }
    }


    private BSTNode root;
    private int size;

    /**
     * Constructor. Initializes an empty BST with root set to null and size set to 0.
     */
    public BST() {
        this.root = null;
        this.size = 0;
    }


    /**
     * Performs an in-order traversal of the BST and records indices and data values.
     */
    private String inOrderTraversal(BSTNode node) {
        StringBuilder sb = new StringBuilder();
        sb.append("In-order Traversal of the BST ...\n==================\n");
        sb.append(inOrderHelper(node));
        return sb.toString();
    }

    private String inOrderHelper(BSTNode node) { 
        // perform recursion outside of the inOrderTraversal
        // to avoid reinitializing sb every call
        if (node == null) {
            return "";
        }
        return inOrderHelper(node.left) + node.toString() + inOrderHelper(node.right);
    }

    /**
     * Returns a string representation of the entire BST using in-order traversal.
     */
    public String toString() {
        return inOrderTraversal(root);
    }

    /**
     * Returns the size of the BST, i.e., the number of valid nodes.
     */
    public int getSize() {
        return this.size;
    }

    /**
     * Adds a new node with the specified index and data to the BST.
     */
    public void addNode(I _index, T _data) {
        if (this.root == null) {
            this.root = new BSTNode(_index, _data);
            this.size++;
        } else if (addHelper(this.root, _index, _data)) {
            this.size++;
        }
    }

    // NOT SPECIFIED BY WRITEUP
    private boolean addHelper(BSTNode currNode, I _index, T _data) {
        int compare = _index.compareTo(currNode.index);
        if (compare == 0) {
            return false;
        }
        if (compare < 0) {
            if (currNode.left == null) {
                currNode.left = new BSTNode(_index, _data);
                return true;
            }
            else {
                return addHelper(currNode.left, _index, _data);
            }
        } 
        else {
            if (currNode.right == null) {
                currNode.right = new BSTNode(_index, _data);
                return true;
            }
            else {
                return addHelper(currNode.right, _index, _data);
            }
        }
    }
    /**
     * Searches for a node with the specified index in the BST.
     */
    public BSTNode searchNode(I _index) {
        return searchHelper(root, _index);
    }

    // NOT SPECIFIED BY WRITEUP
    private BSTNode searchHelper(BSTNode currNode, I _index) {
        if (currNode == null) {
            return null;
        }
        if (_index.compareTo(currNode.index) < 0) {
            return searchHelper(currNode.left, _index);
        }
        else if (_index.compareTo(currNode.index) > 0) {
            return searchHelper(currNode.right, _index);
        }
        else {
            return currNode;
        }
    }

    /**
     * Removes a node with the specified index from the BST.
     */
    public void removeNode(I _index) throws IllegalArgumentException {
        BSTNode nodeToRemove = searchNode(_index);
        if (nodeToRemove == null) {
            throw new IllegalArgumentException("removeNode(I _index): No node with an index "
            + _index.toString() + " in the BST");
        }

        this.root = removeHelper(this.root, _index);
        size--;
        
        // if (nodeToRemove.right == null && nodeToRemove.left == null) { // if currNode is a leaf-node
        //     nodeToRemove.index = null;
        //     nodeToRemove.data = null;
        //     this.size--;
        // }
        // else {
        //     removeHelper(nodeToRemove, root, _index);
        //     this.size--;
        // }
    }

    // NOT SPECIFIED BY WRITEUP
    private BSTNode removeHelper(BSTNode node, I _index) {
        if (node == null) { // if root node is null/empty, no children
            return null;
        }

        int compare = _index.compareTo(node.index);

        if (compare < 0) { // if index is less than node, move left
            node.left = removeHelper(node.left, _index);
        } else if (compare > 0) { // if index is greater than node, move right
            node.right = removeHelper(node.right, _index);
        } else { // 
            if (node.left == null) { // if only right child
                return node.right;
            }
            if (node.right == null) { // if only less child 
                return node.left;
            }
            // if 2 children
            BSTNode succ = findMin(node.right); // find the in-order successor
            node.index = succ.index; // copy the elements from the successor to the node
            node.data = succ.data;
            node.right = removeHelper(node.right, succ.index); // 
        }
        return node;
    }

    private BSTNode findMin(BSTNode node) { // find the in-order sucessor by going left all the way
        while (node.left != null) {
            node = node.left;
        } 
        return node;
    }


    /**
     * Updates a node's data with a new value, given its index.
     */
    public void updateNode(I _index, T _newData) throws IllegalArgumentException {
        BSTNode nodeToUpdate = searchNode(_index);
        if (nodeToUpdate == null) {
            throw new IllegalArgumentException("updateNode(I _index, T _newData): No node with an index "
            + _index.toString() + " in the BST");
        } else {
            nodeToUpdate.setData(_newData);
        }
    }

    
/************************************ GRADING CODE (DO NOT MODIFY) ************************************ */
    /**
     * Performs a pre-order traversal of the BST.
     */
    private void preOrderTraversal(BSTNode node, int[] idx, String[] arr, boolean dataFlag) {
        // DO NOT CHANGE THIS. THIS FOR TESTING PURPOSES
        if(node == null)
            return;

        if(dataFlag)
            arr[idx[0]] = String.valueOf(node.getData());
        else
            arr[idx[0]] = String.valueOf(node.getIndex());
        idx[0]++;
        
        preOrderTraversal(node.left, idx, arr, dataFlag);
        preOrderTraversal(node.right, idx, arr, dataFlag);
    }

    /**
     * Returns an array of data values in pre-order traversal order.
     * @return A String array containing the data values of all nodes in pre-order order
     */
    public String[] getDataArray() {
        /// DO NOT CHANGE THIS. THIS FOR TESTING PURPOSES
        String[] dataArr = new String[size];
        preOrderTraversal(this.root, new int[1], dataArr, true);
        return dataArr;
    }

    /**
     * Returns an array of index values in pre-order traversal order.
     * @return A String array containing the index values of all nodes in pre-order order
     */
    public String[] getIndexArray() {
        // DO NOT CHANGE THIS. THIS FOR TESTING PURPOSES
        String[] indexArr = new String[size];
        preOrderTraversal(this.root, new int[1], indexArr, false);
        return indexArr;
    }

/****************************************************************************************************** */
}