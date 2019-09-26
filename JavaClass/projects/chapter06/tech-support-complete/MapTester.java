import java.util.HashMap;
/**
 * MapTester is a simple class that stores and returns contacts using a hash
 * map.
 *
 * @author William Fuentes
 * @version 9/25/2019
 */
public class MapTester
{
    // instance variable
    private HashMap<String, String> contacts;
    
    /**
     * Constructor for objects of class MapTester, starting the HashMap
     * and adding contacts with fillContacts.
     */
    public MapTester()
    {
        // initialise instance variable
        contacts = new HashMap<>();
        fillContacts();
    }
    
    /**
     * Simple method to fill the HashMap with some people.
     */
    public void fillContacts()
    {
        contacts.put("Jerry Seinfeld", "201-2255");
        contacts.put("Kramer", "201-1234");
        contacts.put("George Costanza", "201-4556");
        contacts.put("Elaine Benes", "201-2250");
    }
    
    /**
     * Simple method to add your own contacts.
     *
     * @param  A Name and a phone number as Strings
     */
    public void enterNumber(String name, String number)
    {
        contacts.put(name, number);
    }
    
     /**
     * Simple method to return phone numbers based on a name.
     *
     * @param  Name of a contact.
     */
    public String lookupNumber(String name)
    {
        String number = contacts.get(name);
        return number;
    }
}
