import java.util.Scanner;

public class Prob18 {
    static final String key = "abcdefghijklmnopqrstuvwxyz";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int ncases = Integer.valueOf(scanner.nextLine());
        for (int g = 0; g < ncases; g++) {
            String[] nums = scanner.nextLine().split(" ");
            float real = Float.valueOf(nums[0]);
            float imag = Float.valueOf(nums[1]);

            double zr = 0;
            double zi = 0;
            int n = 0;
            while (true) {
                zr = zr * zr - zi * zi + real;
                zi = 2 * zi * zr + imag;

                if (Math.pow(zr, 2) + Math.pow(zi, 2) > 100 * 100)
                    break;
                if (n > 50)
                    break;

                n++;
            }

            String color;
            //System.out.println(n);
            if (n <= 10)
                color = "RED";
            else if (n <= 20)
                color = "ORANGE";
            else if (n <= 30)
                color = "YELLOW";
            else if (n <= 40)
                color = "GREEN";
            else if (n <= 50)
                color = "BLUE";
            else
                color = "BLACK";

            String operator = "";
            if (zi >= 0)
                operator = "+";
            System.out.println(nums[0] + operator + nums[1] + "i " + color);
        }
    }
}
