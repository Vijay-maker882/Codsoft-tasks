"""
<<< ARITHMETIC CALCULATOR >>>
----------------------------------
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog
import datetime


# -------------------------
#     MAIN CALCULATOR
# -------------------------

class BigNormalCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("BIG Normal Calculator")
        self.geometry("650x650")
        self.resizable(False, False)

        # Memory variable
        self.memory = 0

        # History list
        self.history = []

        # UI builder
        self.create_widgets()

        # Keyboard binding
        self.bind_keys()

    # -------------------------
    #        WIDGETS
    # -------------------------
    def create_widgets(self):

        # --------- Display Box ---------
        self.display = tk.Entry(self, font=("Consolas", 26), bd=6, relief="sunken",
                                justify="right", background="#FFFFFF")
        self.display.pack(fill="x", padx=10, pady=15, ipady=12)

        # --------- Main Frame ---------
        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=False)

        # Button layout
        # Bigger code → more clarity + features
        buttons = [
            ["MC", "MR", "M+", "M-", "←", "C"],
            ["7", "8", "9", "/", "(", ")"],
            ["4", "5", "6", "*", "%", ""],
            ["1", "2", "3", "-", "", ""],
            ["0", ".", "=", "+", "", ""]
        ]

        # --------- Grid of Buttons ---------
        for row in buttons:
            frame = tk.Frame(main_frame)
            frame.pack(fill="both", expand=True)
            for btn_text in row:
                if btn_text == "":
                    # Empty space for spacing
                    tk.Label(frame, text="", width=6).pack(side="left", expand=True, fill="both")
                    continue
                btn = tk.Button(
                    frame,
                    text=btn_text,
                    font=("Arial", 20, "bold"),
                    command=lambda text=btn_text: self.button_click(text),
                    width=6, height=2,
                    bg="#f1f3f4", relief="raised"
                )
                btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)

        # --------- History Section ---------
        hist_label = tk.Label(self, text="History", font=("Arial", 14, " bold"))
        hist_label.pack()

        hist_frame = tk.Frame(self)
        hist_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.hist_list = tk.Listbox(hist_frame, height=8, font=("Arial", 12))
        self.hist_list.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(hist_frame)
        scrollbar.pack(side="right", fill="y")

        self.hist_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.hist_list.yview)

        # --------- Export Button ---------
        export_btn = tk.Button(self, text="Export History", font=("Arial", 12, "bold"),
                               bg="#ace7ef", command=self.export_history)
        export_btn.pack(pady=8)

    # -------------------------
    #      BUTTON ACTIONS
    # -------------------------
    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)

        elif text == "←":
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])

        elif text == "=":
            self.calculate()

        # Memory Functions
        elif text == "MC":
            self.memory = 0
            messagebox.showinfo("Memory", "Memory Cleared")

        elif text == "MR":
            self.display.insert(tk.END, str(self.memory))

        elif text == "M+":
            self.memory_add()

        elif text == "M-":
            self.memory_subtract()

        else:
            self.display.insert(tk.END, text)

    # -------------------------
    #        CALCULATE
    # -------------------------
    def calculate(self):
        expr = self.display.get()
        if not expr:
            return

        try:
            # Percent conversion: 50% → 50/100
            expr = expr.replace("%", "/100")

            result = str(eval(expr))

            # Store in display
            self.display.delete(0, tk.END)
            self.display.insert(0, result)

            # Add to history
            time = datetime.datetime.now().strftime("%H:%M:%S")
            history_line = f"{time} | {expr} = {result}"

            self.history.append(history_line)
            self.hist_list.insert(tk.END, history_line)

        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    # -------------------------
    #      MEMORY FUNCTIONS
    # -------------------------
    def memory_add(self):
        try:
            val = float(eval(self.display.get()))
            self.memory += val
            messagebox.showinfo("Memory", f"Added {val} to memory")
        except:
            messagebox.showerror("Error", "Invalid Expression")

    def memory_subtract(self):
        try:
            val = float(eval(self.display.get()))
            self.memory -= val
            messagebox.showinfo("Memory", f"Subtracted {val} from memory")
        except:
            messagebox.showerror("Error", "Invalid Expression")

    # -------------------------
    #      EXPORT HISTORY
    # -------------------------
    def export_history(self):
        if not self.history:
            messagebox.showwarning("Warning", "No history to export")
            return

        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            title="Save History"
        )

        if file:
            with open(file, "w") as f:
                for item in self.history:
                    f.write(item + "\n")

            messagebox.showinfo("Success", "History exported successfully!")

    # -------------------------
    #      KEYBOARD SUPPORT
    # -------------------------
    def bind_keys(self):
        self.bind("<Key>", self.key_input)
        self.bind("<Return>", lambda e: self.calculate())
        self.bind("<BackSpace>", lambda e: self.button_click("←"))

    def key_input(self, event):
        char = event.char
        if char in "0123456789+-*/().%":
            self.display.insert(tk.END, char)

# -------------------------
#         RUNNER
# -------------------------
if __name__ == "__main__":
    app = BigNormalCalculator()
    app.mainloop()
