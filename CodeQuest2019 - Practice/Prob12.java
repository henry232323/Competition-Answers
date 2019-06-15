import java.text.DecimalFormat;
import java.util.Scanner;

public class Prob12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] line = scanner.nextLine().split(" ");
        int numDoors = Integer.parseInt(line[0]);
        int numRounds = Integer.parseInt(line[1]);
        int numOpen = Integer.parseInt(line[2]);

        double winpercent = 100.0 / numDoors;
        int numRemaining = numDoors;

        for (int round = 1; round <= numRounds; round++) {
            winpercent += winpercent / numRemaining * numOpen;
            numRemaining -= numOpen + 1;
        }

        DecimalFormat fmt = new DecimalFormat("0.00%");
        System.out.println(fmt.format(winpercent/100));
    }
}
