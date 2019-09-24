
/**
 * The heater class contains methods to increase or decrease the temperature.
 *
 * @author (William Fuentes)
 * @version (9/8/19)
 */
public class Heater
{
    // Instance variable of temperature, set as a double
    private double temperature;

    /**
     * Constructor to set temperature to 15.0.
     */
    public Heater()
    {
        // initial temperature variable
        temperature = 15.0;
    }

    /**
     * The warmer method to increase the temperature by 5 degrees.
     */
    public void warmer()
    {
        // this mutator adds 5.0 to the current temperature
        temperature = temperature + 5.0;
    }
    
    /**
     * The cooler method to decrease the temperature by 5 degrees.
     */
    public void cooler()
    {
        // this mutator subtracts 5.0 from the current temperature
        temperature = temperature - 5.0;
    }
    
    /**
     * An accessor method to return the current temperature.
     */
    public double getTemperature()
    {
        return temperature;
    }
}
