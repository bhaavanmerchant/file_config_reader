#!/bin/python
import re

def string_trimmer(str):
    if str.startswith('"') and str.endswith('"'):
        return str[1:-1]
    else:
        return str

def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def get_env(key):
    return re.search(r"\<([A-Za-z0-9_]+)\>", key).group(0)[1:-1]

def get_par(str):
    parent_re = re.compile(r"\[([A-Za-z0-9_]+)\]")
    return parent_re.match(str).group(0)[1:-1]

def parser(str):
    if str == "yes" or str == "1" or str == "true":
        return True
    elif str == "no" or str == "0" or str == "false":
        return False
    elif isint(str):
        return int(str)
    elif isfloat(str):
        return float(str)
    elif str.startswith('"') and str.endswith('"'):
        return str[1:-1]
    elif ',' in str:
        strArray = str.split(',')
        #Recusrsively call parser
        #for i in range(strArray):
        #    strArray[i] = parser(strArray[i])
        return strArray
    else:
        return str
