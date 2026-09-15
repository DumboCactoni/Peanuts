/**
 * TypeCasting.java
 *
 * Exercise 4: Type Casting Primitive Types
 *
 * This exercise follows Lecture 2 (Variables). Each method below makes you
 * convert a value from one primitive type to another. Some conversions are
 * WIDENING (implicit -- Java does it for you), and some are NARROWING
 * (explicit -- you have to write the cast yourself, like (int) d).
 *
 * Quick reminder from the lecture:
 *
 *   Widening (implicit)            Narrowing (explicit)
 *   int n = 3;                     double d = 3.14;
 *   double d = n;    // 3.0        int n = (int) d;    // 3
 *
 *   boolean cannot be cast to or from ANY other primitive type.
 *
 * Fill in the method bodies below wherever you see a TODO. Do not change
 * the method signatures (name, parameter types, or return type) -- main()
 * calls these methods exactly as they are declared.
 *
 * To compile and run:
 *   javac TypeCasting.java
 *   java TypeCasting
 */
public class TypeCasting {

    // ------------------------------------------------------------------
    // Part 1: Widening (implicit) casts
    // ------------------------------------------------------------------

    /**
     * Returns the Unicode/ASCII code of the character c.
     *
     * Remember: a char is really a 16-bit unsigned integer.
     *   A-Z are 65-90, a-z are 97-122, 0-9 are 48-57.
     *
     * Example:
     *   charToCode('A') -> 65
     *   charToCode('a') -> 97
     *   charToCode('7') -> 55
     *
     * @param c the character to convert
     * @return the integer code of c
     */
    public static int charToCode(char c) {
        // TODO 1: replace the line below with your implementation
        int num = c;
        return num;
    }

    // ------------------------------------------------------------------
    // Part 2: Narrowing (explicit) casts
    // ------------------------------------------------------------------

    /**
     * Returns d with everything after the decimal point chopped off.
     *
     * Casting a double to an int does NOT round -- it truncates (drops the
     * decimal part), which moves the number toward zero.
     *
     * Example:
     *   truncate(3.14)  -> 3
     *   truncate(9.99)  -> 9
     *   truncate(-2.7)  -> -2
     *
     * @param d the number to truncate
     * @return d without its decimal part
     */
    public static int truncate(double d) {
        // TODO 2: replace the line below with your implementation
        int num = (int)d;
        return num;
    }

    /**
     * Returns the character whose code is the given number.
     *
     * An int variable cannot be stored in a char without a cast, because an
     * int (32 bits) is bigger than a char (16 bits).
     *
     * Example:
     *   codeToChar(97) -> 'a'
     *   codeToChar(90) -> 'Z'
     *   codeToChar(48) -> '0'
     *
     * @param code a character code between 0 and 65535
     * @return the character with that code
     */
    public static char codeToChar(int code) {
        // TODO 3: replace the line below with your implementation
        char ans = (char)code;
        return ans;
    }

    /**
     * Casts an int down to a byte.
     *
     * A byte only has 8 bits (-128 to 127). When you cast a bigger integer
     * to a byte, Java keeps only the lowest 8 bits and throws the rest away.
     * If the value doesn't fit, the leftover bits are read using two's
     * complement, so the result can "wrap around" and even change sign.
     *
     *   200 in binary is  0000 0000 1100 1000
     *   keep lowest 8:              1100 1000  -> sign bit is 1 -> -56
     *
     * Example:
     *   toByte(100)  -> 100
     *   toByte(200)  -> -56
     *   toByte(128)  -> -128
     *   toByte(-129) -> 127
     *
     * @param n the int to cast
     * @return n cast to a byte
     */
    public static byte toByte(int n) {
        // TODO 4: replace the line below with your implementation
        byte bytes = (byte)n;
        return bytes;
    }

    /**
     * Casts a double down to a float.
     *
     * A float has about 7 digits of precision and a double has about 15, so
     * a double with lots of digits loses some of them when cast to a float.
     *
     * Example:
     *   toFloat(9.8)              -> 9.8
     *   toFloat(3.14159265358979) -> 3.1415927
     *
     * @param d the double to cast
     * @return d cast to a float
     */
    public static float toFloat(double d) {
        // TODO 5: replace the line below with your implementation
        float ans = (float)d;
        return ans;
    }

