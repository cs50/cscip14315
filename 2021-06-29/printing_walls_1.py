# asks user for wall size value (n) and checks for positive int
while True:
  n = int(input("What's the wall size? "))
  if n > 0:
    break
# prints n many of #'s in one line n many of times in the shell
for _ in range(n):
  print("#" * n)