public class DebugPractice {    public static void main(String[] args) {
    int[] numbers = {5, 3, 8, 6, 2, 1};
    int max = findMax(numbers);
    System.out.println("Max number: " + max);        String text = null;
    printTextLength(text);        int factorialOf = 5;
    int fact = factorial(factorialOf);
    System.out.println("Factorial of " + factorialOf + " is: " + fact);        runLoop();
}    // Bug 1: Off-by-one error
    public static int findMax(int[] arr) {
        int max = arr[0];
        for (int i = 0; i <= arr.length; i++) { // Should be i < arr.length
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }    // Bug 2: NullPointerException
    public static void printTextLength(String str) {
        System.out.println("Length of string: " + str.length()); // str might be null
    }    // Bug 3: Logic error (factorial is incorrect for input > 1)
    public static int factorial(int n) {
        int result = 1;
        for (int i = 1; i <= n; i--) { // Should be i++
            result *= i;
        }
        return result;
    }    // Bug 4: Infinite loop candidate
    public static void runLoop() {
        int count = 0;
        while (count != 5) { // This loop never increments count
            System.out.println("Count is: " + count);
        }
    }
}