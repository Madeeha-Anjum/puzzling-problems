
public class fractions {
    static int den3, num3;

    public static String[] addingFractions(String[] fractions) {

        String[] frac = fractions[1].split("\\+");
        String[] first = frac[0].split("/");
        int fac1 = Integer.parseInt(first[0]) / Integer.parseInt(first[1]);
        String[] second = frac[1].split("/");
        int fac2 = Integer.parseInt(second[0]) / Integer.parseInt(second[1]);

        addFraction(fac1, fac2);
        return fractions;
    }

    // Function to return gcd of a and b
    static int gcd(int a, int b) {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }

    // Function to add two fractions
    static void addFraction(int num1, int den1, int num2, int den2) {
        den3 = gcd(den1, den2);
        den3 = (den1 * den2) / den3;
        num3 = (num1) * (den3 / den1) + (num2) * (den3 / den2);
        lowest();
    }

    static void lowest() {
        int common_factor = gcd(num3, den3);
        den3 = den3 / common_factor;
        num3 = num3 / common_factor;
    }

    public static void main(String[] args) {
        String[] xxx = { "2/6+2/6", "7/10+13/10" };
        addingFractions(xxx);

    }
}
