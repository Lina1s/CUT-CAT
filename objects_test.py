import unittest
from unittest.mock import Mock
from objects import Block # Import your actual class

class TestGameObject(unittest.TestCase):
    def setUp(self):
        # Mock the Pygame Surface and texture returned by get_rect()
        self.mock_screen = Mock()
        self.mock_texture = Mock()
        self.mock_texture.get_rect.return_value = Mock(topleft=(0, 0), size=(32, 32))

        self.pos = (100, 150)
        self.collider = True
        self.name = 'test_block'

        # Instantiate your GameObject
        self.game_object = Block(self.pos, self.mock_texture, self.mock_screen, self.collider, self.name)
    def test_draw_no_scroll(self):
        # With no scrolling, the object should be blitted at its original position
        scroll = (0, 0)
        returned_rect = self.game_object.draw(scroll)

        self.mock_screen.blit.assert_called_once_with(self.mock_texture, self.pos)
        self.assertEqual(returned_rect, self.game_object)

    def test_draw_with_scroll(self):
        # With scrolling, the object's blit position should be adjusted
        scroll = (50, 50)
        expected_position_after_scroll = (self.pos[0] - scroll[0], self.pos[1] - scroll[1])
        returned_rect = self.game_object.draw(scroll)
        self.mock_screen.blit.assert_called_once_with(self.mock_texture, expected_position_after_scroll)
        self.assertEqual(returned_rect, self.game_object)

    def test_rect_is_updated_on_draw(self):
        # Ensure that the rect attribute is updated correctly after drawing
        scroll = (0, 0)
        initial_rect = self.mock_texture.get_rect()
        returned_rect = self.game_object.draw(scroll)

        self.assertEqual(self.game_object.rect, initial_rect)
        self.assertEqual(returned_rect.rect, initial_rect)

if __name__ == '__main__':
    unittest.main()