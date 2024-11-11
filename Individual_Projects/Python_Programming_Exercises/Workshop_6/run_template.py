#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import wx
from template_frame import MyFrame1 as MyFrame  # Inheritance from MyFrame


class GuessFrame(MyFrame):
    def __init__(self, display_text=None):
        super().__init__(None)
        self.display_text = display_text
        self.previous_guess = None
        self.bingo = random.randint(0, 100)
        self.Show()

    def my_guess_func(self, event):
        value = self.m_textCtrl1.GetValue()
        try:
            value = int(value)
            if value > self.bingo:
                display_text = f"{value} is too large"
            elif value < self.bingo:
                display_text = f"{value} is too small"
            else:
                display_text = f"{value} is the correct answer"
        except ValueError:
            display_text = f"{value} is invalid"
        self.Result.SetLabel(display_text)
        self.Layout()

    def on_guess(self, event):
        guess = self.m_textCtrl1.GetValue()
        try:
            guess = int(guess)
            if self.previous_guess is not None:
                self.Previous_Guess.SetLabel(f"Previous Guess: {self.previous_guess}")
            self.previous_guess = guess
            self.Previous_Guess.SetLabel(f"Previous Guess: {guess}")
        except ValueError:
            self.Previous_Guess.SetLabel("Invalid input")
        self.m_textCtrl1.SetValue("")


if __name__ == "__main__":
    app = wx.App()
    frame = GuessFrame()
    app.MainLoop()
