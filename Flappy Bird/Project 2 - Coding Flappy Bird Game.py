# ------------------------------------ Flappy Bird Game ------------------------------------- #
import random  # For generating random number
import sys  # We will use sys.exit to exit the Program
import pygame  # Pygame for Creating Game using Python
from pygame.locals import *  # Basic pygame imports


# ------------------------- Global Variables For Game --------------------- #

FPS = 32  # Frames per Second For Rendering images
SCREEN_WIDTH = 289  # Width of Screen
SCREEN_HEIGHT = 511  # Height of Screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Initialize a window or screen for display
GROUND_Y = (SCREEN_HEIGHT * 0.3) + 34  # For our Base image
GAME_SPRITES = {}  # For all kind of images
GAME_SOUNDS = {}  # For all kind of Sounds
PLAYER = 'gallery/Sprites/bird.png'  # path of Bird image
BACKGROUND = 'gallery/Sprites/Background.png'  # path of Background image
PIPE = 'gallery/Sprites/Pipe.png'  # path of Pipe image

# ------------------------------------------------------------------ #

# --------------------------------- Functions -------------------------- #


# ---------------------- Function For Welcome Screen ------------------- #
def welcomeScreen():
    """
    Shows welcome images on the Screen
    """
    player_x = int(SCREEN_WIDTH - 300)  # For Bird x Position
    player_y = int((SCREEN_HEIGHT - GAME_SPRITES['player'].get_height() + 25)/2)  # For Bird y position

    message_x = int(SCREEN_WIDTH - GAME_SPRITES['message'].get_width())  # For message x Position
    message_y = int(SCREEN_HEIGHT - 530)  # For message y position

    base_x = 0

    while True:
        for event in pygame.event.get():  # get events from the queue
            # if user click on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):  # KEYDOWN == any key press
                pygame.quit()
                sys.exit()

            # if user presses the space or up key start the game for them
            elif event.type == KEYDOWN or (event.type == K_SPACE or event.type == K_UP):
                return
            else:
                # .blit(image for blit, x and y position )
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))  # Screen is a surface where all images will be blit
                SCREEN.blit(GAME_SPRITES['player'], (player_x, player_y))
                SCREEN.blit(GAME_SPRITES['message'], (message_x, message_y))
                SCREEN.blit(GAME_SPRITES['base'], (base_x, GROUND_Y))

                pygame.display.update()  # Update portions of the screen for software displays
                FPS_CLOCK.tick(FPS)  # To control fps of the game.
# ----------------------------------------------------------------------------------------------------------- #


# ---------------------------------------- Function for Main Game ---------------------------------- #
def mainGame():
    """
    This is the main function, run's after welcome screen
    """
    score = 0  # Score variable for storing player score in game
    player_x = int(SCREEN_WIDTH - 300)  # For Bird x Position
    player_y = int((SCREEN_HEIGHT - GAME_SPRITES['player'].get_height() + 25)/2)  # For Bird y position
    base_x = 0  # For base image x position

    # Create two pipes for blitting on the screen
    new_pipe1 = getRandomPipe()
    new_pipe2 = getRandomPipe()

    # my list for upper pipe
    upper_pipe = [
        {'x': SCREEN_WIDTH + 200, 'y': new_pipe1[0]['y']},
        {'x': SCREEN_WIDTH + 200 + (SCREEN_WIDTH/2), 'y': new_pipe2[0]['y']}
    ]

    # my list for lower pipe
    lower_pipe = [
        {'x': SCREEN_WIDTH + 200, 'y': new_pipe1[1]['y']},
        {'x': SCREEN_WIDTH + 200 + (SCREEN_WIDTH/2), 'y': new_pipe2[1]['y']}
    ]

    pipe_velocity_x = -4  # Moving speed of pipes x toward left   <-----

    player_velocity_y = -9  # speed of player spill down (y position)
    player_max_velocity_y = 10
    player_min_velocity_y = -8
    player_acceleration_y = 1

    player_flapped_velocity = -8  # velocity while flap
    player_flapped = False  # it is True when bird is flapping

    # Game Loop
    while True:
        for event in pygame.event.get():  # get events from the queue
            # if user click on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):  # KEYDOWN == any key press
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.type == K_SPACE or event.type == K_UP):
                if player_y > 0:
                    player_velocity_y = player_flapped_velocity
                    player_flapped = True
                    GAME_SOUNDS['wing'].play()

        # Storing isCollide Function in crashTest Variable
        crash_test = isCollide(player_x, player_y, upper_pipe, lower_pipe)
        if crash_test:
            return

        # Check for score
        player_mid_position = player_x + GAME_SPRITES['player'].get_width()/2  # center position of player

        for pipe in upper_pipe:
            pipe_mid_position = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2  # center position of player
            if pipe_mid_position <= player_mid_position < pipe_mid_position + 4:
                score += 1
                print(f"Your Score is {score}")
                GAME_SOUNDS['point'].play()

        # For movement of player
        if player_velocity_y < player_max_velocity_y and not player_flapped:
            player_velocity_y += player_acceleration_y

        if player_flapped:
            player_flapped = False
        player_height = GAME_SPRITES['player'].get_height()
        player_y = player_y + min(player_velocity_y, GROUND_Y - player_y - player_height)

        # move pipes to the left
        for upper_pipe, lower_pipe in zip(upper_pipe, lower_pipe):
            upper_pipe['x'] += pipe_velocity_x
            lower_pipe['x'] += pipe_velocity_x

        # add a new pipe when the first pipe is obout to cross the leftmost part of the screen
        if 0 < upper_pipe[0]['x'] < 5:
            new_pipe = getRandomPipe()
            upper_pipe.append(new_pipe[0])
            lower_pipe.append(new_pipe[1])

        # if the pipe is out of screen, remove it
        if upper_pipe[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upper_pipe.pop(0)
            lower_pipe.pop(0)

        # Let's blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))  # bilt background

        for upper_pipe, lower_pipe in zip(upper_pipe, lower_pipe):  # blit pipes
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upper_pipe['x'], upper_pipe['y']))  # blit upper pipes
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lower_pipe['x'], lower_pipe['y']))  # blit lower pipes

        SCREEN.blit(GAME_SPRITES['base'], (base_x, GROUND_Y))  # blit base
        SCREEN.blit(GAME_SPRITES['player'], (player_x, player_y))  # blit player

        my_digits = [int(x) for x in list(str(score))]
        width = 0
        for digits in my_digits:
            width += GAME_SPRITES['numbers'][digits].get_width()
        x_offset = (SCREEN_WIDTH - width)/2

        for digits in my_digits:
            SCREEN.blit(GAME_SPRITES['numbers'][digits], (x_offset, SCREEN_WIDTH * 0.12))
            x_offset += GAME_SPRITES['numbers'][digits].get_width()
        pygame.display.update()
        FPS_CLOCK.tick(FPS)

