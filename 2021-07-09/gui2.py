import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Hello World!")

    button = tk.Button(window, text="Click me")
    button.grid(row=0, column=0)

    window.mainloop()

if __name__ == "__main__":
    main()
