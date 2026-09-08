#project1 wiget board and daily planner project for snowglobe
import tkinter as tk
from tkinter import ttk, colorchooser, simpledialog

class DraggableWidget(tk.frame):
     """Base class for building custom drag and drop dashboard frames."""
     
     def __init__(self,parent,title="widget" ,bg_color="2e3138",**kwargs):
                 super().__init__(parent,bg=bg_color,bd=2,relief="groove",**kwargs)

self.drag_handle = tk.Frame(self,bg="1e2022",height=25)
self.drag_handle.pack(fill="x",side="top")
self.drag_handle.pack_propagate(False)

self.title_label =  tk.Label( self.drag_handle,text=title,fg="ffffff",bg="1e2022",font="Arial" 9 "bold")

self.title_label.pack(side="left",padx=5)

self.drag_handle.bind("<Button-1>", self.start_drag)
self.drag_handle.bind("<B1-Motion>", self.on_drag)
self.title_label.bind("<Button-1>", self.start_drag)
self.title_label.bind("<B1-Motion>", self.on_drag)

def start_drag(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y
        self.lift()

def on_drag(self, event):
        x = self.winfo_x() - self._drag_start_x + event.x
        y = self.winfo_y() - self._drag_start_y + event.y
        self.place(x=x, y=y)
        
class StickyNote(DraggableWidget):
    """A highly customizable digital sticky note with runtime text and color changes."""

    def __init__(self, parent, text="Double-click to edit note...", x=50, y=50):
        super().__init__(parent, title="📌 Sticky Note", bg_color="#fff275")
        self.place(x=x, y=y, width=200, height=200)

    
        self.color_btn = tk.Frame(self.drag_handle, bg="#e0d030", width=15, height=15)
        self.color_btn.pack(side="right", padx=5, pady=5)
        self.color_btn.bind("<Button-1>", self.change_color)
        
self.text_label = tk.Label(self,text=text,bg="#fff275",fg="#222222",wraplength=180,justify="left",font=("Comic Sans MS", 11),anchor="nw",
        )
self.text_label.pack(fill="both", expand=True, padx=8, pady=8)
self.text_label.bind("<Double-Button-1>", self.edit_text)

def edit_text(self, event):
    new_text = simpledialog.askstring("Edit Note", "Enter note text:", initialvalue=self_text_label["text"])
    if new_text:
     self.text_label.config(text=new_text)

    def change_color(self, event):
        color = colorchooser.askcolor(title="Pick Sticky Note Color")[1]
        if color:
            self.config(bg=color)
            self.text_label.config(bg=color)


class PlaylistWidget(DraggableWidget):
    """A visual playlist frame mocking up music stream deck configurations."""

    def __init__(self, parent, x=50, y=280):
        super().__init__(parent, title="🎵 Playlist Controller", bg_color="#181818")
        self.place(x=x, y=y, width=280, height=150)

        # Simulated Playlist Styling
        track_info = tk.Label(self,text="Lo-Fi Beats For Coding 🎧",fg="#1db954",bg="#181818",font=("Arial", 11, "bold"),
        )
        track_info.pack(pady=10)

        sub_info = tk.Label(self,text="Track: Neon Nights\nStatus: Connected Placeholder",fg="#aaaaaa",bg="#181818",font=("Arial", 9))
        sub_info.pack(pady=5)

        ctrl_frame = tk.Frame(self, bg="#181818")
        ctrl_frame.pack(pady=10)

        for btn_text in ["⏮", "▶", "⏸", "⏭"]:
            btn = tk.Button(ctrl_frame,text=btn_text,fg="#ffffff",bg="#333333",activebackground="#555555",activeforeground="#ffffff",relief="flat",width=4,
            )
            btn.pack(side="left", padx=4)


class PixelPlantTrackerWidget(DraggableWidget):
    """A gamified engine rendering procedural pixel art representing real-time goal metrics."""

    def __init__(self, parent, x=300, y=50):
        super().__init__(
            parent, title="🌱 Habit Matrix & Evolution Engine", bg_color="#282a36"
        )
        self.place(x=x, y=y, width=450, height=380)

        self.xp = 0
        self.habits = ["Complete Daily Code Focus", "Drink 3L Water", "Gym Session"]


        self.left_frame = tk.Frame(self, bg="#282a36")
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.canvas_frame = tk.Frame(self, bg="#282a36")
        self.canvas_frame.pack(side="right", padx=10, pady=10)

        # Pixel Engine Canvas setup
        self.canvas = tk.Canvas(
            self.canvas_frame, width=160, height=180, bg="#1e1f29", bd=0, highlightthickness=0
        )
        self.canvas.pack()

        self.status_lbl = tk.Label(self.canvas_frame,text="Level 1: Tiny Sprout",fg="#50fa7b",bg="#282a36",font=("Arial", 10, "bold"),
        )
        self.status_lbl.pack(pady=5)

        self.xp_lbl = tk.Label(self.canvas_frame,text="Growth XP: 0",fg="#ff79c6",bg="#282a36",font=("Arial", 9),
        )
        self.xp_lbl.pack()

        self.build_habit_list()
        self.render_pixel_plant()

    def build_habit_list(self):
        title = tk.Label(self.left_frame,text="Daily Goals Checklist",fg="#f8f8f2",bg="#282a36",font=("Arial", 11, "bold"),
        )
        title.pack(anchor="w", pady=(0, 10))

        for habit in self.habits:
            f = tk.Frame(self.left_frame, bg="#282a36")
            f.pack(fill="x", pady=4)

            var = tk.BooleanVar()
            cb = tk.Checkbutton(f,text=habit,variable=var,fg="#f8f8f2",bg="#282a36",selectcolor="#1e1f29",
                activebackground="#282a36",
                activeforeground="#f8f8f2",
                font=("Arial", 10),
                command=lambda v=var: self.on_habit_toggle(v),
            )
            cb.pack(side="left")

    def on_habit_toggle(self, variable):
        if variable.get():
            self.xp += 25
        else:
            self.xp = max(0, self.xp - 25)

        self.xp_lbl.config(text=f"Growth XP: {self.xp}")
        self.render_pixel_plant()

    def draw_pixel(self, x, y, size, color):
        """Draws a grid coordinate pixel element safely on the UI resolution system."""
        self.canvas.create_rectangle(x * size,y * size,(x + 1) * size,(y + 1) * size,fill=color,outline=color,
        )

    def render_pixel_plant(self):
        """Draws the pixel art plant dynamically based on the current XP tier."""
        self.canvas.delete("all")
        p_size = 8 


        pot_pixels = [
            (8, 17), (9, 17), (10, 17), (11, 17),
            (7, 16), (8, 16), (9, 16), (10, 16), (11, 16), (12, 16),
            (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15),
            (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14), (13, 14)
        ]
        for px, py in pot_pixels:
            self.draw_pixel(px, py, p_size, "#ff5555")

    
        if self.xp == 0:
            self.status_lbl.config(text="Stage 0: Planted Seed")
            self.draw_pixel(9, 13, p_size, "#ffb86c")
        elif self.xp <= 25:
            self.status_lbl.config(text="Stage 1: Breaking Soil")
            stem = [(9, 13), (9, 12)]
            for px, py in stem:
                self.draw_pixel(px, py, p_size, "#50fa7b")
        elif self.xp <= 50:
            self.status_lbl.config(text="Stage 2: Young Sprout")
            stem = [(9, 13), (9, 12), (9, 11), (8, 11), (10, 12)]
            for px, py in stem:
                self.draw_pixel(px, py, p_size, "#50fa7b")
        else:
            self.status_lbl.config(text="Stage 3: Full Blossom Flower!")
            
            stem = [(9, 13), (9, 12), (9, 11), (9, 10), (8, 11), (10, 10)]
            for px, py in stem:
                self.draw_pixel(px, py, p_size, "#50fa7b")
            
            petals = [(9, 9), (9, 7), (8, 8), (10, 8)]
            for px, py in petals:
                self.draw_pixel(px, py, p_size, "#ff79c6")
            
            self.draw_pixel(9, 8, p_size, "#f1fa8c")


class ProductivityDashboardApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Visual Custom Productivity Suite Engine")
        self.root.geometry("1000x650")
        self.root.configure(bg="#1e1f29")

    
        instruction_frame = tk.Frame(self.root, bg="#282a36", height=40)
        instruction_frame.pack(fill="x", side="top")
        lbl = tk.Label(
            instruction_frame,
            text="💻 Local Dev Dashboard | Drag header components to rearrange workspace freely.",
            fg="#f8f8f2",
            bg="#282a36",
            font=("Arial", 10, "italic"),
        )
        lbl.pack(pady=10)      
        self.workspace = tk.Frame(self.root, bg="#1e1f29")