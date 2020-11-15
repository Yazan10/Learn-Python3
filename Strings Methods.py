# -------------------------------
# ------- Strings Methods -------
# -------------------------------

# strip() & rstrip() & lstrip()
# strip() method was work to remove white space
a="    Python its Amazanig    "

print(a)
print(a.strip())
print(a.rstrip())
print(a.lstrip())

print('___________________________')

# strip("character") method was work to remove the character

b="######Python its Amazanig######"

print(b)
print(b.strip("#"))
print(b.rstrip("#"))
print(b.lstrip("#"))

print('___________________________')

c="#&&#&#&#&#&#Python its Amazanig#&&#&#&#&#&#"

print(c)
print(c.strip("#&"))
print(c.rstrip("#&"))
print(c.lstrip("#&"))

print('___________________________')

# title()
# this method

print("I love 4d Graphics and 5g technology and python")
d="I love 4d Graphics and 5g technology and python"
print(d.title())

print('___________________________')

# capitalize()
# this method

print("I love 4d Graphics and 5g technology and python")
e="i love 4d graphics and 5g technology and python"
print(e.capitalize())

print('___________________________')

# zfill

f,g,h,i="1","11","111","1111"
print(f)
print(g)
print(h)

print('___________________________')

print(f.zfill(3))
print(g.zfill(3))
print(h.zfill(3))
print(i.zfill(4))

print('___________________________')

#upper() & lower()

j = "yazan"
print(j.upper())
print(j.lower())

print('___________________________')

