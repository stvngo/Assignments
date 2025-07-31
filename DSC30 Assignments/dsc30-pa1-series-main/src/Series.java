public class Series {

    /**
     * Row names of the series.
     */
    private String[] rowNames;

    /**
     * The integer array that contains the list of data that constitutes a Series object.
     */
    private int[] data;

    /**
     * Constructs a new Series object.
     *
     * @param _rowNames an array of row names
     * @param _data     an array of int data
     */
    public Series(String[] _rowNames, int[] _data) {

        // initialize data instance variable
        this.data = _data;

        String[] rowNamesCopy = new String[_data.length];

        // initializes rowNames instance variable with a copy
        // using index numbers as the default row names if _rowNames is null
        // using index numbers for some row names if specific rowNames are null
        if (_rowNames == null) {
            for (int i = 0; i < _data.length; i++) {
                rowNamesCopy[i] = Integer.toString(i);
            }
        } else {
            for (int i = 0; i < _data.length; i++) {
                if (_rowNames[i] == null) {
                    rowNamesCopy[i] = Integer.toString(i);
                    // alternatively String.valueOf(i)
                } else { // else-use input rowNames as row names
                    rowNamesCopy[i] = _rowNames[i];
                }
            }
        }

        this.rowNames = rowNamesCopy;
    }

    /**
     * Method: toString
     * Returns a string representation of the Series object.
     */
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("Printing Series...\n\n");
        for (int i = 0; i < this.data.length; i++) {
            s.append(this.rowNames[i]).append("\t").append(this.data[i]).append("\n");
        }
        return s.toString();
    }

    /**
     * Method: getLength
     * Returns the length of the series object.
     */
    public int getLength() {
        return this.data.length;
    }

    /**
     * Method: getRowNames
     * Returns the row names of this Series object.
     */
    public String[] getRowNames() {
        String[] copy = new String[this.rowNames.length];
        for (int i = 0; i < this.rowNames.length; i++) {
            copy[i] = this.rowNames[i];
        }
        return copy;
    }

    /**
     * Method: getData
     * Returns the data of this Series object as strings.
     */
    public String[] getData() {
        String[] dataStrings = new String[this.data.length];
        for (int i = 0; i < this.data.length; i++) {
            dataStrings[i] = Integer.toString(this.data[i]);
        }
        return dataStrings;
    }

    /**
     * Method: append
     * Adds a new pair of rowName and data at the end of the Series object.
     *
     * @param rn the row name to be added
     * @param d  the data value to be added
     */
    public void append(String rn, int d) {
        // local variables to create
        String defaultRowName;
        int oldLength = this.data.length;
        String[] newRowNames = new String[oldLength + 1];
        int[] newData = new int[oldLength + 1];

        // fill in new arrays with old rowNames and data
        for (int i = 0; i < oldLength; i++) {
            newRowNames[i] = this.rowNames[i];
            newData[i] = this.data[i];
        }

        // add input rowNames and data to the end of the Series object
        if (rn == null || rn.isEmpty()) {
            defaultRowName = Integer.toString(oldLength);
            newRowNames[oldLength] = defaultRowName;
        } else {
            newRowNames[oldLength] = rn;
        }
        newData[oldLength] = d;

        // reinitialize instance variables
        this.rowNames = newRowNames;
        this.data = newData;
    }

    /**
     * Method: loc (single)
     * Retrieves a data value given a row name.
     *
     * @param rn the row name to search for
     */
    public int loc(String rn) {
        for (int i = 0; i < this.rowNames.length; i++) {
            if (this.rowNames[i].equals(rn)) {
                return this.data[i];
                // return the data at the same index as rowName
                // element if the rn is found in rowNames
            }
        }
        return -1;
    }

    /**
     * Method: loc (multiple)
     * Retrieves multiple data values given an array of row names.
     *
     * @param rn an array of row names to search for
     */
    public int[] loc(String[] rn) {
        if (rn == null) {
            return null;
        }

        int[] output = new int[rn.length];
        for (int i = 0; i < rn.length; i++) {
            output[i] = loc(rn[i]);
        }

        return output;
    }

    /**
     * Method: iloc
     * Retrieves a data value based on its integer index.
     *
     * @param ind the index of the data to retrieve
     */
    public int iloc(int ind) {
        if (ind < 0 || ind >= this.data.length) {
            return -1;
        }
        return this.data[ind];
    }

    /**
     * Method: drop
     * Removes a pair of rowname-data from the Series, given a row name.
     *
     * @param rn the row name of the pair to be removed
     */
    public boolean drop(String rn) {

        int indexToRemove = -1;

        for (int i = 0; i < this.rowNames.length; i++) {
            if (this.rowNames[i].equals(rn)) {
                indexToRemove = i;
                break;
            }
        }

        if (indexToRemove == -1) {
            return false;
        }

        // create shrunken arrays
        String[] newRowNames = new String[this.rowNames.length - 1];
        int[] newData = new int[this.data.length - 1];
        int newIndex = 0;

        for (int i = 0; i < this.rowNames.length; i++) {
            if (i != indexToRemove) {
                newData[newIndex] = this.data[i];
                newRowNames[newIndex] = this.rowNames[i];
                newIndex++;
            }
        }

        this.data = newData;
        this.rowNames = newRowNames;
        return true;
    }
}