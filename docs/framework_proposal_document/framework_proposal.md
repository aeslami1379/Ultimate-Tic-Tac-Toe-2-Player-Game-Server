# **Framework Proposal Document**

## Database

---
The database is heavily coupled and would require extensive refactoring to modularize it. The profile part of the database, where user profiles are stored, is the only part that would easily be decoupled from the project. This means that storing, loading, and destruction of user profiles would be virtually identical other than whatever other extra attributes a developer would want associated with a user profile. In addition to this, the login verification and updating of both username and passowrd would also remain the same.

The game state part of the database would have to be mostly refactored. If the new game is a two player turn based game, such as checkers and chess, then only some parts need to be refactored. This would be how the game is actually stored, as well as the attributes that are tictactoe specific such as ustate which says what player has won what grid and the next grid which says which says which grid must be played next. The attributes such as the two username IDs, the outcome, and next player would could remain the same to accommodate a turn based two player game as mentioned above. If a turn based game with greater than two players was to be implemented, additional username IDs could be added as attributes to be stored alongside the two username IDs to allow this.  

## User Info   

---
The user info module is one of, if not the most de-coupled modules in our project framework. For most turn based games a player would like to create a profile that stores their username and password, this is something that is more or less uniform, regardless of what type of turn-based game may be implemented. A user should also want to keep track of their game information, as it does now, with wins, losses and history. Now this part of the user information there is a little lee-way in regard to what you might want to tie to a user. For example if you were to be implementing a poker style game with our framework, you may want to keep track of something like overall winnings instead of outright wins or losses. Once again this is a very minor tweak that would have minimal effect on the features currently implemented for a user. In another case, looking at our backlog, you may want to implement a much larger multiplayer game, and in that instance you may want to have a friends list for a user. Something like this would require more work as new functionality for adding friends, removing friends, friends list info, etc. would need to be implemented. Overall, the user info module in our current framework would be adequate for any type of turn based game and the refactoring required would be minimal.  

## Session Management

---
The session management as it stands in our framework, is also quite de-coupled. The idea behind the current implementation is to simply keep track of which users are in a game(which is coupled to the game via the session_id). Regardless of what type of game object is implemented, as long as it has a parameter and attribute for a gameID, can be tied to a session and the users in the session. The current functionality in the Session class, terminate_session, add_player, remove_player, get_session_info, and get_users_in_session would require virtually no refactoring. The Session class as it stands does not require any persistence storage, and there are minimal use cases in the requests from the serverAPI module. As mentioned in our [README.md](../../README.md), the implementation of a Session is not being used, and we are managing sessions by assigning a player in a game to either "x" or "o". If we were to properly implement a Session by tracking a session via a variable in the HTML templates for different pages, this too would require minimal refactoring within the serverAPI and HTML templating modules in our framework. Any turn based game would have users playing, and tracking their unique session_ids in various HTML page would require minimal change. Once again, this module has a far reach in regard to use cases for various games and is heavily de-coupled compared to other modules.  

## HTML Module

---
The HTML module would have to undergo refactoring to extract game-independent components, ensuring reusability across multiple games. Standardized interfaces would need to be introduced to facilitate the integration of new games, defining methods for generating game-specific content and handling user interactions. The proposed architecture would have to separate game-specific logic from HTML generation, allowing for easy integration of new games without modifying existing code extensively. Detailed diagrams would illustrate the revised architecture, emphasizing the modular design and clear separation of concerns. A comparison would highlight the advantages of the DocGameFrame framework over the existing Ultimate Tic-Tac-Toe-specific architecture in terms of flexibility and scalability. Diagrams would visually demonstrate the differences between the two architectures, emphasizing the abstraction of game-specific details in the proposed framework. Developers would be provided with clear instructions on integrating new games into the framework, including guidelines for implementing game-specific logic and defining HTML templates. The framework would emphasize the importance of decoupling between HTML generation and game logic, enabling seamless integration of new games while minimizing code modifications.

The DocGameFrame framework proposal presents a structured method to boost the adaptability of the HTML module to support a variety of web-based games. Through refactoring the current codebase and adopting modular design principles, the framework guarantees scalability and straightforward integration for forthcoming game expansions. In-depth comparisons, elaborate diagrams, and precise usage guidelines empower developers to utilize the framework proficiently, cultivating a resilient environment for diverse web-based gaming encounters.

## ServerAPI   

---
The proposal for modularizing the ServerAPI framework aims to enhance flexibility and scalability, catering to diverse game types. Initially, the profile management component, being relatively decoupled, will undergo refinement to seamlessly accommodate additional user attributes while maintaining operational consistency. Simultaneously, adjustments to the game state management module will be made to align with the intricacies of different games. For instance, transitioning from tic-tac-toe to chess within the ServerAPI framework would require significant updates to the game state module. This involves revising storage mechanisms to handle complex board configurations and piece movements specific to chess, as well as incorporating attributes like castling availability and en passant possibilities. Furthermore, API endpoints and request/response formats would need updating to reflect the rules and mechanics of chess, including defining new endpoints for actions like moving chess pieces and handling special moves unique to chess. Additionally, validation logic within the API would be adjusted to enforce the rules of chess, ensuring that only valid moves are accepted and that the game progresses accordingly.

Moreover, to support turn-based games with multiple players, the API will be bolstered with flexible attribute management and scalable data structures, facilitating efficient handling of player-related information. By incorporating these enhancements, the ServerAPI will emerge as a robust framework for managing diverse gaming scenarios, fostering code maintainability and future scalability. Throughout these changes, the documentation and usage guidelines of the ServerAPI would be updated to reflect the transitions and provide clear instructions on how to interact with the API for different game types, ensuring a smooth and seamless integration of new game functionalities.

# App Logic Module Framework for Board Game

---
## Overview
The app logic module serves as a framework for implementing various board games. Although certain aspects of the module are applicable across different games, many features require customization to fit specific game mechanics.

## Components
1. **State of the Game**
   - Retains the current state of the game, including board positions, player information, and other relevant data.
   - For chess, state includes the positions of all pieces on the board, current player turn, and other game-specific variables.

2. **Players**
   - Tracks information about players participating in the game.
   - Each player is identified by a unique username or ID.

3. **Methods**
   - **getPlayers():** Retrieve information about the players involved in the game.
   - **getGameState():** Obtain the current state of the game.
   - **setGameState():** Update the state of the game based on game progress.
   - **setPlayers():** Modify player information as needed.

## Implementation for Chess
For the game of chess, certain aspects of the framework can be directly applied, while others require customization:

1. **State of the Game**
   - Tracks the positions of all chess pieces on the board.
   - Manages the current player turn and other game-specific variables.

2. **Players**
   - Records information about the two players engaged in the chess match, such as their usernames or IDs.

3. **Methods**
   - **getPlayers():** Returns the usernames of the two players.
   - **getGameState():** Provides the current positions of all chess pieces and other relevant game state information.
   - **setGameState():** Updates the board state after each move.
   - **setPlayers():** Allows for modifications to player information if necessary.

4. **Customizations for Chess**
   - **Next Move:** Determine the validity of moves according to chess rules and update the board accordingly.
   - **Winning Condition:** Check for checkmate or stalemate to determine the winner.
   - **Validating Moves:** Ensure that moves adhere to the rules of chess, considering factors like piece movement, capturing, and special moves (e.g., castling, en passant).

## Conclusion
While the app logic module provides a foundational framework for implementing board games, customization is necessary to accommodate the unique rules and mechanics of each game. By leveraging common functionalities and adapting them to specific game requirements, developers can efficiently create diverse board game experiences.
