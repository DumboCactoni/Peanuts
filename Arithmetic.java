/**
 * Arithmetic.java
 *
 * Exercise 5: Arithmetic Operators on Primitive Types
 *
 * This exercise follows Lecture 3 (Arithmetic Operators). Each method below
 * uses the arithmetic operators (+ - * / %), the increment/decrement
 * operators (++ --), or compound assignment (+= -= *= /= %=), and each one
 * hides a trap from the lecture: integer division, negative modulus,
 * operator precedence, pre- vs post-increment, char math, type promotion,
 * or overflow.
 *
 * Quick reminder from the lecture:
 *
 *   int / int drops the decimal       10 / 4     -> 2      10 / 4.0 -> 2.5
 *   % keeps the sign of the LEFT side -10 % 3    -> -1     10 % -3  -> 1
 *   a % b is the same as              a - (a / b) * b
 *   * / % happen before + -           2 + 3 * 4  -> 14
 *   a++ gives the OLD value of a,     ++a gives the NEW value of a
 *
 *   Type promotion:  byte/short/char -> int -> long -> float -> double
 *   byte + byte is an int, so  byte r = b1 + b2;  does NOT compile,
 *   but  b1 += b2;  does (compound assignment casts for you).
 *
 * Fill in the method bodies below wherever you see a TODO. Do not change
 * the method signatures (name, parameter types, or return type) -- main()
 * calls these methods exactly as they are declared.
 *
 * To compile and run:
 *   javac Arithmetic.java
 *   java Arithmetic
 */
public class Arithmetic {

    // ------------------------------------------------------------------
    // Part 1: Integer division and modulus
    // ------------------------------------------------------------------

    /**
     * Returns the sum of the three digits of a three-digit number.
     *
     * Use / and % to pull the digits apart:
     *   n / 100       -> the hundreds digit
     *   n / 10 % 10   -> the tens digit
     *   n % 10        -> the ones digit
     *
     * Example:
     *   sumOfDigits(123) -> 6    (1 + 2 + 3)
     *   sumOfDigits(907) -> 16   (9 + 0 + 7)
     *   sumOfDigits(500) -> 5    (5 + 0 + 0)
     *
     * @param n a positive number between 100 and 999
     * @return the sum of n's digits
     */
    public static int sumOfDigits(int n) {
        // TODO 1: replace the line below with your implementation
        int digitsum = n%10+n/10%10+n/100; return digitsum;
    }

    /**
     * Returns the remainder of a divided by b, WITHOUT using the % operator.
     *
     * Use the formula from the lecture:  a % b = a - (a / b) * b
     * Integer division rounds toward zero, which is why the result always
     * has the same sign as a (the left side).
     *
     * Example:
     *   remainder(10, 3)   -> 1
     *   remainder(-10, 3)  -> -1
     *   remainder(10, -3)  -> 1
     *   remainder(-10, -3) -> -1
     *
     * @param a the number being divided
     * @param b the number to divide by (never 0)
     * @return the remainder of a / b
     */
    public static int remainder(int a, int b) {
        // TODO 2: replace the line below with your implementation
        int remainder = a%b; return remainder;
    }

    // ------------------------------------------------------------------
    // Part 2: Operator precedence and floating point
    // ------------------------------------------------------------------

    /**
     * Returns the average of four test scores, including any decimal part.
     *
     * Two traps here:
     *   a + b + c + d / 4     only divides d by 4 (precedence!)
     *   (a + b + c + d) / 4   is int / int, so the decimal is dropped
     *
     * Example:
     *   average(1, 2, 3, 4)       -> 2.5
     *   average(90, 85, 77, 100)  -> 88.0
     *   average(1, 1, 1, 2)       -> 1.25
     *
     * @param a the first score
     * @param b the second score
     * @param c the third score
     * @param d the fourth score
     * @return the average of a, b, c, and d
     */
    public static double average(int a, int b, int c, int d) {
        // TODO 3: replace the line below with your implementation
        double average = ((double) a+b+c+d)/4; return average;
    }

    /**
     * Returns the percentage of quiz questions answered correctly.
     *
     * * and / have the same precedence, so they run left to right. That
     * means the ORDER you write them in matters:
     *   correct / total * 100    -> 3 / 8 is 0 first, then 0 * 100 is 0
     *
     * Example:
     *   percentage(3, 8) -> 37.5
     *   percentage(1, 4) -> 25.0
     *   percentage(5, 5) -> 100.0
     *
     * @param correct the number of questions answered correctly
     * @param total   the total number of questions (never 0)
     * @return correct out of total, as a percentage from 0.0 to 100.0
     */
    public static double percentage(int correct, int total) {
        // TODO 4: replace the line below with your implementation
        double percent = 100*(double)correct/total; return percent;
    }

