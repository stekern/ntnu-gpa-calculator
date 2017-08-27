#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Erlend Ekern <dev@ekern.me>
#
# Distributed under terms of the MIT license.

"""
A basic tkinter GUI for gpa_fetcher.py
"""

from tkinter import *

class GPAFetcherGUI(object):
    def __init__(self, login=None, set_gpa=None):
        self.login = login
        self.set_gpa = set_gpa
        self.gui_setup()

    def change_element_state(self, element, state):
        if isinstance(element, Frame) or isinstance(element, Tk):
            for child in element.winfo_children():
                self.change_element_state(child, state)
        else:
            if ('state' in element.keys()):
                element.config(state=state)

    def enable_element(self, element):
        self.change_element_state(element, NORMAL)

    def disable_element(self, element):
        self.change_element_state(element, DISABLED)

    def gui_setup(self):
        self.main = Tk()
        self.main.title('NTNU GPA Calculator')
        self.main.resizable(width=False, height=False)

        self._top_frame_setup()
        self._mid_frame_setup()
        self._bottom_frame_setup()

        self.disable_element(self.mid_frame)
        self.disable_element(self.bottom_frame)

    def is_desc(self):
        return self.desc.get()

    def run(self):
        mainloop()

    def update_status(self, status):
        self.enable_element(self.bottom_frame)
        self.status_text.insert(END, '{}\n'.format(status))
        self.status_text.see(END)
        self.disable_element(self.bottom_frame)

    def _bottom_frame_setup(self):
        self.bottom_frame = Frame(self.main)
        self.bottom_frame.pack(fill=BOTH, expand=True)

        self.status_text = Text(self.bottom_frame)
        self.status_text.pack(fill=BOTH, pady=5, padx=5, expand=True)

    def _mid_frame_setup(self):
        self.mid_frame = Frame(self.main, relief=RAISED, borderwidth=1)
        self.mid_frame.pack(fill=BOTH, expand=True)

        grade_values_frame = Frame(self.mid_frame)
        grade_values_frame.pack(fill=X)

        self.desc = BooleanVar()
        self.desc.set(True)

        grade_values_label = Label(grade_values_frame, text='Grade values:', width=10, anchor='w')
        grade_values_label.pack(side=LEFT, padx=5, pady=5)

        grade_values_radio_button_asc = Radiobutton(grade_values_frame, text='A=1, B=2, ...', variable=self.desc, value=False, command=self.set_gpa, anchor='w')
        grade_values_radio_button_asc.pack(fill=X, expand=True)

        grade_values_radio_button_desc = Radiobutton(grade_values_frame, text='A=5, B=4, ...', variable=self.desc, value=True, command=self.set_gpa, anchor='w')
        grade_values_radio_button_desc.pack(fill=X, expand=True)

        gpa_frame = Frame(self.mid_frame)
        gpa_frame.pack(fill=X)
        
        gpa_info_label = Label(gpa_frame, text='GPA:', anchor='w', width=10)
        gpa_info_label.pack(side=LEFT, padx=5, pady=5)

        self.gpa_label = Label(gpa_frame, text='N/A', anchor='w', width=10)
        self.gpa_label.pack(fill=X, padx=5, expand=True)

    def _top_frame_setup(self):
        top_frame = Frame(self.main, relief=RAISED, borderwidth=1)
        top_frame.pack(fill=BOTH, expand=True)

        username_frame = Frame(top_frame)
        username_frame.pack(fill=X)

        username_label = Label(username_frame, text='Username:', anchor='w', width=10)
        username_label.pack(side=LEFT, padx=5, pady=5)

        self.username_input = Entry(username_frame)
        self.username_input.pack(fill=X, padx=5, expand=True)

        password_frame = Frame(top_frame)
        password_frame.pack(fill=X)

        password_label = Label(password_frame, text='Password:', anchor='w', width=10)
        password_label.pack(side=LEFT, padx=5, pady=5)

        self.password_input = Entry(password_frame, show='*')
        self.password_input.pack(fill=X, padx=5, expand=True)

        submit_frame = Frame(top_frame)
        submit_frame.pack(fill=X)

        submit_button = Button(submit_frame, text='Get GPA!', height=2, width=15, command=self.login)
        submit_button.pack(padx=5, pady=5, expand=True)

if __name__ == '__main__':
    gpa_fetcher_gui = GPAFetcherGUI()
    gpa_fetcher_gui.run()
