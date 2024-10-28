# Tic-Tac-Toe Server Architecture

## 1. Server Class (TicTacToeServer)
- This class represents the main server application.
- It extends the Bottle class, which is a lightweight WSGI micro web-framework for Python.
- The server is initialized with routes for various functionalities of the game.

## 2. Routes
- Routes are defined using the `route()` method of the Bottle framework.
- Each route corresponds to a specific functionality of the Tic-Tac-Toe game, such as loading user data, saving user data, checking for the next move, etc.
- Each route has a corresponding handler method that processes the request and generates an appropriate response.

## 3. Handler Methods
- Handler methods are responsible for processing HTTP requests and generating responses.
- Examples of handler methods include `save_user()`, `load_user()`, etc.
- These methods interact with other components of the system to fulfill the requested functionality.

## 4. HTML Templates
- HTML templates are used to generate HTML pages dynamically.
- Templates are defined as multi-line strings (`html_template`) and are returned by various methods to generate HTML responses.

## 5. Additional Methods
- Apart from route handlers, there are additional methods like `next_move()`, `begin()`, `registration()`, etc., which likely handle game player state, begin game, and player registration operations.

## 6. Main Execution Block
- The main execution block creates an instance of the `TicTacToeServer` class and runs the server on localhost at port 8080.

## 7. UML diagram
- [UML](https://github.com/CS2005W24/term-project-teama/blob/ServerAPI_Final2/docs/arch_serverAPI_docs/serverAPI_UML.pdf) is a UML diagram representing

