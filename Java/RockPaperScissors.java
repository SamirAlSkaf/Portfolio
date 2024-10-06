import java.util.Scanner;

public class RockPaperScissors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String playAgain;

        do {
            String userChoice;
            while (true) {
                System.out.println("Please choose Rock, Paper, or Scissors and type your choice. Then press Enter.");
                userChoice = scanner.nextLine().toLowerCase();

                if (userChoice.equals("rock") || userChoice.equals("paper") || userChoice.equals("scissors")) {
                    break;
                } else {
                    System.out.println("Invalid input! Please try again.");
                }
            }

            String computerChoice = getComputerChoice();
            System.out.println("I chose " + computerChoice + ", so you " + determineWinner(userChoice, computerChoice) + ".");

            System.out.println("Another round? (Press Enter for yes)");
            playAgain = scanner.nextLine();
        } while (playAgain.isEmpty());

        scanner.close();
    }

    private static String getComputerChoice() {
        String[] choices = {"rock", "paper", "scissors"};
        int randomIndex = (int) (Math.random() * choices.length);
        return choices[randomIndex];
    }

    private static String determineWinner(String userChoice, String computerChoice) {
        if (userChoice.equals(computerChoice)) {
            return "tied!";
        }
        if ((userChoice.equals("scissors") && computerChoice.equals("paper")) ||
            (userChoice.equals("rock") && computerChoice.equals("scissors")) ||
            (userChoice.equals("paper") && computerChoice.equals("rock"))) {
            return "won!";
        }
        return "lost!";
    }
}
