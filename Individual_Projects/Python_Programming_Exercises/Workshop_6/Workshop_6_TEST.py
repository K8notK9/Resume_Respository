import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        self.previous_guess = None  # Variable to store the previous guess

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.guess_text = wx.StaticText(panel, label="Previous Guess: None")
        vbox.Add(self.guess_text, flag=wx.ALL, border=10)

        self.input_text = wx.TextCtrl(panel)
        vbox.Add(self.input_text, flag=wx.ALL, border=10)

        guess_button = wx.Button(panel, label="Submit Guess")
        guess_button.Bind(wx.EVT_BUTTON, self.on_guess)
        vbox.Add(guess_button, flag=wx.ALL, border=10)

        panel.SetSizer(vbox)

        self.SetTitle("Guessing Game")
        self.Centre()

    def on_guess(self, event):
        current_guess = self.input_text.GetValue()
        if self.previous_guess is not None:
            self.guess_text.SetLabel(f"Previous Guess: {self.previous_guess}")
        self.previous_guess = current_guess
        self.input_text.SetValue("")


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None)
        frame.Show(True)
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
