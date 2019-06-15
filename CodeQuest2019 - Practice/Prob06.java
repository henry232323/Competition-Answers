import java.text.DecimalFormat;
import java.util.Scanner;

public class Prob06 {
    static final String key = "abcdefghijklmnopqrstuvwxyz";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double erad = 40075 / (2 * Math.PI);
        int ncases = Integer.valueOf(scanner.nextLine());
        for (int n = 0; n < ncases; n++) {
            String[] nums = scanner.nextLine().split(" ");
            int height = Integer.valueOf(nums[0]);
            double frad = erad + height;
            DecimalFormat fmt = new DecimalFormat("0.0");
            System.out.println(fmt.format(frad * 2 * Math.PI));
        }
    }
}
