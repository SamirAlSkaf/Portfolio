import java.util.Random;
import java.util.Scanner;

public class DiceSimulator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        System.out.println("Press Enter to roll the dice.");
        
        while (true) {
            String input = scanner.nextLine();
            
            // Check if the Enter key is pressed
            if (input.equals("")) {
                // Generate a random number between 1 and 6
                int roll = random.nextInt(6) + 1;
                System.out.println("You rolled a " + roll + ".");
                System.out.println("Press Enter again to roll the dice one more time.");
            } else {
                System.out.println("Press Enter to roll the dice.");
            }
        }
    }
}
