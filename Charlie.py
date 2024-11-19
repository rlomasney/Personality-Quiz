import tkinter as tk

window = tk.Tk()
window.title("Window")

page_1 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)
Question_1 = tk.Label(                  #Measuring Opennes
    master=page_1,
    text= "Question TEXT GOES HERE",
    bg= "light grey"
)
q1_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    text= "ANSWER TEXT GOES HERE",
    relief= "raised",
    bg= "grey"
)
q1_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    text= "ANSWER TEXT GOES HERE",
    relief= "raised",
    bg= "grey"
)
q1_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    text= "ANSWER TEXT GOES HERE",
    relief= "raised",
    bg= "grey"
)

page_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
Question_1.place(x= 0, y= 0)
q1_a1.place(x=200, y=0)
q1_a2.place(x=200, y=30)
q1_a3.place(x=200, y=60)
window.mainloop()