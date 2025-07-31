public class DataFrame {
    private HashTable<SeriesV2<Object>> tabularData;
    private int numRows;
    private int numCols;

    public DataFrame() {
        this.tabularData = new HashTable<>();
        this.numRows = 0;
        this.numCols = 0;
    }

    public DataFrame(String _k, SeriesV2<Object> _series) {
        this.tabularData = new HashTable<>();
        this.tabularData.insert(_k, _series);
        this.numRows = _series.getLength();
        this.numCols = 1;
    }

    public SeriesV2<Object> colLoc(String k) {
        return tabularData.lookup(k);
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("printing the dataframe ...\n");
        sb.append("==================\n");
        
        String[] validKeys = tabularData.getValidKeys();
        
        for (String key : validKeys) {
            sb.append("[colName:\t").append(key).append("]\n");
            SeriesV2<Object> series = tabularData.lookup(key);
            if (series != null) {
                sb.append(series.toString()).append("\n");
            }
        }
        
        return sb.toString();
    }

    public int getNumRows() {
        return this.numRows;
    }

    public int getNumCols() {
        return this.numCols;
    }

    public String[] getColNames() {
        String[] validKeys = tabularData.getValidKeys();
        String[] copy = new String[validKeys.length];
        
        for (int i = 0; i < validKeys.length; i++) {
            copy[i] = new String(validKeys[i]);
        }
        
        return copy;
    }

    public void addColumn(String k, SeriesV2<Object> s) throws IllegalArgumentException {
        if (numCols >  0 && s.getLength() != numRows) {
            throw new IllegalArgumentException("addColumn(String k, SeriesV2<Object> s):" +
            " the length of s does not match the dataframe's # of rows");
        }
        this.tabularData.insert(k, s);

        if (this.numCols == 0) {
            this.numRows = s.getLength();
        }
        numCols = this.tabularData.getSize();
    }

    public void removeColumn(String k) {
        this.tabularData.delete(k);
        this.numCols = this.tabularData.getSize();

        if (this.numCols == 0) {
            this.numRows = 0;
        }
    }
}
