import java.util.Scanner;

public class Prob03 {
    static final String key = "abcdefghijklmnopqrstuvwxyz";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int ncases = Integer.valueOf(scanner.nextLine());
        for (int n = 0; n < ncases; n++) {
            String[] nums = scanner.nextLine().split(" ");
            boolean a = nums[0].equals("true");
            boolean b = nums[1].equals("true");

            System.out.println(a == b);
        }
    }
}
