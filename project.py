#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, colorchooser, simpledialog
import random
import copy


class DraggableWidget(tk.Frame):
    """Base class for building custom drag and drop dashboard frames."""

    def __init__(self, parent, title="widget", bg_color="#2e3138", **kwargs):
        super().__init__(parent, bg=bg_color, bd=2, relief="groove", **kwargs)
        self._locked = False
        self.drag_handle = tk.Frame(self, bg="#1e2022", height=25)
        self.drag_handle.pack(fill="x", side="top")
        self.drag_handle.pack_propagate(False)
        self.title_label = tk.Label(
            self.drag_handle,
            text=title,
            fg="#ffffff",
            bg="#1e2022",
            font=("Arial", 9, "bold"),
        )
        self.title_label.pack(side="left", padx=5)
        self.drag_handle.bind("<Button-1>", self.start_drag)
        self.drag_handle.bind("<B1-Motion>", self.on_drag)
        self.drag_handle.bind("<Button-3>", self.show_context_menu)
        self.title_label.bind("<Button-1>", self.start_drag)
        self.title_label.bind("<B1-Motion>", self.on_drag)
        self.title_label.bind("<Button-3>", self.show_context_menu)
        self.content_frame = tk.Frame(self, bg=bg_color)
        self.content_frame.pack(fill="both", expand=True)
        self._make_resize_handle()
        self._make_context_menu()

    def _make_resize_handle(self):
        self.resize_handle = tk.Frame(self, width=12, height=12, cursor="size_nw_se", bg="#1e2022")
        self.resize_handle.place(relx=1.0, rely=1.0, x=-12, y=-12, anchor="se")
        self.resize_handle.bind("<Button-1>", self.start_resize)
        self.resize_handle.bind("<B1-Motion>", self.do_resize)

    def _make_context_menu(self):
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Duplicate", command=self.duplicate)
        self.context_menu.add_command(label="Edit", command=self.context_edit)
        self.context_menu.add_command(label="Change Color", command=self.context_color)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Lock/Unlock", command=self.toggle_lock)
        self.context_menu.add_command(label="Delete", command=self.delete_widget)

    def context_edit(self):
        pass

    def context_color(self):
        color = colorchooser.askcolor(title="Pick Color")[1]
        if color:
            try:
                self.config(bg=color)
                self.content_frame.config(bg=color)
            except Exception:
                pass

    def show_context_menu(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()

    def duplicate(self):
        parent = self.master
        cls = self.__class__
        try:
            x = self.winfo_x() + 20
            y = self.winfo_y() + 20
            new_widget = cls(parent, x=x, y=y)
        except Exception:
            try:
                new_widget = cls(parent)
                new_widget.place(x=self.winfo_x() + 20, y=self.winfo_y() + 20)
            except Exception:
                return
        return new_widget

    def delete_widget(self):
        try:
            self.destroy()
        except Exception:
            pass

    def toggle_lock(self):
        self._locked = not self._locked
        indicator = "🔒" if self._locked else "🔓"
        try:
            self.title_label.config(text=f"{indicator} {self.title_label.cget('text').lstrip('🔒🔓 ')}")
        except Exception:
            pass

    def start_drag(self, event):
        if getattr(self, "_locked", False):
            return
        self._drag_start_x = event.x
        self._drag_start_y = event.y
        try:
            self.lift()
        except Exception:
            pass

    def on_drag(self, event):
        if getattr(self, "_locked", False):
            return
        x = self.winfo_x() - self._drag_start_x + event.x
        y = self.winfo_y() - self._drag_start_y + event.y
        parent = self.nametowidget(self.winfo_parent())
        if isinstance(parent, (tk.Tk, tk.Toplevel, tk.Frame)):
            pw = parent.winfo_width()
            ph = parent.winfo_height()
            w = self.winfo_width()
            h = self.winfo_height()
            x = max(0, min(x, max(0, pw - w)))
            y = max(0, min(y, max(0, ph - h)))
        self.place(x=x, y=y)

    def start_resize(self, event):
        self._resizing = True
        self._resize_start_x = event.x_root
        self._resize_start_y = event.y_root
        self._orig_width = self.winfo_width()
        self._orig_height = self.winfo_height()

    def do_resize(self, event):
        if getattr(self, "_locked", False):
            return
        dx = event.x_root - self._resize_start_x
        dy = event.y_root - self._resize_start_y
        new_w = max(80, int(self._orig_width + dx))
        new_h = max(50, int(self._orig_height + dy))
        try:
            self.place_configure(width=new_w, height=new_h)
        except Exception:
            pass


class StickyNote(DraggableWidget):
    """A highly customizable digital sticky note with runtime text and color changes."""

    def __init__(self, parent, text="Double-click to edit note...", x=50, y=50):
        super().__init__(parent, title="📌 Sticky Note", bg_color="#fff275")
        self.place(x=x, y=y, width=220, height=160)
        self._palette = ["#fff275", "#ffd1dc", "#c8ffd4", "#d0e8ff", "#fff0b3", "#e0d030", "#a8a8ff", "#ffffff"]
        self.color_btn = tk.Frame(self.drag_handle, bg="#e0d030", width=18, height=18, bd=1, relief="ridge", cursor="hand2")
        self.color_btn.pack(side="right", padx=6, pady=3)
        self.color_btn.pack_propagate(False)
        self.color_btn.bind("<Button-1>", self.show_palette)
        self.color_btn.bind("<Button-3>", lambda e: self.change_color())
        self.text_label = tk.Label(
            self.content_frame,
            text=text,
            bg="#fff275",
            fg="#222222",
            wraplength=200,
            justify="left",
            font=("Comic Sans MS", 11),
            anchor="nw",
        )
        self.text_label.pack(fill="both", expand=True, padx=8, pady=8)
        self.text_label.bind("<Double-Button-1>", self.edit_text)

    def edit_text(self, event=None):
        new_text = simpledialog.askstring("Edit Note", "Enter note text:", initialvalue=self.text_label["text"])
        if new_text is not None:
            self.text_label.config(text=new_text)

    def change_color(self, event=None):
        color_tuple = colorchooser.askcolor(title="Pick Sticky Note Color")
        if color_tuple:
            color = color_tuple[1]
            if color:
                self._apply_color(color)

    def show_palette(self, event=None):
        try:
            x = self.winfo_rootx() + 40
            y = self.winfo_rooty() + 30
        except Exception:
            x = 100
            y = 100
        palette = tk.Toplevel(self)
        palette.wm_overrideredirect(True)
        palette.geometry(f"+{x}+{y}")
        frm = tk.Frame(palette, bd=1, relief="raised")
        frm.pack()
        def choose(c):
            self._apply_color(c)
            palette.destroy()
        for i, c in enumerate(self._palette):
            b = tk.Button(frm, bg=c, width=3, height=1, command=lambda cc=c: choose(cc))
            b.grid(row=0, column=i, padx=1, pady=1)

    def _apply_color(self, color):
        try:
            self.config(bg=color)
            self.content_frame.config(bg=color)
            self.text_label.config(bg=color)
        except Exception:
            pass


class PlaylistWidget(DraggableWidget):
    """A visual playlist frame mocking up music stream deck configurations."""

    def __init__(self, parent, x=50, y=280):
        super().__init__(parent, title="🎵 Playlist Controller", bg_color="#181818")
        self.place(x=x, y=y, width=360, height=180)
        self.tracks = [
            "Lo-Fi Beats For Coding",
            "Neon Nights",
            "Rainy Window",
            "Sunset Drive",
            "Calm Focus",
            "Midnight Loop",
        ]
        self.current_index = 0
        self.is_playing = False
        self.shuffle = tk.BooleanVar(value=False)
        self._build_ui()

    def _build_ui(self):
        header = tk.Label(self.content_frame, text=self.tracks[self.current_index], fg="#1db954", bg="#181818", font=("Arial", 11, "bold"))
        header.pack(pady=(8, 2))
        sub = tk.Label(self.content_frame, text="Status: Stopped", fg="#aaaaaa", bg="#181818", font=("Arial", 9))
        sub.pack(pady=(0, 6))
        self.status_label = sub
        list_frame = tk.Frame(self.content_frame, bg="#181818")
        list_frame.pack(side="left", padx=8, pady=4)
        self.listbox = tk.Listbox(list_frame, height=5, width=24, bg="#0f0f0f", fg="#fff", selectbackground="#333333", activestyle="none")
        for t in self.tracks:
            self.listbox.insert("end", t)
        self.listbox.select_set(self.current_index)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)
        self.listbox.pack()
        ctrl_frame = tk.Frame(self.content_frame, bg="#181818")
        ctrl_frame.pack(side="right", padx=8, pady=6, fill="y")
        buttons_frame = tk.Frame(ctrl_frame, bg="#181818")
        buttons_frame.pack()
        for txt, cmd in [("⏮", self.prev_track), ("▶", self.toggle_play), ("⏸", self.toggle_play), ("⏭", self.next_track)]:
            b = tk.Button(buttons_frame, text=txt, fg="#ffffff", bg="#333333", activebackground="#555555", activeforeground="#ffffff", relief="flat", width=3, command=lambda c=cmd: c())
            b.pack(side="left", padx=3)
        vol_lbl = tk.Label(ctrl_frame, text="Vol", fg="#ddd", bg="#181818")
        vol_lbl.pack(pady=(8, 2))
        self.volume = tk.Scale(ctrl_frame, from_=0, to=100, orient="horizontal", length=120, bg="#181818", fg="#ddd", troughcolor="#333333")
        self.volume.set(70)
        self.volume.pack()
        sh = tk.Checkbutton(ctrl_frame, text="Shuffle", variable=self.shuffle, fg="#ddd", bg="#181818", selectcolor="#282828")
        sh.pack(pady=(6, 0))

    def on_select(self, event):
        sel = self.listbox.curselection()
        if sel:
            self.current_index = sel[0]
            self._update_status()

    def _update_status(self):
        self.status_label.config(text=f"Now: {self.tracks[self.current_index]} {'(Playing)' if self.is_playing else '(Stopped)'}")

    def toggle_play(self):
        self.is_playing = not self.is_playing
        if self.is_playing:
            self.status_label.config(text=f"Now: {self.tracks[self.current_index]} (Playing)")
        else:
            self.status_label.config(text=f"Now: {self.tracks[self.current_index]} (Paused)")

    def next_track(self):
        if self.shuffle.get():
            self.current_index = random.randrange(len(self.tracks))
        else:
            self.current_index = (self.current_index + 1) % len(self.tracks)
        self.listbox.select_clear(0, "end")
        self.listbox.select_set(self.current_index)
        self._update_status()

    def prev_track(self):
        if self.shuffle.get():
            self.current_index = random.randrange(len(self.tracks))
        else:
            self.current_index = (self.current_index - 1) % len(self.tracks)
        self.listbox.select_clear(0, "end")
        self.listbox.select_set(self.current_index)
        self._update_status()


