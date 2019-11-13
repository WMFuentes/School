
/**
 * This class makes comparisons between the efficiency of collections.
 *
 * @author William Fuentes
 * @version 1 11/10/19
 */

import java.util.Random;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Comparison
{

    /**
     * Constructor for objects of class Comparison
     */
    public Comparison()
    {
        compare();
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public void compare()
    {
        // Initializing variables, such as the contents of the lists and
        // the 2 lists, array and linked.
        int a;
        int b;
        List<Integer> array = new ArrayList<Integer>();
        List<Integer> linked = new LinkedList<Integer>();
        Random random = new Random();
        
        System.out.println("Adding 10,000 items to an array:");
        
        long start = System.currentTimeMillis();
        
        for(a = 0; a<10000; a++){
            array.add(a);
        }
        
        long end = System.currentTimeMillis();
        long duration = end-start;
        
        System.out.println("Duration: " + duration + " Milliseconds");
        
        System.out.println("Getting 10,000 items from an array:");
        
        start = System.currentTimeMillis();
        
        for(a = 0; a<10000; a++){
            int index = random.nextInt(10000);
            
            int x = array.get(index);
        }
        
        end = System.currentTimeMillis();
        duration = end-start;
        
        System.out.println("Duration: " + duration + " Milliseconds");
        
        System.out.println("Removing 10,000 items from an array:");
        
        start = System.currentTimeMillis();
        
        for(a = 0; a<10000; a++){
            array.remove(0);
        }
        
        end = System.currentTimeMillis();
        duration = end-start;
        
        System.out.println("Duration: " + duration + " Milliseconds");
        
        System.out.println("Adding 10,000 items to a Linked List:");
        
        start = System.currentTimeMillis();
        
        for(b = 0; b<10000; b++){
            linked.add(b);
        }
        
        end = System.currentTimeMillis();
        duration = end-start;
        
        System.out.println("Duration: " + duration + " Milliseconds");
        
        System.out.println("Getting 10,000 items from a Linked List:");
        
        start = System.currentTimeMillis();
        
        for(b = 0; b<10000; b++){
            int index = random.nextInt(10000);
            
            int x = linked.get(index);
        }
        
        end = System.currentTimeMillis();
        duration = end-start;
        
        System.out.println("Duration: " + duration + " Milliseconds");
        
        System.out.println("Removing 10,000 items from a Linked list:");
        
        start = System.currentTimeMillis();
        
        for(b = 0; b<10000; b++){
            linked.remove(0);
        }
        
        end = System.currentTimeMillis();
        duration = end-start;
        
        System.out.println("Duration: " + duration + " Milliseconds");
    }
}
