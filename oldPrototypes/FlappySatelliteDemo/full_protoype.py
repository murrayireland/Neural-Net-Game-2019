""" Simple movement program """

import arcade
import os
import random

#Set sprite sizes
SPRITE_SCALING_PLAYER = 0.25
SPRITE_SCALING_FIRE = 0.01
SPRITE_SCALING_CLOUD = 0.05
FIRE_COUNT = 1
CLOUD_COUNT = 3
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 900

MOVEMENT_SPEED = 2

CPU_SPEED = 1.25 
CPU_TRACK_SPEED = 0.5

SCROLL_SPEED = 1
class Satellite(arcade.Sprite):

    def update(self):
        #Change satellite position to new x and y
        self.center_x += self.change_x
        self.center_y += self.change_y

        #Ensure satellite doesn't run off screen
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

    def cpu_update(self, Fire,Player):
        
        #If fire is there, track it else, track player
        if (self.center_x <Fire.center_x and Fire.center_x < SCREEN_WIDTH):
            self.center_x += CPU_SPEED
        elif (self.center_x > Fire.center_x and Fire.center_x < SCREEN_WIDTH):
            self.center_x -= CPU_SPEED
        
        else: 
            if (self.center_x <Player.center_x):
                self.center_x += CPU_TRACK_SPEED
            else:
                self.center_x -= CPU_TRACK_SPEED

            
         
        if (self.center_y <Fire.center_y and Fire.center_x < SCREEN_WIDTH):
            self.center_y += CPU_SPEED
        elif (self.center_y > Fire.center_y and Fire.center_x < SCREEN_WIDTH):
            self.center_y -= CPU_SPEED
        else: 
            if (self.center_y <Player.center_y):
                self.center_y += CPU_TRACK_SPEED
            else:
                self.center_y -= CPU_TRACK_SPEED



class Fire(arcade.Sprite):
    """
    This class represents the emergency on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the fire to a random spot to the right of the screen
        self.center_y = random.randrange(0,SCREEN_HEIGHT )
        self.center_x = SCREEN_WIDTH + random.randrange(0,SCREEN_WIDTH/2) #


    def update(self):

        # Move the fire
        self.center_x -= SCROLL_SPEED 

        # See if the fire has fallen off the bottom of the screen.
        # If so, reset it.
        if self.left < 0:
            self.reset_pos()

 
class Cloud(arcade.Sprite):
    """
    This class represents the Clouds on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the fire to a random spot to the right of the screen
        self.center_y = random.randrange(0,SCREEN_HEIGHT )
        self.center_x = SCREEN_WIDTH + random.randrange(0,SCREEN_WIDTH) #


    def update(self):

        # Move the fire
        self.center_x -= SCROLL_SPEED 

        # See if the fire has fallen off the left of the screen.
        # If so, reset it.
        if self.left < 0:
            self.reset_pos()       

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold the sprite lists
        self.player_list = None
        self.fire_sprite_list=None
        self.cpu_list = None 
        self.clouds_list = None
        # Set up the player info
        self.player_sprite = None
        self.player_score = 0

        #Set up CPU sprite
        self.cpu_sprite = None
        self.cpu_score = 0

        # Background image will be stored in this variable
        self.background = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.fire_sprite_list = arcade.SpriteList()
        self.cpu_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()

        # Set up the player
        self.player = True
        self.player_score = 0
        self.player_sprite = Satellite("images/satellite.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        self.player_health = 100
        #Set up CPU
        self.cpu = True
        self.cpu_score = 0
        self.cpu_health = 100
        self.cpu_sprite = Satellite("images/cpu.png", SPRITE_SCALING_PLAYER)
        self.cpu_sprite.center_x = SCREEN_WIDTH - 50
        self.cpu_sprite.center_y = SCREEN_HEIGHT - 50
        self.cpu_list.append(self.cpu_sprite)
        

        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        self.background = arcade.load_texture("images/fire.jpg")

        # Create the fires
        for i in range(FIRE_COUNT):

            # Create the fire instance
            fire = Fire("images/fire.png", SPRITE_SCALING_FIRE)

            # Position the fire
            fire.center_x = random.randrange(SCREEN_WIDTH)
            fire.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.fire_sprite_list.append(fire)
        
        # Create the Cloud
        for i in range(CLOUD_COUNT):

            # Create the fire instance
            cloud=Cloud("images/clouds.png", SPRITE_SCALING_CLOUD)

            # Position the fire
            cloud.center_x = random.randrange(SCREEN_WIDTH)
            cloud.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.clouds_list.append(cloud)
    
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        
        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw all the sprites.
        self.fire_sprite_list.draw()
        self.player_list.draw()
        self.cpu_list.draw()
        self.clouds_list.draw()

        # Put the text on the screen.
         
        # Player Score
        score_player= f"Player Score: {self.player_score}"
        arcade.draw_text(score_player, 10, 20, arcade.color.WHITE, 14)

        #CPU Score   
        score_cpu= f"CPU Score: {self.cpu_score}"
        arcade.draw_text(score_cpu, SCREEN_WIDTH-155, 20, arcade.color.RED, 14)

        # Player Scor
        player_health = int(self.player_health)
        health_player= f"Player Health: {player_health}"
        arcade.draw_text((health_player), 10, 50, arcade.color.WHITE, 14)

        #CPU Score   
        cpu_health = int(self.cpu_health)
        health_cpu= f"CPU Health: {cpu_health}"
        arcade.draw_text(health_cpu, SCREEN_WIDTH-155, 50, arcade.color.RED, 14)



    def update(self, delta_time):
        """ Movement and game logic """
        
        #Get CPU movement 

        # Call update on player and fire sprites (The sprites don't do much in this
        # example though.)
        if self.player:
            self.player_list.update()
        
        self.fire_sprite_list.update()
        self.clouds_list.update()
        #Update cpu satellite
        if self.cpu:
            for cpu in self.cpu_list:
                cpu.cpu_update(self.fire_sprite_list[0],self.player_list[0])
            self.cpu_list.update()

            # Generate a list of all emergencies that collided with the satellite.
            hit_list = arcade.check_for_collision_with_list(self.cpu_sprite,self.fire_sprite_list)

            # Loop through each colliding fire, remove it, and add to the cpu_score.
            for fire in hit_list:
                fire.reset_pos()
                self.cpu_score += 1

            # Generate a list of all emergencies that collided with the satellite.
            hit_list = arcade.check_for_collision_with_list(self.cpu_sprite,self.clouds_list)

            # Loop through each colliding sprite, remove it, and add to the player_score.
            for cloud in hit_list:
                self.cpu_health -= 0.1

                if self.cpu_health <0:
                    self.cpu_sprite.kill()
                    self.cpu = False

        if self.player:
            # Generate a list of all emergencies that collided with the satellite.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.clouds_list)

            # Loop through each colliding sprite, remove it, and add to the player_score.
            for cloud in hit_list:
                self.player_health -= 0.1

                if self.player_health <0:
                    self.player_sprite.kill()
                    self.player = False






    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:

            # Generate a list of all sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.fire_sprite_list)

            # Loop through each colliding sprite, remove it, and add to the player_score.
            for fire in hit_list:
                fire.reset_pos()
                self.player_score += 1



    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
