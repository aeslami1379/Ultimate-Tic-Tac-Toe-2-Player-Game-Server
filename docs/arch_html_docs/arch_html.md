# HTML construction Module:
---
web_page.py: 

It was discussed and agreed with teammates that JavaScript would be used for the pages instead of Python, enhancing the interactivity and responsiveness of the user interface.

# Description: 
The startPage method in web_page.py generates HTML for the Ultimate Tic-Tac-Toe game's start page. It adheres to HTML5 standards, specifies English language, and includes metadata in the head section. CSS styles are embedded for visual presentation. The body contains a centered container div with the main heading 'Ultimate Tic-Tac-Toe!' and two buttons, 'Start Game' and 'Load Game,' which redirect users accordingly. Button styles change on hover for improved user experience.

The beginPage method in web_page.py generates the HTML code for the initial page of the Ultimate Tic-Tac-Toe game. It establishes the document as HTML5 with English language specification and provides metadata in the head section. The body contains visible content within a container div, including a prominent heading and a descriptive paragraph inviting player participation. User interaction is facilitated through links for registration and login. CSS styles are applied to enhance visual presentation. Overall, it serves as an inviting introduction to the game, encouraging user engagement for an enjoyable experience.


The gamePage method in the web_page.py module generates the HTML code for the game page of the Ultimate Tic-Tac-Toe game. It includes embedded CSS styles for various elements, defining the layout and appearance of the game board. The page displays the game state, allowing players to make moves within individual subgrids. Instructions and player information are dynamically updated based on the game state. Additionally, buttons are provided for actions such as stopping the game, saving the game progress, and restarting the game. The layout is structured to enhance user interaction and facilitate gameplay, contributing to an immersive gaming experience.

The registerPage method in web_page.py generates HTML for the registration page of the Ultimate Tic-Tac-Toe game. It includes CSS styles for layout and visual presentation. The page features a form for user registration with fields for username and password. Upon submission, the form sends data to the server for processing. If a registration attempt fails due to an existing username, an error message is displayed. Additionally, a 'Next' button allows users to navigate to the next page. Overall, the page provides a user-friendly interface for registering to play the game.


The loginPage method in web_page.py generates HTML for the login page of the Ultimate Tic-Tac-Toe game. It includes CSS styles for layout and visual presentation. The page features a form for user login with fields for username and password. Upon submission, the form sends data to the server for authentication. If login credentials are incorrect, an error message is displayed. Overall, the page provides a user-friendly interface for logging in to play the game.


The win_page method in web_page.py generates HTML for the win page of the Ultimate Tic-Tac-Toe game. It incorporates CSS styles for layout and visual appeal. The page displays a congratulatory message indicating the winning player. Two buttons are provided: one to play again and another to end the game. The HTML code dynamically substitutes the winning player's name into the page. Overall, the page offers a visually pleasing and user-friendly interface for celebrating game victories and managing gameplay options.


# Purpose: 
The UltimateTicTacToeGame class plays a central role in crafting the Tic Tac Toe game page, providing an array of methods to dynamically generate pages based on user interactions. With functions like startPage, beginPage, gamePage, registerPage, loginPage, and win_page, this class empowers the server to respond dynamically to user actions, enriching the overall gaming experience and fostering deeper engagement. Through carefully constructed HTML structures and well-applied styling, each generated page seamlessly combines functionality and visual appeal, ensuring easy navigation and an aesthetically pleasing presentation. From the inviting start page to the thrilling win page, the UltimateTicTacToeGame class orchestrates a cohesive journey, guiding users through different phases of gameplay with finesse. By offering multiple avenues for user interaction and feedback, this class demonstrates the game's adaptability and responsiveness, transforming it into an immersive digital experience that captivates players and encourages continued participation.





