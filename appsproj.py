from tkinter import *
import random
import math
counter = 0
op = 0
num1 = ""
num2 = ""
def calc():
    def inp(num):
        global op, num1, num2
        end = 0
        global counter
        if num != "delete":
            res.insert(48, num)
        elif num == "delete":
            res.delete(0, END)
            num1 = ""
            num2 = ""
            op = 0
        oper = res.get()
        if (num == "*" or num == "-" or num == "+" or num == "/") and op == 0:
            for i in oper:
                num1 +=i
            op = 1
            act = num
        elif op == 1 and num == "=":
            op = len(num1)
            while oper[op] != "=":
                num2+=oper[op]
                op +=1
                res.delete(0,END)
            if num1[-1] == "*":
                num1 = num1.replace(num1[-1], "")
                res.insert(48, str(float(num1)*float(num2)))
                op = 0
                num1 = ""
                num2 = ""
            elif num1[-1] == "+":
                num1 = num1.replace(num1[-1], "")
                res.insert(48, str(float(num1)+float(num2)))
                op = 0
                num1 = ""
                num2 = ""
            elif num1[-1] == "-":
                num1 = num1.replace(num1[-1], "")
                res.insert(48, str(float(num1)-float(num2)))
                op = 0
                num1 = ""
                num2 = ""
            elif num1[-1] == "/":
                num1 = num1.replace(num1[-1], "")
                res.insert(48, str(float(num1)/float(num2)))
                op = 0
                num1 = ""
                num2 = ""
        elif num == "√":
            op = 2
        if op == 2 and num == "=":
            for i in oper:
                num1+=i
            res.delete(0,END)
            num1 = num1.replace(num1[0],"")
            num1 = num1.replace(num1[-1],"")
            res.insert(48, str(math.sqrt(float(num1))))
            op = 0
        elif num == "sin(":
            op = 3
        elif num == "cos(":
            op = 4
        elif num == "tg(":
            op = 5
        if op == 3 and num == "=":
            res.delete(0,END)
            num1 = oper.replace("sin(","")
            num1 = num1.replace("=","")
            res.insert(48, str(round(math.sin(math.radians(int(num1))), 3)))
        if op == 4 and num == "=":
            res.delete(0,END)
            num1 = oper.replace("cos(","")
            num1 = num1.replace("=","")
            res.insert(48, str(round(math.cos(math.radians(int(num1))), 3)))
        if op == 5 and num == "=":
            res.delete(0,END)
            num1 = oper.replace("tg(","")
            num1 = num1.replace("=","")
            print(num1)
            res.insert(48, str(round(math.tan(math.radians(int(num1))), 3)))
    cl = Toplevel()
    cl.geometry('300x350')
    cl.resizable(False, False)
    res = Entry(cl,width = 48, bd = 2)
    res.pack()
    one = Button(cl, text = "1", font = "Verdana 12", command = lambda: inp("1"), height = 3, width = 3).place(relx = 0, rely = 0.1)
    two = Button(cl, text = "2", font = "Verdana 12", command = lambda: inp("2"), height = 3, width = 3).place(relx = 0.15, rely = 0.1)
    three = Button(cl, text = "3", font = "Verdana 12", command = lambda: inp("3"), height = 3, width = 3).place(relx = 0.3, rely = 0.1)
    four = Button(cl, text = "4", font = "Verdana 12", command = lambda: inp("4"), height = 3, width = 3).place(relx = 0, rely = 0.3)
    five = Button(cl, text = "5", font = "Verdana 12", command = lambda: inp("5"), height = 3, width = 3).place(relx = 0.15, rely = 0.3)
    six = Button(cl, text = "6", font = "Verdana 12", command = lambda: inp("6"), height = 3, width = 3).place(relx = 0.3, rely = 0.3)
    seven = Button(cl, text = "7", font = "Verdana 12", command = lambda: inp("7"), height = 3, width = 3).place(relx = 0, rely = 0.5)
    eight = Button(cl, text = "8", font = "Verdana 12", command = lambda: inp("8"), height = 3, width = 3).place(relx = 0.15, rely = 0.5)
    nine = Button(cl, text = "9", font = "Verdana 12", command = lambda: inp("9"), height = 3, width = 3).place(relx = 0.3, rely = 0.5)
    zero = Button(cl, text = "0", font = "Verdana 12", command = lambda: inp("0"), height = 3, width = 3).place(relx = 0.15, rely = 0.7)
    minus = Button(cl, text = "-", font = "Verdana 12", command = lambda: inp("-"), height = 3, width = 3).place(relx = 0, rely = 0.7)
    plus = Button(cl, text = "+", font = "Verdana 12", command = lambda: inp("+"), height = 3, width = 3).place(relx = 0.3, rely = 0.7)
    sqrt = Button(cl, text = "√", font = "Verdana 12", command = lambda: inp("√"), height = 3, width = 2).place(relx = 0.45, rely = 0.1)
    cbut = Button(cl, text = "C", font = "Verdana 12", command = lambda: inp("delete"), height = 3, width = 3).place(relx = 0.6, rely = 0.1)
    sin = Button(cl, text = "sin", font = "Verdana 12", command = lambda: inp("sin("), height = 1, width = 3).place(relx = 0.45, rely = 0.3)
    cos = Button(cl, text = "cos", font = "Verdana 12", command = lambda: inp("cos("), height = 1, width = 3).place(relx = 0.6, rely = 0.3)
    tg = Button(cl, text = "tg", font = "Verdana 12", command = lambda: inp("tg("), height = 1, width = 3).place(relx = 0.75, rely = 0.3)
    mul = Button(cl, text = "*", font = "Verdana 12", command = lambda: inp("*"), height = 1, width = 3).place(relx = 0.75, rely = 0.1)
    equ = Button(cl, text = "=", font = "Verdana 12", command = lambda: inp("="), height = 5, width = 4).place(relx = 0.45, rely = 0.4)
    div = Button(cl, text = "/", font = "Verdana 12", command = lambda: inp("/"), height = 1, width = 3).place(relx = 0.75, rely = 0.2)
    dot = Button(cl, text = ".", font = "Verdana 12", command = lambda: inp("."), height = 3, width = 4).place(relx = 0.45, rely = 0.7)
