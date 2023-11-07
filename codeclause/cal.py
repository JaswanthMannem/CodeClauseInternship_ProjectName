import tkinter as tk

caluclation=""
def add_to_calculation(symbol):
    global caluclation
    caluclation=caluclation+str(symbol)
    text_result.delete(1.0,'end')
    text_result.insert(1.0,caluclation)

def evaluate_caluclation():
    global caluclation
    try:
        caluclation=str(eval(caluclation))
        text_result.delete(1.0,'end')
        text_result.insert(1.0,caluclation)
    except:
        clear_field()
        text_result.insert(1.0,"Error!")

def clear_field():
    global caluclation
    caluclation=""
    text_result.delete(1.0,'end')

root= tk.Tk()
root.geometry("300x275")
text_result=tk.Text(root,height=2,width=16,font=("Arial",24),bg="black",fg="white")
text_result.grid(columnspan=5)

btn_1=tk.Button(root,text="1",command=lambda: add_to_calculation(1),width=5,font=("Arial,14"),bg="green",fg="white")
btn_1.grid(row=2,column=1)
btn_2=tk.Button(root,text="2",command=lambda: add_to_calculation(2),width=5,font=("Arial,14"),bg="green",fg="white")
btn_2.grid(row=2,column=2)
btn_3=tk.Button(root,text="3",command=lambda: add_to_calculation(3),width=5,font=("Arial,14"),bg="green",fg="white")
btn_3.grid(row=2,column=3)
btn_4=tk.Button(root,text="4",command=lambda: add_to_calculation(4),width=5,font=("Arial,14"),bg="green",fg="white")
btn_4.grid(row=3,column=1)
btn_5=tk.Button(root,text="5",command=lambda: add_to_calculation(5),width=5,font=("Arial,14"),bg="green",fg="white")
btn_5.grid(row=3,column=2)
btn_6=tk.Button(root,text="6",command=lambda: add_to_calculation(6),width=5,font=("Arial,14"),bg="green",fg="white")
btn_6.grid(row=3,column=3)
btn_7=tk.Button(root,text="7",command=lambda: add_to_calculation(7),width=5,font=("Arial,14"),bg="green",fg="white")
btn_7.grid(row=4,column=1)
btn_8=tk.Button(root,text="8",command=lambda: add_to_calculation(8),width=5,font=("Arial,14"),bg="green",fg="white")
btn_8.grid(row=4,column=2)
btn_9=tk.Button(root,text="9",command=lambda: add_to_calculation(9),width=5,font=("Arial,14"),bg="green",fg="white")
btn_9.grid(row=4,column=3)
btn_10=tk.Button(root,text="0",command=lambda: add_to_calculation(0),width=5,font=("Arial,14"),bg="green",fg="white")
btn_10.grid(row=5,column=2)
btn_11=tk.Button(root,text="+",command=lambda: add_to_calculation("+"),width=5,font=("Arial,14"),bg="hotpink",fg="white")
btn_11.grid(row=2,column=4)
btn_12=tk.Button(root,text="-",command=lambda: add_to_calculation("-"),width=5,font=("Arial,14"),bg="hotpink",fg="white")
btn_12.grid(row=3,column=4)
btn_12=tk.Button(root,text="x",command=lambda: add_to_calculation("*"),width=5,font=("Arial,14"),bg="hotpink",fg="white")
btn_12.grid(row=4,column=4)
btn_13=tk.Button(root,text="%",command=lambda: add_to_calculation("%"),width=5,font=("Arial,14"),bg="hotpink",fg="white")
btn_13.grid(row=5,column=4)
btn_14=tk.Button(root,text="(",command=lambda: add_to_calculation("("),width=5,font=("Arial,14"),bg="blue",fg="white")
btn_14.grid(row=5,column=1)
btn_15=tk.Button(root,text=")",command=lambda: add_to_calculation(")"),width=5,font=("Arial,14"),bg="blue",fg="white")
btn_15.grid(row=5,column=3)
btn_17=tk.Button(root,text="Clear",command=clear_field,width=11,font=("Arial,14"),bg="orange",fg="white")
btn_17.grid(row=6,column=1,columnspan=2)
btn_16=tk.Button(root,text="=",command=evaluate_caluclation,width=11,font=("Arial,14"),bg="orange",fg="white")
btn_16.grid(row=6,column=3,columnspan=2)


root.mainloop()