class PixelPlantTrackerWidget(DraggableWidget):
    """A gamified engine rendering procedural pixel art representing real-time goal metrics."""

    def __init__(self, parent, x=300, y=50):
        super().__init__(parent, title="🌱 Habit Matrix & Evolution Engine", bg_color="#282a36")
        self.place(x=x, y=y, width=420, height=360)
        self.xp = 0
        self.habits = ["Complete Daily Code Focus", "Drink 3L Water", "Gym Session"]
        self.habit_vars = []
        self.leaf_color = "#25c281"
        self.stem_color = "#50fa7b"
        self.bloom_color = "#ff79c6"
        self._build_ui()
        self.render_pixel_plant()

    def _build_ui(self):
        self.left_frame = tk.Frame(self.content_frame, bg="#282a36")
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        self.canvas_frame = tk.Frame(self.content_frame, bg="#282a36")
        self.canvas_frame.pack(side="right", padx=10, pady=10)
        self.canvas = tk.Canvas(self.canvas_frame, width=160, height=180, bg="#1e1f29", bd=0, highlightthickness=0)
        self.canvas.pack()
        self.status_lbl = tk.Label(self.canvas_frame, text="Level 1: Tiny Sprout", fg="#50fa7b", bg="#282a36", font=("Arial", 10, "bold"))
        self.status_lbl.pack(pady=5)
        self.xp_lbl = tk.Label(self.canvas_frame, text="Growth XP: 0", fg="#ff79c6", bg="#282a36", font=("Arial", 9))
        self.xp_lbl.pack()
        title = tk.Label(self.left_frame, text="Daily Goals Checklist", fg="#f8f8f2", bg="#282a36", font=("Arial", 10, "bold"))
        title.pack(anchor="nw")
        for habit in self.habits:
            var = tk.IntVar(value=0)
            chk = tk.Checkbutton(
                self.left_frame,
                text=habit,
                variable=var,
                onvalue=1,
                offvalue=0,
                fg="#f8f8f2",
                bg="#282a36",
                activebackground="#282a36",
                selectcolor="#44475a",
                anchor="w",
                command=self._habit_toggled,
            )
            chk.pack(fill="x", pady=4, anchor="w")
            self.habit_vars.append(var)
        ctrl = tk.Frame(self.left_frame, bg="#282a36")
        ctrl.pack(pady=6, anchor="w")
        reset_btn = tk.Button(ctrl, text="Reset XP", command=self.reset_xp, bg="#44475a", fg="#fff")
        reset_btn.pack(side="left", padx=4)
        rand_btn = tk.Button(ctrl, text="Randomize Colors", command=self.randomize_colors, bg="#ffb86b", fg="#111")
        rand_btn.pack(side="left", padx=4)
        pick_btn = tk.Button(ctrl, text="Pick Theme", command=self.pick_theme, bg="#8be9fd", fg="#111")
        pick_btn.pack(side="left", padx=4)

    def _habit_toggled(self):
        new_xp = sum(v.get() for v in self.habit_vars) * 10
        self.xp = new_xp
        self.xp_lbl.config(text=f"Growth XP: {self.xp}")
        self._update_level_label()
        self.render_pixel_plant()

    def _update_level_label(self):
        if self.xp < 20:
            level = "Level 1: Tiny Sprout"
        elif self.xp < 40:
            level = "Level 2: Growing Seedling"
        else:
            level = "Level 3: Flourishing Plant"
        self.status_lbl.config(text=level)

    def render_pixel_plant(self):
        self.canvas.delete("all")
        base_x = 80
        base_y = 140
        height = 1 + self.xp // 10
        max_width = 7
        width = min(max_width, 1 + self.xp // 15)
        pixel_size = 12
        for i in range(height):
            x0 = base_x - pixel_size // 2
            y0 = base_y - (i + 1) * pixel_size
            self.canvas.create_rectangle(x0, y0, x0 + pixel_size, y0 + pixel_size, fill=self.stem_color, outline="")
        for row in range(width):
            x0 = base_x - (row + 2) * pixel_size
            y0 = base_y - (height + row) * pixel_size
            self.canvas.create_rectangle(x0, y0, x0 + pixel_size, y0 + pixel_size, fill=self.leaf_color, outline="")
            x1 = base_x + pixel_size + (row + 0) * pixel_size
            y1 = y0
            self.canvas.create_rectangle(x1, y1, x1 + pixel_size, y1 + pixel_size, fill=self.leaf_color, outline="")
        if self.xp >= 30:
            self.canvas.create_oval(base_x - 14, base_y - height * pixel_size - 30, base_x + 14, base_y - height * pixel_size - 2, fill=self.bloom_color, outline="")
        elif self.xp >= 10:
            self.canvas.create_oval(base_x - 10, base_y - height * pixel_size - 22, base_x + 10, base_y - height * pixel_size - 4, fill=self.bloom_color, outline="")

    def reset_xp(self):
        for v in self.habit_vars:
            v.set(0)
        self.xp = 0
        self.xp_lbl.config(text="Growth XP: 0")
        self._update_level_label()
        self.render_pixel_plant()

    def randomize_colors(self):
        self.leaf_color = random.choice(["#25c281", "#40c4ff", "#7bed9f", "#8be9fd", "#c8ffd4"])
        self.stem_color = random.choice(["#50fa7b", "#32a852", "#2ecc71", "#7ef5a6"])
        self.bloom_color = random.choice(["#ff79c6", "#ffb86b", "#ffd1dc", "#ffa8a8"])
        self.render_pixel_plant()

    def pick_theme(self):
        c = colorchooser.askcolor(title="Pick Leaf Color")[1]
        if c:
            self.leaf_color = c
        c2 = colorchooser.askcolor(title="Pick Stem Color")[1]
        if c2:
            self.stem_color = c2
        c3 = colorchooser.askcolor(title="Pick Bloom Color")[1]
        if c3:
            self.bloom_color = c3
        self.render_pixel_plant()


def main():
    root = tk.Tk()
    root.title("Widget Board — Demo")
    root.geometry("960x640")
    root.configure(bg="#121217")
    sticky1 = StickyNote(root, text="Plan sprint tasks\n- Fix bugs\n- Review PRs", x=30, y=30)
    sticky2 = StickyNote(root, text="Buy groceries:\n- Milk\n- Eggs\n- Bread", x=300, y=30)
    playlist = PlaylistWidget(root, x=30, y=240)
    plant = PixelPlantTrackerWidget(root, x=420, y=30)
    help_lbl = tk.Label(root, text="Right-click widgets for options. Drag by title bar. Double-click sticky to edit. Use controls to interact.", fg="#d0d0d0", bg="#121217")
    help_lbl.place(x=20, y=600)
    root.mainloop()


if __name__ == "__main__":
    main()


       
