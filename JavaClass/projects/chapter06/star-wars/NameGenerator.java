import java.util.Scanner;
/**
 * This program generates a name based on user input.
 *
 * @author William Fuentes
 * @version 9/25/19
 */
public class NameGenerator
{
    // instance variables
    private Scanner reader;

    /**
     * Constructor for objects of class NameGenerator
     */
    public NameGenerator()
    {
        // initialise instance variable
        reader = new Scanner(System.in);
    }

    /**
     * This method prints prompts and gathers input to create a
     * Star Wars name.
     */
    public void generateStarWarsName()
    {
        System.out.println("Welcome to the Star Wars Name Generator!");
        System.out.println();
        System.out.println("To get started, please provide the info below:");
        // Get 3 letters of the first name
        System.out.print("What is your first name? > ");
        String firstName = reader.nextLine().trim().toLowerCase();
        firstName = firstName.substring(0,2);
        // Get 2 letters of the last name
        System.out.print("What is your last name? > ");
        String lastName = reader.nextLine().trim();
        lastName = lastName.substring(0,3);
        // Get 2 letters of mother's maiden name
        System.out.print("What is your mother's maiden name? > ");
        String maidenName = reader.nextLine().trim();
        maidenName = maidenName.substring(0,2);
        // Get 3 letters of the city of birth
        System.out.print("What city were you born in? > ");
        String cityName = reader.nextLine().trim().toLowerCase();
        cityName = cityName.substring(0,3);
        // Print out the user's star wars name
        System.out.println();
        System.out.println("Your Star Wars name is "+lastName+firstName+" "
                           +maidenName+cityName);
        System.out.println("May the force be with you!");
    }
}
