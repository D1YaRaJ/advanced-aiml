import tkinter as tk

W,H=5,5
obstacles={(1,1),(2,2),(3,1)}
tasks={(0,2),(2,3),(3,0)}
agent=[0,0]
CELL_SIZE=60

root=tk.Tk()
root.title("Maze Game")
outer_frame=tk.Frame(root,padx=5,pady=5,bd=2)
outer_frame.pack(padx=5,pady=5)
tk.Label(outer_frame,text="Task Collecting Maze",font=("Arial",20,"bold")).pack(pady=(0,10))
canvas=tk.Canvas(outer_frame,width=W*CELL_SIZE,height=H*CELL_SIZE,bg="white",bd=2)
canvas.pack(pady=10)

def draw_grid():
    canvas.delete("all")
    for y in range(H):
        for x in range(W):
            color="white"
            symbol="."
            if (x,y)==tuple(agent): symbol="A"
            elif (x,y) in tasks: symbol="T"
            elif (x,y) in obstacles: symbol="X"
            canvas.create_rectangle(x*CELL_SIZE,y*CELL_SIZE,(x+1)*CELL_SIZE,(y+1)*CELL_SIZE,fill=color,outline="black")
            canvas.create_text(x*CELL_SIZE+CELL_SIZE//2,y*CELL_SIZE+CELL_SIZE//2,text=symbol,font=("Arial",24,"bold"))
    if not tasks:
        text="All Tasks Collected!"
        x_center=W*CELL_SIZE/2
        y_center=H*CELL_SIZE/2
        canvas.create_rectangle(x_center-120,y_center-25,x_center+120,y_center+25,fill="white",outline="black",width=2)
        canvas.create_text(x_center,y_center,text=text,font=("Arial",18,"bold"))

def valid(x,y): return 0<=x<W and 0<=y<H and (x,y) not in obstacles
def move(dx,dy):
    if not tasks: return
    nx,ny=agent[0]+dx,agent[1]+dy
    if valid(nx,ny):
        agent[0],agent[1]=nx,ny
        if (nx,ny) in tasks: tasks.remove((nx,ny))
        draw_grid()

move_up=lambda:move(0,-1)
move_down=lambda:move(0,1)
move_left=lambda:move(-1,0)
move_right=lambda:move(1,0)

control_frame=tk.Frame(outer_frame)
control_frame.pack(pady=10)
btn_style={"width":5,"height":2,"font":("Arial",16,"bold")}
tk.Button(control_frame,text="↑",command=move_up,**btn_style).grid(row=0,column=1,padx=5,pady=5)
tk.Button(control_frame,text="←",command=move_left,**btn_style).grid(row=1,column=0,padx=5,pady=5)
tk.Button(control_frame,text="→",command=move_right,**btn_style).grid(row=1,column=2,padx=5,pady=5)
tk.Button(control_frame,text="↓",command=move_down,**btn_style).grid(row=2,column=1,padx=5,pady=5)

root.bind("<Up>",lambda e:move_up())
root.bind("<Down>",lambda e:move_down())
root.bind("<Left>",lambda e:move_left())
root.bind("<Right>",lambda e:move_right())

draw_grid()
root.mainloop()
