#!/bin/python
import parse_config
import disk_reader
import os
import cache_manager

#class ConfigLoader:

__current_environment__ = ["_default"]
def ConfigLoad(filename, env=[]):
    global __current_environment__
    if isinstance(env, str):
        __current_environment__.append(env)
    elif isinstance(env, list):
        __current_environment__ += reversed(env)
    parent = "default"
    try:
        f = open(filename, 'r')
        for line in f:
            line = line.split(";")[0].strip()
            if (line and line!= "") :
                if (line.startswith('[')):
                    parent = parse_config.get_par(line)
                    cache_manager.create_as_dict(parent)
                    continue
                split_line = line.split('=')
                key = split_line[0].strip()
                value = "NULL"
                if len (split_line) > 2:
                    value = ""
                    for l in split_line[1:]:
                        value += l
                elif len (split_line) == 2:
                    value = split_line[1]
                value = parse_config.parser(value.strip())
                if (key.endswith('>')) :
                    environment = parse_config.get_env(key)
                    key = key.split('<')[0]
                    cache_manager.create_as_dict(parent,key)
                    cache_manager.set_val(parent,key,environment,value)
                else:
                    cache_manager.create_as_dict(parent,key)
                    cache_manager.set_val(parent,key,"_default",value)
        f.close()
    except IOError:
        print("Could not read file:", filename)
    except Exception as e:
        print("Unexpected error:", e)


def get(propName):
    if isinstance(propName, str) != True:
        return "NULL"
    propertyArray = propName.split(".")
    if (len(propertyArray) == 3):
        par = propertyArray[0]
        key = propertyArray[1]
        env = propertyArray[2]
        if cache_manager.is_present_in_dict(par,key,env):
            return cache_manager.return_and_update_cache(par,key,env)
    elif (len(propertyArray) == 2):
        par = propertyArray[0]
        key = propertyArray[1]
        if cache_manager.is_present_in_dict(par,key):
            for env in reversed(__current_environment__):
                if cache_manager.is_present_in_dict(par,key,env):
                    return cache_manager.return_and_update_cache(par,key,env)
        else:
            return cache_manager.check_and_put_cache(par,key)
    elif (len(propertyArray) == 1):
        par = propertyArray[0]
        if cache_manager.is_present_in_dict(par):
            ConfigMap = {}
            for key in cache_manager.get_keys(par):
                for env in reversed(__current_environment__):
                    if cache_manager.is_present_in_dict(par,key,env):
                        ConfigMap[key] = cache_manager.get_val(par,key,env)
                        break
            return ConfigMap
    return cache_manager.check_and_put_cache(par,key)
