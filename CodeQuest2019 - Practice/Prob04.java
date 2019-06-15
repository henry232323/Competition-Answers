import java.util.Scanner;

public class Prob04 {
    static final String key = "abcdefghijklmnopqrstuvwxyz";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int ncases = Integer.valueOf(scanner.nextLine());
        for (int n = 0; n < ncases; n++) {
            String[] nums = scanner.nextLine().split(" ");
            int speed = Integer.valueOf(nums[0]);
            boolean bday = nums[1].equals("true");
            if (bday) {
                speed -= 5;
            }

            if (speed <= 60) {
                System.out.println("no ticket");
            } else if (speed >= 61 && speed <= 80) {
                System.out.println("small ticket");
            } else {
                System.out.println("big ticket");
            }
        }
    }
}
