from flamme_rouge_alternate import *
import unittest

class MyTest(unittest.TestCase):
    def test_create_player(self):
        player = Player()
        self.assertTrue(isinstance(player, Player))

    def test_draw_hand_by_name(self):
        player = Player()
        card_value = player.roller.draw.cards[0].value
        player.draw_hand(player.roller, player.draw_amount, card_value)
        self.assertEqual(0, len(player.roller.hand.cards))
        self.assertEqual(1, len(player.roller.select.cards))
        self.assertEqual(3, len(player.roller.discard.cards))

if __name__ == '__main__':
    unittest.main()