def cube():
    cb = Toplevel()
    cb.geometry('150x180')
    cb.resizable(False, False)
    cb['bg'] = '#7CC399'
    c = Canvas(cb, width = 160, height = 100)
    c.pack()
    l1 = Label(cb, text = "Количество граней", background = "white").pack()
    e1 = Entry(cb, bd = 2, width = 2)
    e1.pack()
    c.create_rectangle(30, 25, 105, 100,outline='black',width=3,activedash=(5, 4), fill = "white")
    def kubik():
        c.create_rectangle(35,35,90,90, outline ="white", fill = "white")
        sides = e1.get()
        c.create_text(65, 70, text=(random.randint(1, int(sides))),font="Verdana 20",fill="#153626", width = 100)
    b= Button(cb,text="запустить", command=kubik, width = 20, background = "#7CC398").pack()
def func():
    fc = Toplevel()
    WIN_H=500
    WIN_W=800
    PANEL_H=WIN_H
    PANEL_W=200
    CANVAS_H=WIN_H
    CANVAS_W=WIN_W-PANEL_W
    fc.title("График")
    fc.config(width=WIN_W, height=WIN_H)
    fc.resizable(False, False)
    panel=Frame(fc, width=PANEL_W, height=PANEL_H, bd=4, relief=GROOVE)
    panel.place(x=0, y=0, width=PANEL_W, height=PANEL_H)
    canvas=Canvas(fc, width=CANVAS_W, height=CANVAS_H, bg="#90ee90")
    canvas.place(x=PANEL_W, y=0, width=CANVAS_W, height=CANVAS_W)
    def draw(x_left, x_right, y_bottom, y_top):
        dx= CANVAS_W/(x_right-x_left)
        dy=CANVAS_H/(y_top-y_bottom)
        cx=-x_left*dx
        cy= y_top*dy
        canvas.create_line(0, cy, CANVAS_W, cy, fill="#153626")
        canvas.create_line(cx, 0, cx, CANVAS_H, fill="#153626")
        x_step=(x_right-x_left)/25
        x=x_left
        y_step = (y_top - y_bottom)/25
        y = y_top
        while x <= x_right:
            x_canvas=(x-x_left)*dx
            canvas.create_line(x_canvas, cy+3,x_canvas,cy-3,fill="#153626")
            if x != 0:
                     canvas.create_text(x_canvas, cy-5, text=str(int(x)),font="Verdana 7",fill="#153626", width = 0.05)
            x+=1
        while y >= y_bottom:
            y_canvas = (y-y_top)*dy
            canvas.create_line(cx-3, -y_canvas, cx+3 ,-y_canvas,fill="#153626")
            canvas.create_text(cx+15, -y_canvas, text=str(int(round(y))),font="Verdana 7",fill="#153626", width = 0.05)
            y -= 1
        return dx, dy
    def frange(begin,end,step):
        x = begin
        t = []
        while x<= end:
            t.append(x)
            x += step
        return t
    def power(x_tmp,a,b,c,n):
        y_tmp = []
        for x in x_tmp:
            y = a*x**n+b*x+c
            y_tmp.append(y)
        return y_tmp
    def dot(x_tmp, y_tmp, col):
        i = 0
        for x in x_tmp:
            y = y_tmp[i]
            x = (x-x_tmp[0])*dx
            y = (y-y_top)*dy
            canvas.create_oval(x-1, -(y-1), x+1, -(y+1), fill = col, outline = col)
            i += 1

    def power_redraw():
        global y_power
        a = float(ent1.get())
        b = float(ent2.get())
        c = float(ent3.get())
        n = float(ent4.get())
        y_power= power(x_list, a, b, c, n)
        dot(x_list, y_power, '#153626')
    x_left, x_right= -5,15
    y_bottom, y_top= -15,20
    dx, dy = draw(x_left,x_right,y_bottom,y_top)
    x_list = frange(x_left, x_right, 0.001)
    lab01 = Label(panel, text="график вида y=ax^n+bx+c")
    lab01.place(x=0,y=0,width = 190, height = 30)
    lab1 = Label(panel,text="a")
    lab1.place(x=5, y=30, width=10, height=30)
    lab2 = Label(panel, text="b")
    lab2.place(x=5, y=60, width=10, height=30)
    lab3 = Label(panel, text="c")
    lab3.place(x=5, y=90, width=10, height=30)
    lab4 = Label(panel,text="n")
    lab4.place(x=5, y=120, width=10, height=30)
    ent1 = Entry (panel, bd=2)
    ent1.place(x=20, y=30, width=45)
    ent1.insert(0, "2")
    ent2 = Entry (panel, bd=2)
    ent2.place (x=20, y=60, width=45)
    ent2.insert (0, "-9")
    ent3 = Entry(panel,bd = 2)
    ent3.place (x=20, y=90, width=45)
    ent3. insert (0, "0")
    ent4 = Entry(panel,bd = 2)
    ent4.place (x=20, y=120, width=45)
    ent4. insert (0, "2")
    but1 = Button(panel, text = "отобразить", command = power_redraw)
    but1.place(x = 80, y = 50, width = 130, height = 30)
    
