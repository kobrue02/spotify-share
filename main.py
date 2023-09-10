import pyperclip
import tkinter as tk

def read_clipboard() -> str:
    root = tk.Tk()
    root.withdraw()
    return root.clipboard_get()

def fix_url(url: str) -> str:
    return url.replace('intl-de/', '')

def write_clipboard(url: str):
    pyperclip.copy(url)


if __name__ == "__main__":
    while True:
        try:
            url = read_clipboard()
            fixed = fix_url(url)
            write_clipboard(fixed)
        except tk.TclError:
            pass
            