import java.util.*;
public class Hangman {
    private String secretPhrase;
    private String userSolution;
    private int wrongGuesses = 0;
    private ArrayList<String> guessedLetters;

    public Hangman() {
        Scanner scanner = new Scanner(System.in);
        String playAgain = "Y";

        while(playAgain.equals("Y")) {
        userSolution = "";
        wrongGuesses = 0;
        System.out.println("[1] Foods\t [4] Items\n" 
                         + "[2] Animals\t [5] Phrases\n"
                         + "[3] Names\n");
        System.out.print("Select category number: ");

        secretPhrase = selectSecret(Integer.parseInt(scanner.nextLine()));
        guessedLetters = new ArrayList<String>();

        for(int i = 0; i < secretPhrase.length(); i++) {
            if(secretPhrase.substring(i, i+1).equals(" "))
                userSolution += " ";
            else
                userSolution += "_";
        }

        while(wrongGuesses < 13) {
            printBoard();
            if(userSolution.equals(secretPhrase) || wrongGuesses == 12)
                break;

            System.out.print("\n\nGuess a letter: ");
            parseGuess(scanner.nextLine().toUpperCase());

            System.out.println();
        }

        System.out.println();
        if(userSolution.equals(secretPhrase))
            System.out.println("YOU WIN!");
        else
            System.out.println("YOU LOSE\nSecret Phrase: " + secretPhrase);

        System.out.println();
        System.out.print("Play again? [Y/N]: ");
        playAgain = scanner.nextLine().toUpperCase();    
        }

        System.out.println("\nThank you for playing.");
    }

    public String selectSecret(int category) {
        String[] foodsArr = {"APPLE", "PINEAPPLE", "PINECONE", "PEANUT BUTTTER", 
                             "HAM", "GOUDA", "PAD THAI", "EMPANADA", "CLEMENTINE",
                             "DURIAN", "TRIPE", "LATKES", "MATZAH BALL SOUP", "SPAM",
                             "BLOOD SAUSAGE", "CHICKEN NOODLE SOUP", "TOMATO BISQUE SOUP",
                             "KNISH", "POTATO CHIPS", "PORKCHOP", "FRANKFURTER", "BISCUITS AND GRITS",
                             "BLUEBERRY PANCAKES", "MOON CAKES", "RASPBERRIES", "SUSHI"};
        String[] animalsArr = {"CAT", "DOG", "TURTLE", "STALLION", "SOW", "AARDVARK", 
                               "ALBATROSS", "ALLIGATOR", "ALPACA", "ANTELOPE", "ARMADILLO",
                               "BARRACUDA", "CHAMELEON", "CHINCHILLA", "COCKROACH", "COYOTE",
                               "CROCODILE", "DRAGONFLY", "ECHIDNA", "EMU", "FLAMINGO", "GNAT",
                               "HAWK", "HEDGEHOG", "HYENA", "IBIS", "KOALA", "MOSQUITO", 
                               "NARWHAL", "NEWT", "NIGHTINGALE", "OCTOPUS", "OSTRICH", 
                               "PELICAN", "PHEASANT", "QUAIL", "SALAMANDER", "SHREW", 
                               "STEGOSAURUS", "CYGNET", "WASP", "WOLVERINE", "WREN", 
                               "YAK", "WHALE", "WALRUS"};
        String[] namesArr = {"MCDOUGAL", "JOHN", "PELAFINA", "AUGUSTUS", "BRUTUS",
                             "AMADEUS", "ANDROMEDA", "ANASTASIA", "AURORA", "BEATRIX",
                             "HENRIETTA", "OLYMPIA", "MAGNOLIA", "THALASSA", "VALENTINA",
                             "ABDULLAH", "AHMED", "ALFIE", "ARJUN", "CALLUM", "IDRIS", 
                             "JAN", "VINNY", "JOHANN", "GUSTAV", "LARS", "MATHIAS", 
                             "LINUS", "MONTY", "REGGIE", "YUSUF", "WILFRED", "ZACHERY",
                             "VERONICA", "CUMMINGS", "VINNY", "CHUNGUS", "ROD"};
        String[] itemsArr = {"PENCIL", "ROCK", "TURNTABLE", "WALLET", "MACBOOK AIR", 
                             "EARBUDS", "SCOOTER", "DOMINO", "DILDO", "POCKET PUSSY", 
                             "CHARM BRACELET", "OAK WOOD PLANK", "POWERDRILL", "CALLIPERS",
                             "COFFEE TABLE", "COWBOY BOOTS", "OTTOMAN", "TELEVISION", 
                             "ARCADE CABINET", "TAXI CAB", "FURBY", "BARBIE DOLL", 
                             "UNIVERSAL REMOTE", "FLATHEAD SCREWDRIVER", "CARDBOARD BOX", 
                             "SHOELACE", "TUBE SOCKS", "SATCHEL", "MAGAZINE", "INFIDELITY"};
        String[] phrasesArr = {"HOW DO YOU DO", "A STRANGE TURN OF EVENTS", "THE END IS NIGH",
                               "I LOVE YOU", "I WILL DESTROY YOU", "SON OF A BITCH", "KILL ME", 
                               "MY HOUSE IS BURNING DOWN", "I SET MY GRANDMA ON FIRE", "PLEASE",
                               "I YEARN FOR THE RESPECT OF MY FATHER", "CAN YOU PLEASE TOUCH ME",
                               "MY MOTHER NEVER VISITS", "MY GRANDMA SOURED", "LIGMA NUTS", "GOD DAMN", 
                               "IF THE SHOE FITS", "I DID NOT HIT HER", "KILL YOURSELF", "YEET", 
                               "DAD STOP HITTING ME", "WHEN YOU EAT DADS PAINKILLERS BUT CANT FEEL THE SPANKING"};

        String[][] categories = {foodsArr, animalsArr, namesArr, itemsArr, phrasesArr};

        String[] selectedArr = categories[category -1];
        int rand = (int) Math.floor(Math.random() * selectedArr.length);

        return selectedArr[rand];
    }

