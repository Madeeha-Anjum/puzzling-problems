/*
Array "nums" -> length 2n elements -> [x1,x2,...,xn,y1,y2,...,yn]
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
*/

public class Solutions {

    public static int[] shuffle(int[] nums, int n) {
        int[] x = new int[n];
        int[] y = new int[n];
        int[] result = new int[nums.length];

        // split the arrays into two different arrays
        for (int i = 0; i < n; i++) {
            x[i] = nums[i];
        }

        for (int j = n; j < nums.length; j++) {
            y[j - n] = nums[j];
        }

        // Combine the array
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            result[i] = x[index];

            i = i + 1;
            result[i] = y[index];
            index++;

        }

        return result;

    }

    public static void main(String[] args) {
        // Solutions className = new Solutions();
        int[] myNumsArray = { 2, 5, 1, 3, 4, 7 };
        int n = 3;
        Solutions.shuffle(myNumsArray, n);

    }

}
