import java.util.Scanner;

public class Prob13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < Integer.valueOf(scanner.nextLine()); i++) {
            String[] line = scanner.nextLine().split(" ");
            int nrows = Integer.valueOf(line[0]);
            int ncolumns = Integer.valueOf(line[1]);
            int nbombs = Integer.valueOf(line[2]);
            int[] bombs = new int[nbombs * 2];
            for (int b = 0; b < nbombs; b++) {
                String[] xy = scanner.nextLine().split(" ");
                bombs[(2 * b)] = Integer.valueOf(xy[0]);
                bombs[(2 * b) + 1] = Integer.valueOf(xy[1]);
            }
            int[][] minearray = new int[nrows][ncolumns];
            for (int r = 0; r < nrows; r++) {
                for (int c = 0; c < ncolumns; c++) {
                    //System.out.println(r + " " + c);

                    for (int b = 0; b < nbombs * 2; b += 2) {
                        int x = bombs[b];
                        int y = bombs[b + 1];

                        if (x == r && y == c) {
                            minearray[r][c] = 10;
                            break;
                        }
                        int xdist = Math.abs(r - x);
                        int ydist = Math.abs(c - y);
                        if (xdist <= 1 && ydist <= 1) {
                            minearray[r][c] += 1;
                        }
                    }
                    int val = minearray[r][c];
                    if (val != 10)
                        System.out.print(minearray[r][c]);
                    else
                        System.out.print("*");
                }
                System.out.println();
            }
        }
    }
}
