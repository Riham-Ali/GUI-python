import tkinter as tk

window =tk.Tk()
window.geometry("600x600")
window.title("hello...!")

def first_function():
    text="hello World!.."
    text_output=tk.Label(window, text=text)
    text_output.grid(row=1, column=1)

first_button=tk.Button(text="open ", command=first_function)
first_button.grid(row=0 , column=0)


if __name__=="__main__":
    window.mainloop()