# Store Module

This module is implementing a SQLite3 database system. This is implemented through the use of the Persist class. The Persist class consists solely of static methods, as there is no reason to instantiate a class whose sole purpose is to manage persistant storage. It contains functionality for managing user profiles and game states. \
[UML diagram](arch_store_UML_diagram.pdf) 

## User Profiles

The managing of user profiles is done through the use of 3 methods. store_profile stores the user profile, load_profile loads the user profile from storage, and destroy_profile removes the user profile from storage permanantly. In addition to this, each user profile contains an attribute for wins and losses. There are two methods, add_win and add_loss, to increment these respectively. In addition there are also methods to update username and update password. There is also a method to verify the login credentials of a given user.

## Game States

The mananaging of game sessions is done through the use of 3 methods. store_game_state stores game object, load_game_state returns all of the data necessary to rebuild the game object, and destroy_game_state removes a game state from storage permanantly. Also, there is a method get_games that will return the game IDs of all games associated with a given username.
