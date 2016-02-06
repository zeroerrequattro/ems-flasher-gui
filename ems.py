#!/usr/bin/python

import wx, subprocess, dialog, strings, vars

class Flasher:
    def __init__(self): 
        self.version  = ['--version']
        self.title    = ['--title']
        self.format   = ['--format']
        self.delete01 = ['--delete','BANK','1']
        self.delete02 = ['--delete','BANK','2']
        self.read01   = ['--read','--rom','--bank','1']
        self.read02   = ['--read','--rom','--bank','2']
        self.readSR   = ['--read','--save']
        self.write01  = ['--write','--rom','--bank','1']
        self.write02  = ['--write','--rom','--bank','2']
        self.writeSR  = ['--write','--save']

    def callBash(self, command):
        if(self.checkEms()):
            instruction = [vars.emsPath,'--verbose'] + command
            try:
                output = subprocess.check_output(instruction)
                return output
            except subprocess.CalledProcessError as e:
                return e.output
        else:
            return strings.notFound

    def checkEms(self):
        if(vars.emsPath != None):
            return True
        else:
            return False

    def loadEms(self):
        def ok_handler(dlg,path):
            vars.emsPath = path
            return strings.emsSet + vars.emsPath + '\n'
        
        return dialog.file_dialog(strings.dlgLoadEms,'',wx.OPEN,ok_handler)

    def checkVersion(self):
        return self.callBash(self.version)

    def checkCart(self):
        return self.callBash(self.title)

    def deleteBank01(self):
        return self.callBash(self.delete01)

    def deleteBank02(self):
        return self.callBash(self.delete02)

    def formatCart(self):
        return self.callBash(self.format)

    def readBank01(self):
        def ok_handler(dlg,path):
            command = self.read01 + [str(path)]
            return self.callBash(command)
        
        if(vars.GBSavePath != None):
            command = self.read01 + [str(vars.GBSavePath)]
            return self.callBash(command)
        else:
            return dialog.file_dialog(strings.dlgSaveROM,'*.gb',wx.SAVE,ok_handler,'backup_bank-1.gb')

    def readBank02(self):
        def ok_handler(dlg,path):
            command = self.read02 + [str(path)]
            return self.callBash(command)

        if(vars.GBSavePath != None):
            command = self.read02 + [str(vars.GBSavePath)]
            return self.callBash(command)
        else:
            return dialog.file_dialog(strings.dlgSaveROM,'*.gb',wx.SAVE,ok_handler,'backup_bank-2.gb')

    def readSRam(self):
        def ok_handler(dlg,path):
            command = self.readSR + [str(path)]
            return self.callBash(command)

        if(vars.SRAMSavePath != None):
            command = self.readSR + [str(vars.SRAMSavePath)]
            return self.callBash(command)
        else:
            return dialog.file_dialog(strings.dlgSaveSav,'*.sav',wx.SAVE,ok_handler,'backup.sav')

    def writeBank01(self):
        def ok_handler(dlg,path):
            command = self.write01 + [str(path)]
            return self.callBash(command)

        if(vars.GBWritePath != None):
            command = self.write01 + [str(vars.GBWritePath)]
            return self.callBash(command)
        else:
            return dialog.file_dialog(strings.dlgLoadROM,'*.gb',wx.OPEN,ok_handler)

    def writeBank02(self):
        def ok_handler(dlg,path):
            command = self.write02 + [str(path)]
            return self.callBash(command)

        if(vars.GBWritePath != None):
            command = self.write02 + [str(vars.GBWritePath)]
            return self.callBash(command)
        else:
            return dialog.file_dialog(strings.dlgLoadROM,'*.gb',wx.OPEN,ok_handler)

    def writeSRam(self):
        def ok_handler(dlg,path):
            command = self.writeSR + [str(path)]
            return self.callBash(command)

        if(vars.SRAMWritePath != None):
            command = self.writeSR + [str(vars.SRAMWritePath)]
            return self.callBash(command)
        else:
            return dialog.file_dialog(strings.dlgLoadSav,'*.sav',wx.OPEN,ok_handler)
