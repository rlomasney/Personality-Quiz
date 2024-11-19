import tkinter as tk

window = tk.Tk()
window.title("Window")

page_welcome = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)
welcome = tk.Label(
    master=page_welcome,
    text= "Welcome! \n Please press the button below to begin your Personality Quiz Journey:",
    bg= "light grey"
)

page_welcome.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
welcome.place(x= 200, y= 200)
window.mainloop()