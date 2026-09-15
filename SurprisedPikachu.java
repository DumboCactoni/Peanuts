/**
 * SurprisedPikachu.java
 *
 * Exercise 3: ASCII Art (2D Arrays)
 *
 * Instead of typing the picture in by hand, this program "paints" the
 * Surprised Pikachu meme onto a 2D char array (our canvas), one shape at a
 * time, and then prints the array row by row.
 *
 * The style copies the classic "meme made in Notepad" version: every cell is
 * filled. Dark areas use "heavy" characters like # & % and light areas use
 * "thin" characters like , so the picture shows up as light and dark regions.
 *
 * Big ideas shown here:
 *   - A 2D array (char[][]) works like a grid of pixels.
 *   - Point-in-polygon and ellipse formulas decide which cells a shape covers.
 *   - "Painter's algorithm": shapes drawn later cover shapes drawn earlier.
 *   - Shading: a String of characters ordered from darkest to lightest.
 *   - Terminal characters are about twice as tall as they are wide, so each
 *     row covers twice as many image pixels as each column does.
 *
 * Every printed line is kept under 120 characters.
 *
 * To compile and run:
 *   javac SurprisedPikachu.java
 *   java SurprisedPikachu
 */
public class SurprisedPikachu {

    /** Number of columns (characters per line). Must stay under 120. */
    public static final int WIDTH = 104;

    /** Number of rows (lines) in the picture. */
    public static final int HEIGHT = 46;

    /** Image pixel shown at the top-left corner of the canvas. */
    public static final double LEFT = 130;
    public static final double TOP = 85;

    /** How many image pixels one character covers (rows are twice as tall). */
    public static final double PIXELS_PER_COL = 6.25;
    public static final double PIXELS_PER_ROW = 12.5;

    /** Dark characters for the background, used to give it a patchy texture. */
    public static final String BACKGROUND_SHADES = "#&%(/";

    /** The canvas: canvas[row][col] holds one "pixel" character. */
    private static char[][] canvas = new char[HEIGHT][WIDTH];

    // ----- Shapes traced from the image (x values, then matching y values) -----

    /** Outline of the ears and head, going clockwise from the left ear tip. */
    private static final double[] BODY_X = {
        140, 190, 260, 330, 375, 392,          // left ear, top edge
        450, 520, 590,                         // top of head
        660, 720, 775, 830,                    // right ear, top edge (runs off the canvas)
        830, 770, 705,                         // right ear, bottom edge
        720, 745, 765, 780, 830,               // right cheek line (runs off the canvas)
        830, 290,                              // bottom (below the canvas)
        285, 262, 245, 242, 250, 268, 292,     // left side of head
        250, 200, 160                          // left ear, bottom edge
    };
    private static final double[] BODY_Y = {
        97, 112, 160, 200, 232, 250,
        245, 242, 245,
        210, 185, 165, 145,
        290, 295, 342,
        390, 450, 520, 580, 580,
        720, 720,
        655, 600, 540, 480, 420, 370, 327,
        265, 190, 125
    };

    /** The dark brown sliver at the tip of the left ear. */
    private static final double[] EAR_TIP_X = {140, 188, 205, 160};
    private static final double[] EAR_TIP_Y = {97, 113, 205, 125};

    /** The open mouth: a rounded shape that is a little flatter on top. */
    private static final double[] MOUTH_X = {440, 470, 515, 528, 525, 505, 470, 445, 435};
    private static final double[] MOUTH_Y = {500, 495, 498, 510, 545, 565, 568, 555, 525};

    // ----- Converting between canvas cells and image pixels -----

    /** Image x coordinate at the center of a column. */
    public static double pixelX(int col) {
        return LEFT + (col + 0.5) * PIXELS_PER_COL;
    }

    /** Image y coordinate at the center of a row. */
    public static double pixelY(int row) {
        return TOP + (row + 0.5) * PIXELS_PER_ROW;
    }

    // ----- Shape tests -----

    /**
     * Returns true if the center of cell (row, col) is inside the polygon.
     * Uses ray casting: shoot a ray to the right and count how many edges it
     * crosses. An odd number of crossings means the point is inside.
     */
    public static boolean inPolygon(int row, int col, double[] xs, double[] ys) {
        double px = pixelX(col);
        double py = pixelY(row);
        boolean inside = false;
        int j = xs.length - 1;
        for (int i = 0; i < xs.length; i++) {
            if ((ys[i] > py) != (ys[j] > py)) {
                double crossX = xs[i] + (xs[j] - xs[i]) * (py - ys[i]) / (ys[j] - ys[i]);
                if (px < crossX) {
                    inside = !inside;
                }
            }
            j = i;
        }
        return inside;
    }

