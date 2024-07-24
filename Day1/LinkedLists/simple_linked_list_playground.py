from LinkedList import LinkedList
from Node import Node

def main():

    """
    flowers = LinkedList()
    flowers.insert(Node("Rose"))
    flowers.insert(Node("Sun Flower"))
    flowers.insert(Node("Tulip"))
    flowers.display() # should display 3 flowers above
    flowers.insert(Node("Orchid"))
    flowers.insert(Node("Lily"))
    flowers.insert(Node("Daisy"))
    flowers.display() # should display all 6 flowers above
    flowers.insert(Node("Cherry Blosom"))
    flowers.insert(Node("Iris"))
    flowers.insert(Node("Peony"))
    flowers.insert(Node("Marigold"))
    #flowers.display() # should display all 10 flowers above
    """
    

    songs = LinkedList()
    user_choice = ""
    FINISHED = False
    while(not(FINISHED)):

        print("1. Press 1 to add a song\nPress 2 to display the list of songs")
        print("\n Press 3 to display the number of songs.\n4 To delete a song. \n 9 To exit")
        user_choice = int(input("Enter a menu choice: "))
        if user_choice == 1:
            song_title = input("Enter the title of the new song to add: ")
            new_song_object = Node(song_title)
            songs.insert(new_song_object)
        elif user_choice == 2:
            songs.display()
        elif user_choice == 3:
            print("You have ",songs.item_counts()," songs in your album")
        elif user_choice == 4:
            title_of_song_to_delete = input("Enter the title of the song to delete")
            title_of_song_to_delete = title_of_song_to_delete.lower()
            songs.delete(title_of_song_to_delete)
        elif user_choice == 9:
            print("You are exiting the program. Thank you!")
            FINISHED = True
        else:
            print("We cant find that choice on the user menu")

    songs.display()

main()
    
