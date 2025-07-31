public class RuntimeAnalysis {
    public static void main(String[] args) {
        // Number of elements to insert
        int n = 100_000;
        String[] rowNames = new String[n];
        Double[] data = new Double[n];
        for (int i = 0; i < n; i++) {
            rowNames[i] = "key" + i;
            data[i] = (double) i;
        }

        // Build both series implementations
        SeriesV1<Double> v1 = new SeriesV1<>(rowNames, data);
        SeriesV2<Double> v2 = new SeriesV2<>(rowNames, data);

        // Prepare random queries
        int m = 100_000;
        java.util.Random rand = new java.util.Random(12345);
        String[] queries = new String[m];
        for (int i = 0; i < m; i++) {
            queries[i] = "key" + rand.nextInt(n);
        }

        // Measure SeriesV1 (linked-list) lookups
        long start1 = System.nanoTime();
        for (String q : queries) {
            v1.loc(q);
        }
        long end1 = System.nanoTime();

        // Measure SeriesV2 (BST lookup) lookups
        long start2 = System.nanoTime();
        for (String q : queries) {
            v2.loc(q);
        }
        long end2 = System.nanoTime();

        double timeV1 = (end1 - start1) / 1_000_000.0;
        double timeV2 = (end2 - start2) / 1_000_000.0;

        System.out.printf("SeriesV1 (LL) search time: %.2f ms\n", timeV1);
        System.out.printf("SeriesV2 (BST) search time: %.2f ms\n", timeV2);
    }
}
