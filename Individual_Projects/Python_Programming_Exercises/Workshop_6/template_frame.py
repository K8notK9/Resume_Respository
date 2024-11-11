# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"BINGO"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Guess the generated number 0~100"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

        self.Guess = wx.Button( self, wx.ID_ANY, _(u"Guess"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.Guess, 0, wx.ALL, 5 )

        self.Result = wx.StaticText( self, wx.ID_ANY, _(u"Result"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Result.Wrap( -1 )

        bSizer2.Add( self.Result, 0, wx.ALL, 5 )

        self.Previous_Guess = wx.StaticText( self, wx.ID_ANY, _(u"Previous Guess"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Previous_Guess.Wrap( -1 )

        bSizer2.Add( self.Previous_Guess, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_textCtrl1.Bind( wx.EVT_TEXT, self.on_guess )
        self.Guess.Bind( wx.EVT_BUTTON, self.my_guess_func )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_guess( self, event ):
        event.Skip()

    def my_guess_func( self, event ):
        event.Skip()
