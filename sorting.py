import tkinter as tk
import random

worker=None

def highlight(selected):
    insert.config(bg="lightgray", fg="black")
    select.config(bg="lightgray", fg="black")
    bubble.config(bg="lightgray", fg="black")
    selected.config(bg="green", fg="white")

def swap(pos_0,pos_1):
    bar11,_,bar12,_=canvas.coords(pos_0)
    bar21,_,bar22,_=canvas.coords(pos_1)
    canvas.move(pos_0,bar21-bar11,0)
    canvas.move(pos_1,bar12-bar22,0)

def _insertion_sort():
    global barList,lengthList
    for i in range(len(lengthList)):
        cursor=lengthList[i]; cursorBar=barList[i]; pos=i
        while pos>0 and lengthList[pos-1]>cursor:
            lengthList[pos]=lengthList[pos-1]
            barList[pos],barList[pos-1]=barList[pos-1],barList[pos]
            swap(barList[pos],barList[pos-1]); yield
            pos-=1
        lengthList[pos]=cursor
        barList[pos]=cursorBar

def _bubble_sort():
    global barList,lengthList
    for i in range(len(lengthList)-1):
        for j in range(len(lengthList)-i-1):
            if lengthList[j]>lengthList[j+1]:
                lengthList[j],lengthList[j+1]=lengthList[j+1],lengthList[j]
                barList[j],barList[j+1]=barList[j+1],barList[j]
                swap(barList[j+1],barList[j]); yield

def _selection_sort():
    global barList,lengthList
    for i in range(len(lengthList)):
        m=i
        for j in range(i+1,len(lengthList)):
            if lengthList[j]<lengthList[m]:
                m=j
        lengthList[m],lengthList[i]=lengthList[i],lengthList[m]
        barList[m],barList[i]=barList[i],barList[m]
        swap(barList[m],barList[i]); yield

def insertion_sort():
    global worker
    highlight(insert)
    worker=_insertion_sort(); animate()
def selection_sort():
    global worker
    highlight(select)
    worker=_selection_sort(); animate()
def bubble_sort():
    global worker
    highlight(bubble)
    worker=_bubble_sort(); animate()

def animate():
    global worker
    if worker:
        try:
            next(worker)
            window.after(10,animate)
        except StopIteration:
            worker=None

def generate():
    global barList,lengthList
    insert.config(bg="lightgray",fg="black")
    select.config(bg="lightgray",fg="black")
    bubble.config(bg="lightgray",fg="black")
    canvas.delete("all")
    barList=[]; lengthList=[]
    s,e=5,15
    for _ in range(1,60):
        y=random.randint(1,360)
        b=canvas.create_rectangle(s,y,e,365,fill="skyblue")
        barList.append(b); s+=10; e+=10
    for b in barList:
        c=canvas.coords(b)
        lengthList.append(c[3]-c[1])
    mn,mx=min(lengthList),max(lengthList)
    for i,v in enumerate(lengthList):
        if v==mn: canvas.itemconfig(barList[i],fill="red")
        elif v==mx: canvas.itemconfig(barList[i],fill="black")

window=tk.Tk()
window.title("Sorting Visualizer")
window.geometry("600x450")
canvas=tk.Canvas(window,width=600,height=400)
canvas.grid(column=0,row=0,columnspan=50)
insert=tk.Button(window,text="Insertion Sort",command=insertion_sort)
select=tk.Button(window,text="Selection Sort",command=selection_sort)
bubble=tk.Button(window,text="Bubble Sort",command=bubble_sort)
shuf=tk.Button(window,text="Shuffle",command=generate)
shuf.grid(column=0,row=1); insert.grid(column=1,row=1); select.grid(column=2,row=1); bubble.grid(column=3,row=1)
generate()
window.mainloop()

