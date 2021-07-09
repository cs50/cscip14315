import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Hello World!")
    window.geometry("200x200")

    button = tk.Button(window, text="Click me")
    button.grid(row=0, column=0)

    window.mainloop()

if __name__ == "__main__":
    main()
