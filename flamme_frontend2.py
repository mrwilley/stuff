# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:04:01 2020

@author: ljo20
"""

import flamme_backend as fb
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


class Flamme_GUI():
    def __init__(self, parent):
                
        self.parent = parent
        self.parent.title("Flamme Rouge")
        
        self.main_widgets()
    
    def main_widgets(self):

        self.label_top = ttk.Label(self.parent, 
                                   text = "Welcome to the Le Flamme Rouge")
        self.label_top.grid(row = 0, column = 0, sticky="nw")

        self.frame_setup = Setup_Frame(self.parent)
        self.frame_setup.grid(row = 1, column = 0)

        self.frame_r = Rider_Frame(self.parent, 'roller')
        self.frame_r.grid(row = 2, column = 0, columnspan = 9)
        
        self.frame_s = Rider_Frame(self.parent, 'sprinter')
        self.frame_s.grid(row = 3, column = 0, columnspan = 9)

        self.frame_turn = Turn_Frame(self.parent)
        self.frame_turn.grid(row = 4, column = 3)


class Setup_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.widgets()
        
    def widgets(self):
        self.new_game_btn = tk.Button(self, 
                                  text = 'New game',
                                  command = self.new_game_setup)

        self.load_game_btn = tk.Button(self, 
                                  text = 'Load game',
                                  command = self.load_game_setup)

        self.save_game_btn = tk.Button(self, 
                                  text = 'Save game',
                                  command = self.save_game_setup)        

        self.end_game_btn = tk.Button(self,
                                  text = 'End game',
                                  command = self.end_game)

        self.new_game_btn.grid(row = 1, column = 0)
        self.load_game_btn.grid(row = 1, column = 1)
        self.save_game_btn.grid(row = 1, column = 2)
        self.end_game_btn.grid(row = 1, column = 3)
    
    def new_game_setup(self):
        pass
    
    def get_file_name(self):
        return filedialog.askopenfilename(
                title = 'Select game file',
                filetypes = (('game file','*.json'),('all files','*.*')))
    
    def load_game_setup(self):
        filename = self.get_file_name()
        record.load_game(filename, player)

    def save_game_setup(self):
        record.save_game()
    
    def end_game(self):
        self.save_game_setup()
        self.parent.quit()
   

class Rider_Frame(tk.Frame):
    def __init__(self, parent, rider_type):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.rider_type = rider_type
        
        self.attributes(self.rider_type)
        self.widgets()
        
        self.update_game_state()

    def attributes(self, rider_type):
        if rider_type == 'sprinter':
            self.rider = player.sprinter
        elif rider_type == 'roller':
            self.rider = player.roller

    def widgets(self):
        self.frames()
        self.labels()
        self.listboxes()
        self.buttons()

    def frames(self):
        self.pre_ex = Ex_Frame(self, 'pre', self.rider_type, self.rider)
        self.in_ex = Ex_Frame(self, 'in', self.rider_type, self.rider)
      
        self.pre_ex.grid(row = 1, column = 0)
        self.in_ex.grid(row = 1, column = 8)
        
    
    def buttons(self):
        self.button_draw = ttk.Button(self, text = 'Draw ' + self.rider_type,
                                   command = self.try_draw_hand)
        
        self.button_select = ttk.Button(self, text = 'Select ' + self.rider_type,
                                   command = self.select)
                
        self.button_draw.grid(row = 1, column = 2)        
        self.button_select.grid(row = 1, column = 4)

    def listboxes(self):
        self.list_draw = tk.Listbox(self)
        self.list_hand = tk.Listbox(self, selectmode = 'SINGLE')
        self.list_discard = tk.Listbox(self)
        self.list_remove = tk.Listbox(self)
        self.list_select = tk.Listbox(self)
        
        l_boxes = [self.list_draw, self.list_hand, self.list_discard, 
                   self.list_remove]
        for l_box in l_boxes:
            l_box.configure(height = 20, justify="center")        
        self.list_select.configure(height = 1, justify="center")
        
        for l_box, col in zip(l_boxes, [1, 3, 6, 7]):
            l_box.grid(row = 1, column = col, rowspan = 5)        
        self.list_select.grid(row = 3, column = 4)

    def labels(self):
        self.lab_draw = tk.Label(self, text = self.rider_type + ' draw deck')
        self.lab_you_drew = tk.Label(self, text = 'You have drawn...')
        self.lab_choose = tk.Label(self, text = 'Select your card')
        self.lab_discard = tk.Label(self, text = 'Dicsard pile')
        self.lab_remove = tk.Label(self, text = 'Removed pile')
        self.lab_selected = tk.Label(self, text = 'You have selected')

        self.lab_draw.grid(row = 0, column = 1)
        self.lab_you_drew.grid(row = 0, column = 3)
        self.lab_choose.grid(row = 0, column = 4)
        self.lab_discard.grid(row = 0, column = 6)
        self.lab_remove.grid(row = 0, column = 7)
        self.lab_selected.grid(row = 2, column = 4)

    def update_game_state(self):        
        l_boxes = [self.list_draw, self.list_hand, self.list_discard,
                   self.list_remove, self.list_select]
        
        decks = [self.rider.draw, self.rider.hand,
                 self.rider.discard, self.rider.removed,
                 self.rider.select]
        
        for l_box, deck in zip(l_boxes, decks):
            self.update_deck(l_box, deck)

        record.update_data_decks(self.rider, self.rider_type, turn)

    def next_turn(self):
        player.remove_select(self.rider) 
        player.end_cleanup(self.rider)
        self.update_game_state()
               
    def try_draw_hand(self):
        if self.check_opposing_hand():
            if self.rider.turn:
                self.draw_hand()
            else:
                self.turn_error()
        else:
            self.draw_error()        

    def check_opposing_hand(self):
        return player.can_be_drawn(self.rider)

    def draw_hand(self):
        player.draw_hand(self.rider)         
        self.update_game_state()

    def selected_card(self):
        all_items = self.list_hand.get(0, tk.END)
        sel_idx = self.list_hand.curselection()
        return all_items[sel_idx[0]]

    def make_selection(self, card_value):
            player.select_card_to_play(self.rider.hand, 
                                       self.rider.select, 
                                       self.rider.discard,
                                       card_value)        

    def select(self):
        card_value = self.selected_card()
        if player.found_selected_card(self.rider.hand, card_value):
            self.make_selection(card_value)
        else:
            self.cant_find_error()
        self.update_game_state()
       
    def clear_listbox(self, l_box):
        l_box.delete(0, tk.END)

    def write_l_box(self, l_box, card_list):
        for c in card_list:
            l_box.insert(tk.END, c)        

    def card_value_to_list(self, deck):
        list_ = []
        for c in deck.cards:
            list_.append(c.value)
        list_.sort()
        return list_

    def get_write_list(self, deck, l_box):
        card_list = self.card_value_to_list(deck)
        self.write_l_box(l_box, card_list)        

    def update_deck(self, l_box, deck):
        self.clear_listbox(l_box)
        self.get_write_list(deck, l_box)

    def error_box(self, title_, message_):
        messagebox.showerror(title = title_, message = message_)

    def draw_error(self):
        title_ = 'Draw error'
        message_ = 'Ye cannae draw cards fur this rider \'til ye hae \
        selcted caird fur ither rider.'
        self.error_box(title_, message_)

    def turn_error(self):
        title_ = 'Turn error'
        message_ = 'Ye hae awready drawn cards fur this rider this gang.'
        self.error_box(title_, message_)

    def cant_find_error(self):
        title_ = 'Not found error'
        message_ = 'Ah cannae fin\' that caird. Huv a go again.'
        self.error_box(title_, message_)


class Ex_Frame(tk.Frame):
    def __init__(self, parent, pre_or_in, rider_type, rider):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.rider_type = rider_type
        self.rider = rider
                
        self.attributes(pre_or_in, rider_type)
        self.widgets()

    def attributes(self, pre_or_in, rider_type):
        if pre_or_in.lower() == 'pre':
            self.prefix = 'Pre'
            self.pre_case = True
        else:
            self.prefix = 'In'
            self.pre_case = False
        
    def widgets(self):        
        
        self.label_1 = tk.Label(
                self,
                text = self.prefix + ' game exhaustion controls')
                
        self.button_1 = ttk.Button(
                self,
                text = 'Add ' + self.rider_type + ' exhaustion',
                command = self.add_rider_ex)

        self.button_2 = ttk.Button(
                self,
                text = 'Remove ' + self.rider_type + ' exhaustion',
                command = self.rem_rider_ex)
                
        self.label_1.grid(row = 0, column = 0)        
        self.button_1.grid(row = 1, column = 0)
        self.button_2.grid(row = 2, column = 0)

    def add_rider_ex(self):
        player.add_exhaust(self.rider, self.pre_case)
        self.parent.update_game_state()

    def rem_rider_ex(self):
        player.remove_exhaust(self.rider, self.pre_case)
        self.parent.update_game_state()


class Turn_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.widgets()
    
    def widgets(self):
        
        self.label_turn = tk.Label(self, text = 'Current turn')
        self.listbox_turn = tk.Listbox(self)
        self.button_turn = tk.Button(self, text = 'Next Turn',
                                     command = self.check_end_turn)
        
        self.listbox_turn.configure(height = 1, justify="center")
        
        self.label_turn.grid(row = 0, column = 0)
        self.listbox_turn.grid(row = 1, column = 0)
        self.button_turn.grid(row = 2, column = 0)
        
        self.show_turn()
    
    def next_turn(self):
        turn.next_turn()
        self.show_turn()
        
        gui.frame_r.next_turn()
        gui.frame_s.next_turn()
    
    def show_turn(self):
        self.listbox_turn.delete(0, tk.END)
        self.listbox_turn.insert(tk.END, turn.turn_no)

    def check_end_turn(self):
        if player.sprinter.turn or player.roller.turn:
            self.no_end_turn_error()
        else:
            self.next_turn()

    def no_end_turn_error(self):
        self.error_box('End of turn error', 
                       'Ye hae nae selected cards fur a\' yer riders yit. \
                       Ye cannae end th\' caw.')
    
    def error_box(self, title_, message_):
        messagebox.showerror(title = title_, message = message_)


if __name__=='__main__':

    turn = fb.Turn()    
    record = fb.Record()
    player = fb.Player()
    
    root = tk.Tk()
    gui = Flamme_GUI(root)
    root.mainloop()
