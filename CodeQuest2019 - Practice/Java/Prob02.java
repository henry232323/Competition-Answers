import java.util.Scanner;

public class Prob02 {
    static final String key = "abcdefghijklmnopqrstuvwxyz";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int ncases = Integer.valueOf(scanner.nextLine());
        for (int n = 0; n < ncases; n++) {
            String[] nums = scanner.nextLine().split(" ");
            int n1 = Integer.valueOf(nums[0]);
            int n2 = Integer.valueOf(nums[1]);

            if (n1 == n2) {
                System.out.println( 4 * n1 );
            } else {
                System.out.println(n1 + n2);
            }
        }
    }
}
