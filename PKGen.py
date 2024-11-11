import random
import time
import string

is_loop = 1
print("          PRODUCT KEY GENERATOR")
print("kaka developing. all rights reserved.")
print("")
print("!the product key has 25 letters!")
print("")
while is_loop < 10:
    is_loop = is_loop + 1
    print("")
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    c = random.choice(string.ascii_letters)
    d = random.choice(string.ascii_letters)
    e = random.choice(string.ascii_letters)
    f = random.choice(string.ascii_letters)
    g = random.choice(string.ascii_letters)
    h = random.choice(string.ascii_letters)
    i = random.choice(string.ascii_letters)
    j = random.choice(string.ascii_letters)
    k = random.choice(string.ascii_letters)
    l = random.choice(string.ascii_letters)
    m = random.choice(string.ascii_letters)
    n = random.choice(string.ascii_letters)
    o = random.choice(string.ascii_letters)
    p = random.choice(string.ascii_letters)
    r = random.choice(string.ascii_letters)
    s = random.choice(string.ascii_letters)
    t = random.choice(string.ascii_letters)
    u = random.choice(string.ascii_letters)
    v = random.choice(string.ascii_letters)
    z = random.choice(string.ascii_letters)
    za = random.choice(string.ascii_letters)
    zb = random.choice(string.ascii_letters)
    zc = random.choice(string.ascii_letters)
    prod_key = a+b+c+d+e+"-"+f+g+h+i+j+"-"+k+l+m+n+o+"-"+p+r+s+t+u+"-"+v+z+za+zb+zc
    print("your product key:")
    print(prod_key.upper())
    print("")
input("press enter to exit...")
exit()