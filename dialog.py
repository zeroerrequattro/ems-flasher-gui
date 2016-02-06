#!/usr/bin/python

import os, wx, vars

def popup_dialog(caption, msg, parent, exception=None):
    print(msg)

    if exception is not None or isinstance(msg, Exception):
        print(traceback.format_exc())

    showWindow = wx.MessageDialog(parent, msg, caption, wx.OK)
    showWindow.ShowModal()

def file_dialog(message, wildcard, style, ok_handler, default_file=''):
    last_opened_dir_file = os.path.join(vars.CACHE_DIR, 'last_opened_dir')

    last_opened_dir = None

    if os.path.exists(last_opened_dir_file):
        with open(last_opened_dir_file, 'r') as fp:
            last_opened_dir = fp.read().strip()

    if last_opened_dir is None or len(last_opened_dir) == 0:
        last_opened_dir = os.path.expanduser('~')

    dlg = wx.FileDialog(
        None, message, last_opened_dir, default_file, wildcard, style)

    res = None

    try:
        if dlg.ShowModal() == wx.ID_OK:
            last_opened_dir = dlg.GetDirectory()

            path = os.path.join(dlg.GetDirectory(), dlg.GetFilename())
            res = ok_handler(dlg, path)
    finally:
        dlg.Destroy()

    if not os.path.exists(vars.CACHE_DIR):
        os.makedirs(vars.CACHE_DIR)

    with open(last_opened_dir_file, 'w+') as fp:
        fp.write(last_opened_dir)

    return res
