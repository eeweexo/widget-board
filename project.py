#project1 wiget board and daily planner project for snowglobe
# project1 widget board and daily planner project for snowglobe
import tkinter as tk
from tkinter import ttk, colorchooser, simpledialog


class DraggableWidget(tk.Frame):
    """Base class for building custom drag and drop dashboard frames."""
def __init__(self, parent, title="widget", bg_color="#2e3138", **kwargs):
        super().__init__(parent, bg=bg_color, bd=2, relief="groove", **kwargs)

self.drag_handle = tk.Frame(self, bg="#1e2022", height=25)
self.drag_handle.pack(fill="x", side="top")
self.drag_handle.pack_propagate(False)

self.title_label = tk.Label(self.drag_handle,text=title,fg="#ffffff",bg="#1e2022",font=("Arial", 9, "bold"),(self.title_label.pack(side="left", padx=5)
(self.drag_handle.bind("<Button-1>", self.start_drag)
(self.drag_handle.bind("<B1-Motion>", self.on_drag)
(self.title_label.bind("<Button-1>", self.start_drag)
(self.title_label.bind("<B1-Motion>", self.on_drag)

self.content_frame = tk.Frame(self, bg=bg_color)
self.content_frame.pack(fill="both", expand=True)

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

        self.text_label = tk.Label(self.content_frame,text=text,bg="#fff275",fg="#222222",wraplength=180,justify="left",
        font=("Comic Sans MS", 11),
            anchor="nw",
        )
        self.text_label.pack(fill="both", expand=True, padx=8, pady=8)
        self.text_label.bind("<Double-Button-1>", self.edit_text)

    def edit_text(self, event):
        new_text = simpledialog.askstring(
            "Edit Note", "Enter note text:", initialvalue=self.text_label["text"]
        )
        if new_text is not None:
            self.text_label.config(text=new_text)

    def change_color(self, event):
        color = colorchooser.askcolor(title="Pick Sticky Note Color")[1]
        if color
            self.config(bg=color)
            self.content_frame.config(bg=color)
            self.text_label.config(bg=color)


class PlaylistWidget(DraggableWidget):
    """A visual playlist frame mocking up music stream deck configurations."""

    def __init__(self, parent, x=50, y=280):
        super().__init__(parent, title="🎵 Playlist Controller", bg_color="#181818")
        self.place(x=x, y=y, width=280, height=150)
     
        track_info = tk.Label 
            self.content_frame,
            text="Lo-Fi Beats For Coding 🎧",
            fg="#1db954",
            bg="#181818",
            font=("Arial", 11, "bold"),
        )
        track_info.pack(pady=10)

        sub_info = tk.Label(
            self.content_frame,
            text="Track: Neon Nights\nStatus: Connected Placeholder",
            fg="#aaaaaa",
            bg="#181818",
            font=("Arial", 9),
        )
        sub_info.pack(pady=5)

        ctrl_frame = tk.Frame(self.content_frame, bg="#181818")
        ctrl_frame.pack(pady=10)

        for btn_text in ["⏮", "▶", "⏸", "⏭"]:
            btn = tk.Button(
                ctrl_frame,
                text=btn_text,
                fg="#ffffff",
                bg="#333333",
                activebackground="#555555",
                activeforeground="#ffffff",
                relief="flat",
                width=4,
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

        self.left_frame = tk.Frame(self.content_frame, bg="#282a36")
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.canvas_frame = tk.Frame(self.content_frame, bg="#282a36")
        self.canvas_frame.pack(side="right", padx=10, pady=10)

        
        self.canvas = tk.Canvas(
            self.canvas_frame,
            width=160,
            height=180,
            bg="#1e1f29",
            bd=0,
            highlightthickness=0,
        )
        self.canvas.pack()

        self.status_lbl = tk.Label(
            self.canvas_frame,
            text="Level 1: Tiny Sprout",
            fg="#50fa7b",
            bg="#282a36",
            font=("Arial", 10, "bold"),
        )
        self.status_lbl.pack(pady=5)

        self.xp_lbl = tk.Label(
            self.canvas_frame, text="Growth XP: 0", fg="#ff79c6", bg="#282a36", font=("Arial", 9)
        )
        self.xp_lbl.pack()

        self.build_habit_list()
        self.render_pixel_plant()

    def build_habit_list(self):
        title = tk.Label(
            self.left_frame,
            text="Daily Goals Checklist",**


       