    // ------------------------------------------------------------------
    // Part 3: Increment and decrement
    // ------------------------------------------------------------------

    // These two counters are already written for you. Each call to the
    // methods below should change them, so they live outside the methods.
    private static int nextTicket = 100;
    private static int visitors = 0;

    /**
     * Hands out the next ticket number at a deli counter.
     *
     * The customer gets the CURRENT value of nextTicket, and then nextTicket
     * goes up by one for the next customer. This can be done in a single
     * line with post-increment (nextTicket++).
     *
     * Example (nextTicket starts at 100):
     *   takeTicket() -> 100    (nextTicket is now 101)
     *   takeTicket() -> 101    (nextTicket is now 102)
     *   takeTicket() -> 102    (nextTicket is now 103)
     *
     * @return the ticket number before it was incremented
     */
    public static int takeTicket() {
        // TODO 5: replace the line below with your implementation
        return nextTicket++;
    }

    /**
     * Records one more visitor and returns the updated visitor count.
     *
     * This time visitors should go up by one FIRST, and then the new value
     * is returned. This can be done in a single line with pre-increment
     * (++visitors).
     *
     * Example (visitors starts at 0):
     *   addVisitor() -> 1
     *   addVisitor() -> 2
     *   addVisitor() -> 3
     *
     * @return the visitor count after adding one
     */
    public static int addVisitor() {
        // TODO 6: replace the line below with your implementation
        return ++visitors;
    }

    // ------------------------------------------------------------------
    // Part 4: Arithmetic on characters
    // ------------------------------------------------------------------

    /**
     * Returns the number that a digit character stands for.
     *
     * The character '7' is NOT the number 7 -- its code is 55. The digit
     * characters '0' to '9' have codes 48 to 57, in order, so subtracting
     * the code of '0' gives you the digit's value.
     *
     * Example:
     *   digitValue('7') -> 7
     *   digitValue('0') -> 0
     *   digitValue('9') -> 9
     *
     * @param digit a character from '0' to '9'
     * @return the int value of that digit
     */
    public static int digitValue(char digit) {
        // TODO 7: replace the line below with your implementation
        int targetchar = '0'; return (char) digit - targetchar;
    }

    /**
     * Shifts a lowercase letter forward in the alphabet, wrapping from 'z'
     * back around to 'a' (a Caesar cipher).
     *
     * Steps:
     *   1. c - 'a'  turns the letter into a position from 0 ('a') to 25 ('z')
     *   2. add shift, then use % 26 so the position wraps back into 0-25
     *   3. add 'a' back and cast to char (char + int is an int!)
     *
     * Example:
     *   caesarShift('a', 3)  -> 'd'
     *   caesarShift('x', 3)  -> 'a'
     *   caesarShift('z', 1)  -> 'a'
     *   caesarShift('h', 55) -> 'k'
     *
     * @param c     a lowercase letter from 'a' to 'z'
     * @param shift how many letters to move forward (0 or more)
     * @return the shifted lowercase letter
     */
    public static char caesarShift(char c, int shift) {
        // TODO 8: replace the line below with your implementation
        char target = (char)('a' + (c - 'a' + shift) % 26); return target;
    }

    // ------------------------------------------------------------------
    // Part 5: Type promotion, overflow, and underflow
    // ------------------------------------------------------------------

    /**
     * Adds amount to the byte b and returns the result as a byte.
     *
     * b + amount is promoted to an int, so  return b + amount;  will not
     * compile. Either cast the sum back to a byte, or use compound
     * assignment (b += amount), which casts for you.
     *
     * A byte only holds -128 to 127, so going past either end wraps around
     * to the other end (overflow and underflow).
     *
     * Example:
     *   addToByte(10, 4)    -> 14
     *   addToByte(127, 1)   -> -128
     *   addToByte(-128, -1) -> 127
     *   addToByte(100, 100) -> -56
     *
     * @param b      the starting byte
     * @param amount the amount to add (can be negative)
     * @return b + amount, wrapped to fit in a byte
     */
    public static byte addToByte(byte b, int amount) {
        // TODO 9: replace the line below with your implementation
        byte ans = (byte) (b+amount); return ans;
    }

