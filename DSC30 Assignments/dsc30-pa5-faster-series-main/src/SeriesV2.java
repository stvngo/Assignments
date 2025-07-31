public class SeriesV2<T> implements Series<T>{

    private LL<T> seriesData;
    private BST<String, T> seriesDataBST;

    public SeriesV2(String[] _rowNames, T[] _data) {
        if (_data == null) { // Exception for null _data
            throw new NullPointerException(
                    "Series(String[] _index, T[] _data): " +
                            "_data can't be null. Terminating the program"
            );
        }

        this.seriesData = new LL<T>();
        this.seriesDataBST = new BST<>();

        String[] rowNamesCopy = new String[_data.length];
        try {
            if (_rowNames == null) {
                throw new NullPointerException();
            }
            if (_data.length != _rowNames.length) { // Exception for inconsistent lengths
                throw new IllegalArgumentException(
                        "Series(String[] _index, T[] _data): " +
                            "the length of _index and _data must be the same"
                );
            }
            for (int i = 0; i < _data.length; i++) {
                if (_rowNames[i] == null) { // exception for element specific null value
                    throw new IllegalArgumentException(
                            "Series(String[] _index, T[] _data): " +
                                "_rowNames is not valid"
                        );
                }
                rowNamesCopy[i] = _rowNames[i];
            }
        } catch (NullPointerException npe) {
            for (int i = 0; i < _data.length; i++) {
                rowNamesCopy[i] = Integer.toString(i);
            }
        }

        for (int i = 0; i < _data.length; i++) {
            this.seriesData.appendNode(rowNamesCopy[i], _data[i]);
            this.seriesDataBST.addNode(rowNamesCopy[i], _data[i]);
        }

    }

    public String toString() {
        return "print the series" + 
            this.seriesData.toString().substring(21);
    }

    public int getLength() {
        return this.seriesData.getLength();
    }

    public String[] getRowNames() {
        return this.seriesData.getIndexArray();
    }

    public String[] getData() {
        return this.seriesData.getDataArray();
    }

    public void append(String rn, T d) {
    //     String newIdx = Integer.toString(this.seriesDataBST.getSize());
    //     if (rn == null || rn.isEmpty()) {
    //         this.seriesDataBST.addNode(newIdx, d);
    //         this.seriesData.appendNode(newIdx, d);
    //     } else {
    //         this.seriesDataBST.addNode(rn, d);
    //         this.seriesData.appendNode(rn, d);
    //     }
    // }
        // Let the LL handle null/empty and give us back a node
        seriesData.appendNode(rn, d);
        // Fetch the *actual* index string it assigned (always the last one)
        String[] allIdx = seriesData.getIndexArray();
        String realKey = allIdx[allIdx.length - 1];
        // Now insert into the BST with exactly that key
        seriesDataBST.addNode(realKey, d);
    }

    public T loc(String rn) throws NullPointerException, IllegalArgumentException {
        if (rn == null) {
            throw new NullPointerException("loc(String rn): rn can't be null");
        }
        if (rn.isEmpty()) {
            throw new IllegalArgumentException("loc(String rn): rn can't be an empty string");
        }
        // LL<T>.LLNode node = this.seriesData.searchNode(rn); // old searchNode using LL
        BST<String, T>.BSTNode node = this.seriesDataBST.searchNode(rn);
        if (node == null) {
            return null;
        }
        return node.getData();
    }

    public T[] loc(String[] rn) throws NullPointerException, IllegalArgumentException {
        if (rn == null) {
            throw new NullPointerException(
                    "loc(String[] rn): rn[] can't be null"
            );
        }
        if (rn.length == 0) {
            throw new IllegalArgumentException(
                    "loc(String[] rn): rn[] can't be an empty array"
            );
        }
        T[] output = (T[]) new Object[rn.length];
        for (int i = 0; i < rn.length; i++) {
            output[i] = this.loc(rn[i]);
        }
        return output;
    }

    public T iloc(int ind) {
        try {
            String[] rowNames = this.seriesData.getIndexArray();
            return this.loc(rowNames[ind]); 
        } catch (IndexOutOfBoundsException e) {
            System.out.println("the index " + ind + " is not valid.. returning null");
            return null;
        }
    }

    public boolean drop(String rn) throws NullPointerException, IllegalArgumentException {
        if (rn == null) {
            throw new NullPointerException("drop(String rn): rn can't be null");
        }

        if (rn.isEmpty()) {
            throw new IllegalArgumentException("drop(String rn): rn can't be an empty String");
        }

        // if (this.seriesData.searchNode(rn) == null) { // old searchNode using LL
        //     return false;
        // } else {
        //     this.seriesData.removeNode(rn);
        //     return true;
        // }

        if (this.seriesDataBST.searchNode(rn) == null) { // new searchNode using BST
            return false;
        } else {
            this.seriesData.removeNode(rn);
            this.seriesDataBST.removeNode(rn);
            return true;
        }
    }

    public void fillNull(T value) throws IllegalArgumentException {
        if (value == null) {
            throw new IllegalArgumentException("fillNull(T value): value can't be null");
        }
        String[] indexArray = this.seriesData.getIndexArray();
        for (int i = 0; i < this.seriesData.getLength(); i++) {
            if (this.loc(indexArray[i]) == null) {
                this.seriesData.updateNode(indexArray[i], value);
                this.seriesDataBST.updateNode(indexArray[i], value);
            }
        }
    }
}
