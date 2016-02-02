#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import dialog
import vars

class FileDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        for name in filenames:
            try:
                string = self.window.GetLabel()
                if(name.lower().endswith('.gb')):
                    vars.GBWritePath = str(name)
                    string += '\n ROM file set:\n' + str(name)
                elif(name.lower().endswith('.sav')):
                    vars.SRAMWritePath = str(name)
                    string += '\n .sav file set:\n' + str(name)
                else:
                    string += '\n the file you chosen can\'t be used' 
                self.window.SetLabel(string)
            except IOError, error:
                dialog.popup_dialog('IOError Exception!','Error opening file\n' + str(error),None)
            except UnicodeDecodeError, error:
                dialog.popup_dialog('UnicodeDecodeError Exception!','Cannot open non ascii files\n' + str(error),None)
