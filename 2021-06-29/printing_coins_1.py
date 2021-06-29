#Version 1
print ("Version 1")
for _ in range(4):
  print("?", end = "")
print ("\n")

#Version 2
print("Version 2")

while True:
  width = int(input("What's the width? "))
  if width >= 0:
    break

for _ in range(width):
  print("?", end = "")
print ("\n")