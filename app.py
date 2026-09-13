"""Auto Number Filler - a small offline Tkinter desktop application."""

import tkinter as tk
from tkinter import messagebox, ttk


class AutoNumberFillerApp:
    """Build and control the Auto Number Filler interface."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Auto Number Filler")
        self.root.geometry("540x470")
        self.root.minsize(440, 380)

        self.start_var = tk.StringVar()
        self.end_var = tk.StringVar()
        self.prefix_var = tk.StringVar()
        self.digits_var = tk.StringVar(value="3")

        self._build_ui()

    def _build_ui(self) -> None:
        main = ttk.Frame(self.root, padding=16)
        main.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main.columnconfigure(1, weight=1)
        main.rowconfigure(5, weight=1)

        ttk.Label(main, text="Start:").grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")
        ttk.Entry(main, textvariable=self.start_var).grid(row=0, column=1, pady=5, sticky="ew")

        ttk.Label(main, text="End:").grid(row=1, column=0, padx=(0, 10), pady=5, sticky="w")
        ttk.Entry(main, textvariable=self.end_var).grid(row=1, column=1, pady=5, sticky="ew")

        ttk.Label(main, text="Prefix:").grid(row=2, column=0, padx=(0, 10), pady=5, sticky="w")
        ttk.Entry(main, textvariable=self.prefix_var).grid(row=2, column=1, pady=5, sticky="ew")

        ttk.Label(main, text="Digits:").grid(row=3, column=0, padx=(0, 10), pady=5, sticky="w")
        ttk.Entry(main, textvariable=self.digits_var).grid(row=3, column=1, pady=5, sticky="ew")

        buttons = ttk.Frame(main)
        buttons.grid(row=4, column=0, columnspan=2, pady=(12, 8), sticky="w")
        ttk.Button(buttons, text="Generate", command=self.generate).grid(row=0, column=0, padx=(0, 8))
        ttk.Button(buttons, text="Copy", command=self.copy_results).grid(row=0, column=1, padx=(0, 8))
        ttk.Button(buttons, text="Clear", command=self.clear).grid(row=0, column=2)

        ttk.Label(main, text="Results:").grid(row=5, column=0, columnspan=2, sticky="nw")
        self.results = tk.Text(main, height=14, wrap="none", state="disabled")
        self.results.grid(row=6, column=0, columnspan=2, sticky="nsew")
        main.rowconfigure(6, weight=1)

    def _read_inputs(self) -> tuple[int, int, str, int] | None:
        """Validate the form and return usable values, or show an error."""
        try:
            start = int(self.start_var.get().strip())
            end = int(self.end_var.get().strip())
            digits = int(self.digits_var.get().strip())
        except ValueError:
            messagebox.showerror("Invalid input", "Start, End, and Digits must be whole numbers.")
            return None

        if start > end:
            messagebox.showerror("Invalid range", "Start must be less than or equal to End.")
            return None
        if digits < 1:
            messagebox.showerror("Invalid digits", "Digits must be at least 1.")
            return None

        return start, end, self.prefix_var.get(), digits

    def generate(self) -> None:
        values = self._read_inputs()
        if values is None:
            return

        start, end, prefix, digits = values
        lines = [f"{prefix}{number:0{digits}d}" for number in range(start, end + 1)]
        self._set_results("\n".join(lines))

    def copy_results(self) -> None:
        content = self._get_results()
        if not content:
            messagebox.showwarning("Nothing to copy", "Generate a list before copying it.")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(content)
        self.root.update()
        messagebox.showinfo("Copied", "All results have been copied to the clipboard.")

    def clear(self) -> None:
        self.start_var.set("")
        self.end_var.set("")
        self.prefix_var.set("")
        self.digits_var.set("3")
        self._set_results("")

    def _get_results(self) -> str:
        return self.results.get("1.0", "end-1c")

    def _set_results(self, content: str) -> None:
        self.results.config(state="normal")
        self.results.delete("1.0", tk.END)
        self.results.insert("1.0", content)
        self.results.config(state="disabled")


def main() -> None:
    root = tk.Tk()
    AutoNumberFillerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
