class Solution {

    public static int[] getConcatenation(int[] nums) {
        int n = nums.length;

        // create an array of 2n
        int[] anArray = new int[2*n];

        for (int i = 0; i < nums.length; i++) {
            anArray[i] = nums[i];
            anArray[i + n] = nums[i];

        }

        // return an array of ints
        // for (int i = 0; i < anArray.length; i++) {
        //     System.out.print(anArray[i]);            
        // }
        return anArray;
    }

    public static void main(String[] args) {
        int[] anArrayOfNums = { 1, 2, 1 };
        // Solution ans = new Solution();
        getConcatenation(anArrayOfNums);

    }
}