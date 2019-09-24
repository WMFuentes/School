
/**
 * The Screen class asks for the number of pixels in the Y and X axis.
 *
 * @author William Fuentes
 * @version 9/15/2019
 */
public class Screen
{
    // instance variables for X and Y pixels.
    private int xPixels;
    private int yPixels;

    /**
     * Constructor to set the variables.
     */
    public Screen(int xRes, int yRes)
    {
        xPixels = xRes;
        yPixels = yRes;
    }

    /**
     * This method calculates the number of pixels on the screen.
     */
    public int numberOfPixels()
    {
        int resolution = xPixels * yPixels;
        return resolution;
    }

    /**
     * This method clears the number of pixels if the value of numberOfPixles is greater than 2 million.
     */    
    public void clear(boolean invert)
    {
        if(numberOfPixels() > 2000000) {
            xPixels = 0;
            yPixels = 0;
    }
    }
}
