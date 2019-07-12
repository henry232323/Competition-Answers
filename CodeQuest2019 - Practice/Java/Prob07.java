import java.text.DecimalFormat;
import java.util.Scanner;

public class Prob07 {
    static final String key = "abcdefghijklmnopqrstuvwxyz";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double erad = 40075 / (2 * Math.PI);
        int ncases = Integer.valueOf(scanner.nextLine());
        for (int n = 0; n < ncases; n++) {
            int nitems = Integer.valueOf(scanner.nextLine());
            double[] knums = new double[nitems];
            for (int i = 0; i < nitems; i++) {
                knums[i] = Float.valueOf(scanner.nextLine());
            }

            double min = knums[0];
            double max = knums[0];
            for (double d : knums) {
                if (d > max)
                    max = d;
                if (d < min)
                    min = d;
            }

            DecimalFormat fmt = new DecimalFormat("0");
            for (double d : knums) {
                System.out.println(fmt.format((d - min) / (max - min) * 255));
            }
        }
    }
}
