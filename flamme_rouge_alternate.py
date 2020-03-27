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
        
        self.draw_amount = 4
        
        # Make the roller and sprinter cards
        self.roller_cards = self.build({3:3, 4:3, 5:3, 6:3, 7:3})
        self.sprinter_cards = self.build({2:3, 3:3, 4:3, 5:3, 9:3})
        
        # Create roller card areas
        self.roller_draw = Deck()
        self.roller_draw.add_to_deck(self.roller_cards)
        self.roller_draw.shuffle()
        self.roller_removed = Deck()
        self.roller_hand = Deck()
        self.roller_select = Deck()
        self.roller_discard = Deck()
        self.roller_turn = True
        
        #Create sprinter card areas
        self.sprinter_draw = Deck()
        self.sprinter_draw.add_to_deck(self.sprinter_cards)
        self.sprinter_draw.shuffle()
        self.sprinter_removed = Deck()
        self.sprinter_hand = Deck()
        self.sprinter_select = Deck()
        self.sprinter_discard = Deck()
        self.sprinter_turn = True
        
    def r_draw(self):
        self.roller_turn = self.draw_hand(
                self.roller_hand, self.sprinter_hand, self.roller_draw,
                self.roller_discard, self.draw_amount, self.roller_select,
                self.roller_turn)

    def s_draw(self):
        self.sprinter_turn = self.draw_hand(
                self.sprinter_hand, self.roller_hand, self.sprinter_draw,
                self.sprinter_discard, self.draw_amount, 
                self.sprinter_select, self.sprinter_turn)
    

    def build(self, deck_dict):
        card_list = []
        for k, v in deck_dict.items():
            for x in range(1, v + 1):
                card_list.append(Card(k))
        return card_list


    def check_remain(self, deck):
        return len(deck.cards)


    def draw_hand(self, hand, oppo_hand, deck, discard, draw_amount, select,
                  turn):
        if self.check_remain(oppo_hand) > 0:
            print('Must select a card from your drawn hand before drawing\
                  from this deck.')
        elif turn == False:
            print('You have already made the selection for this deck this turn.')
        else:
            for d in range(1, draw_amount + 1):
                if self.check_remain(deck) <= 0:
                    if self.check_remain(discard) <= 0:
                        break
                    else:
                        self.reshuffle_discard(discard, deck)
                hand.cards.append(deck.draw_card())
            
            print('\nYou have drawn the cards...\n')
            hand.show()
            
            self.select_card_to_play(hand, select, discard)

            return False

    def reveal_choice(self, r_value, s_value):
        print('\nYour Roller is moving ', r_value)
        print('\nYour Sprinter is moving ', s_value)
        
    def add_exhaust(self, discard):
        discard.cards.append(Card('Ex-2'))
            
    def reshuffle_discard(self, discard, deck):
        for c in discard.cards:
            deck.cards.append(discard.draw_card())
        deck.shuffle()

    
    def select_card_to_play(self, hand, select, discard):
        selecting = True
        while selecting:
            print('Type your chosen value')
            chosen_value = input()
            if chosen_value == 'q':
                break
            else:
                chosen_value = int(chosen_value)
            for c in hand.cards:
                if chosen_value == c.value:
                    select.cards.append(hand.draw_card(hand.cards.index(c)))
                    selecting = False
                    break
            if selecting == False:
                # Dump remaing hand to discard
                for c in range(len(hand.cards)):
                    discard.cards.append(hand.draw_card(0))
            else:
                print("I couldn't find that card. Please try and enter the \
                      value again. Or enter q to exit.")
                

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
        
        self.roller_draw = []
        self.roller_removed = []
        self.roller_hand = []
        self.roller_discard = []


class Deck:
    def __init__(self):
        self.cards = []
    
    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0 , -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def draw_card(self, pos = 0):
        return self.cards.pop(pos)

    def add_to_deck(self, list_of_cards):
        for c in list_of_cards:
            self.cards.append(c)


class Card:
    def __init__(self, value):
        self.value = value
    
    def show(self):
        print(self.value)
    
    def __repr__(self):
        return str(self.value)