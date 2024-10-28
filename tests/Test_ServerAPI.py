import sys
import unittest
from unittest.mock import patch, MagicMock
from bottle import HTTPResponse
from ServerAPI.serverAPI import TicTacToeServer


class TestTicTacToeServer(unittest.TestCase):
    def setUp(self):
        self.server = TicTacToeServer()

    @patch('ServerAPI.serverAPI.Persist')
    def test_load(self, mock_Persist):
        game_id = "example_game_id"
        self.server.load(game_id)
        mock_Persist.load_game_state.assert_called_once_with(gameID=game_id)

    @patch('ServerAPI.serverAPI.Persist')
    def test_save(self, mock_Persist):
        self.server.save()
        mock_Persist.store_game_state.assert_called_once_with(
            self.server.Tictocgame.getGameState()[0], "Player1", "Player2"
        )

    @patch('ServerAPI.serverAPI.static_file')
    def test_serve(self, mock_static_file):
        fname = "example.html"
        expected_content = "Content of example.html"
        mock_static_file.return_value = expected_content
        result = self.server.serve(fname)
        self.assertEqual(result, expected_content)

    @patch('ServerAPI.serverAPI.os')
    @patch('ServerAPI.serverAPI.signal')
    @patch('ServerAPI.serverAPI.sys')
    def test_halt(self, mock_sys, mock_signal, mock_os):
        self.server.halt()
        mock_sys.stderr.close.assert_called_once()
        mock_os.kill.assert_called_once()

    def test_restart(self):
        result = self.server.restart()
        self.assertIsInstance(result, str)

    @patch('ServerAPI.serverAPI.request')
    def test_handle_next_move_empty_index(self, mock_request):
        mock_request.query.index1 = ''
        mock_request.query.index2 = ''
        with self.assertRaises(ValueError):
            self.server.handle_next_move()

    @patch('ServerAPI.serverAPI.Persist')
    def test_save_user_duplicate_username(self, mock_Persist):
        mock_Persist.store_profile.side_effect = IOError("Username in use")
        username = "duplicate_user"
        with self.assertRaises(IOError):
            self.server.save_user(username)

    @patch('ServerAPI.serverAPI.Persist')
    def test_load_user(self, mock_Persist):
        username = "example_username"
        mock_Persist.load_profile.side_effect = IOError("Username does not exist")
        with self.assertRaises(IOError):
            self.server.load_user(username)

    def test_check_other_player_move(self):
        state = "example_state"
        result = self.server.check_other_player_move(state)
        self.assertIsInstance(result, str)

    def test_next_move(self):
        index1, index2, user = 0, 0, "example_user"
        result = self.server.next_move(index1, index2, user)
        self.assertIsInstance(result, str)

    def test_start(self):
        result = self.server.start()

    def test_begin(self):
        result = self.server.begin()
        self.assertIsInstance(result, str)

    def test_registration(self):
        result = self.server.registration()
        self.assertIsInstance(result, str)



    def test_play(self):
        result = self.server.play()
        self.assertIsInstance(result, str)

    @patch('ServerAPI.serverAPI.Persist')
    def test_user_update_invalid_username(self, mock_Persist):
        mock_Persist.update_username.side_effect = ValueError("Username must be 1-15 alphanumerical characters")
        invalid_username = "invalid_username"
        with self.assertRaises(ValueError):
            self.server.user_update(invalid_username)

if __name__ == '__main__':
    unittest.main()