    /**
     * Multiplies two ints and returns the exact product as a long.
     *
     * Careful:  return a * b;  compiles, but it's wrong for big numbers.
     * a * b is int * int, so the multiplication happens in 32 bits and
     * overflows BEFORE the result is widened to a long. Make one of the
     * operands a long first so the whole multiplication is promoted.
     *
     * Example:
     *   multiplyBig(3, 4)               -> 12
     *   multiplyBig(100000, 100000)     -> 10000000000
     *   multiplyBig(-2000000000, 2)     -> -4000000000
     *
     * @param a the first number
     * @param b the second number
     * @return the product of a and b, without overflow
     */
    public static long multiplyBig(int a, int b) {
        // TODO 10: replace the line below with your implementation
        long ans = (long)a*b; return ans;
    }

    // ------------------------------------------------------------------
    // Everything below this line is the self-grading test harness.
    // You do not need to write or edit any of it -- just implement the
    // TODOs above and run this file to see how you did.
    // ------------------------------------------------------------------

    private static int passCount = 0;
    private static int failCount = 0;

    public static void main(String[] args) {
        System.out.println("Running tests for Arithmetic.java...\n");

        // sumOfDigits()
        check("sumOfDigits(123)", 6, sumOfDigits(123));
        check("sumOfDigits(907)", 16, sumOfDigits(907));
        check("sumOfDigits(500)", 5, sumOfDigits(500));

        // remainder()
        check("remainder(10, 3)", 1, remainder(10, 3));
        check("remainder(-10, 3)", -1, remainder(-10, 3));
        check("remainder(10, -3)", 1, remainder(10, -3));
        check("remainder(-10, -3)", -1, remainder(-10, -3));

        // average()
        check("average(1, 2, 3, 4)", 2.5, average(1, 2, 3, 4));
        check("average(90, 85, 77, 100)", 88.0, average(90, 85, 77, 100));
        check("average(1, 1, 1, 2)", 1.25, average(1, 1, 1, 2));

        // percentage()
        check("percentage(3, 8)", 37.5, percentage(3, 8));
        check("percentage(1, 4)", 25.0, percentage(1, 4));
        check("percentage(5, 5)", 100.0, percentage(5, 5));

        // takeTicket()
        check("takeTicket() [1st call]", 100, takeTicket());
        check("takeTicket() [2nd call]", 101, takeTicket());
        check("takeTicket() [3rd call]", 102, takeTicket());

        // addVisitor()
        check("addVisitor() [1st call]", 1, addVisitor());
        check("addVisitor() [2nd call]", 2, addVisitor());
        check("addVisitor() [3rd call]", 3, addVisitor());

        // digitValue()
        check("digitValue('7')", 7, digitValue('7'));
        check("digitValue('0')", 0, digitValue('0'));
        check("digitValue('9')", 9, digitValue('9'));

        // caesarShift()
        check("caesarShift('a', 3)", 'd', caesarShift('a', 3));
        check("caesarShift('x', 3)", 'a', caesarShift('x', 3));
        check("caesarShift('z', 1)", 'a', caesarShift('z', 1));
        check("caesarShift('h', 55)", 'k', caesarShift('h', 55));

        // addToByte()
        check("addToByte(10, 4)", (byte) 14, addToByte((byte) 10, 4));
        check("addToByte(127, 1)", (byte) -128, addToByte((byte) 127, 1));
        check("addToByte(-128, -1)", (byte) 127, addToByte((byte) -128, -1));
        check("addToByte(100, 100)", (byte) -56, addToByte((byte) 100, 100));

        // multiplyBig()
        check("multiplyBig(3, 4)", 12L, multiplyBig(3, 4));
        check("multiplyBig(100000, 100000)", 10000000000L, multiplyBig(100000, 100000));
        check("multiplyBig(-2000000000, 2)", -4000000000L, multiplyBig(-2000000000, 2));

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
     *   check("sumOfDigits(123)", 6, 6) prints:
     *     [PASS] sumOfDigits(123) -> expected: 6, your output: 6
     *   check("sumOfDigits(123)", 6, 0) prints:
     *     [FAIL] sumOfDigits(123) -> expected: 6, your output: 0
     *
     * @param testName a short description of the test, e.g. "sumOfDigits(123)"
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
