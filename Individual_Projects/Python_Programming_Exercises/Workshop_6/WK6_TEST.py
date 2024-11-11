import wx


class BingoFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(BingoFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl = wx.TextCtrl(panel)
        vbox.Add(self.m_textCtrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.m_staticText = wx.StaticText(panel, label="Your guess will appear here")
        vbox.Add(self.m_staticText, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.m_prevGuessText = wx.StaticText(panel, label="Previous guess: None")
        vbox.Add(self.m_prevGuessText, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.m_button = wx.Button(panel, label="Submit Guess")
        vbox.Add(self.m_button, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.m_button.Bind(wx.EVT_BUTTON, self.OnSubmit)

        panel.SetSizer(vbox)

        self.SetTitle('Bingo Game')
        self.Centre()

    def OnSubmit(self, event):
        current_guess = self.m_textCtrl.GetValue()
        previous_guess = self.m_staticText.GetLabel()

        self.m_prevGuessText.SetLabel(f"Previous guess: {previous_guess}")
        self.m_staticText.SetLabel(current_guess)


def main():
    app = wx.App()
    frame = BingoFrame(None)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
