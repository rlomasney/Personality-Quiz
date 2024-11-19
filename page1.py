import tkinter as tk

window = tk.Tk()
window.title("Window")

page_1 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)
Question_1 = tk.Label(
    master=page_1,
    text= "How do you typically react to change:",
    bg= "light grey"
)
q1_a1 = tk.Button(
    text= "I embrace change whenever it comes!",
    relief= "raised",
    bg= "grey"
)
q1_a2 = tk.Button(
    text= "i hate change!",
    relief= "raised",
    bg= "grey"
)

page_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
Question_1.place(x= 0, y= 0)
q1_a1.place(x=200, y=0)
q1_a2.place(x=200, y=30)
window.mainloop()