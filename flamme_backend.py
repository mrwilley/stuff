# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:36:10 2020

@author: ljo20
"""

import random
import json

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
        self.sprinter = MasterDeck("sprinter", sprinter_cards)

    def build(self, deck_dict):
        card_list = []
        for k, v in deck_dict.items():
            for x in range(1, v + 1):
                card_list.append(Card(k))
        return card_list

    def draw_hand(self, deck):
        for d in range(self.draw_amount):
            if self.check_remain(deck.draw) <= 0:
                if self.check_remain(deck.discard) <= 0:
                    break
                else:
                    self.reshuffle_discard(deck.discard, deck.draw)
            deck.hand.cards.append(deck.draw.draw_card())
        deck.turn = False
            
    def select_card_to_play(self, hand, select, discard, card_value):                        
        for c in hand.cards:
            if card_value == c.value:
                select.cards.append(hand.draw_card(hand.cards.index(c)))
                break
        self.discard_hand(hand, discard)

    def discard_hand(self, hand, discard):
        for c in range(len(hand.cards)):
            discard.cards.append(hand.draw_card(0))

    def found_selected_card(self, hand, card_value):
        for c in hand.cards:
            if card_value == c.value:
                return True
        return False

    def can_be_drawn(self, deck):
        oppo = self.sprinter if deck == self.roller else self.roller
        if self.check_remain(oppo.hand) > 0:
            return False
        else:
            return True

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
#        deck.turn = True
    
    def end_cleanup(self, deck):
        deck.turn = True

    def load_saved_data(self, data):
        self.remove_all_cards()
        self.write_new_deck_data(data)
    
    def remove_all_cards(self):
        for r in [self.roller, self.sprinter]:
            for d in [r.draw, r.hand, r.select, r.discard, r.removed]:
                d.remove_all()
    
    def write_new_deck_data(self, data):
        riders = [self.roller, self.sprinter]
        rider_names = ['roller', 'sprinter']
        deck_names = ['draw', 'hand', 'select', 'discard', 'removed']
        for rider, rider_name in zip(riders, rider_names):
            rider_decks = [rider.draw, rider.hand, rider.select, 
                           rider.discard, rider.removed]
            for rider_deck, deck_name in zip(rider_decks, deck_names):
                rider_deck.add_to_deck(self.data['rider'][rider_name][deck_name])

#    def rider_decks(self, rider):
#        return [rider.draw, rider.hand, rider.select, rider.discard, rider.removed]
            
                
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
    
    def remove_all(self):
        for c in self.cards:
            self.cards.remove(c)

    def card_value_to_list(self):
        list_ = []
        for c in self.cards:
            list_.append(c.value)
        return list_

class Card:
    def __init__(self, value):
        self.value = value
    
    def show(self):
        print(self.value)
    
    def __repr__(self):
        return 'Card({0})'.format(self.value)

    def __str__(self):
        return str(self.value)


class Turn():
    def __init__(self):
        self.turn_no = 1
    
    def next_turn(self):
        self.turn_no = self.turn_no + 1



class Record():
    def __init__(self):
        self.data = {}
        self.can_save = False
        self.new_game()

    def file_name(self):
        self.file_name = self.player + '_' + self.color + '.json'

    def append_data(self, lst, to_append):
        lst.append(to_append)

    def write_data(self):
        with open('save_data.json', 'w') as outfile:
            json.dump(self.data, outfile, indent = 4)
    
    def new_game(self):              
        deck_dict = {'draw' : [],
                'hand' : [],
                'select' : [],
                'discard' : [],
                'removed' : []}
        self.data['turn_no'] : 1
        self.data['rider'] = {'roller' : deck_dict, 'sprinter' : deck_dict}        
        self.data['played'] = {'roller': {}, 'sprinter' :{}}

    def update_data_decks(self, rider, rider_type, turn):
        self.data['turn_no'] = turn.turn_no
        print(rider_type)
        deck_names = ['draw', 'hand', 'select', 'discard', 'removed']
          
        rider_decks = [rider.draw, rider.hand, rider.select, 
                       rider.discard, rider.removed]          
            
        for deck_name, rider_deck in zip(deck_names, rider_decks):
            
            self.data['rider'][rider_type][deck_name] = []
            
            card_list = rider_deck.card_value_to_list()
            
            for c in card_list:
                self.data['rider'][rider_type][deck_name].append(c)
    
    def write_played_card(self):
        pass

    def read_data(self, filename):
        with open(filename) as json_file:
            self.data = json.load(json_file)

    def save_game(self):
        self.write_data()
    
    def load_game(self, filename, player):
        #self.filename = filename
        self.read_data(filename)
        player.load_saved_data(self.data)
        self.save_ok()
   
    def end_game(self):
        self.write_data()

    def get_player_name(self, player_name):
        self.player_name = player_name

    def get_player_color(self, player_color):
        self.player_color = player_color
    
    def get_file_name(self, file_name):
        self.file_name = file_name

    def save_ok(self):
        self.can_save = True        