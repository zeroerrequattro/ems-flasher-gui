#!/usr/bin/python

import os.path
import wx
import subprocess
import dialog
import vars

class Flasher:
    def __init__(self):
        self.ems      = 'ems-flasher'
        self.emsCmd   = './' + self.ems
        self.test  = ['echo','ciao mondo']
        self.version  = ['--version']
        self.title    = ['--title']
        self.read01   = ['--read','--bank','1']
        self.read02   = ['--read','--bank','2']
        self.readSR   = ['--read']
        self.write01  = ['--write','--bank','1']
        self.fWrite01 = ['--rom','--bank','1']
        self.write02  = ['--write','--bank','2']
        self.fWrite02 = ['--rom','--bank','2']
        self.writeSR  = ['--write']
        self.fWriteSR = ['--save']

    def callBash(self, command):
        instruction = [self.emsCmd] + command
        if(self.checkEms()):
            try:
                output = subprocess.check_output(instruction) #,shell=True,stderr=subprocess.STDOUT
                return output
            except subprocess.CalledProcessError as e:
                return e.output
        else:
            return 'can\'t find ems-flasher. Is it in the same folder of this app?'

    def checkEms(self):
        if(not os.path.isfile(self.ems)):
            return False
        else:
            return True
        
    def checkCart(self):
        return self.callBash(self.title)
    
    def checkVersion(self):
        return self.callBash(self.version)
    
    def readBank01(self):
        def ok_handler(dlg,path):
            command = self.read01 + [str(path)]
            return self.callBash(command)

        if(vars.GBSavePath != None):
            command = self.read01 + [str(vars.GBSavePath)]
            return self.callBash(command)
        else:
            dialog.file_dialog('Save ROM as...','*.gb',wx.SAVE,ok_handler)

    def readBank02(self):
        def ok_handler(dlg,path):
            command = self.read02 + [str(path)]
            return self.callBash(command)

        if(vars.GBSavePath != None):
            command = self.read02 + [str(vars.GBSavePath)]
            return self.callBash(command)
        else:
            dialog.file_dialog('Save ROM as...','*.gb',wx.SAVE,ok_handler)

    def readSRam(self):
        def ok_handler(dlg,path):
            command = self.readSR + [str(path)]
            return self.callBash(command)

        if(vars.SRAMSavePath != None):
            command = self.readSR + [str(vars.SRAMSavePath)]
            return self.callBash(command)
        else:
            dialog.file_dialog('Save .sav file as...','*.sav',wx.SAVE,ok_handler)

    def writeBank01(self):
        def ok_handler(dlg,path):
            command = self.write01 + [str(path)]
            return self.callBash(command)

        if(vars.GBWritePath != None):
            command = self.write01 + [str(vars.GBWritePath)]
            return self.callBash(command)
        else:
            dialog.file_dialog('Load ROM file','*.gb',wx.OPEN,ok_handler)

    def forceWriteBank01(self):
        def ok_handler(dlg,path):
            command = self.write01 + [str(path)]
            return self.callBash(command)

        if(vars.GBWritePath != None):
            command = self.write01 + [str(vars.GBWritePath)]
            return self.callBash(command)
        else:
            dialog.file_dialog('Load ROM file','*.gb',wx.OPEN,ok_handler)

    def writeBank02(self):
        def ok_handler(dlg,path):
            command = self.write02 + [str(path)]
            return self.callBash(command)

        if(vars.GBWritePath != None):
            command = self.write02 + [str(vars.GBWritePath)]
            return self.callBash(command)
        else:
            dialog.file_dialog('Load ROM file','*.gb',wx.OPEN,ok_handler)

    def forceWriteBank02(self):
        def ok_handler(dlg,path):
            command = self.write02 + [str(path)]
            return self.callBash(command)

        if(vars.GBWritePath != None):
            command = self.write02 + [str(vars.GBWritePath)]
            return self.callBash(command)
        else:
            dialog.file_dialog('Load ROM file','*.gb',wx.OPEN,ok_handler)

    def writeSRam(self):
        def ok_handler(dlg,path):
            command = self.writeSR + [str(path)]
            return self.callBash(command)

        if(vars.SRAMWritePath != None):
            command = self.writeSR + [str(vars.SRAMWritePath)]
            return self.callBash(command)
        else:
            dialog.file_dialog('Load .sav file','*.sav',wx.OPEN,ok_handler)

    def forceWriteSRam(self):
        def ok_handler(dlg,path):
            command = self.fWriteSR + [str(path)]
            return self.callBash(command)

        if(vars.SRAMWritePath != None):
            command = self.fWriteSR + [str(vars.SRAMWritePath)]
            return self.callBash(command)
        else:
            dialog.file_dialog('Load .sav file','*.sav',wx.OPEN,ok_handler)