# ----------------------------------------------------------------------------------------------------- #


# ----------------------------------- For for random pipes ------------------------- #
def getRandomPipe():
    """
    generate two pipes (one rotated for top, and one bottom straight ) for blitting on the screen
    """
    pipe_height = GAME_SPRITES['pipe'][0].get_height()   # For Pipe Height
    offset = SCREEN_HEIGHT / 3  # For top rotated pipe
    y2 = offset + random.randrange(0, int(SCREEN_HEIGHT - GAME_SPRITES['base'].get_height() + 1.2 * offset))
    # lower pipe y position

    pipe_x = SCREEN_WIDTH + 10  # For x position of upper pipe and lower pipe
    y1 = pipe_height - y2 + offset  # upper pipe y position
    pipe = [
        {'x': pipe_x, 'y': -y1},  # For upper pipe (that's why in -1)
        {'x': pipe_x, 'y': y2}  # For lower pipe
    ]
    return pipe
# ----------------------------------------------------------------------------------- #


def isCollide(player_x, player_y, upper_pipe, lower_pipe):
    if player_y > GROUND_Y - 25 or player_y < 0:
        GAME_SOUNDS['hit'].play()
        return True

    for pipe in upper_pipe:
        pipe_height = GAME_SPRITES['pipe'][0].get_height()
        if player_y < pipe_height + pipe['y'] and abs(player_x - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lower_pipe:
        if (player_y + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(player_x - pipe['x']) < \
                GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    return False

# -------------------------------------------------------------------------------------- #
# ------------------------------------------ !!!!! ---------------------------------------------- #


if __name__ == '__main__':
    # This will be the main point from where our Game start's
    pygame.init()  # initialize all imported pygame modules
    FPS_CLOCK = pygame.time.Clock()  # create an object to help track time
    pygame.display.set_caption('FlappyBird By Sheheryar')  # Set the current window caption

    # ---------------------------- Adding All Images in Game_Sprites Dictionary ------------------------ #

    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/Sprites/Zero.png').convert_alpha(),
        pygame.image.load('gallery/Sprites/One.png').convert_alpha(),
        pygame.image.load('gallery/Sprites/Two.png').convert_alpha(),
        pygame.image.load('gallery/Sprites/Three.png').convert_alpha(),
        pygame.image.load('gallery/Sprites/Four.png').convert_alpha(),
        pygame.image.load('gallery/Sprites/Five.png').convert_alpha(),
        pygame.image.load('gallery/Sprites/Seven.png').convert_alpha(),
        pygame.image.load('gallery/Sprites/Eight.png').convert_alpha(),
        pygame.image.load('gallery/Sprites/Nine.png').convert_alpha()
    )  # Adding all numbers images in Game Sprites Dictionary after storing in a tuple
    # Convert_alpha == change the pixel format of an image including per pixel alphas)

    GAME_SPRITES['message'] = pygame.image.load('gallery/Sprites/message.png').convert_alpha()  # Adding a message image
    GAME_SPRITES['base'] = pygame.image.load('gallery/Sprites/Base.png').convert_alpha()  # Adding a Base image
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()  # Adding a Background image
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()  # Adding a Bird image

    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),  # Rotate image (180)
                            pygame.image.load(PIPE))  # Pipe image for base
    # -------------------------------------------------------------------------------------- #

    # ---------------------------- Adding All Sounds in Game_Sounds Dictionary ------------------------ #

    # pygame.mixer.Sound() == Create a new Sound object from a file or buffer object
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/Audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/Audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/Audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/Audio/swooshing.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/Audio/wing.wav')

    # Game Loop
    while True:
        welcomeScreen()  # Shows the welcome screen util the user presses a button
        mainGame()  # This is the main Game Function
