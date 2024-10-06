import java.util.Random;
import java.util.Scanner;

public class ReactionTimeTester {
    public static void main(String[] args) throws InterruptedException {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        while (true) {
            System.out.println("Press Enter to start the Reaction-Test. An X will appear, and you should quickly press Enter to meassure your reaction-time.");
            scanner.nextLine();

            // Wartezeit zwischen 1 und 3 Sekunden
            Thread.sleep(1000 + random.nextInt(2000));

            System.out.println("X");
            long startTime = System.nanoTime();
            scanner.nextLine();
            long endTime = System.nanoTime();

            double reactionTime = (endTime - startTime) / 1_000_000.0; // in Millisekunden
            System.out.printf("Your reaction time was %.3f ms.%n", reactionTime);
            System.out.println("Press Enter to try again.");
        }
    }
}
