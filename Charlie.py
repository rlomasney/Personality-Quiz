import tkinter as tk

window = tk.Tk()
window.title("Window")

page_4 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)
question_labels_4 = tk.Frame(
    master=page_4,
    bg="light grey",
    width=275, 
    height=475,
)
answers_labels_4 = tk.Frame(
    master=page_4,
    bg="light grey",
    width=500, 
    height=510,
)

def next4to5():
    page_4.forget()
    page_5.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

def next5tofinish():
    page_5.forget()
    #PACK the final page here 


page_5 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)
question_labels_5 = tk.Frame(
    master=page_5,
    bg="light grey",
     width=275, 
    height=475
)
answers_labels_5 = tk.Frame(
    master=page_5,
    bg="light grey",
     width=500, 
    height=510,
)


Question_13 = tk.Label(                  #Measuring Openness
    master=question_labels_4,
    text= "How do you react when meeting new people?",
    bg= "light grey"
)
q13_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master= answers_labels_4,
    text= "I don't find myself excited, but I am not scared to.",
    relief= "raised",
    bg= "grey"
)
q13_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_4,
    text= "I love to meet new people, and strike up conversation with them.",
    relief= "raised",
    bg= "grey"
)
q13_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "I get nervous and tend to avoid meeting new people.",
    relief= "raised",
    bg= "grey"
)

Question_14 = tk.Label(                  #Measuring Agreableness
    master=question_labels_4,
    text= "How do you typically treat others?",
    bg= "light grey"
)
q14_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_4,
    text= "I don't think I am particularly kind, but I don't think I am mean.",
    relief= "raised",
    bg= "grey"
)
q14_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_4,
    text= "I try to always treat others with kindness and respect.",
    relief= "raised",
    bg= "grey"
)
q14_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "I am typically not sensitive of other peoples feelings.",
    relief= "raised",
    bg= "grey"
)

Question_15 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_4,
    text= "How Often do you feel sad or depressed?",
    bg= "light grey"
)
q15_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_4,
    text= "I only find myself feeling sad or depressed when a situation warrants it.",
    relief= "raised",
    bg= "grey"
)
q15_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_4,
    text= "I dont find myself feeling sad or depressed.",
    relief= "raised",
    bg= "grey"
)
q15_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "I frequently feel sad or depressed.",
    relief= "raised",
    bg= "grey"
)

Question_16 = tk.Label(                  #Measuring Consientiousness
    master=question_labels_4,
    text= "What's your process when making decisions?",
    bg= "light grey"
)
q16_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_4,
    text= "Sometimes I plan things out, but I also trust my gut.",
    relief= "raised",
    bg= "grey"
)
q16_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_4,
    text= "I think about the consequences of one decision over another and choose the best one.",
    relief= "raised",
    bg= "grey"
)
q16_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "I just trust my gut and go with what I feel..",
    relief= "raised",
    bg= "grey"
)
Next_p4 = tk.Button(
    master=answers_labels_4,
    text="Next",
    relief="raised",
    command=next4to5
)


Question_17 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_5,
    text= "Do you get stressed easily?",
    bg= "light grey"
)
q17_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_5,
    text= "Yes, but sometimes I am better at managing it than other times.",
    relief= "raised",
    bg= "grey"
)
q17_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_5,
    text= "No, but even when I do feel stressed, I bounce back quickly.",
    relief= "raised",
    bg= "grey"
)
q17_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_5,
    text= "Yes, and once I'm stressed, it's hard for me to calm down.",
    relief= "raised",
    bg= "grey"
)

Question_18 = tk.Label(                  #Measuring Extraversion
    master=question_labels_5,
    text= "How do you feel about small talk?",
    bg= "light grey"
)
q18_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_5,
    text= "It depends on how I am feeling, but occasionally I engage in small talk.",
    relief= "raised",
    bg= "grey"
)
q18_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_5,
    text= "I consider myself a small talk expert.",
    relief= "raised",
    bg= "grey"
)
q18_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_5,
    text= "Small talk makes me anxious, and I tend to avoid talking about myself.",
    relief= "raised",
    bg= "grey"
)

Question_19 = tk.Label(                  #Measuring ???Not sure???
    master=question_labels_5,
    text= "Would your firends describe you as dependable?",
    bg= "light grey"
)
q19_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_5,
    text= "It depends on what we're doing, but generally yes.",
    relief= "raised",
    bg= "grey"
)
q19_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_5,
    text= "Yes, I'm reliable and honor my commitments or plans.",
    relief= "raised",
    bg= "grey"
)
q19_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_5,
    text= "Probably not. I tend to be kind of flaky.",
    relief= "raised",
    bg= "grey"
)

Question_20 = tk.Label(                  #Measuring ???Not sure???
    master=question_labels_5,
    text= "How do you feel about repetitive tasks?",
    bg= "light grey"
)
q20_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_5,
    text= "Sometimes I need tasks like that to help me calm down.",
    relief= "raised",
    bg= "grey"
)
q20_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_5,
    text= "I'm comfortable with repetitive tasks; routine is good.",
    relief= "raised",
    bg= "grey"
)
q20_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_5,
    text= "I get bored easily and need variety whenever possible.",
    relief= "raised",
    bg= "grey"
)
Next_p5 = tk.Button(
    master=answers_labels_4,
    text="Next",
    relief="raised",
    command=next5tofinish
)



page_4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

question_labels_4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Question_13.place(x= 0, y= 0)
q13_a1.place(x=00, y=0)
q13_a2.place(x=00, y=30)
q13_a3.place(x=00, y=60)

Question_14.place(x= 0, y= 120)
q14_a1.place(x=00, y=120)
q14_a2.place(x=00, y=150)
q14_a3.place(x=00, y=180)

Question_15.place(x= 0, y= 240)
q15_a1.place(x=00, y=240)
q15_a2.place(x=00, y=270)
q15_a3.place(x=00, y=300)

Question_16.place(x= 0, y= 360)
q16_a1.place(x=00, y=360)
q16_a2.place(x=00, y=390)
q16_a3.place(x=00, y=420)

Next_p4.place(x=0, y= 480)

question_labels_5.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_5.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Question_17.place(x= 0, y= 0)
q17_a1.place(x=0, y=0)
q17_a2.place(x=0, y=30)
q17_a3.place(x=0, y=60)
Question_18.place(x= 0, y= 120)
q18_a1.place(x=0, y=120)
q18_a2.place(x=0, y=150)
q18_a3.place(x=0, y=180)
Question_19.place(x= 0, y= 240)
q19_a1.place(x=0, y=240)
q19_a2.place(x=0, y=270)
q19_a3.place(x=0, y=300)
Question_20.place(x= 0, y= 360)
q20_a1.place(x=0, y=360)
q20_a2.place(x=0, y=390)
q20_a3.place(x=0, y=420)

Next_p5.place(x=0, y=480)

window.mainloop()