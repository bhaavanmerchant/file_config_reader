#!/bin/python

import config_loader


config_loader.ConfigLoad("file.config", ["ubuntu", "production"])
#print(config_loader.get("ftp.name"))
print("Executing Test cases...")
assert(config_loader.get("common.paid_users_size_limit") == 2147483648)
assert(config_loader.get("ftp.name") == "hello there, ftp uploading")
assert(config_loader.get("http.params") == ['array', 'of', 'values'])
assert(config_loader.get("ftp.lastname") == "NULL")
assert(config_loader.get("ftp.enabled") == False)
assert(config_loader.get("ftp.path") == "/etc/var/uploads")
assert(config_loader.get("ftp") == {
                                        'path': '/etc/var/uploads',
                                        'name': 'hello there, ftp uploading',
                                        'enabled': False
                                    })
print("All tests done!")
