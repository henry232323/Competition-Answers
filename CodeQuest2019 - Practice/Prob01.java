import java.util.Scanner;

public class Prob01 {
    static final String key = "abcdefghijklmnopqrstuvwxyz";
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int ncases = Integer.valueOf(scanner.nextLine());
        for (int n = 0; n < ncases; n++) {
            System.out.println(scanner.nextLine().toLowerCase());
        }
    }
}
