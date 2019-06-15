import java.util.Scanner;

public class Prob10 {
    static final String key = "abcdefghijklmnopqrstuvwxyz";
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int ninputs = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < ninputs; i++) {
            String fin = "";

            int offset = scanner.nextInt();
            scanner.nextLine();
            String input = scanner.nextLine();
            for (char c : input.toCharArray()) {
                int idx = key.indexOf(c);
                if (idx == -1) {
                    fin += c;
                    continue;
                }
                fin += key.charAt((((idx - offset) % 26) + 26) % 26);
            }

            System.out.println(fin);
        }
    }
}