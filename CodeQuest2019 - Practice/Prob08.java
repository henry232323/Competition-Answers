import java.util.Scanner;

public class Prob08 {
    static final String key = "abcdefghijklmnopqrstuvwxyz";
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int ninputs = scanner.nextInt();
        scanner.nextLine();

        for (int k = 0; k < ninputs; k++) {
            String[] nums = scanner.nextLine().split(" ");
            int x = Integer.parseInt(nums[0]);
            int y = Integer.parseInt(nums[1]);

            for (int i = 0; i <= 19; i++) {
                for (int j = 0; j <= 19; j++) {
                    int dist = (int) Math.sqrt(Math.pow(x-i, 2) + Math.pow(y-j, 2));
                    switch (dist) {
                        case 0:
                            System.out.print(100 + " ");
                            break;
                        case 1:
                            System.out.print(50 + " ");
                            break;
                        case 2:
                            System.out.print(25 + " ");
                            break;
                        default:
                            System.out.print(10 + " ");
                            break;
                    }
                }
                System.out.println();
            }
        }
    }
}