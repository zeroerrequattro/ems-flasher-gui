#!/usr/bin/python
# -*- coding: utf-8 -*-

import dialog
import appdirs

_dirs = appdirs.AppDirs("ems-flasher_gui", "0r4")

CONFIG_DIR     = _dirs.user_config_dir
DATA_DIR       = _dirs.user_data_dir
CACHE_DIR      = _dirs.user_cache_dir
LOG_DIR        = _dirs.user_log_dir
GBSavePath     = None
SRAMSavePath   = None
GBWritePath    = None
SRAMWritePath  = None
