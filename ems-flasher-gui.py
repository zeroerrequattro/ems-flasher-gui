#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx, dialog, strings
from filedrop import FileDrop
from ems import Flasher

class EmsGui(wx.Frame):

    def __init__(self, parent, title):
        super(EmsGui, self).__init__(parent, title=title, size=(500, 450))
        
        # Call the Flasher class
        self.ems = Flasher()
        
        # Set the panels and their hierarchies
        self.mainContainer = wx.Panel(self)
        self.innerPanel    = wx.Panel(self.mainContainer)
        self.buttonPanel   = wx.Panel(self.innerPanel)
        self.textPanel     = wx.ScrolledWindow(self.innerPanel, -1)
        
        self.resultText    = wx.StaticText(self.textPanel)
        
        self.buttonLoadEms      = wx.Button(self.buttonPanel, label=strings.loadEms)
        self.buttonCheckVersion = wx.Button(self.buttonPanel, label=strings.emsVer)
        self.buttonCheckCart    = wx.Button(self.buttonPanel, label=strings.chkCart)
        
        self.buttonReadBank01   = wx.Button(self.buttonPanel, label=strings.save01)
        self.buttonReadBank02   = wx.Button(self.buttonPanel, label=strings.save02)
        self.buttonReadSRam     = wx.Button(self.buttonPanel, label=strings.saveSR)
        
        self.buttonWriteBank01  = wx.Button(self.buttonPanel, label=strings.write01)
        self.buttonWriteBank02  = wx.Button(self.buttonPanel, label=strings.write02)
        self.buttonWriteSRam    = wx.Button(self.buttonPanel, label=strings.writeSR)
        
        self.buttonDeleteBank01 = wx.Button(self.buttonPanel, label=strings.del01)
        self.buttonDeleteBank02 = wx.Button(self.buttonPanel, label=strings.del02)
        self.buttonFormatCart   = wx.Button(self.buttonPanel, label=strings.format)
        
        self.i = 0
        
        # GUI init
        self.InitMenu()
        self.InitUI()
        self.InitBind()
        self.InitDropFile()
        self.InitCheck()
        
        self.Centre()
        self.Show()

    def InitMenu(self):
        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)

    def InitUI(self):
        # Set Colors
        _red    = '#F14A52'
        _blue   = '#95C4E8'
        _azure  = '#E6F4FA'
        _gray   = '#374650'
        _black  = '#19262C'
        _white  = '#EFEFEF'
        
        # Font formatting
        _font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        _font.SetPointSize(12)
        
        _codeFont = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FIXED_FONT)
        _codeFont.SetPointSize(12)
        
        _H1Font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        _H1Font.SetPointSize(16)
        
        # Set background colors of panels
        self.mainContainer.SetBackgroundColour(_red)
        self.innerPanel.SetBackgroundColour(_blue)
        self.buttonPanel.SetBackgroundColour(_azure)
        self.textPanel.SetBackgroundColour(_black)
        
        # button panel layout
        buttonBox = wx.BoxSizer(wx.VERTICAL)
        buttonBox.Add((-1, 10))
        
        emsTitle = wx.StaticText(self.buttonPanel, label=strings.ems)
        emsTitle.SetFont(_H1Font)
        emsTitle.SetForegroundColour(_gray)
        
        emsBox = wx.BoxSizer(wx.HORIZONTAL)
        emsBox.Add(emsTitle, 1, wx.EXPAND|wx.LEFT, 10)
        emsBox.Add(self.buttonLoadEms, 1, wx.EXPAND|wx.RIGHT, 10)
        emsBox.Add(self.buttonCheckVersion, 1, wx.EXPAND|wx.RIGHT, 10)
        emsBox.Add(self.buttonCheckCart, 1, wx.EXPAND|wx.RIGHT, 10)
        
        buttonBox.Add(emsBox, 1, wx.EXPAND)
        buttonBox.Add((-1, 5))
        
        readTitle = wx.StaticText(self.buttonPanel, label=strings.read)
        readTitle.SetFont(_H1Font)
        readTitle.SetForegroundColour(_gray)
        
        readBox = wx.BoxSizer(wx.HORIZONTAL)
        readBox.Add(readTitle, 1, wx.EXPAND|wx.LEFT, 10)
        readBox.Add(self.buttonReadBank01, 1, wx.EXPAND|wx.RIGHT, 10)
        readBox.Add(self.buttonReadBank02, 1, wx.EXPAND|wx.RIGHT, 10)
        readBox.Add(self.buttonReadSRam, 1, wx.EXPAND|wx.RIGHT, 10)
        
        buttonBox.Add(readBox, 1, wx.EXPAND)
        buttonBox.Add((-1, 5))
        
        writeTitle = wx.StaticText(self.buttonPanel, label=strings.write)
        writeTitle.SetFont(_H1Font)
        writeTitle.SetForegroundColour(_gray)
        
        writeBox = wx.BoxSizer(wx.HORIZONTAL)
        writeBox.Add(writeTitle, 1, wx.EXPAND|wx.LEFT, 10)
        writeBox.Add(self.buttonWriteBank01, 1, wx.EXPAND|wx.RIGHT, 10)
        writeBox.Add(self.buttonWriteBank02, 1, wx.EXPAND|wx.RIGHT, 10)
        writeBox.Add(self.buttonWriteSRam, 1, wx.EXPAND|wx.RIGHT,10)
        
        buttonBox.Add(writeBox, 1, wx.EXPAND)
        buttonBox.Add((-1, 5))
        
        deleteTitle = wx.StaticText(self.buttonPanel, label=strings.delete)
        deleteTitle.SetFont(_H1Font)
        deleteTitle.SetForegroundColour(_gray)
        
        formatBox = wx.BoxSizer(wx.HORIZONTAL)
        formatBox.Add(deleteTitle, 1, wx.EXPAND|wx.LEFT, 10)
        formatBox.Add(self.buttonDeleteBank01, 1, wx.EXPAND|wx.RIGHT, 10)
        formatBox.Add(self.buttonDeleteBank02, 1, wx.EXPAND|wx.RIGHT, 10)
        formatBox.Add(self.buttonFormatCart, 1, wx.EXPAND|wx.RIGHT, 10)
        
        buttonBox.Add(formatBox, 1, wx.EXPAND)
        buttonBox.Add((-1, 10))
        
        self.buttonPanel.SetSizer(buttonBox)
        
        # text panel layout
        textBox = wx.BoxSizer(wx.VERTICAL)
        
        self.textPanel.SetScrollbars(1, 1, 1, 1)
        self.textPanel.SetAutoLayout(True)
        self.textPanel.Layout()
        
        self.resultText.SetFont(_codeFont)
        self.resultText.SetForegroundColour(_white)
        self.resultText.SetBackgroundColour(_black)
        
        textBox.Add(self.resultText, 1, wx.EXPAND|wx.ALL, 10)
        
        self.textPanel.SetSizer(textBox)
        
        # Set the inner box and insert the panels
        innerBox = wx.BoxSizer(wx.VERTICAL)
        innerBox.Add(self.textPanel, 3, wx.EXPAND|wx.LEFT,7)
        innerBox.Add(self.buttonPanel, 1, wx.EXPAND|wx.LEFT, 7)
        
        # Include the inner box in the inner panel
        self.innerPanel.SetSizer(innerBox)
        
        mainBox = wx.BoxSizer(wx.VERTICAL)
        mainBox.Add(self.innerPanel, 1, wx.EXPAND | wx.LEFT, 7)
        
        # Include the main box in the main container
        self.mainContainer.SetSizer(mainBox)

    def InitBind(self):
        self.Bind(wx.EVT_BUTTON, self.loadEmsClick, self.buttonLoadEms)
        self.Bind(wx.EVT_BUTTON, self.checkVersionClick, self.buttonCheckVersion)
        self.Bind(wx.EVT_BUTTON, self.checkCartClick, self.buttonCheckCart)
        
        self.Bind(wx.EVT_BUTTON, self.deleteBank01Click, self.buttonDeleteBank01)
        self.Bind(wx.EVT_BUTTON, self.deleteBank02Click, self.buttonDeleteBank02)
        self.Bind(wx.EVT_BUTTON, self.formatCartClick, self.buttonFormatCart)
        
        self.Bind(wx.EVT_BUTTON, self.readBank01Click, self.buttonReadBank01)
        self.Bind(wx.EVT_BUTTON, self.readBank02Click, self.buttonReadBank02)
        self.Bind(wx.EVT_BUTTON, self.readBankSRamClick, self.buttonReadSRam)
        
        self.Bind(wx.EVT_BUTTON, self.writeBank01Click, self.buttonWriteBank01)
        self.Bind(wx.EVT_BUTTON, self.writeBank02Click, self.buttonWriteBank02)
        self.Bind(wx.EVT_BUTTON, self.writeBankSRamClick, self.buttonWriteSRam)

    def InitCheck(self):
        self.writeAndScroll(strings.welcome)

    def InitDropFile(self):
        dt = FileDrop(self.resultText)
        self.mainContainer.SetDropTarget(dt)
    
    # define button functions
    def loadEmsClick(self,e):
        result = self.ems.loadEms()
        self.writeAndScroll(result)

    def checkVersionClick(self,e):
        result = self.ems.checkVersion()
        self.writeAndScroll(result)

    def checkCartClick(self,e):
        result = self.ems.checkCart()
        self.writeAndScroll(result)

    def deleteBank01Click(self,e):
        result = self.ems.deleteBank01()
        self.writeAndScroll(result)

    def deleteBank02Click(self,e):
        result = self.ems.deleteBank02()
        self.writeAndScroll(result)

    def formatCartClick(self,e):
        result = self.ems.formatCart()
        self.writeAndScroll(result)

    def readBank01Click(self,e):
        result = self.ems.readBank01()
        self.writeAndScroll(result)

    def readBank02Click(self,e):
        result = self.ems.readBank02()
        self.writeAndScroll(result)

    def readBankSRamClick(self,e):
        result = self.ems.readSRam()
        self.writeAndScroll(result)

    def writeBank01Click(self,e):
        result = self.ems.writeBank01()
        self.writeAndScroll(result)

    def writeBank02Click(self,e):
        result = self.ems.writeBank02()
        self.writeAndScroll(result)
            
    def writeBankSRamClick(self,e):
        result = self.ems.writeSRam()
        self.writeAndScroll(result)

    # Useful function, write on resultText panel and scroll to the bottom
    def writeAndScroll(self, string):
        if (string and string != ''):
            prevStr = self.resultText.GetLabel()
            stringa = prevStr + string
            self.resultText.SetLabel(stringa)
            
            lines = string.split('\n')
            for n in lines:
                self.i += 20
            
            self.textPanel.FitInside()
            if(self.i > (self.textPanel.Size.GetHeight() - 20)):
                self.textPanel.Scroll(0,self.i)
        
            
if __name__ == '__main__':
    app = wx.App()
    EmsGui(None, title=strings.title)
    app.MainLoop()