
/**
 * Chaos equation program taken from Python and implemented in Java.
 *
 * @author Bill Fuentes
 * @version 9/18/19
 */
public class Chaos
{
    // instance variables
    private float variable;

    /**
     * Constructor for objects of class Chaos
     */
    public Chaos()
    {
        // initialise instance variables
        variable = 0.0f;
    }

    /**
     * This method takes a variable
     */
    public void chaos(float variable)
    {
        // put your code here
        int y = 0;
        
        while (y < 10) {
            variable = 3.9f * variable * (1.0f - variable);
            System.out.println(variable);
            y++;
        }
    }
}
