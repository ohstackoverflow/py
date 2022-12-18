import hashlib
import codecs

publickey = codecs.decode('038d5b9221e12fe27fade96f3c2ca72c53c587508206a13b6bfdaafc01494a12ad', 'hex')
s = hashlib.new('sha256', publickey).digest()
r = hashlib.new('ripemd160', s).digest()

print(codecs.encode(s, 'hex').decode("utf-8"))
print(codecs.encode(r, 'hex').decode("utf-8"))
