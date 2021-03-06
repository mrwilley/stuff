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
        roller_cards = self.build({3:3, 4:3, 5:3, 6:3, 7:3})
        sprinter_cards = self.build({2:3, 3:3, 4:3, 5:3, 9:3})
        
        # Create roller card areas
        self.roller = MasterDeck("roller", roller_cards)
        
        #Create sprinter card areas
        self.sprinter = MasterDeck("sprinter", sprinter_cards)
        
    def draw(self, deck_name):
        if deck_name == 'roller':
            self.draw_hand(self.roller, self.draw_amount)
        else:
            self.draw_hand(self.sprinter, self.draw_amount)

    def exhaust(self, deck_name, pre = False):
        # discard_deck, e.g. self.roller.discard
        if deck_name == 'roller':
            self.add_exhaust(self.roller, pre)
        else:
            self.add_exhaust(self.sprinter, pre)

    def add_exhaust(self, deck, pre):
        if pre == False:
            deck.discard.cards.append(Card(2))
        else:
            deck.draw.cards.append(Card(2))
            deck.draw.shuffle()            

    def build(self, deck_dict):
        card_list = []
        for k, v in deck_dict.items():
            for x in range(1, v + 1):
                card_list.append(Card(k))
        return card_list

    def check_remain(self, deck):
        return len(deck.cards)

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
            
            print('\nYou have drawn the cards...\n')
            deck.hand.show()
            
            self.select_card_to_play(deck.hand, deck.select, deck.discard)

            deck.turn = False

    def reveal(self):
        print('\nYour Roller is moving {0}'.format(self.roller.select.cards[0]))
        print('\nYour Sprinter is moving {0}'.format(self.sprinter.select.cards[0]))
        

            
    def reshuffle_discard(self, discard, deck):
        for c in range(len(discard.cards)):
            deck.cards.append(discard.draw_card())
        deck.shuffle()

    def end_turn(self):
        #Need to send each selected card to removed
        self.remove_select(self.roller)
        self.remove_select(self.sprinter)
    
    def remove_select(self, master_deck):
        master_deck.removed.cards.append(master_deck.select.draw_card())
        master_deck.turn = True
    
    def select_card_to_play(self, hand, select, discard):
        selecting = True
        while selecting:

            print('Type your chosen value')
            chosen_value = input()
            try:
                chosen_value = int(chosen_value)
            except:
                print('I don\t think you entered a number. Try again, Champ.')
                continue
            
            for c in hand.cards:
                if chosen_value == c.value:
                    select.cards.append(hand.draw_card(hand.cards.index(c)))
                    selecting = False
                    break
                
            if selecting == False:
                # Dump remaining hand to discard
                for c in range(len(hand.cards)):
                    discard.cards.append(hand.draw_card(0))
            else:
                print("I couldn't find that card. Please try and enter the \
                      value again.")
                

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

def deck_input():
    going = True
    while going:
        deck_in = input()
        if deck_in.lower() in ['s','r']:
            going = False
            if deck_in.lower() == 'r':
                return 'roller'
            else:
                return 'sprinter'
        else:
            print('Enter r for roller or s for sprinter.')

def numeric_input():
    going = True
    while going:
        num_in = input()
        try:
            num_in = int(num_in)
            going = False
        except:
            print('I don\'t think you entered a number. Try again.')
    return num_in            


def exhaust_check(player, pre = False):
    for deck in ["roller", "sprinter"]:
        input_exhaust(player, deck, pre)

def input_exhaust(player, deck, pre):
    print('\nDo you need to add any exhaustion cards to the ', deck, ' deck? y/n')
    ans = input()
    if ans.lower() == 'y' or ans.lower() == 'yes':
        if pre:
            print('How many?')
            amount = numeric_input()
        else:
            amount = 1
        exhaust_loop(player, deck, amount, pre)

def exhaust_loop(player, deck, amount, pre):
    for ex in range(amount):
        player.exhaust(deck, pre)

def end_game_check():
    print('Is game over? y/n')
    game_over = input()
    if game_over.lower() == 'y':
        print('For sure? y/n')
        game_over = input()
        if game_over.lower() == 'y':
            return False
        else:
            return True
    else:
        return True

if __name__ == '__main__':
    print("\nWelcome to le Flamme Rouge!")
    player = Player()
    
    exhaust_check(player, pre = True)
    
    turn = 1
    game = True
    while game:
        print('\nTurn ', turn, '!')
        print('Which rider do you want to choose first? roller (r) or sprinter (s)')
        first_deck = deck_input()
        sec_deck = 'sprinter' if first_deck == "roller" else 'roller'
        for d in [first_deck, sec_deck]:
            print('\nOkay. Let\'s draw the cards for your ', d)
            player.draw(d)
        player.reveal()
        exhaust_check(player)
        player.end_turn()
        print('End of turn ', turn)
        game = end_game_check()
        turn = turn + 1
    print('The game has ended. I hope you won and did not suck.')