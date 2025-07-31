public class Series {

     /** Row names of the series. */
     private String[] rowNames;
 
     /** The Integer array that contains the list of data that constitutes a Series object. */
     private Integer[] data;
 
     /**
      * Constructs a new Series object.
      *
      * @param _rowNames an array of row names
      * @param _data an array of Integer data
      */
     public Series(String[] _rowNames, Integer[] _data) {
          if (_data == null) { // Exception for null _data
               throw new NullPointerException(
                       "Series(String[] _index, Integer[] _data): " +
                       "_data can't be null. Terminating the program"
               );
          }

          this.data = new Integer[_data.length];
          for (int i = 0; i < _data.length; i++) {
               this.data[i] = _data[i];
          }

          String[] rowNamesCopy = new String[_data.length];
          try {
               if (_rowNames == null) {
                    throw new NullPointerException();
               }
               if (_data.length != _rowNames.length) { // Exception for inconsistent lengths
                    throw new IllegalArgumentException(
                            "Series(String[] _index, Integer[] _data): " +
                            "the length of _index and _data must be the same"
                    );
               }
               for (int i = 0; i < _data.length; i++) {
                    if (_rowNames[i] == null) { // exception for element specific null value
                         throw new IllegalArgumentException(
                                 "Series(String[] _index, Integer[] _data): " +
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

          this.rowNames = rowNamesCopy;
     }
 
     /**
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
      * Returns the length of the series object.
      */
     public int getLength() {
          return this.data.length;
     }
 
     /**
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
      * Adds a new pair of rowName and data at the end of the Series object.
      *
      * @param rn the row name to be added
      * @param d the Integer data value to be added
      */
     public void append(String rn, Integer d) {
          // local variables to create
          String defaultRowName;
          int oldLength = this.data.length;
          String[] newRowNames = new String[oldLength + 1];
          Integer[] newData = new Integer[oldLength + 1];

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
      * Retrieves a data value given a row name.
      *
      * @param rn the row name to search for
      */
     public Integer loc(String rn) throws NullPointerException, IllegalArgumentException {
          if (rn == null) {
               throw new NullPointerException("loc(String rn): rn can't be null");
          }
          if (rn.isEmpty()) {
               throw new IllegalArgumentException("loc(String rn): rn can't be an empty string");
          }
          for (int i = 0; i < this.rowNames.length; i++) {
               if (this.rowNames[i].equals(rn)) {
                    return this.data[i];
               }
          }
          return null;
     }
 
     /**
      * Retrieves multiple data values given an array of row names.
      *
      * @param rn an array of row names to search for
      */
     public Integer[] loc(String[] rn) throws NullPointerException, IllegalArgumentException {
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
          Integer[] output = new Integer[rn.length];
          for (int i = 0; i < rn.length; i++) {
               output[i] = loc(rn[i]);
          }
          return output;
     }
 
     /**
      * Retrieves a data value based on its integer index.
      *
      * @param ind the index of the data to retrieve
      */
     public Integer iloc(int ind) {
          try {
               return this.data[ind];
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

          String[] newRowNames = new String[this.rowNames.length - 1];
          Integer[] newData = new Integer[this.data.length - 1];
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
 
     /**
      * Replace any data value that is null with value.
      *
      * @param value the new value to replace null values
      */
     public void fillNull(Integer value) throws IllegalArgumentException {
          if (value == null) {
               throw new IllegalArgumentException("fillNull(T value): value can't be null");
          }
          for (int i = 0; i < this.data.length; i++) {
               if (this.data[i] == null) {
                   this.data[i] = value;
               }
          }
     }
 
     /**
      * Replace any data value that is null with the mean of the Series.
      *
      */
     public void fillNullWithMean() throws IllegalArgumentException {
          Integer meanVal = null;
          try {
               meanVal = Tool.mean(this);
               fillNull(meanVal);
          } catch (ArithmeticException ae) {
               fillNull(meanVal);
          } catch (NullPointerException npe) {
               fillNull(meanVal);
          } catch (IllegalArgumentException iae) {
               fillNull(meanVal);
          }
     }
 }