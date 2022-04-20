import tkinter as tk


class master:
    def __init__(self, *args, **kwargs, master = None):
        self.master = master

        self.create()

    def create(self):

        self.mainCan = Canvas(self.master)

        self.R8X = self.canvas.create_rectangle(
                0, 0, 100, 100,
                fill = "pink",
                outline = "black",
                width = 2
                )

        self.R4X = self.canvas.create_rectangle(
                100, 0, 200, 200,
                fill = "pink",
                outline = "black",
                width = 2
                )

        self.R2X = self.canvas.create_rectangle(
                200, 0, 300, 300,
                fill = "pink",
                outline = "black",
                width = 2
                )

        self.R1X = self.canvas.create_rectangle(
                300, 0, 400, 400
                fill = "pink",
                outline = "black",
                width = 2
                )

        mainCan.grid(
                master,


        self.canvas.grid


root = tk.Tk()
root.title("Binary Counter Display")
root.grid()
root.geometry("600x100")

root.mainloop()
