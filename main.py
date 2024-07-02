import pygame
import sys

# Constants for window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080

def main():
    """Main function to initialize and run the game."""
    # Initialize Pygame
    pygame.init()
    
    # Set up display surface
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Airship Assault')

    # Load images
    ship_surf = pygame.image.load('assets/imgs/placeholder-aircraft.png').convert_alpha()

    # Main game loop
    while True:  # Runs forever to keep the game running
        handle_events()
        update_display(display_surface, ship_surf)

def handle_events():
    """Handle input events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_display(display_surface, ship_surf):
    """Update the display with the current game state."""
    # Fill the display surface with a black background
    display_surface.fill((0, 0, 0))
    
    # Draw the ship image onto the display surface
    display_surface.blit(ship_surf, (0, 0))

    # Update the display
    pygame.display.update()

if __name__ == "__main__":
    main()