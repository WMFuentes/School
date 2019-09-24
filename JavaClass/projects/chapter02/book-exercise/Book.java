/**
 * A class that maintains information on a book.
 * This might form part of a larger application such
 * as a library system, for instance.
 *
 * @author (William Fuentes)
 * @version (9/8/2019)
 */
class Book
{
    // The fields.
    private String author;
    private String title;
    // New field created, called refNumber
    private String refNumber;

    /**
     * Set the author and title fields when this object
     * is constructed.
     */
    public Book(String bookAuthor, String bookTitle)
    {
        author = bookAuthor;
        title = bookTitle;
        // refNumber initialized to "" rather than null.
        refNumber = "";
    }

    /**
     * This method allows us to assign a refNumber to a book.
     */
    public void setRefNumber(String ref)
    {
        refNumber = ref;
    }
    
    /**
     * A simple method to return the refNumber set in the previous method.
     */
    public String getRefNumber()
    {
        return refNumber;
    }
}