    /** Returns true if the center of cell (row, col) is inside the ellipse. */
    public static boolean inEllipse(int row, int col, double cx, double cy, double rx, double ry) {
        double x = (pixelX(col) - cx) / rx;
        double y = (pixelY(row) - cy) / ry;
        return x * x + y * y <= 1.0;
    }

    // ----- Drawing -----

    /**
     * Fills the background with dark characters. Two overlapping waves pick
     * which character goes in each cell, which makes soft patches of the same
     * character, like the uneven shading in the Notepad meme.
     */
    public static void drawBackground() {
        for (int row = 0; row < HEIGHT; row++) {
            for (int col = 0; col < WIDTH; col++) {
                double wave = Math.sin(col / 11.0 + row / 7.0) + Math.cos(row / 13.0 - col / 23.0);
                int index = (int) ((wave + 2.0) / 4.0 * BACKGROUND_SHADES.length());
                index = Math.max(0, Math.min(BACKGROUND_SHADES.length() - 1, index));
                canvas[row][col] = BACKGROUND_SHADES.charAt(index);
            }
        }
    }

    /**
     * Fills a polygon with the fill character and traces its border with the
     * edge character. A cell is on the border if it is inside the shape but
     * one of its four neighbors is not.
     */
    public static void drawPolygon(double[] xs, double[] ys, char fill, char edge) {
        for (int row = 0; row < HEIGHT; row++) {
            for (int col = 0; col < WIDTH; col++) {
                if (inPolygon(row, col, xs, ys)) {
                    boolean border = !inPolygon(row - 1, col, xs, ys)
                            || !inPolygon(row + 1, col, xs, ys)
                            || !inPolygon(row, col - 1, xs, ys)
                            || !inPolygon(row, col + 1, xs, ys);
                    canvas[row][col] = border ? edge : fill;
                }
            }
        }
    }

    /** Same idea as drawPolygon, but for an ellipse. */
    public static void drawEllipse(double cx, double cy, double rx, double ry, char fill, char edge) {
        for (int row = 0; row < HEIGHT; row++) {
            for (int col = 0; col < WIDTH; col++) {
                if (inEllipse(row, col, cx, cy, rx, ry)) {
                    boolean border = !inEllipse(row - 1, col, cx, cy, rx, ry)
                            || !inEllipse(row + 1, col, cx, cy, rx, ry)
                            || !inEllipse(row, col - 1, cx, cy, rx, ry)
                            || !inEllipse(row, col + 1, cx, cy, rx, ry);
                    canvas[row][col] = border ? edge : fill;
                }
            }
        }
    }

    /**
     * Draws one eye centered on cell (row, col).
     *
     * Why a cell and not a pixel? If one eye is centered at pixel 372 and the
     * other at pixel 596, they sit at different spots inside their character
     * cells, so the grid "rounds" them differently and the two eyes come out
     * different shapes. Centering both eyes on a cell makes them identical.
     */
    public static void drawEye(int row, int col) {
        double cx = pixelX(col);
        double cy = pixelY(row);
        drawEllipse(cx, cy, 27, 31, '&', '/');

        // Shiny highlight: 2 characters wide, one row up and to the left
        double highlightX = cx - 1.5 * PIXELS_PER_COL;
        double highlightY = cy - PIXELS_PER_ROW;
        drawEllipse(highlightX, highlightY, 4, 4, ' ', ' ');
    }

    /** Paints every part of Pikachu's face onto the canvas, back to front. */
    public static void paintPikachu() {
        // 1. Dark, textured background
        drawBackground();

        // 2. Ears and head as one outline, then the brown tip on the left ear
        drawPolygon(BODY_X, BODY_Y, ',', '*');
        drawPolygon(EAR_TIP_X, EAR_TIP_Y, '&', '&');

        // 3. Rosy cheeks
        drawEllipse(295, 490, 40, 33, '(', '*');
        drawEllipse(660, 492, 43, 35, '(', '*');

        // 4. Shocked eyes (column 38 is pixel ~371, column 74 is pixel ~596)
        drawEye(24, 38);
        drawEye(24, 74);

        // 5. Little nose
        drawEllipse(pixelX(53), pixelY(28), 16, 6, '%', '%');

        // 6. The famous open mouth
        drawPolygon(MOUTH_X, MOUTH_Y, '*', '(');
    }

    /** Prints the canvas, one row per line. */
    public static void printCanvas() {
        for (int row = 0; row < HEIGHT; row++) {
            System.out.println(new String(canvas[row]));
        }
    }

    public static void main(String[] args) {
        paintPikachu();
        printCanvas();
    }
}
