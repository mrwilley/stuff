# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:04:23 2020

@author: ljo20
"""

import random


class Deck_Types:
    def __init__(self):
        roller = {3:3, 4:3, 5:3, 6:3, 7:3}
        sprinter = {2:3, 3:3, 4:3, 5:3, 9:3}
        roller_peloton = {3:3, 4:3, 5:3, 6:3, 7:3, 'attack!':2}
        sprinter_muscle = {2:3, 3:3, 4:3, 5:4, 9:3}

        self.deck_setups = {
                'human': {'roller' : roller, 'sprinter' : sprinter},
                'muscle_team': {'roller' : roller, 'sprinter' : sprinter_muscle},
                'peloton_team': {'roller' : roller_peloton}
                }
        
        self.draw_count = {'human': 4, 'muscle_team':1, 'peloton_team':1}


class Player(Deck_Types):
    def __init__(self, name, colour, p_type):
        Deck_Types.__init__(self)
        
        self.name = name
        self.colour = colour        
        self.p_type = p_type
        self.p_decks_setup = self.get_deck_info()
        
        self.draw_decks = self.build_player_decks()
        self.setup_shuffle()
        
        self.removed = self.build_empty_decks()
        self.hand = self.build_empty_decks()
        self.discard = self.build_empty_decks()

    def get_deck_info(self):
        return self.deck_setups[self.p_type]

    def build_player_decks(self):
        deck_builds = {}
        for deck_name in self.p_decks_setup.keys():
                deck_builds[deck_name] = Deck(self.p_decks_setup[deck_name])                      
        return deck_builds

    def build_empty_decks(self):
        deck_builds = {}
        for deck_name in self.p_decks_setup.keys():
            deck_builds[deck_name] = Deck()                     
        return deck_builds
        
    def get_draw_amount(self):
        return self.draw_count[self.p_type]

    def check_remain(self, deck):
        return len(deck)
        
#    def show_hand(self):
#        for card in self.hand:
#            card.show()

    def setup_shuffle(self):
        for d in self.draw_decks:
            self.draw_decks[d].shuffle()



class Deck:
    def __init__(self, deck_dict = {}):
        self.cards = []
        self.deck_dict = deck_dict
        self.build()

    def build(self):
        for k, v in self.deck_dict.items():
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

    def draw_hand(self, draw_amount):
        draw_amount = self.get_draw_amount()
        return draw_amount
#        for d in range(draw_amount):
#            if len(deck) == 0:
#                if len(discard_deck) == 0:
#                    break
#                deck = discard_reshuffle()
#            
#        
#        self.hand.append(deck.draw_card())
#        return self

class Card:
    def __init__(self, value):
        self.value = value
    
    def show(self):
        print(self.value)

#class Draw_Pile:
#    def __init__(self):
#        pass
#    
#class Discard_Pile:
#    def __init__(self):
#        pass
#
#class Remove_Pile:
#    def __init__(self):
#        pass
#   
#class Hand_Pile:
#    def __init__(self):
#        pass
#
#class Play_Pile:
#    def __init__(self):
#        pass
#
#class Exhaust_Pile:
#    def __init__(self):
#        pass