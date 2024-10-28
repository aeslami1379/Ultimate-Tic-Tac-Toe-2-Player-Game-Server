import sys
sys.path.append("../")

import unittest
from html_page.web_page import UltimateTicTacToeGame


class TestUltimateTicTacToe(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
    def test_startPage(self):
        expected_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Tic-Tac-Toe - Start Page</title>
</head>
<body>
    <div class="container">
        <h1>Ultimate Tic-Tac-Toe!</h1>
        <button onclick="window.location.href='playing'">Start Game</button>
        <button onclick="window.location.href='load_game'">Load Game</button>
    </div>
</body>
</html>"""

        self.assertEqual(UltimateTicTacToeGame.startPage(), expected_html)

    def test_beginPage(self):
        expected_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Tic-Tac-Toe</title>
</head>
<body>
    <div class="container">
        <h1>Welcome to Ultimate Tic-Tac-Toe</h1>
        <p>Ultimate Tic-Tac-Toe is an exciting twist on the classic game of Tic-Tac-Toe, offering a strategic challenge for players of all ages.</p>
        <a href="registration" class="btn">Register Now</a>
        <a href="login" class="btn">Login</a>
    </div>
</body>
</html>
"""
        self.assertEqual(UltimateTicTacToeGame.beginPage(), expected_html)

    def test_gamePage(self):
        expected_html = '''
            <body>
                
                 <div class="panel">
                    <p style="font-weight: bold";>INSTRUCTION</p>
                    <p>{user1}'s  move</p>
                    <p> Your move could  be played {nsubgrid}</p>
                    <p style="color: black;font-weight: bold;">{error}</p>
                    <button onclick="window.location.href='halt'">Stop</button>
                    <button onclick="window.location.href='save_game'">Save game</button>
                    <button onclick="window.location.href='restart_game'">Restart game</button>
                </div>
                <div class="game-container">
                    <table class="big_table live">
                        <tr class="1">
                            <td class="1">
                                <table class="little_table col-1_row-1">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=0&index2=0&user={user}'"> {matrix[0][0]} </button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=0&index2=1&user={user}'"> {matrix[0][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=0&index2=2&user={user}'"> {matrix[0][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=0&index2=3&user={user}'"> {matrix[0][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=0&index2=4&user={user}'"> {matrix[0][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=0&index2=5&user={user}'"> {matrix[0][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=0&index2=6&user={user}'"> {matrix[0][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=0&index2=7&user={user}'"> {matrix[0][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=0&index2=8&user={user}'"> {matrix[0][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="2">
                                <table class="little_table col-2 row-1">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=1&index2=0&user={user}'"> {matrix[1][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=1&index2=1&user={user}'"> {matrix[1][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=1&index2=2&user={user}'"> {matrix[1][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=1&index2=3&user={user}'"> {matrix[1][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=1&index2=4&user={user}'"> {matrix[1][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=1&index2=5&user={user}'"> {matrix[1][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=1&index2=6&user={user}'"> {matrix[1][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=1&index2=7&user={user}'"> {matrix[1][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=1&index2=8&user={user}'"> {matrix[1][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="3">
                                <table class="little_table col-3 row-1">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=2&index2=0&user={user}'">{matrix[2][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=2&index2=1&user={user}'">{matrix[2][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=2&index2=2&user={user}'">{matrix[2][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=2&index2=3&user={user}'">{matrix[2][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=2&index2=4&user={user}'">{matrix[2][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=2&index2=5&user={user}'">{matrix[2][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=2&index2=6&user={user}'">{matrix[2][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=2&index2=7&user={user}'">{matrix[2][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=2&index2=8&user={user}'">{matrix[2][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr class="2">
                            <td class="1">
                                <table class="little_table col-1 row-2">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=3&index2=0&user={user}'">{matrix[3][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=3&index2=1&user={user}'">{matrix[3][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=3&index2=2&user={user}'">{matrix[3][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=3&index2=3&user={user}'">{matrix[3][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=3&index2=4&user={user}'">{matrix[3][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=3&index2=5&user={user}'">{matrix[3][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=3&index2=6&user={user}'">{matrix[3][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=3&index2=7&user={user}'">{matrix[3][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=3&index2=8&user={user}'">{matrix[3][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="2">
                                <table class="little_table col-2 row-2">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=4&index2=0&user={user}'">{matrix[4][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=4&index2=1&user={user}'">{matrix[4][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=4&index2=2&user={user}'">{matrix[4][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=4&index2=3&user={user}'">{matrix[4][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=4&index2=4&user={user}'">{matrix[4][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=4&index2=5&user={user}'">{matrix[4][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=4&index2=6&user={user}'">{matrix[4][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=4&index2=7&user={user}'">{matrix[4][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=4&index2=8&user={user}'">{matrix[4][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="3">
                                <table class="little_table col-3 row-2">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=5&index2=0&user={user}'">{matrix[5][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=5&index2=1&user={user}'">{matrix[5][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=5&index2=2&user={user}'">{matrix[5][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=5&index2=3&user={user}'">{matrix[5][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=5&index2=4&user={user}'">{matrix[5][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=5&index2=5&user={user}'">{matrix[5][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=5&index2=6&user={user}'">{matrix[5][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=5&index2=7&user={user}'">{matrix[5][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=5&index2=8&user={user}'">{matrix[5][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr class="3">
                            <td class="1">
                                <table class="little_table col-1 row-3">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=6&index2=0&user={user}'">{matrix[6][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=6&index2=1&user={user}'">{matrix[6][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=6&index2=2&user={user}'">{matrix[6][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=6&index2=3&user={user}'">{matrix[6][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=6&index2=4&user={user}'">{matrix[6][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=6&index2=5&user={user}'">{matrix[6][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=6&index2=6&user={user}'">{matrix[6][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=6&index2=7&user={user}'">{matrix[6][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=6&index2=8&user={user}'">{matrix[6][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="2">
                                <table class="little_table col-2 row-3">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=7&index2=0&user={user}'">{matrix[7][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=7&index2=1&user={user}'">{matrix[7][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=7&index2=2&user={user}'">{matrix[7][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=7&index2=3&user={user}'">{matrix[7][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=7&index2=4&user={user}'">{matrix[7][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=7&index2=5&user={user}'">{matrix[7][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=7&index2=6&user={user}'">{matrix[7][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=7&index2=7&user={user}'">{matrix[7][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=7&index2=8&user={user}'">{matrix[7][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="3">
                                <table class="little_table col-3 row-3">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=8&index2=0&user={user}'">{matrix[8][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=8&index2=1&user={user}'">{matrix[8][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=8&index2=2&user={user}'">{matrix[8][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=8&index2=3&user={user}'">{matrix[8][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=8&index2=4&user={user}'">{matrix[8][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=8&index2=5&user={user}'">{matrix[8][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=8&index2=6&user={user}'">{matrix[8][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=8&index2=7&user={user}'">{matrix[8][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=8&index2=8&user={user}'">{matrix[8][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </div>
                
            </body>
                '''
        self.assertEqual(UltimateTicTacToeGame.gamePage(), expected_html)

    
    def test_registerPage(self):
        expected_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ultimate Tic-Tac-Toe - Register</title>
        </head>
        <body>
            <div class="container">
                <h1>Register</h1>
                <form action="/register_user" method="POST">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                    <p style="color: red; display: none;">Username already exists. Please try another username.</p>
                    <div class="btn-container">
                        <button class="btn register" type="submit">Register</button>
                    </div>
                </form>
                <div class="btn-container">
                    <a href="start_game" class="btn next">Next</a>
                </div>
            </div>
        </body>
        </html>
        """

        self.assertEqual(UltimateTicTacToeGame.registerPage(), expected_html)

    def test_loginPage(self):
        expected_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ultimate Tic-Tac-Toe - Login</title>
        </head>
        <body>
            <div class="container">
                <h1>Login</h1>
                <form action="/login_user" method="POST">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                    <p style="color: red; display: none;">Invalid username or password. Please try again.</p>
                    <div class="btn-container">
                        <button class="btn login" type="submit">Login</button>
                    </div>
                </form>
                <div class="btn-container">
                    <a href="start_game" class="btn next">Next</a>
                </div>
            </div>
        </body>
        </html>
        """

        self.assertEqual(UltimateTicTacToeGame.loginPage(), expected_html)

    def win_page(self):
        expected_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ultimate Tic-Tac-Toe - Win</title>
        </head>
        <body>
            <div class="container">
                <h1>Congratulations!</h1>
                <p>You have won the game!</p>
                <div class="btn-container">
                    <a href="start_game" class="btn next">Next</a>
                </div>
            </div>
        </body>
        </html>
        """

        self.assertEqual(UltimateTicTacToeGame.winPage(), expected_html)



if __name__ == '__main__':
    unittest.main()


