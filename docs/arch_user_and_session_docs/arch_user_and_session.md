# Sprint 1

## User Info Module
The updated userInfo module now implements just a User Class in the users.py file. The functionality has been reduced to the core needs of a User.
It now provides public user methods for updating a users name,password and users history.
update_username, which updates the calling Users username attribute and calls on the database module to update the users name in the database.
update_password, which updates the calling Users password attribute and calls on the database module to update the users password in the database.
update_user_history, that adds a win or loss to the calling Users history attribute, and wins or losses attribute and once again calls on the database module to update the Users info in the database.
A public method is also provided to display a users game history, providing a string showing the total games played, wins, losses and overall win/ratio.
There are also private methods: __save_user__, that saves a user to the database using the database module and __load_user__, which has planned functionality
for Sprint 2, which will load previously saved user information. The __load_user__ method may become a public method as the project progresses in Sprint 2. 
Some planned functionality that may be implemented along with the __load_user__ function is to implement a friends list for a User.


## Session Management Module
The updated sessionManagement module still implements a single Session class in the session.py file. The Session class represents a single
game session, where only 2 users can be present, it keeps track of the users in the session as well as the user client ids via a dictionary, it also generates a session id for each session. 
There are 4 public methods in the class, terminate_session, add_player, remove_player and get_session_info. 
terminate_session removes all users from the game session, and deletes the session instance. add_player adds a user object to the
session, only if there is a slot available to join. remove_player removes a user from the session, and if that leaves 0 users in the session, terminates the session.
get_session_info returns a string detailing the current session_id and the players in the session. There are also two private methods, __validate_session__ and __generate_id__.
__validate_session__ validates an active game session, checking that the session has a valid game id. __generate_id__ generates an id for a game session instance,
This is not a complete implementation and in sprint 2 I will look to add functionality to broaden the utility of the Session class. I will also look to generate a unique
session id.

## UML Diagram
Below is a UML diagram representing the planned organization and interaction of both modules. This is version 1 of the
diagram and implementation is likely to change.
[UML diagram](arch_user_UMLDiagram_sprint1.png) 

---
# Sprint 2

## User Info Module
The changes to the core of the User class in users.py was minimal in sprint 2. It still has the same instance variables of that in sprint 1: 
- username (string)
- password (string)
- client (string)
- history (list)
- wins (string)
- losses (string)

There have been some updates to the user functionality:
- update_username, update_password, update_user_history and user_history have remained the same.
- save_user has been changed to a public method, along with the load user function.
    - save_user is called on a User object, checks if the User is already in the database(updating User attributes if there is a discrepancy between the local user variables and what is stored in the database), otherwise it saves all the Users info to the database.
    - load_user takes a username parameter, searches for the User in the database and returns a new User object with the stored information associated with the username. This function may be called outside a user instance to create a user (i.e: new = User.load_user("tyler")).
- verify_user_login is a new function implemented in Sprint 2. It takes a username and password as parameters and checks if a user is in the database and thus can be signed in.

The user module provides a level of abstraction between the serverApi module and the database module. It allows users to be created when certain requests like the saveUserPage and loadUserPage are made. This abstraction along with the database module can be useful if using our framework to design another type of turn based game, as the user information should not have major changes. 


## Session Management Module
Unfortunately, throughout sprint 2, we were unable to make great use of the session management module as my understanding of what constitutes a session was not correct. Towards the end of the sprint I tried implementing a proper multiplayer session management feature using the Beaker framework, but time was not on my side, and I was unable to finish this. However, I did make a few minor updates to how I was imagining the session management module to function.
The Session class still represents a single game session, where only 2 users can be present, it keeps track of the users in the session as well as the user client ids via a dictionary, it also generates a session id for each session. The 4 public functions from sprint 1 remain unchanged:
- terminate_session, add_player, remove_player and get_session_info are unchanged.
- the instance variable players (dictionary), remains unchanged.
- the instance variable session_id, now generates a random integer for a session id upon creation, without relying on the previously implemented private function: generate_session_id.
  - *Edit*: this functionality is not in master, it is implemented in branch: 103 - Ashfaq, our final update for the game that did not meet our code review deadline.
- the private method validate_session remains unchanged.
- the private method generate_session_id was removed.
- A new public function added in sprint 2 was get_users_in_session.
  - This function is similar to get_session_info, however it only returns a string of the usernames in a session.
  - This was required functionality for the serverAPI and app logic modules, as we needed a way to get the usernames from a session into a game object in the serverAPI module.

As mentioned earlier, this module was not really used in our final product for sprint 2. The idea of a session to me was that a session would be created ahead of a game object, using the session id to match to a game. As users are created they are then added to a session and hence a game. This is not the proper ideology as we found put late in the sprint, thus we have decided to tie a users session to whether they are the "x" or "o" player in the tic-tac-toe game. Further improvements for a proper multiplayer session management with more than 2 players, was placed on the backlog for a potential future sprint.
  - *Edit*: The Session Management was used in branch: 103 - Ashfaq, and can be seen in use in the serverAPI module, where a session is created ahead of a game object, and is used as we had initially planned.


## UML Diagram  
For the updated UML diagram reflecting the changes for both user info and session management modules please click here -> [UML diagram](arch_user_UMLDiagram_sprint2.png)