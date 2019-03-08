#Scaling for sprites
SPRITE_SCALING_POINTER = 1
SPRITE_SCALING_KEY = 1

#Set sprite sizes
SPRITE_SCALING_PLAYER = 1
SPRITE_SCALING_FIRE = 1
SPRITE_SCALING_CLOUD = 1
SPRITE_SCALING_BUTTON = 1
BACKGROUND_SCALING = 1

#Set number of elements to appear on screen (This will be removed when sprites are generated from co-ordinates)
#Window size
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 597

#Raspberry Pi speeds
RASP = 0
#RASP = 20

#Sprite Speeds
MOVEMENT_SPEED = 1.5 + RASP  #Player speeds
CPU_SPEED = 1.25 + RASP #Normal CPU speed
CPU_TRACK_SPEED = 0.5 + RASP #CPU speed when no emergency on screen and is tracking player movement
SCROLL_SPEED = 1 + RASP #Speed of background_sprite, clouds and fire sprites

#Variable for setting difficulty
CLOUD_DAMAGE = 0.1*(RASP +1)
HEALTH = 100

#Number of buttons in the menu
BUTTON = 2

#Image source (global variable so can be used in testing)
SOURCE=["images/background2.png","images/background3.png", "images/background2.png", "images/background3.png","images/sea.png"]
NNDir = "NNData/"
#PLayer's score for saving in Highscore file
Final_score = 0

#Game states
SPLASH = -1
START_PAGE = 0
INSTRUCT1 = 1
INSTRUCT2 = 2
GAME_PAGE = 3
END_PAGE = 4
ENTER_NAME = 5
HIGH_SCORE_PAGE = 6
FEEDBACK_PAGE = 7

#Demo states
#Game states
INS0 = 10
INS1 = 11
INS2 = 12
INS3 = 13
INS4 = 14
INS5 = 15
INS6 = 16
INS7 = 17
INS8 = 18
INS9 = 19

#Initial game state
STATE = START_PAGE

#Player co-ordinates
PLAYER_START_X = 50
PLAYER_START_Y = 50

#Demo co-ordinates
STARTX= 50
STARTY = 50

#CPU co-ordinates
CPU_START_X = 50
CPU_START_Y = SCREEN_HEIGHT - 50

#Variables used for joystick movement
DEAD_ZONE = 0.02