    // ------------------------------------------------------------------
    // Part 3: Types that can't be cast
    // ------------------------------------------------------------------

    /**
     * Returns 1 if b is true and 0 if b is false.
     *
     * Careful: (int) b does NOT compile -- boolean cannot be cast to any
     * other primitive type. You'll have to find another way.
     *
     * Example:
     *   boolToInt(true)  -> 1
     *   boolToInt(false) -> 0
     *
     * @param b the boolean to convert
     * @return 1 for true, 0 for false
     */
    public static int boolToInt(boolean b) {
        // TODO 6: replace the line below with your implementation
        if (b) {
            return 1;
        } else {
            return 0;
        }
    }

    // ------------------------------------------------------------------
    // Everything below this line is the self-grading test harness.
    // You do not need to write or edit any of it -- just implement the
    // TODOs above and run this file to see how you did.
    // ------------------------------------------------------------------

    private static int passCount = 0;
    private static int failCount = 0;

    public static void main(String[] args) {
        System.out.println("Running tests for TypeCasting.java...\n");

        // charToCode()
        check("charToCode('A')", 65, charToCode('A'));
        check("charToCode('a')", 97, charToCode('a'));
        check("charToCode('7')", 55, charToCode('7'));

        // truncate()
        check("truncate(3.14)", 3, truncate(3.14));
        check("truncate(9.99)", 9, truncate(9.99));
        check("truncate(-2.7)", -2, truncate(-2.7));

        // codeToChar()
        check("codeToChar(97)", 'a', codeToChar(97));
        check("codeToChar(90)", 'Z', codeToChar(90));
        check("codeToChar(48)", '0', codeToChar(48));

        // toByte()
        check("toByte(100)", (byte) 100, toByte(100));
        check("toByte(200)", (byte) -56, toByte(200));
        check("toByte(128)", (byte) -128, toByte(128));
        check("toByte(-129)", (byte) 127, toByte(-129));

        // toFloat()
        check("toFloat(9.8)", 9.8f, toFloat(9.8));
        check("toFloat(3.14159265358979)", 3.1415927f, toFloat(3.14159265358979));

        // boolToInt()
        check("boolToInt(true)", 1, boolToInt(true));
        check("boolToInt(false)", 0, boolToInt(false));

        int total = passCount + failCount;
        System.out.println("\n----------------------------------------");
        System.out.println("Score: " + passCount + " / " + total + " test cases correct");
        if (failCount == 0) {
            System.out.println("All tests passed! Nice work.");
        } else {
            System.out.println("Some tests failed -- check the [FAIL] lines above.");
        }
    }

    /**
     * Compares the expected and actual results of one test case and prints
     * a [PASS] or [FAIL] line that always shows what the correct output
     * should be and what your code actually produced. char values are shown
     * in single quotes so you can tell 'a' apart from a blank space.
     *
     * Example:
     *   check("truncate(3.14)", 3, 3) prints:
     *     [PASS] truncate(3.14) -> expected: 3, your output: 3
     *   check("truncate(3.14)", 3, 0) prints:
     *     [FAIL] truncate(3.14) -> expected: 3, your output: 0
     *
     * @param testName a short description of the test, e.g. "truncate(3.14)"
     * @param expected the correct/expected result
     * @param actual   the value actually returned by your method
     */
    private static void check(String testName, Object expected, Object actual) {
        boolean passed = expected.equals(actual);
        String label = passed ? "[PASS] " : "[FAIL] ";
        System.out.println(label + testName
                + " -> expected: " + show(expected) + ", your output: " + show(actual));
        if (passed) {
            passCount++;
        } else {
            failCount++;
        }
    }

    /**
     * Returns a printable version of a test value: chars are wrapped in
     * single quotes, everything else is printed normally.
     *
     * @param value the value to display
     * @return the text to print for that value
     */
    private static String show(Object value) {
        if (value instanceof Character) {
            return "'" + value + "'";
        }
        return String.valueOf(value);
    }
}
