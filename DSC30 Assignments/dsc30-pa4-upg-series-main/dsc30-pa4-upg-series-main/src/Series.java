public class Series<T> {

     /**
      * Linked-List containing row names and data of the series.
      */
     private LL<T> seriesData;

     /**
      * Constructs a new Series object.
      *
      * @param _rowNames an array of row names
      * @param _data     an array of T data
      */
     public Series(String[] _rowNames, T[] _data) {
          if (_data == null) { // Exception for null _data
               throw new NullPointerException(
                       "Series(String[] _index, T[] _data): " +
                               "_data can't be null. Terminating the program"
               );
          }

          this.seriesData = new LL<T>();

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

          for (int i = 0; i< _data.length; i++) {
               this.seriesData.appendNode(rowNamesCopy[i], _data[i]);
          }

     }

     /**
      * Returns a string representation of the Series object.
      */
     public String toString() {
          return this.seriesData.toString();
     }

     /**
      * Returns the length of the series object.
      */
     public int getLength() {
          return this.seriesData.getLength();
     }

     /**
      * Returns the row names of this Series object.
      */
     public String[] getRowNames() {
          return this.seriesData.getIndexArray();
     }

     /**
      * Returns the data of this Series object as strings.
      */
     public String[] getData() {
          return this.seriesData.getDataArray();
     }

     /**
      * Adds a new pair of rowName and data at the end of the Series object.
      *
      * @param rn the row name to be added
      * @param d  the T data value to be added
      */
     public void append(String rn, T d) {
          this.seriesData.appendNode(rn, d);
     }

     /**
      * Retrieves a data value given a row name.
      *
      * @param rn the row name to search for
      */
     public T loc(String rn) throws NullPointerException, IllegalArgumentException {
          if (rn == null) {
               throw new NullPointerException("loc(String rn): rn can't be null");
          }
          if (rn.isEmpty()) {
               throw new IllegalArgumentException("loc(String rn): rn can't be an empty string");
          }
          LL<T>.LLNode node = this.seriesData.searchNode(rn);
          if (node == null) {
               return null;
          }
          return node.getData();
     }

     /**
      * Retrieves multiple data values given an array of row names.
      *
      * @param rn an array of row names to search for
      */
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

     /**
      * Retrieves a data value based on its integer index.
      *
      * @param ind the index of the data to retrieve
      */
     public T iloc(int ind) {
          try {
               String[] rowNames = this.seriesData.getIndexArray();
               return this.loc(rowNames[ind]); 
          } catch (IndexOutOfBoundsException e) {
               System.out.println("the index " + ind + " is not valid.. returning null");
               return null;
          }
     }

     /**
      * Removes a pair of rowname-data from the Series, given a row name.
      *
      * @param rn the row name of the pair to be removed
      */
     public boolean drop(String rn) throws NullPointerException, IllegalArgumentException {
          if (rn == null) {
               throw new NullPointerException("drop(String rn): rn can't be null");
          }

          if (rn.isEmpty()) {
               throw new IllegalArgumentException("drop(String rn): rn can't be an empty String");
          }

          if (this.seriesData.searchNode(rn) == null) {
               return false;
          } else {
               this.seriesData.removeNode(rn);
               return true;
          }
     }

     /**
      * Replace any data value that is null with value.
      *
      * @param value the new value to replace null values
      */
     public void fillNull(T value) throws IllegalArgumentException {
          if (value == null) {
               throw new IllegalArgumentException("fillNull(T value): value can't be null");
          }
          String[] indexArray = this.seriesData.getIndexArray();
          for (int i = 0; i < this.seriesData.getLength(); i++) {
               if (this.loc(indexArray[i]) == null) {
                    this.seriesData.updateNode(indexArray[i], value);
               }
          }
     }
}