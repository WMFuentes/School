import java.util.ArrayList;

/**
 * This class stores information about a post in a social network news feed. 
 * The main part of the post consists of a (possibly multi-line)
 * text message. Other data, such as author and time, are also stored.
 * 
 * @author Michael Kölling and David J. Barnes
 * @version 0.2
 * 
 * Exercise 10.6 completed. You can find the printShortSummary method at the bottom.
 * by William Fuentes 10/27/19
 */
public class MessagePost extends Post
{
    private String message;  // an arbitrarily long, multi-line message

    /**
     * Constructor for objects of class MessagePost.
     * 
     * @param author    The username of the author of this post.
     * @param text      The text of this post.
     */
    public MessagePost(String author, String text)
    {
        super(author);
        message = text;
    }

    /**
     * Return the text of this post.
     * 
     * @return The post's message text.
     */
    public String getText()
    {
        return message;
    }
    
    /**
     * Exercise 10.6. This method prints a simple summary using a method in the superclass Post.
     */
    public void printShortSummary()
    {
        String name = getUserName();
        System.out.println("Message post from " + name + ".");
    }
    
    /**
     * Exercise 11.2
     */
    public void display()
    {
        System.out.println(message);
    }
}
