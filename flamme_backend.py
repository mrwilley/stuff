# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:36:10 2020

@author: ljo20
"""

import random


class MasterDeck():
    def __init__(self, deck_name, cards):
        self.name = deck_name

        # Create card areas
        self.draw = Deck()
        self.draw.add_to_deck(cards)
        self.draw.shuffle()
        self.removed = Deck()
        self.hand = Deck()
        self.select = Deck()
        self.discard = Deck()
        self.turn = True


class Player():
    def __init__(self):
        
        self.draw_amount = 4
        
        # Make the roller and sprinter cards
        roller_cards = self.build({'3':3, '4':3, '5':3, '6':3, '7':3})
        sprinter_cards = self.build({'2':3, '3':3, '4':3, '5':3, '9':3})
        
        # Create roller card areas
        self.roller = MasterDeck("roller", roller_cards)
        
        #Create sprinter card areas
        self.sprinter = MasterDeck("sprinter", sprinter_cards)

    def build(self, deck_dict):
        card_list = []
        for k, v in deck_dict.items():
            for x in range(1, v + 1):
                card_list.append(Card(k))
        return card_list


    def draw_hand(self, deck, draw_amount):
        oppo = self.sprinter if deck == self.roller else self.roller
        if self.check_remain(oppo.hand) > 0:
            print('Must select a card from your drawn hand before drawing\
                  from this deck.')
        elif deck.turn == False:
            print('You have already made the selection for this deck this turn.')
        else:
            for d in range(draw_amount):
                if self.check_remain(deck.draw) <= 0:
                    if self.check_remain(deck.discard) <= 0:
                        break
                    else:
                        self.reshuffle_discard(deck.discard, deck.draw)
                deck.hand.cards.append(deck.draw.draw_card())
            deck.turn = False
            
    def select_card_to_play(self, hand, select, discard, card_value):            
        card_found = False
        
        for c in hand.cards:
            if card_value == c.value:
                card_found = True
            
        if card_found:
            for c in hand.cards:
                if card_value == c.value:
                    select.cards.append(hand.draw_card(hand.cards.index(c)))
                    break
            for c in range(len(hand.cards)):
                discard.cards.append(hand.draw_card(0))
        else:
            print("I couldn't find that card. Please try and enter the \
                  value again.")

    def add_exhaust(self, deck, pre):
        if pre == False:
            deck.discard.cards.append(Card('ex2'))
        else:
            deck.draw.cards.append(Card('ex2'))
            deck.draw.shuffle()

    def remove_exhaust(self, deck, pre):
        if pre == False:
            for c in deck.discard.cards:
                if 'ex2' == c.value:
                    deck.discard.cards.index(c)
                    del deck.discard.cards[deck.discard.cards.index(c)]
                    break
        else:
            for c in deck.draw.cards:
                if 'ex2' == c.value:
                    deck.draw.cards.index(c)
                    del deck.draw.cards[deck.draw.cards.index(c)]                    
                    deck.draw.shuffle()
                    break

    def check_remain(self, deck):
        return len(deck.cards)
              
    def reshuffle_discard(self, discard, deck):
        for c in range(len(discard.cards)):
            deck.cards.append(discard.draw_card())
        deck.shuffle()
 
    def remove_select(self, deck):
        deck.removed.cards.append(deck.select.draw_card())
        deck.turn = True
    

                

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
        return 'Card({0})'.format(self.value)

    def __str__(self):
        return str(self.value)
         