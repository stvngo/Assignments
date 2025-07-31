public class Tool {

    /**
     * Calculates the mean of a Series object.
     *
     * @param d the Series object to calculate the mean from
     */
    public static Integer mean(Series d) throws NullPointerException, IllegalArgumentException,
            ArithmeticException {

        if (d == null) {
            throw new NullPointerException("mean (Series d): d can't be null");
        }
        if (d.getLength() == 0) {
            throw new IllegalArgumentException("mean (Series d): d can't be an empty Series");
        }
        int sum = 0;
        int count = 0; // count only non-null entries
        for (int i = 0; i < d.getLength(); i++) {
            try {
                if (d.iloc(i) == null) {
                    throw new NullPointerException();
                }
                sum += d.iloc(i);
                count++; // if all null, it will throw AE because division by count 0
            } catch (NullPointerException npe) {
                // skip any null data entries
            }
        }
        return Math.floorDiv(sum, count);
    }

    /**
     * Finds the maximum value in a Series object.
     *
     * @param d the Series object to find the maximum value from
     */
    public static Integer max(Series d) throws NullPointerException, IllegalArgumentException,
            ArithmeticException {

        if (d == null) {
            throw new NullPointerException("max (Series d): d can't be null");
        }
        if (d.getLength() == 0) {
            throw new IllegalArgumentException("max (Series d): d can't be an empty Series");
        }

        Integer maxNum = null;
        for (int i = 0; i < d.getLength(); i++) {
            try {
                Integer temp = d.iloc(i);
                if (temp == null) {
                    throw new NullPointerException();
                }
                if (maxNum == null || temp > maxNum) { // maxNum == null for the first element only
                    maxNum = temp;
                }
            } catch (NullPointerException npe) {
                // skip any null data entries
            }
        }
        if (maxNum == null) {
            throw new ArithmeticException();
        }
        return maxNum;
    }
}
