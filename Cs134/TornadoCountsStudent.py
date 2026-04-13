# @author Your name
# This program processes tornado data
def main():
    # Named constants for menu choices (COMPLETED)
    SHOW_STATES_IN_RANGE = "1"
    CHANGE_TORNADO_COUNT = "2"
    QUIT = "3"
    
    # ADD CODE 1
    
    # ADD CODE 2
 
    choice = "0"
    while(choice != QUIT): # while header COMPLETED
        # Show the menu COMPLETED
        print("=====================================================")
        print("(1) Show states with tornado counts in a given range.")
        print("(2) Change the tornado count for a given state.")
        print("(3) Quit")
        
        # Get the user's menu choice COMPLETED (This stays as a string)
        choice = input("Choice? ")
        
        # Process the menu choice PARTIALLY COMPLETED
        if choice == SHOW_STATES_IN_RANGE:
            # ADD CODE 3 

        elif choice == CHANGE_TORNADO_COUNT:
            # ADD CODE 4 
                
        elif choice != QUIT:
            print("Invalid choice entered.")
        print()
            
    # ADD CODE 5

# define getTornadoData here

# define showStatesInRange here
            
# define linearSearch from the notes here

# define saveTornadoData here

main()