    public void parseGuess(String letter) {
        if(secretPhrase.indexOf(letter) != -1) {
            for(int i = 0; i < secretPhrase.length(); i++) {
                if(secretPhrase.substring(i, i+1).equals(letter))
                    userSolution = userSolution.substring(0,i) + letter + userSolution.substring(i+1);                
            }
        }
        else {
            guessedLetters.add(letter);
            wrongGuesses++;
        }
    }

    public void printBoard() {
        String[] hangingBoard = {"  _________,_________ ",
                                 " |  _______|______   |",
                                 " |_|       |      |  |",
                                 "           |      |  |",
                                 "          /       |  |",
                                 "                  |  |",
                                 "                  |  |",
                                 "                  |  |",
                                 "                  |  |",
                                 "                  |  |",
                                 "                  |  |",
                                 "                  |  |",
                                 "                  |  |",
                                 "                  |  |",
                                 " _________________|  |____",
                                 "|_________________________|"};

        for(int i = 1; i <= wrongGuesses; i++) {
            if(i >= 1) {
                hangingBoard[3] = "     ___  |       |  |";
                hangingBoard[4] = "    (   )/        |  |";
            }
            if(i >= 2)
                hangingBoard[4] = "    (X  )/        |  |";
            if(i >= 3)
                hangingBoard[4] = "    (X_ )/        |  |";
            if(i >= 4)
                hangingBoard[4] = "    (x_x)/        |  |";
            if(i >= 5)
                hangingBoard[5] = "    _===_         |  |";
            if(i >= 6)
                hangingBoard[6] = "     | |          |  |";
            if(i >= 7)
                hangingBoard[7] = "     | |          |  |";
            if(i >= 8)
                hangingBoard[8] = "     | |          |  |";
            if(i >= 9) {
                hangingBoard[6] = "   | | |          |  |";
                hangingBoard[7] = "   | | |          |  |";
                hangingBoard[8] = "   ^ | |          |  |";
            }
            if(i >= 10) {
                hangingBoard[6] = "   | | | |        |  |";
                hangingBoard[7] = "   | | | |        |  |";
                hangingBoard[8] = "   ^ | | ^        |  |"; 
            }
            if(i >= 11) {
                hangingBoard[10] = "    /             |  |";
                hangingBoard[11] = "   _|             |  |";
            }
            if(i >= 12) {
                hangingBoard[10] = "    /   \\         |  |";
                hangingBoard[11] = "   _|   |_        |  |";
            } 
        }

        for(String line : hangingBoard)
            System.out.println(line);

        
        System.out.println();
        for(int i = 0; i < userSolution.length(); i++) {
            System.out.print(userSolution.substring(i, i+1) + " ");
        }

        System.out.println();
        if(guessedLetters.size() > 0) {
            System.out.println(" _________________\n"
                             + "| GUESSED LETTERS |");
            String letterList = "| ";
            for(int i = 0; i < guessedLetters.size(); i++) {
                if(i % 6 == 0 && i > 0)
                    letterList += "\n| ";

                letterList += " " + guessedLetters.get(i);
            }

            System.out.println(letterList);
            System.out.println("| _______________ |");
        }
    }

    public static void main(String[] args) {
        Hangman game = new Hangman();
    }
}

/*
  _________,_________
 |  _______|______   | 
 |_|       |      |  |
      ___  |      |  |
     (x_x)/       |  |
     _===_        |  |
    | | | |       |  |
    | | | |       |  |
    ^ | | ^       |  |
     /   \        |  |
    _|   |_       |  |
                  |  |
                  |  |
 _________________|  |____
|_________________________|

 _________________
| GUESSED LETTERS |  
| A B C D E F G   |
| H I J K L M N   |
| O P Q R S T U   |
| V W X Y Z       |
| _______________ |
*/