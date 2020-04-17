# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:45:22 2020

@author: ljo20
"""

import flamme_backend as fb
import tkinter as tk
from tkinter import ttk


class Flamme_GUI():
    def __init__(self, parent):
                
        self.parent = parent
        self.parent.title("Flamme Rouge")
        
        self.main_widgets()
    
    def main_widgets(self):

        self.label_top = ttk.Label(self.parent, 
                                   text = "Welcome to the Le Flamme Rouge")
        self.label_top.grid(row = 0, column = 0, sticky="nw")
 
       
        self.end_game = tk.Button(self.parent,
                                  text = 'End game',
                                  command = self.parent.quit)
        
        self.end_game.grid(row = 4, column = 0, sticky="sw")       

        self.frame_r = Roller_Frame(self.parent)
        self.frame_r.grid(row = 1, column = 0, columnspan = 9)
        
        self.frame_r = Sprinter_Frame(self.parent)
        self.frame_r.grid(row = 2, column = 0, columnspan = 9)
        
        self.frame_pre_ex = Pre_Exhaust_Frame(self.parent)
        self.frame_pre_ex.grid(row = 3, column = 0, columnspan = 4)
        
        self.frame_game_ex = Game_Exhaust_Frame(self.parent)
        self.frame_game_ex.grid(row = 3, column = 5, columnspan = 4)

        

class Roller_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.widgets()
        
        self.setup()
    
    def widgets(self):
        
        self.selected = tk.StringVar()
        
        self.label_1 = tk.Label(self, text = 'roller draw deck')
        self.label_2 = tk.Label(self, text = 'You have drawn...')
        self.label_3 = tk.Label(self, text = 'Select your card')
        self.label_4 = tk.Label(self, text = 'Dicsard pile')
        self.label_5 = tk.Label(self, text = 'Removed pile')
        self.label_6 = tk.Label(self, text = 'You have selected')
    
        self.entry_1 = tk.Entry(self, textvariable = self.selected)
        
        self.button_1 = ttk.Button(self, text = 'Draw roller',
                                   command = self.draw_roller)
        
        self.button_2 = ttk.Button(self, text = 'Select roller',
                                   command = self.select_roller)
        
        self.listbox_1 = tk.Listbox(self)
        self.listbox_2 = tk.Listbox(self)
        self.listbox_3 = tk.Listbox(self)
        self.listbox_4 = tk.Listbox(self)        
        self.listbox_5 = tk.Listbox(self)

        self.label_1.grid(row = 0, column = 0)
        self.label_2.grid(row = 0, column = 2)
        self.label_3.grid(row = 0, column = 3, columnspan = 2)
        self.label_4.grid(row = 0, column = 5)
        self.label_5.grid(row = 0, column = 6)
        self.label_6.grid(row = 2, column = 3)
    
        self.entry_1.grid(row = 1, column = 3)
        
        self.button_1.grid(row = 1, column = 1)
        
        self.button_2.grid(row = 1, column = 4)
        
        self.listbox_1.configure(height = 20, justify="center")
        self.listbox_2.configure(height = 20, justify="center")
        self.listbox_3.configure(height = 20, justify="center")
        self.listbox_4.configure(height = 20, justify="center")        
        self.listbox_5.configure(height = 1, justify="center")
        
        self.listbox_1.grid(row = 1, column = 0, rowspan = 5)
        self.listbox_2.grid(row = 1, column = 2, rowspan = 5)
        self.listbox_3.grid(row = 1, column = 5, rowspan = 5)
        self.listbox_4.grid(row = 1, column = 6, rowspan = 5)
        self.listbox_5.grid(row = 3, column = 3)
        
        

    def setup(self):
        self.update_draw()

    def next_turn(self):
        pass
        
    def draw_roller(self):
        if player.roller.turn == True:
            player.draw_hand(player.roller, 4)
        
            self.update_hand()
        
            self.clear_draw()
            
            self.update_draw()

    def select_roller(self):
        player.select_card_to_play(player.roller.hand, 
                                   player.roller.select, 
                                   player.roller.discard,
                                   self.selected.get())
        self.clear_hand()
        self.clear_draw()
        self.update_draw()
        self.update_select()
        self.update_discard()
        
#        self.entry_1.delete(0, tk.END)

    def clear_draw(self):
        self.listbox_1.delete(0, tk.END)

    def clear_hand(self):
        self.listbox_2.delete(0, tk.END)
    
    def clear_discard(self):
        self.listbox_3.delete(0, tk.END)

    def clear_removed(self):
        self.listbox_4.delete(0, tk.END)
    
    def clear_select(self):
        self.listbox_5.delete(0, tk.END)

    def update_draw(self):
        draw_deck = []
        for c in player.roller.draw.cards:
            draw_deck.append(c.value)
        draw_deck.sort()
        for c in draw_deck:
            self.listbox_1.insert(tk.END, c)

    def update_hand(self):
        hand_deck = []
        for c in player.roller.hand.cards:
            hand_deck.append(c.value)
        for c in hand_deck:
            self.listbox_2.insert(tk.END, c)

    def update_discard(self):
        discard_deck = []
        for c in player.roller.discard.cards:
            discard_deck.append(c.value)
        for c in discard_deck:
            self.listbox_3.insert(tk.END, c)

    def update_removed(self):
        removed_deck = []
        for c in player.roller.removed.cards:
            removed_deck.append(c.value)
        for c in removed_deck:
            self.listbox_4.insert(tk.END, c)

    def update_select(self):
        select_deck = []
        for c in player.roller.select.cards:
            select_deck.append(c.value)
        for c in select_deck:
            self.listbox_5.insert(tk.END, c) 

class Sprinter_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.widgets()
        
        self.setup()
    
    def widgets(self):
        
        self.selected = tk.StringVar()
        
        self.label_1 = tk.Label(self, text = 'sprinter draw deck')
        self.label_2 = tk.Label(self, text = 'You have drawn...')
        self.label_3 = tk.Label(self, text = 'Select your card')
        self.label_4 = tk.Label(self, text = 'Dicsard pile')
        self.label_5 = tk.Label(self, text = 'Removed pile')
        self.label_6 = tk.Label(self, text = 'You have selected')
    
        self.entry_1 = tk.Entry(self, textvariable = self.selected)
        
        self.button_1 = ttk.Button(self, text = 'Draw sprinter',
                                   command = self.draw_sprinter)
        
        self.button_2 = ttk.Button(self, text = 'Select sprinter',
                                   command = self.select_sprinter)
        
        self.listbox_1 = tk.Listbox(self)
        self.listbox_2 = tk.Listbox(self)
        self.listbox_3 = tk.Listbox(self)
        self.listbox_4 = tk.Listbox(self)
        self.listbox_5 = tk.Listbox(self)


        self.label_1.grid(row = 0, column = 0)
        self.label_2.grid(row = 0, column = 2)
        self.label_3.grid(row = 0, column = 3, columnspan = 2)
        self.label_4.grid(row = 0, column = 5)
        self.label_5.grid(row = 0, column = 6)
        self.label_6.grid(row = 2, column = 3)
    
        self.entry_1.grid(row = 1, column = 3)
        
        self.button_1.grid(row = 1, column = 1)
        
        self.button_2.grid(row = 1, column = 4)

        self.listbox_1.configure(height = 20, justify="center")
        self.listbox_2.configure(height = 20, justify="center")
        self.listbox_3.configure(height = 20, justify="center")
        self.listbox_4.configure(height = 20, justify="center")
        self.listbox_5.configure(height = 1, justify="center")
        
        self.listbox_1.grid(row = 1, column = 0, rowspan = 5)
        self.listbox_2.grid(row = 1, column = 2, rowspan = 5)
        self.listbox_3.grid(row = 1, column = 5, rowspan = 5)
        self.listbox_4.grid(row = 1, column = 6, rowspan = 5)
        self.listbox_5.grid(row = 3, column = 3)

    def setup(self):
        self.update_draw()
        
    def draw_sprinter(self):
        pass

    def select_sprinter(self):
        pass        

    def update_draw(self):
        draw_deck = []
        for c in player.sprinter.draw.cards:
            draw_deck.append(c.value)
        draw_deck.sort()
        for c in draw_deck:
            self.listbox_1.insert(tk.END, c)

    def update_discard(self):
        pass

    def update_removed(self):
        pass

    def update_hand(self):
        pass   

class Game_Exhaust_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.widgets()
        
    def widgets(self):        
        
        self.label_1 = tk.Label(self, text = 'In game exhaustion controls')
        
        
        self.button_1 = ttk.Button(self, text = 'Add roller exhaustion',
                           command = self.add_roller_ex)

        self.button_2 = ttk.Button(self, text = 'Remove roller exhaustion',
                           command = self.rem_roller_ex)

        self.button_3 = ttk.Button(self, text = 'Add sprinter exhaustion',
                           command = self.add_sprinter_ex)

        self.button_4 = ttk.Button(self, text = 'Remove sprinter exhaustion',
                           command = self.rem_sprinter_ex)
        
        
        self.label_1.grid(row = 0, column = 0, columnspan = 2)
        
        self.button_1.grid(row = 1, column = 0)
        self.button_2.grid(row = 1, column = 1)
        self.button_3.grid(row = 2, column = 0)
        self.button_4.grid(row = 2, column = 1)

    def add_roller_ex(self):
        pass
    
    def rem_roller_ex(self):
        pass
    
    def add_sprinter_ex(self):
        pass
    
    def rem_sprinter_ex(self):
        pass
        
        
class Pre_Exhaust_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.widgets()
        
    def widgets(self):        
        
        self.label_1 = tk.Label(self, text = 'Pre game exhaustion controls')
        
        
        self.button_1 = ttk.Button(self, text = 'Add roller exhaustion',
                           command = self.add_roller_ex)

        self.button_2 = ttk.Button(self, text = 'Remove roller exhaustion',
                           command = self.rem_roller_ex)

        self.button_3 = ttk.Button(self, text = 'Add sprinter exhaustion',
                           command = self.add_sprinter_ex)

        self.button_4 = ttk.Button(self, text = 'Remove sprinter exhaustion',
                           command = self.rem_sprinter_ex)
        
        
        self.label_1.grid(row = 0, column = 0, columnspan = 2)
        
        self.button_1.grid(row = 1, column = 0)
        self.button_2.grid(row = 1, column = 1)
        self.button_3.grid(row = 2, column = 0)
        self.button_4.grid(row = 2, column = 1)

    def add_roller_ex(self):
        pass
    
    def rem_roller_ex(self):
        pass
    
    def add_sprinter_ex(self):
        pass
    
    def rem_sprinter_ex(self):
        pass

if __name__=='__main__':
    
    player = fb.Player()

    root = tk.Tk()
    gui = Flamme_GUI(root)
    root.mainloop()
