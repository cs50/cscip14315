#Question and failsafe
while True:
  n = int(input("What's the size? "))
  if n > 0:
    break

#Loops
for _ in range (n):
  for _ in range (n):
    print("#", end="")
  print()