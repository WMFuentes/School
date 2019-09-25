import java.util.Random;
/**
 * This class generates a random number using the methods within.
 *
 * @author William Fuentes
 * @version 9/25/2019
 */
public class RandomTester
{
    // instance variable
    private Random randomGenerator;

    /**
     * Constructor for object of class RandomTester
     */
    public RandomTester()
    {
        // initialise instance variables
        randomGenerator = new Random();
    }

    /**
     * The printOneRandom method prints one random number.
     */
    public void printOneRandom()
    {
        int index = randomGenerator.nextInt();
        System.out.println(index);
    }
    
        /**
     * The printMultiRandom method prints multiple random numbers, as many
     * as the parameter is supplied
     *
     * @param  howMany defines the number of times a loop will run
     */
    public void printMultiRandom(int howMany)
    {
        while(howMany > 0){
        int index = randomGenerator.nextInt();
        System.out.println(index);
        howMany = howMany - 1;
    }
    }
}
