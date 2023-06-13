import tkinter as tk
from tkinter import messagebox
from ..Gameplay.World import World


class Application(tk.Frame) :
    def __init__(self, master = None, size = 20, cell_size = 30) :
        super().__init__(master)
        self.size = size
        self.cell_size = cell_size
        self.canvas = tk.Canvas(self, width = size * cell_size, height = size * cell_size + 10)
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_cell_click)
        self.world = World.basic()

        button_frame = tk.Frame(self)
        button_frame.pack(side = tk.BOTTOM)

        self.new_game_button = tk.Button(self, text = "Next round", command = None)
        self.new_game_button.pack(side = tk.LEFT)

        self.menu_button = tk.Menubutton(self, text = "Options")
        self.menu = tk.Menu(self.menu_button, tearoff = False)
        self.menu.add_command(label = "Load", command = None)
        self.menu.add_command(label = "Save", command = self.save)
        self.menu_button.configure(menu = self.menu)
        self.menu_button.pack(side = tk.RIGHT)

    def draw_board(self) :
        for row in range(self.size) :
            for col in range(self.size) :
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = "cyan"

                for org in self.world:
                    if (org.x == col and org.y == row) :
                        color = org.draw()


                self.canvas.create_rectangle(x1, y1, x2, y2, fill = color)


    def on_cell_click(self, event) :
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        self.show_menu(event.x, event.y)


    def show_menu(self, x, y) :
        menu = tk.Menu(self, tearoff = False)
        menu.add_command(label = "Antylopa", command = None)
        menu.add_command(label = "Cyber Owca", command = None)
        menu.add_command(label = "Owca", command = None)
        menu.add_command(label = "Lis", command = None)
        menu.add_command(label = "Wilk", command = None)
        menu.add_command(label = "Zolw", command = None)
        menu.add_command(label = "====================", command = None)
        menu.add_command(label = "Barszcz Sosnowskiego", command = None)
        menu.add_command(label = "Guarana", command = None)
        menu.add_command(label = "Mlecz", command = None)
        menu.add_command(label = "Trawa", command = None)
        menu.add_command(label = "Wilcze Jagody", command = None)
        menu.post(x, y)

    def save(self) :
        messagebox.showinfo("Successful save", "Game has been saved!")

root = tk.Tk()
root.title("Patryk Miszke 193249")

app = Application(root)
app.pack()




