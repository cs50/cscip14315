def main():
  size = int(input("What's the size? ")) # ask user for size
  wallPrinter(size) # call size function

def wallPrinter(n): # declare size function
  for i in range(n): # I want to print this vertically n times, and it will auto - 
                     # matically add the \n character for me
    print('#'*n) # then i print out the horizontal line n times

if __name__ == "__main__":
  main()