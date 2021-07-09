import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Hello World!")
    window.geometry("200x200")

    button = tk.Button(window, text="Click me")
    button["command"] = greet
    button.grid(row=0, column=0)

    label = tk.Label(window, text="This is a label")
    label.grid(row=1, column=0)

    window.mainloop()

def greet():
    print("Hi there")

if __name__ == "__main__":
    main()
