MIN_HEIGHT = 1
MAX_HEIGHT = 8

def main():
    while True:
        height = int(input("Height: "))
        if is_valid_height(height):
            break
    pyramid = build_pyramid(height)
    print(pyramid)

def is_valid_height(height):
    return height >= MIN_HEIGHT and height <= MAX_HEIGHT

def build_pyramid(height):
    pyramid = ""
    for row in range(height):
        pyramid += get_spaces_for(row, height)
        pyramid += get_hashtags_for(row)
        if row < height - 1:
            pyramid += "\n"
    return pyramid

def get_spaces_for(row, height):
    spaces = ""
    num_of_spaces = height - row - 1
    for _ in range(num_of_spaces):
        spaces += " "
    return spaces

def get_hashtags_for(row):
    num_of_hashtags = row + 1
    hashtags = ""
    for _ in range(num_of_hashtags):
        hashtags += "#"
    return hashtags

if __name__ == "__main__":
    main()
