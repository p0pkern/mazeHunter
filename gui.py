import tkinter as tk
from mazeHunter import BFS, DFS

class GUI:
    """
    This is the main grid and gui interface for the maze hunter.
    The grid size is pre-set to 25 rows and 70 columns. This is chosen to 
    look good on a smaller screen that I have, and also running efficiently.

    It could be adjusted larger, but I feel like in it's current state it is 
    just enough to get the ponit accross.
    """

    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.wndw_frame = tk.Frame(master=self.window, 
                                   width=1500, 
                                   height=1500)
        # Top Console
        self.top_frame = tk.Frame(master=self.wndw_frame, 
                                         width=800, 
                                         height=100)
        self.top_frame.pack(fill=tk.X, padx=20, pady=5)

        # Toggle Start
        self.start_toggle = tk.Button(master=self.top_frame,
                                      text="Start Position",
                                      pady=5,
                                      command=self.toggle_start)
        self.start_toggle.pack(side=tk.LEFT, padx=10)
        
        self.start_button_toggled = False

        # Toggle End
        self.end_toggle = tk.Button(master=self.top_frame,
                                    text="End Position",
                                    pady=5,
                                    command=self.toggle_end)
        
        self.end_toggle.pack(side=tk.LEFT, padx=10)

        self.end_button_toggled = False

        # Toggle Barrier
        self.barrier_toggle = tk.Button(master=self.top_frame,
                                        text="Create Barrier",
                                        pady=5,
                                        command=self.toggle_barrier)
        self.barrier_toggle.pack(side=tk.LEFT, padx=10)

        self.barrier_button_toggled = False

        # Start Search
        self.start_BFS = tk.Button(master=self.top_frame,
                                      text="Breadth First Search",
                                      pady=5,
                                      command=self.initiate_BFS)

        self.start_BFS.pack(side=tk.LEFT, padx=10)

        self.start_DFS = tk.Button(master=self.top_frame,
                                      text="Depth First Search",
                                      pady=5,
                                      command=self.initiate_DFS)

        self.start_DFS.pack(side=tk.LEFT, padx=10)

        # Clear Grid
        self.clear_grid_button = tk.Button(master= self.top_frame,
                                           text="Clear Grid",
                                           pady=5,
                                           command=self.clear_grid)
        
        self.clear_grid_button.pack(side=tk.LEFT, padx=10)
        # Center Grid
        self.grid_frame = tk.Frame(master=self.wndw_frame, 
                            background="black", 
                            width=800, 
                            height=500,
                            borderwidth=5,
                            relief=tk.SUNKEN)
        self.grid_frame.pack()

        # Bottom Square
        self.bottom_frame = tk.Frame(master=self.wndw_frame,
                                width=800,
                                height=20)
        self.bottom_frame.pack(fill=tk.X)

        # Dictionary for storing data
        self.grid_dict = {}

        # Grid Contents
        self.grid_rows = 25
        self.grid_columns = 70

        for i in range(self.grid_rows):
            for j in range(self.grid_columns):
                label = tk.Label(master=self.grid_frame, text="x")
                label.grid(row=i, column=j)
                label.bind('<Double 1>', lambda e, i=i, j=j: self.double_click(i,j))

                top = None
                bottom = None
                left = None
                right = None

                if i - 1 >= 0:
                    top = f"x{i-1}y{j}"
                if i + 1 <= self.grid_rows - 1:
                    bottom = f"x{i+1}y{j}"
                if j - 1 >= 0:
                    left = f"x{i}y{j-1}"
                if j + 1 <= self.grid_columns - 1:
                    right = f"x{i}y{j+1}"

                self.grid_dict[f'x{i}y{j}'] = {"label": label,
                                             "color": "white",
                                             "x" : i,
                                             "y" : j,
                                             "top" : top,
                                             "bottom": bottom,
                                             "left": left,
                                             "right": right,
                                             "id" : f'x{i}y{j}'}
        self.wndw_frame.pack()

    def initiate_BFS(self):
        """
        Activate the breadth first search. 
        """
        BFS(self.get_dictionary(), self.adjust_colors)
    
    def initiate_DFS(self):
        """
        Activate Depth first search.
        """
        DFS(self.get_dictionary(), self.adjust_colors)

    def change_color(self, x, y, color):
        """
        Changes color at coordinate to assigned color. Not for the animation funcitonality.
        """
        self.grid_dict[f'x{x}y{y}']["color"] = color
        self.grid_dict[f'x{x}y{y}']["label"].configure(background=color)

    def toggle_start(self):
        """
        Changes the start button to True or False
        If True it will disable all other buttons and let you set the start square on the grid.
        If False will not let any placement or adjustment of the start button.
        """
        if self.start_button_toggled:
            self.start_button_toggled = False
            self.start_toggle.configure(highlightbackground="white")
        else:
            self.start_button_toggled = True
            self.start_toggle.configure(highlightbackground="green")
            if self.end_button_toggled:
                self.toggle_end()
            if self.barrier_button_toggled:
                self.toggle_barrier()
            
    def toggle_end(self):
        """
        Changes the end button to True or False
        If True it will disable all other buttons and let you set the end square on the grid.
        If False will not let any placement or adjustment of the end button
        """
        if self.end_button_toggled:
            self.end_button_toggled = False
            self.end_toggle.configure(highlightbackground="white")
        else:
            self.end_button_toggled = True
            self.end_toggle.configure(highlightbackground="red")
            if self.start_button_toggled:
                self.toggle_start()
            if self.barrier_button_toggled:
                self.toggle_barrier()

    def toggle_barrier(self):
        """
        Changes the barrier button to True or False
        If True it will let you put in a barrier square
        If False it will not let you make placements of any barrier.
        """
        if self.barrier_button_toggled:
            self.barrier_button_toggled = False
            self.barrier_toggle.configure(highlightbackground="white")
        else:
            self.barrier_button_toggled = True
            self.barrier_toggle.configure(highlightbackground="black")
            if self.end_button_toggled:
                self.toggle_end()
            if self.start_button_toggled:
                self.toggle_start()

    def double_click(self, x, y):
        """
        Reads a double click and 
        """
        if self.start_button_toggled:
            if self.grid_dict[f'x{x}y{y}']["color"] == "green":
                self.change_to_start(x, y)
            else:
                self.delete_position()
                self.change_to_start(x, y)
        elif self.end_button_toggled:
            if self.grid_dict[f'x{x}y{y}']["color"] == "red":
                self.change_to_end(x, y)
            else:
                self.delete_position()
                self.change_to_end(x, y)
        elif self.barrier_button_toggled:
            if self.grid_dict[f'x{x}y{y}']["color"] == "white":
                self.change_color(x, y, "black")
            else:
                self.change_color(x, y, "white")

    def change_to_start(self, x, y):
        """
        Changes the color of the selected square to green to indicate the start position.
        """
        if self.grid_dict[f'x{x}y{y}']["color"] == "red":
            return
        elif self.grid_dict[f'x{x}y{y}']["color"] == "white":
            self.change_color(x, y, "green")
        else:
            self.change_color(x, y, "white")
    
    def change_to_end(self, x, y):
        """
        Changes the color of the selected square to red to indicate end position.
        """
        if self.grid_dict[f'x{x}y{y}']["color"] == "green":
            return
        elif self.grid_dict[f'x{x}y{y}']["color"] == "white":
            self.change_color(x, y, "red")
        else:
            self.change_color(x, y, "white")
    
    def create_barrier(self, x, y):
        """
        Changes the correspoding square to black, to indicate it is a barrier
        """
        if self.grid_dict[f'x{x}y{y}']["color"] == "green" or self.grid_dict[f'x{x}y{y}']["color"] == "red":
            return
        elif self.grid_dict[f'x{x}y{y}']["color"] == "white":
            self.change_color(x, y, "black")
        
    def delete_position(self):
        """
        Deletes all other colors to ensure only one start and one end.
        """
        if self.start_button_toggled:
            for key in self.grid_dict:
                if self.grid_dict[key]["color"] == "green":
                    x = self.grid_dict[key]["x"]
                    y = self.grid_dict[key]["y"]
                    self.change_to_start(x, y)
        if self.end_button_toggled:
            for key in self.grid_dict:
                if self.grid_dict[key]["color"] == "red":
                    x = self.grid_dict[key]["x"]
                    y = self.grid_dict[key]["y"]
                    self.change_to_end(x, y)

    def adjust_colors(self, id):
        """
        Callable function for the algorithms that will update the colors of the grid.
        Currently this function does not work how I hope and I'm looking into options
        on how to get the desired effect.
        """
        self.grid_dict[id]["label"].configure(background=self.grid_dict[id]["color"])

    def clear_grid(self):
        """
        Clears the grid by setting all grid items to the color white indicating it is blank.
        """
        for i in self.grid_dict:
            self.grid_dict[i]["color"] = "white"
            self.adjust_colors(i)

    def do_loop(self):
        """
        Loop the GUI
        """
        self.window.mainloop()

    def get_dictionary(self):
        """
        Returns dictionary containing the data of the grid.
        """
        return self.grid_dict


if __name__ == "__main__":
    g = GUI()
    g.do_loop()