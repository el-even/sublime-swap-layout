SwapKeyboardLayout
===============

SwapKeyboardLayout is a plugin for Sublime Text 2 and 3
(http://www.sublimetext.com/3) for swapping of selected text keyboard layout.
It can be useful for _______

This plugin is based on SublimeTranslit.

Intented to be used via Command Palette or via Hotkey.

Try openning Command Palette and typing "swap".

Creating Transliteration Dictionaries
=====================================

SwapKeyboardLayout supports extending it with additional dictionaries.

Every Dictionary is described by two files:

1. *dictionary_name.dict* is used to define characters mapping.
2. *dictionary_name.sublime-commands* is used to add a command for this
dictionary to Command Palette.

All these dictionary files should be placed into *SwapKeyboardLayout*
plugin directory.

dictionary_name.dict
--------------------

Contains mapping (dictionary *chars_mapping*) of latin characters to source
characters which will be transliterated.

Take a look at example:

    {
        "name": "Cyrillic (russian)",
        "description": "GOST 7.79 System B, modified ISO 9:1995",
        "link": "http://en.wikipedia.org/wiki/ISO_9",
        "chars_mapping":
        {
            "A":   "\u0410",
            "B":   "\u0411",
        }
    }

All other fields (name, description, link) is optional and specified in order
to explain used translit rules and point to source documents.

dictionary_name.sublime-commands
--------------------------------

It is a ordinary .sublime-commands file for Command Palette item for this
dictionary.

Should run command *swap_keyboard_layout* with parameter
*dictionary_file* - a file name of **dictionary_name.dict**.

Example:

    [
        {
            "caption": "Swap keyboard layout: QWERTY-JCUKEN",
            "command": "swap_keyboard_layout", "args":
            {
                "dictionary_file": "dictionary_name.sublime-commands"
            }
        }
    ]
