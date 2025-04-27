#Toni Bethune
#04202025
#P5HW
#Creating a game

"""
Fire Dodging Game
A character-based game where players select one of four characters and navigate an obstacle course
while dodging fire falling from the sky.
"""
import random
import time
import os

def create_character():
    """
    Creates a new character for the game based on user selection.
    
    Returns:
        dict: A dictionary containing character attributes
    """
    characters = [
        {"name": "Knight", "health": 100, "speed": 3, "shield": 2, "symbol": "🛡️"},
        {"name": "Archer", "health": 80, "speed": 5, "shield": 0, "symbol": "🏹"},
        {"name": "Wizard", "health": 60, "speed": 4, "shield": 1, "symbol": "🧙"},
        {"name": "Ninja", "health": 70, "speed": 7, "shield": 0, "symbol": "🥷"}
    ]
    
    print("\n=== CHARACTER SELECTION ===")
    for i, character in enumerate(characters, 1):
        print(f"{i}. {character['name']} {character['symbol']}")
        print(f"   Health: {character['health']} | Speed: {character['speed']} | Shield: {character['shield']}")
        print()
    
    while True:
        try:
            choice = int(input("Select your character (1-4): "))
            if 1 <= choice <= 4:
                return characters[choice - 1]
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

def display_character(character):
    """
    Displays the character's attributes.
    
    Args:
        character (dict): The character dictionary with attributes
    """
    print("\n=== YOUR CHARACTER ===")
    print(f"Name: {character['name']} {character['symbol']}")
    print(f"Health: {character['health']}")
    print(f"Speed: {character['speed']}")
    print(f"Shield: {character['shield']}")

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_fire_obstacles(width, intensity):
    """
    Generates fire obstacles falling from the sky.
    
    Args:
        width (int): Width of the game field
        intensity (int): Number of fire obstacles to generate
        
    Returns:
        list: Positions of fire obstacles
    """
    fire_positions = []
    for _ in range(intensity):
        position = random.randint(0, width - 1)
        fire_positions.append(position)
    return fire_positions

def display_game_field(width, position, fire_positions, character, health, score, difficulty):
    """
    Displays the game field with fire in the sky and character on the ground.
    
    Args:
        width (int): Width of the game field
        position (int): Player's current position
        fire_positions (list): Positions of fire obstacles
        character (dict): Character information
        health (int): Current health
        score (int): Current score
        difficulty (int): Current difficulty level
    """
    # Display top border
    print("=" * (width + 2))
    
    # Display sky with fire
    sky_rows = 3  # Show multiple rows of sky to see fire coming
    for row in range(sky_rows):
        sky_row = [" "] * width
        # Put fire in upper rows for visual warning
        if row == sky_rows - 1:  # Fire appears in the last sky row
            for pos in fire_positions:
                sky_row[pos] = "🔥"
        print("|" + "".join(sky_row) + "|")
    
    # Display ground with character
    ground_row = [" "] * width
    ground_row[position] = character['symbol']
    print("|" + "".join(ground_row) + "|")
    
    # Display bottom border
    print("=" * (width + 2))
    
    # Display stats
    print(f"Health: {health} | Score: {score} | Level: {difficulty}")
    
    # Show control hints
    print("\nControls:")
    print("A = Move Left | D = Move Right | Q = Quit")

def run_obstacle_course(character):
    """
    Runs the main game loop where the character dodges fire obstacles.
    
    Args:
        character (dict): The character dictionary with attributes
        
    Returns:
        int: Final score
    """
    width = 20  # Width of the game field
    position = width // 2  # Starting position (middle)
    score = 0
    health = character['health']
    shield = character['shield']
    
    print("\nGet ready to dodge the fire (🔥) falling from the sky!")
    print("The fire will appear above you before it falls - move to avoid it!")
    print("Press Enter to start...")
    input()
    
    difficulty = 1
    game_active = True
    
    while game_active and health > 0:
        clear_screen()
        # Generate fire obstacles based on difficulty
        intensity = 1 + difficulty // 2
        fire_positions = generate_fire_obstacles(width, intensity)
        
        # Show the game field WITH fire in the sky so player can see what's coming
        display_game_field(width, position, fire_positions, character, health, score, difficulty)
        
        # Get player's move
        valid_move = False
        while not valid_move:
            move = input("Enter your move (A/D/Q): ").lower()
            
            if move == 'a' and position > 0:  # Move left
                position -= 1
                valid_move = True
            elif move == 'd' and position < width - 1:  # Move right
                position += 1
                valid_move = True
            elif move == 'q':  # Quit game
                print("\nGame ended early.")
                game_active = False
                valid_move = True
            else:
                if move == 'a' and position == 0:
                    print("You can't move further left!")
                elif move == 'd' and position == width - 1:
                    print("You can't move further right!")
                elif move not in ['a', 'd', 'q']:
                    print("Invalid move. Use A (left), D (right), or Q (quit).")
        
        if not game_active:
            break
            
        # Now check if the move was successful in dodging the fire
        clear_screen()
        
        # Show the result of the move (fire has "fallen")
        print("=" * (width + 2))
        
        # Display fire that has "fallen"
        fire_row = [" "] * width
        for pos in fire_positions:
            fire_row[pos] = "🔥"
        print("|" + "".join(fire_row) + "|")
        
        # Display character after move
        character_row = [" "] * width
        character_row[position] = character['symbol']
        print("|" + "".join(character_row) + "|")
        
        # Display bottom border
        print("=" * (width + 2))
        
        # Display stats
        print(f"Health: {health} | Score: {score} | Level: {difficulty}")
        
        # Check for collision
        if position in fire_positions:
            damage = max(1, 5 - shield)  # Shield reduces damage
            health -= damage
            print(f"Hit by fire! Lost {damage} health.")
            time.sleep(1.5)  # Give player time to see they were hit
        else:
            print("You dodged the fire! +1 point")
            time.sleep(0.7)  # Brief pause to show success
        
        # Increment score and difficulty
        score += 1
        if score % 10 == 0:
            difficulty += 1
            print(f"Difficulty increased to level {difficulty}!")
            time.sleep(1)
    
    return score

def show_game_over(score):
    """
    Displays the game over screen with final score.
    
    Args:
        score (int): The player's final score
    """
    print("\n====================")
    print("    GAME OVER")
    print("====================")
    print(f"Final Score: {score}")

def main():
    """
    Main function that runs the game.
    """
    print("Welcome to the FIRE DODGE CHALLENGE!")
    print("Select a character and dodge the fire falling from the sky.")
    
    # Create character
    character = create_character()
    display_character(character)
    
    # Run the game
    score = run_obstacle_course(character)
    
    # Game over
    show_game_over(score)
    
    # Ask to play again
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
