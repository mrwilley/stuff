# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:37:24 2020

@author: ljo20
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:04:23 2020

@author: ljo20
"""

import random


class Player():
    def __init__(self):
        
        self.draw_count = 4
        
        self.roller_draw = Deck({3:3, 4:3, 5:3, 6:3, 7:3})
        self.roller_draw.shuffle()
        self.roller_removed = []
        self.roller_hand = []
        self.roller_discard = []
        
        self.sprinter_draw = Deck({2:3, 3:3, 4:3, 5:3, 9:3})
        self.sprinter_draw.shuffle()
        self.sprinter_removed = []
        self.sprinter_hand = []
        self.sprinter_discard = []
        
        self.selected_cards = {'roller': [], 'srinter': []}

    def get_deck_info(self):
        return self.deck_setups[self.p_type]

    def setup_shuffle(self):
        for d in self.draw_decks:
            self.draw_decks[d].shuffle()
        
    def get_draw_amount(self):
        return self.draw_count[self.p_type]

    def check_remain(self, deck):
        return len(deck)

    def draw_hand(self, hand, deck, draw_amount):
        for d in range(1, draw_amount):
            hand.append(deck.draw_card())
        print(hand)

    def select_card(self, hand, remove, discard):
        print('Pick a value to play')
        select = input()
        self.choose_card()

class Muscle_Team:
    def __init__(self): 
        
        self.draw_count = 1
        
        self.roller_draw = Deck({3:3, 4:3, 5:3, 6:3, 7:3})
        self.roller_draw.shuffle()
        self.roller_removed = []
        self.roller_hand = []
        self.roller_discard = []
        
        self.sprinter_draw = Deck({2:3, 3:3, 4:3, 5:4, 9:3})
        self.sprinter_draw.shuffle()
        self.sprinter_removed = []
        self.sprinter_hand = []
        self.sprinter_discard = []


class Peloton_Team:
    def __init__(self):
        
        self.draw_count = 1
        
        self.roller_draw = Deck({3:3, 4:3, 5:3, 6:3, 7:3, 'attack!':2})
        self.roller_draw.shuffle()
        self.roller_removed = []
        self.roller_hand = []
        self.roller_discard = []


class Deck:
    def __init__(self, deck_dict = {}):
        self.cards = []
        self.build(deck_dict)

    def build(self, deck_dict):
        for k, v in deck_dict.items():
            for x in range(1, v + 1):
                self.cards.append(Card(k))
    
    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0 , -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def draw_card(self):
        return self.cards.pop()



class Card:
    def __init__(self, value):
        self.value = value
    
    def show(self):
        print(self.value)