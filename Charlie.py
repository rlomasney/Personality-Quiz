import tkinter as tk

window = tk.Tk()
window.title("Window")

Openess_list= [1,1,0,1]

Extraversion_list = [-1,-1,0,1]
combined_scores = []


def opn_score():
    total = 0
    for num in Openess_list:
        total += num
    total = float(total/4)
    opn_tuple = ("Openess Score:", total)
    #print(opn_tuple)
    combined_scores.append(opn_tuple)
    #print(combined_scores)
    
def ext_score():
    total = 0
    for num in Extraversion_list:
        total += num
    total = float(total/4)
    ext_tuple = ("Exraversion Score:", total)
    #print(ext_tuple)
    combined_scores.append(ext_tuple)
    #print(combined_scores)

def result_list():
    opn_score()
    ext_score()
    print(combined_scores)

pleasework = tk.Button(
    master=window,
    text="Please",
    command= result_list
)

results = tk.Button(
    master=window,
    text="click for results",
    command=lambda: print(combined_scores)
)


pleasework.pack()
results.pack()

opn_score()
ext_score()
print(combined_scores)
#window.mainloop()