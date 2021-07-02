def main():
    for _ in range(height):
        print("#")

def get_height():
    while True:
        try:
            return int(input("What's height? "))
        except:
            pass

main()
