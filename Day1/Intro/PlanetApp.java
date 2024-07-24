import java.util.Scanner;

public class PlanetApp{

    public static String [] planets ;


    public static void main(String[] args) {
        int M = 9 ;
        Scanner input = new Scanner(System.in);
        planets = new String[M];
        int menuChoice ;
        final int FINISHED = 9 ;
        int level = -1 ;
        String newPlanetName ;
        int planetIndexToUpdate ;
        do{
            System.out.println("###############################################");
            System.out.println("1. Enter 1 to add a planet to the list");
            System.out.println("2. Enter 2 to update a planet based on its ID");
            System.out.println("3. Enter 3 to display the number of planets in the list");
            System.out.println("4. Enter 4 to delete a planet in the list");
            System.out.println("5. Enter 5 to display the list of planets");
            System.out.println(FINISHED+". Enter "+FINISHED+" to exit");
            System.out.println("###############################################");
            System.out.println("Make a choice: ");
            menuChoice = input.nextInt();

            switch(menuChoice){
                case 1: {
                    System.out.println("Enter your new planet's name: ");
                    newPlanetName = "";
                    newPlanetName = input.next();
                    level += 1; // level = level + 1;
                    planets[level] = newPlanetName ;
                }
                break;
                case 2: {
                    System.out.print("Enter your planets ID to update : ");
                    planetIndexToUpdate = input.nextInt();
                    if ( planetIndexToUpdate >= 0 && planetIndexToUpdate <= level) {
                        String oldPlanet = planets[planetIndexToUpdate] ;
                        System.out.println("Enter your new name for the current planet at index  "+ planetIndexToUpdate + " : ");
                        newPlanetName = input.next();
                        planets[planetIndexToUpdate] = newPlanetName ;
                        System.out.println("You updated the planet name from "+ oldPlanet + " to " + newPlanetName);
                    } else {
                        System.out.println("Sorry! We could not find the index of the planet your need!");
                    }
                }
                break;
                case 3:{
                    System.out.println("You now have "+(level+1)+" planets in your list");
                } ;break;
                case 5:
                    if (level > -1 && level < planets.length)
                    {
                        System.out.print("\nList of planets: [");
                        for(int i=0 ; i <= level; i++) {
                            System.out.print(planets[i] + " ");
                        };  
                        System.out.println("]");
                    }  else {
                         System.out.println("No planet to print for now ");
                    }
                break;
                case FINISHED:
                    System.out.println("You are exiting the app. Thank you!");
                break;
                default:
                    System.out.println("We do not recognize the choice you made!");
                break;

            }

        } while (menuChoice != FINISHED) ;



    }
}