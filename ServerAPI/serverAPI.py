import sys
sys.path.append("./")
from database.store import Persist
from html_page.web_page import UltimateTicTacToeGame
from logic.app_logic import Game
from userInfo.users import User
from bottle import Bottle, run, request, static_file
import os
import signal





class TicTacToeServer(Bottle):
    """TicTacToe Server consisting of routing requests to different modules
    """

    Tictocgame = Game()

    def __init__(self):
        super(TicTacToeServer, self).__init__()
        self.route("/", callback=self.begin)
        self.route("/begin", callback=self.begin)
        self.route("/registration", callback=self.registration)
        self.route("/register_user",
                   callback=self.register_user, method="POST")
        self.route("/login", callback=self.login_game)
        self.route("/login_user", callback=self.login_user, method="POST")
        self.route("/start_game", callback=self.start)
        self.route("/restart_game", callback=self.restart)
        self.route("/playing", callback=self.play)
        self.route("/save_user", callback=self.save_user, method="POST")
        self.route("/load_user/<username>", callback=self.load_user)
        self.route("/check_other_player_move/<username>/<state>",
                   callback=self.check_other_player_move)
        self.route("/next_move", method="GET", callback=self.handle_next_move)
        self.route("/update_user/<username>", callback=self.user_update)
        self.route("/halt", callback=self.halt)
        self.route("/static/<fname>", callback=self.serve)
        self.route("/save_game", callback=self.save)
        self.route("/load_game/game_id", callback=self.load)

    def load(cls, gameID):
        """Load the game state.

        Argument:
            gameID: The ID of the game we want to load
        """
        Persist.load_game_state(gameID=gameID)

    def save(cls):
        """Save the game state.
        """
        Persist.store_game_state(cls.Tictocgame.getGameState()[
                                 0], "Player1", "Player2")

    def serve(self, fname):
        """Serve static files.

        Args:
            fname (str): The filename of the static file to be served.

        Returns:
            str: The content of the static file.
        """
        return static_file(fname, root='./html_page/')

    def halt(cls):
        """Halt the server.
        """
        sys.stderr.close()
        os.kill(os.getpid(), signal.SIGTERM)

    def restart(cls):
        """Restart the game.

        Returns:
            str: The HTML page of the restarted game.
        """
        cls.Tictocgame.setGameState([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']], ["NC", "NC", "NC", "NC", "NC", "NC", "NC", "NC", "NC"])
        cls.Tictocgame.outcome = 0
        cls.Tictocgame.next_subgrid = ""
        cls.Tictocgame.next_player = 'x'

        return UltimateTicTacToeGame.gamePage(cls.Tictocgame)

    def handle_next_move(self):
        """Handle the next move in the game.

        Returns:
            str: The HTML page of the game after the move.
        """
        index1 = int(request.query.index1)
        index2 = int(request.query.index2)
        user = request.query.user

        return self.next_move(index1, index2, user)

    @classmethod
    def saveUserPage(cls, username):
        """Save user profile.

        Args:
            username (str): The username of the user to be saved.

        Returns:
            str: Confirmation message of user creation.
        """
        user_ip = request.environ.get('REMOTE_ADDR')
        user = User(username=username, client=user_ip)
        user.save_user()

        return f"user {username} is created!"

    @classmethod
    def loadUserPage(cls, username):
        """Load user profile.

        Args:
            username (str): The username of the user to be loaded.

        Returns:
            str: Confirmation message of user loading.
        """
        user = User(username=username)
        user.load_user()
        return f"{username} Added to the game!"

    @classmethod
    def login_game(cls):
        """Login to the game.

        Returns:
            str: The HTML page of the login screen.
        """
        return UltimateTicTacToeGame.loginPage()

    def login_user(self):
        """Authenticate a user profile by checking it in the database.

        Returns:
            The login page again if a username is invalid, otherwise the game page.
        """
        if Persist.verify_login(request.forms.get("username"), request.forms.get("password")):
            return self.start_game()
        else:
            return UltimateTicTacToeGame.loginPage(second_try=True)

    @classmethod
    def start_game(cls):
        """ Send start_game request to app_services module
            Returns:
            str: HTML page containing game page.
        """
        return UltimateTicTacToeGame.startPage()

    def begin_game(cls):
        """ Send start_game request to app_services module
            Returns:
            str: HTML page containing game page.
        """
        return UltimateTicTacToeGame.beginPage(cls)

    def registration_game(cls):
        """ Send start_game request to app_services module
            Returns:
            str: HTML page containing game page.
        """
        return UltimateTicTacToeGame.registerPage()

    def register_user(self):
        """Register a user profile by storing it in the database.

        Returns:
            The registration page again if a username is invalid, otherwise the game page.
        """
        try:
            Persist.store_profile(request.forms.get(
                "username"), request.forms.get("password"))
            return self.start_game()
        except IOError:
            return UltimateTicTacToeGame.registerPage(second_try=True)

    @classmethod
    def play_game(cls):
        """ Send restart request to app_services module
            Returns:
            str: HTML page containing game log info.
        """
        return UltimateTicTacToeGame.gamePage(cls.Tictocgame)

    @classmethod
    def user_info_update(cls, username):
        """Send user_update request to users module with username as a parameter

        Args:
            username (str): The username of the user

        Returns:
            str: HTML page containing user updated information from html construction module.
        """

        user = User()
        user.update_username(username)
        return "user info updated"

    @classmethod
    def checkOtherPlayerMovePage(cls, state):
        """Send check_other_player_move request to game module with username as a parameter

        Args:
            state (Array): The matrix of the game state

        Returns:
            str: HTML page containing information about whether the other player has moved.
        """
        return f"current state: {state}"

    def save_user(self, username):
        """Handler for saving a user profile.

           Args:
                username (str): The username of the user to be loaded.
        """
        return self.saveUserPage(username)

    def load_user(self, username):
        """Handler for loading a user profile.
            Args:
                username (str): The username of the user to be loaded.
        """
        return self.loadUserPage(username)

    def check_other_player_move(self, state):
        """Handler for checking the other player's move in the game.
            Args:
                state (Array): The matrix of the game state
        """
        return self.checkOtherPlayerMovePage(state)

    def next_move(cls, index1, index2, user):
        """Handler for the next move in the game.

        Args:
            index1 (int): The index of the row in the game grid.
            index2 (int): The index of the column in the game grid.
            user (str): The username of the user.

        Returns:
            str: HTML page containing information about the next move.
        """
        try:
            cls.Tictocgame.next_move(index1, index2, user)
        except ValueError:
            return UltimateTicTacToeGame.gamePage(cls.Tictocgame, "You made an illegal move")

        return UltimateTicTacToeGame.gamePage(cls.Tictocgame)

    def start(self):
        """Handler for starting the server."""
        return self.start_game()

    def begin(self):
        """Handler for starting the server."""
        return self.begin_game()

    def registration(self):
        """Handler for starting the server."""
        return self.registration_game()

    def play(self):
        """Handler for restarting the game."""
        return self.play_game()

    def user_update(self, username):
        """Handler for user update.
           Args:
                username (str): The username of the user"""
        return self.user_info_update(username)


if __name__ == "__main__":
    server = TicTacToeServer()
    server.run(host="localhost", port=8080, debug=True)
