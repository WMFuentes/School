/**
 *  This class is the main class of the "World of Zuul" application. 
 *  "World of Zuul" is a very simple, text based adventure game.  Users 
 *  can walk around some scenery. That's all. It should really be extended 
 *  to make it more interesting!
 * 
 *  To play this game, create an instance of this class and call the "play"
 *  method.
 * 
 *  This main class creates and initialises all the others: it creates all
 *  rooms, creates the parser and starts the game.  It also evaluates and
 *  executes the commands that the parser returns.
 * 
 * @author  Michael Kölling and David J. Barnes
 * @version 2016.02.29
 */
import java.util.Random;
import java.util.ArrayList;

public class Game 
{
    private Parser parser;
    private Room currentRoom;
    private Room lastRoom;
    private ArrayList<Room> roomsList = new ArrayList<Room>();
    private Random random = new Random();
    private TransporterRoom transporter;
        
    /**
     * Create the game and initialise its internal map.
     */
    public Game() 
    {
        createRooms();
        parser = new Parser();
    }

    /**
     * Create all the rooms and link their exits together.
     */
    private void createRooms()
    {
        Room outside, theater, pub, lab, office, transporter;
      
        // create the rooms
        outside = new Room("outside the main entrance of the university");
        theater = new Room("in a lecture theater");
        pub = new Room("in the campus pub");
        lab = new Room("in a computing lab");
        office = new Room("in the computing admin office");
        transporter = new TransporterRoom("in the transporter room");
        
        // initialise room exits
        outside.setExit("east", theater);
        outside.setExit("south", lab);
        outside.setExit("west", pub);
        outside.setExit("north", transporter);

        theater.setExit("west", outside);

        pub.setExit("east", outside);

        lab.setExit("north", outside);
        lab.setExit("east", office);

        office.setExit("west", lab);

        currentRoom = outside;  // start game outside
        lastRoom = null;
        
        roomsList.add(outside);
        roomsList.add(theater);
        roomsList.add(pub);
        roomsList.add(lab);
        roomsList.add(office);
    }

    /**
     *  Main play routine.  Loops until end of play.
     */
    public void play() 
    {            
        printWelcome();

        // Enter the main command loop.  Here we repeatedly read commands and
        // execute them until the game is over.
                
        boolean finished = false;
        while (! finished) {
            Command command = parser.getCommand();
            finished = processCommand(command);
        }
        System.out.println("Thank you for playing.  Good bye.");
    }

    /**
     * Print out the opening message for the player.
     */
    private void printWelcome()
    {
        System.out.println();
        System.out.println("Welcome to the World of Zuul!");
        System.out.println("World of Zuul is a new, incredibly boring adventure game.");
        System.out.println("Type '" + CommandWord.HELP + "' if you need help.");
        System.out.println();
        System.out.println(currentRoom.getLongDescription());
    }

    /**
     * Given a command, process (that is: execute) the command.
     * @param command The command to be processed.
     * @return true If the command ends the game, false otherwise.
     */
    private boolean processCommand(Command command) 
    {
        boolean wantToQuit = false;

        CommandWord commandWord = command.getCommandWord();

        switch (commandWord) {
            case UNKNOWN:
                System.out.println("I don't know what you mean...");
                break;

            case HELP:
                printHelp();
                break;
            
            // Exercise 8.15
            case EAT:
                System.out.println("You have eaten now and you are not hungry anymore.");
                break;

            case GO:
                goRoom(command);
                break;
                
            // Exercise 8.23
            case BACK:
                goBack(command);
                break;

            case QUIT:
                wantToQuit = quit(command);
                break;
        }
        return wantToQuit;
    }

    // implementations of user commands:

    /**
     * Print out some help information.
     * Here we print some stupid, cryptic message and a list of the 
     * command words.
     */
    private void printHelp() 
    {
        System.out.println("You are lost. You are alone. You wander");
        System.out.println("around at the university.");
        System.out.println();
        System.out.println("Your command words are:");
        parser.showCommands();
    }

    /** 
     * Try to go in one direction. If there is an exit, enter the new
     * room, otherwise print an error message.
     */
    private void goRoom(Command command) 
    {
        if(!command.hasSecondWord()) {
            // if there is no second word, we don't know where to go...
            System.out.println("Go where?");
            return;
        }

        String direction = command.getSecondWord();

        // Try to leave current room.
        Room nextRoom = currentRoom.getExit(direction);

        if (nextRoom == null) {
            System.out.println("There is no door!");
        }
        //Exercise 8.45
        if (nextRoom.isTransporterRoom(nextRoom)){
            currentRoom = nextRoom;
            System.out.println(currentRoom.getShortDescription());
            System.out.println("The floor drops from beneath you and you drop into darkness...");
            lastRoom = null;
            //int size = roomsList.size();
            currentRoom = roomsList.get((random.nextInt(roomsList.size())));
            System.out.println("You softly land "+currentRoom.getShortDescription());
        }
        else {
            lastRoom = currentRoom;
            currentRoom = nextRoom;
            System.out.println(currentRoom.getLongDescription());
        }
    }
    
    /**
     * Exercise 8.23 & 8.24
     * If a player types "back", the character will return to the previous room.
     * If a second word is entered, it is ignored and does not affect the movement.
     */
    private void goBack(Command command){
        Room tempRoom;
        if(lastRoom == null){
            System.out.println("You cannot go back.");
        }
        else{
            //This is intended to take "back" as literal jokingly, trapping the player between 2
            //rooms if they keep typing back, going back and forth.
            tempRoom = currentRoom;
            currentRoom = lastRoom;
            System.out.println(currentRoom.getLongDescription());
            lastRoom = tempRoom;
        }
    }

    /** 
     * "Quit" was entered. Check the rest of the command to see
     * whether we really quit the game.
     * @return true, if this command quits the game, false otherwise.
     */
    private boolean quit(Command command) 
    {
        if(command.hasSecondWord()) {
            System.out.println("Quit what?");
            return false;
        }
        else {
            // Exercise 14.44
            parser.createFile();
            return true;  // signal that we want to quit
        }
    }
    
    public ArrayList<Room> getList(){
        return roomsList;
    }
}