def geometry():
    def square4():
        t.delete(1.0, END)
        if en1.get() != "" and en2.get() != "" and en3.get() !="":
            t.insert(1.0,0.5*float(en1.get())*float(en2.get())*math.sin(math.radians(float(en3.get()))))
        elif en4.get() != "" and en5.get() != "" and en6.get() != "" and en7.get() != "":
            a = float(en4.get())
            b = float(en5.get())
            c = float(en6.get())
            d = float(en7.get())
            p = (a+b+c+d)*0.5
            a1 = float(en8.get())
            a2 = float(en9.get())
            print((p-a)*(p-b)*(p-c)*(p-d))
            print(math.cos(math.radians(a1+a2))**2)
            t.insert(1.0, math.sqrt((p-a)*(p-b)*(p-c)*(p-d)-(a*b*c*d*(math.cos(math.radians((a1+a2)/2)))**2)))
        elif (en1.get() == "" or en2.get() == "" or en3.get() =="") and (en4.get() == "" or en5.get() != "" and en6.get() != "" and en7.get() != ""):
            t.insert(1.0,"недостаточно данных")
        elif (en1.get() != "" and en2.get() != "" and en3.get() !="") and (en4.get() != "" and en5.get() != "" and en6.get() != "" and en7.get() != ""):
            t.insert(1.0,0.5*float(en1.get())*float(en2.get())*math.sin(math.radians(float(en3.get()))))
    ge = Toplevel()
    ge.geometry('600x500')
    ge.resizable(False, False)
    g = Canvas(ge, width = 600, height = 500, bg = "#ADCBB5")
    g.pack()
    g.create_polygon(30, 30, 100, 30, 120, 80, 50, 80, fill = "white", outline = "#153626")
    g.create_polygon(320, 30, 270, 80, 370, 80, fill = "white", outline = "#153626")
    g.create_text(320, 20, text="A",font="Verdana 14",fill="#153626", width = 0.05)
    g.create_text(260, 90, text="B",font="Verdana 14",fill="#153626", width = 0.05)
    g.create_text(380, 90, text="C",font="Verdana 14",fill="#153626", width = 0.05)
    g.create_line(30,30,120,80)
    g.create_line(100,30,50,80)
    g.create_line(320,30,320,80)
    g.create_line(219,0,219,600)
    g.create_text(20, 20, text="A",font="Verdana 14",fill="#153626", width = 0.05)
    g.create_text(110, 20, text="B",font="Verdana 14",fill="#153626", width = 0.05)
    g.create_text(40, 90, text="D",font="Verdana 14",fill="#153626", width = 0.05)
    g.create_text(130, 90, text="C",font="Verdana 14",fill="#153626", width = 0.05)
    g.create_text(65, 55, text="a",font="Verdana 8",fill="#153626", width = 0.05)
    g.create_text(25, 25, text="b",font="Verdana 8",fill="#153626", width = 0.05)
    g.create_text(65, 55, text="c",font="Verdana 8",fill="#153626", width = 0.05)
    g.create_text(110, 110, text="произвольный четырёхугольник",font="Verdana 10",fill="#153626", width = 0.05)
    en1 = Entry(ge)
    g.create_text(313, 110, text="произвольный треугольник",font="Verdana 10",fill="#153626", width = 0.05)
    en1 = Entry(ge)
    en1.place(x = 0, y = 120, width = 30)
    lb = Label(ge, text ="AC", bg = "#ADCBB5").place(x = 30, y = 120)
    en2 = Entry(ge)
    en2.place(x = 0, y = 140, width = 30)
    lb = Label(ge, text ="BD", bg = "#ADCBB5").place(x = 30, y = 140)
    en3 = Entry(ge)
    en3.place(x = 0, y = 160, width = 30)
    lb = Label(ge, text ="угол a", bg = "#ADCBB5").place(x = 30, y = 160)
    en4 = Entry(ge)
    en4.place(x = 0, y = 180, width = 30)
    lb = Label(ge, text ="AB", bg = "#ADCBB5").place(x = 30, y = 180)
    en5 = Entry(ge)
    en5.place(x = 0, y = 200, width = 30)
    lb = Label(ge, text ="BC", bg = "#ADCBB5").place(x = 30, y = 200)
    en6 = Entry(ge)
    en6.place(x = 0, y = 220, width = 30)
    lb = Label(ge, text ="CD", bg = "#ADCBB5").place(x = 30, y = 220)
    en7 = Entry(ge)
    en7.place(x = 0, y = 240, width = 30)
    lb = Label(ge, text ="DA", bg = "#ADCBB5").place(x = 30, y = 240)
    en8 = Entry(ge)
    en8.place(x = 0, y = 260, width = 30)
    lb = Label(ge, text ="угол c", bg = "#ADCBB5").place(x = 30, y = 260)
    en9 = Entry(ge)
    en9.place(x = 0, y = 280, width = 30)
    lb = Label(ge, text ="угол b", bg = "#ADCBB5").place(x = 30, y = 280)
    bu = Button(ge,text = "Найти площадь", bg = "#7CC398", command=square4).place(x = 0, y = 300)
    t = Text(ge, width=10, height=2)
    t.place(x = 80, y = 140)
    g.create_text(130, 125, text = "результат:", font="Verdana 14",fill="#153626", width = 0.05)
    en10 = Entry(ge)
    en10.place(x = 220, y = 120, width = 30)
    lb = Label(ge, text ="BC", bg = "#ADCBB5").place(x = 250, y = 120)
    en11= Entry(ge)
    en11.place(x = 220, y = 140, width = 30)
    lb = Label(ge, text ="AH", bg = "#ADCBB5").place(x = 250, y = 140)
    en12 = Entry(ge)
    en12.place(x = 220, y = 160, width = 30)
    lb = Label(ge, text ="угол a", bg = "#ADCBB5").place(x = 250, y = 160)
    en13 = Entry(ge)
    en13.place(x = 220, y = 180, width = 30)
    lb = Label(ge, text ="AB", bg = "#ADCBB5").place(x = 250, y = 180)
    en14 = Entry(ge)
    en14.place(x = 220, y = 200, width = 30)
    lb = Label(ge, text ="BC", bg = "#ADCBB5").place(x = 250, y = 200)
    en16 = Entry(ge)
    
root = Tk()
root.resizable(False, False)
root.geometry('182x155')
root.configure(background = "#ADCBB5")
l1 = Label(text="Микроприложения", width = 25, background = "#62A77C").pack()
b1 = Button(text="Калькулятор", command=calc, width = 25, background = "#7CC398").pack()
b2 = Button(text="Кубик", command=cube, width = 25, background = "#7CC398").pack()
b3 = Button(text="График ф-ций", command=func, width = 25, background = "#7CC398").pack()
b4 = Button(text="площади геометрических фигур", command=geometry, width = 25, background = "#7CC398").pack()
b5 = Button(text="", command=calc, width = 25, background = "#7CC398").pack()
root.mainloop()
