#!/bin/python

disk_storage = {}

def fetch_from_disk(par,key,env):
    disk_emulator()
    try:
        val = disk_storage[par][key][env]
    except Exception as e:
        val = "NULL"
    return val


def disk_emulator():
    disk_storage["common"] = {}
    disk_storage["common"]["deamonizable"] = {}
    disk_storage["common"]["deamonizable"]["ubuntu"] = True
    disk_storage["common"]["deamonizable"]["_default"] = False
    disk_storage["common"]["deamonizable"]["staging"] = True
    disk_storage["common"]["port"] = {}
    disk_storage["common"]["port"]["production"] = 9000
    #disk_storage["common"][""] = {}
