import sys;
import os.path;

from passlib.hash import md5_crypt;

if len(sys.argv) != 4:
  print("Usage: password_crack [dictionary] [password] [prefix]")
  sys.exit(0);

if not os.path.isfile(sys.argv[1]):
  print("[!] Dictionary " + sys.argv[1] + " not found.");
  sys.exit(0);

with open(sys.argv[1]) as file:
  content = file.readlines();

content = [x.strip() for x in content];

for password in content:
  if md5_crypt.verify(sys.argv[3] + password, sys.argv[2]):
    print("[!] Password found: %s" % (sys.argv[3] + password))
    sys.exit(0);


print("[!] Password not found");
