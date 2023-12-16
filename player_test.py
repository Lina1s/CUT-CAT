import unittest
from unittest.mock import Mock, patch
import pygame as pg

GRAVITY = 9.81  # Define the gravity constant as per your game's physics; adjust if necessary

# Assuming your_player_module is where your Player class is defined.
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Mock the Pygame Surface and images returned by get_rect()
        self.mock_screen = Mock()
        self.mock_image = Mock()
        self.mock_image.get_rect.return_value = Mock(topleft=(0, 0), size=(32, 32))
        self.mock_font = Mock()

        # Assume each image list has 3 images for running right and left
        self.player_images_r = [self.mock_image] * 3
        self.player_images_l = [self.mock_image] * 3
        self.player_img_dead = [self.mock_image] * 2

        # Instantiate your Player
        self.player = Player(self.mock_screen, self.player_images_r, self.player_images_l, self.player_img_dead, self.mock_font)


    def test_change_dir_no_keypress(self):
        with patch('pygame.key.get_pressed', return_value={pg.K_LEFT: False, pg.K_RIGHT: False}):
            self.player.change_dir()
            self.assertEqual(self.player.movement[0], 0)
            self.assertFalse(self.player.is_run)

    def test_change_dir_keypress_left(self):
        with patch('pygame.key.get_pressed', return_value={pg.K_LEFT: True, pg.K_RIGHT: False}):
            self.player.change_dir()
            self.assertEqual(self.player.movement[0], -1)
            self.assertTrue(self.player.is_run)

if __name__ == '__main__':
    unittest.main()
