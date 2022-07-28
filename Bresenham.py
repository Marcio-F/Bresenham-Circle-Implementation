import tkinter
import math

def showCoord(event):
    x = math.floor(((event.x - 500) / 10))
    y = math.floor(((500 - event.y) / 10))
    
    if event.x > 500:
        x = x + 1
    if event.y < 500:
        y = y + 1
    
    
    text = C.itemconfigure(tag, text=f'({x}, {y})')
    back = C.create_rectangle(C.bbox(tag), fill='black')
    C.tag_lower(back, text)

def drawPixel():
    for i in range(0, 1000, 10):
        if i != 500:
            C.create_line(0, i, 1000, i)
            C.create_line(i, 0, i, 1000)
        else:
            C.create_line(0, i, 1000, i, width=2)
            C.create_line(i, 0, i, 1000, width=2)
    
    C.bind('<Motion>', showCoord)
    
    global tag 
    tag = C.create_text(10, 10, text='', anchor='nw', font='Arial 20 bold', fill='white')
    
def circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    
    if xc <= 0: xc = xc + 1
    if yc <= 0: yc = yc + 1
    
    C.create_rectangle(500 + 10 * (xc - 1), 500 - 10 * (yc - 1), 500 + 10 * xc, 500 - 10 * yc, fill='red', outline='')
    drawCircle(xc, yc, x, y)
    
    while x <= y:
        if d <= 0:
            d = d + 2 * 10 * x + 3 * 10
        else:
            d = d + 2 * 10 * (x - y) + 5 * 10
            
            y = y - 1
        x = x + 1
        
        drawCircle(xc, yc, x, y)
    
def drawCircle(x_c, y_c, x, y):
    coord = 500 + 10 * (x_c + x - 1), 500 - 10 * (y_c + y - 1), 500 + 10 * (x_c + x), 500 - 10 *(y_c + y)
    C.create_rectangle(coord, fill='black', outline='')
    
    coord = 500 + 10 * (x_c - x - 1), 500 - 10 * (y_c + y - 1), 500 + 10 * (x_c - x), 500 - 10 * (y_c + y)
    C.create_rectangle(coord, fill='black', outline='')
    
    coord = 500 + 10 * (x_c + x - 1), 500 - 10 * (y_c - y - 1), 500 + 10 * (x_c + x), 500 - 10 * (y_c - y)
    C.create_rectangle(coord, fill='black', outline='')
    
    coord = 500 + 10 * (x_c - x - 1), 500 - 10 * (y_c - y - 1), 500 + 10 * (x_c - x), 500 - 10 * (y_c - y)
    C.create_rectangle(coord, fill='black', outline='')
    
    coord = 500 + 10 * (x_c + y - 1), 500 - 10 * (y_c + x - 1), 500 + 10 * (x_c + y), 500 - 10 * (y_c + x)
    C.create_rectangle(coord, fill='black', outline='')
    
    coord = 500 + 10 * (x_c - y - 1), 500 - 10 * (y_c + x - 1), 500 + 10 * (x_c - y), 500 - 10 * (y_c + x)
    C.create_rectangle(coord, fill='black', outline='')
    
    coord = 500 + 10 * (x_c + y - 1), 500 - 10 * (y_c - x - 1), 500 + 10 * (x_c + y), 500 - 10 * (y_c - x)
    C.create_rectangle(coord, fill='black', outline='')
    
    coord = 500 + 10 * (x_c - y - 1), 500 - 10 * (y_c - x - 1), 500 + 10 * (x_c - y), 500 - 10 * (y_c - x)
    C.create_rectangle(coord, fill='black', outline='')
    
    
if __name__ == '__main__':
    xc = int(input('Digite a coordenada x do centro: '))
    yc = int(input('Digite a coordenada y do centro: '))
    r = int(input('Digite o raio: '))
    
    root = tkinter.Tk()
    C = tkinter.Canvas(root, bg='white', height=1000, width=1000)
    C.pack()
    
    drawPixel()
    circle(xc, yc, r)
    
    root.mainloop()