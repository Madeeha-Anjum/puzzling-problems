/**
 * Solutions
 */
public class Solutions {

    public static boolean arrayStringsAreEqual(String[] word1array, String[] word2array) {
        // Combine Array to word
        String word1 = "";
        for (String i : word1array) {
            word1 = word1 + i;
        }
        String word2 = "";
        for (String i : word2array) {
            word2 = word2 + i;
        }
        return word1.equals(word2);
    }

    public static void main(String[] args) {
        // Array of strings
        String[] word1 = { "ab", "c" };
        String[] word2 = { "a", "bc" };
        Solutions.arrayStringsAreEqual(word1, word2);
    }
}