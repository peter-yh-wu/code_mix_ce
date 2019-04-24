#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Zimeng Qiu <zimengq@andrew.cmu.edu>
# Licensed under the Apache License v2.0 - http://www.apache.org/licenses/

import os
import re

def read_dataset(data_path):
    data = []
    for (dirpath, dirs, files) in os.walk(data_path):
        for file in files:
            with open(os.path.join(dirpath, file), "r") as f:
                text = f.readlines()
                data.extend([[word for word in line.strip().split(" ")[3:] if word != '<v-noise>'] for line in text])
    return data


def is_english_word(word):
    """
    Decide if a token in a document is an valid English word.
    For this project, we define valid English words to be ASCII strings that
    contain only letters (both upper and lower case), single quotes ('),
    double quotes ("), and hyphens (-). Double quotes may only appear at the
    beginning or end of a token unless the beginning/end of a token is no-letter
    characters. Double quotes cannot appear in the middle of letter characters.
    (for example, "work"- is valid, but home"work and -bi"cycle- are not).
    Tokens cannot be empty.
    :param word: A token in document.
    :return: Boolean value, True or False
    """
    return all([char in ["\"", "\'", "-", "*", "~", "*", "."] or char.isalpha() for char in word])

def has_chinese_char(word):
    return len(re.findall(r'[\u4e00-\u9fff]+', word)) > 0


def is_chinese_word(char):
    if len(char) > 1:
        return False
    ranges = [
        {"from": ord(u"\u3300"), "to": ord(u"\u33ff")},  # compatibility ideographs
        {"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},  # compatibility ideographs
        {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},  # compatibility ideographs
        {"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")},  # compatibility ideographs
        {'from': ord(u'\u3040'), 'to': ord(u'\u309f')},  # Japanese Hiragana
        {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},  # Japanese Katakana
        {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},  # cjk radicals supplement
        {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
        {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
        {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
        {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
        {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
        {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # included as of Unicode 8.0
    ]
    return any([range["from"] <= ord(char) <= range["to"] for range in ranges])