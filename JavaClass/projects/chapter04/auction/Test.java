
/**
 * Test for Auction class
 *
 * @author William Fuentes
 * @version 9/19/19
 */
public class Test
{
    public void Test()
    {
        Auction auction1 = new Auction();
        Person person1 = new Person("Michael");
        Person person2 = new Person("Jim");
        Person person3 = new Person("Creed");
        Person person4 = new Person("Dwight");
        auction1.enterLot("Sabre Copier");
        auction1.enterLot("Dunder Mifflin Paper");
        auction1.enterLot("Schrute Beets");
        auction1.makeABid(1, person1, 10);
        auction1.makeABid(2, person2, 10);
        auction1.makeABid(1, person3, 15);
        auction1.close();
    }
}
