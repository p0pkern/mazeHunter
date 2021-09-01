import tkinter as tk
import pprint

class GUI:
    
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
        self.top_frame.pack(fill=tk.X)

        # Toggle Start
        self.start_toggle = tk.Button(master=self.top_frame,
                                      text="Start Position",
                                      pady=5,
                                      command=self.toggle_start)
        self.start_toggle.pack()
        
        self.start_button_toggled = False

        # Toggle End
        self.end_toggle = tk.Button(master=self.top_frame,
                                    text="End Position",
                                    pady=5,
                                    command=self.toggle_end)
        
        self.end_toggle.pack()

        self.end_button_toggled = False

        # Center Grid
        self.grid_frame = tk.Frame(master=self.wndw_frame, 
                            background="black", 
                            width=800, 
                            height=500,
                            borderwidth=5,
                            relief=tk.SUNKEN)
        self.grid_frame.pack()

        # Bottom Console
        self.bottom_frame = tk.Frame(master=self.wndw_frame,
                                width=800,
                                height=20)
        self.bottom_frame.pack(fill=tk.X)

        # Dictionary for storing data
        self.grid_dict = {}

        # Grid Contents
        for i in range(25):
            for j in range(70):
                label = tk.Label(master=self.grid_frame, text="x")
                label.grid(row=i, column=j)
                label.bind('<Double 1>', lambda e, i=i, j=j: self.double_click(i,j))
                self.grid_dict[f'x{i}y{j}'] = {"label": label,
                                             "color": "white",
                                             "x" : i,
                                             "y" : j}
        self.wndw_frame.pack()
    
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

    def change_to_start(self, x, y):
        """
        Changes the color of the selected square to green to indicate the start position.
        """
        if self.grid_dict[f'x{x}y{y}']["color"] == "red":
            return
        elif self.grid_dict[f'x{x}y{y}']["color"] == "white":
            self.grid_dict[f'x{x}y{y}']["color"] = "green"
            self.grid_dict[f'x{x}y{y}']["label"].configure(background=self.grid_dict[f'x{x}y{y}']["color"])
        else:
            self.grid_dict[f'x{x}y{y}']["color"] = "white"
            self.grid_dict[f'x{x}y{y}']["label"].configure(background=self.grid_dict[f'x{x}y{y}']["color"])
    
    def change_to_end(self, x, y):
        if self.grid_dict[f'x{x}y{y}']["color"] == "green":
            return
        elif self.grid_dict[f'x{x}y{y}']["color"] == "white":
            self.grid_dict[f'x{x}y{y}']["color"] = "red"
            self.grid_dict[f'x{x}y{y}']["label"].configure(background=self.grid_dict[f'x{x}y{y}']["color"])
        else:
            self.grid_dict[f'x{x}y{y}']["color"] = "white"
            self.grid_dict[f'x{x}y{y}']["label"].configure(background=self.grid_dict[f'x{x}y{y}']["color"])

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

new_grid = GUI()
new_grid.do_loop()
