import java.util.ArrayList;

/**
 * This class stores information about a post in a social network news feed. 
 * The main part of the post consists of a (possibly multi-line)
 * text message. Other data, such as author and time, are also stored.
 * 
 * @author Michael Kölling and David J. Barnes
 * @version 0.3
 * Exercise 11.7 completed by changin the username to protected and accessing
 * it from the MessagePost class.
 * 
 * by William Fuentes
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
     * Exercise 11.7 reformatting of the returned messagePost. Accomplished
     * by setting the username field to Protected so we can access it from 
     * the MessagePost class.
     */
    public String toString()
    {
        return super.username + "\n" + message + "\n" + 
        super.toString() + "\n";
    }
    
    /**
     * Display the details of this post.
     * 
     * (Currently: Print to the text terminal. This is simulating display 
     * in a web browser for now.)
     */
    public void display()
    {
        System.out.println(toString());
    }
}
