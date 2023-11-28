import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
import os


def merge_files():
    # Open file dialog for selecting multiple files
    filenames = filedialog.askopenfilenames()

    if filenames:
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create the output filename using the timestamp
        output_filename = f"merged_{timestamp}.txt"

        # Open the output file in write mode
        with open(output_filename, 'w', encoding="utf-8", errors="ignore") as outfile:
            # Iterate through the selected files
            for filename in filenames:
                # Open each file in read mode
                with open(filename, encoding="utf-8", errors="ignore") as infile:
                    # Read the data from the file and write it to the output file
                    outfile.write(infile.read())

                # Add a newline character to separate the content of different files
                outfile.write("\n")

        result_label.config(text=f"Merged files successfully into {output_filename}!")
        messagebox.showinfo("Merge Complete", f"Merged files successfully into {output_filename}!")


def optimize_window(window):
    window.title("File Merger")
    window.geometry("300x100")
    window.resizable(False, False)


if __name__ == "__main__":
    window = tk.Tk()
    optimize_window(window)

    merge_button = tk.Button(window, text="Merge Files", command=merge_files)
    merge_button.pack(pady=10)

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()
