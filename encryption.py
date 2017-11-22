import hashlib

print(hashlib.md5('yokoi'.encode('utf-8')).hexdigest())
print(hashlib.sha1('takuya'.encode('utf-8')).hexdigest())
