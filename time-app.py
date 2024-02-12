import tkinter as tk
from datetime import datetime

class TimeManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Time Manager")

        self.time_in_label = tk.Label(master, text="Time In:")
        self.time_in_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.time_in_var = tk.StringVar()
        self.time_in_entry = tk.Entry(master, textvariable=self.time_in_var, state="disabled")
        self.time_in_entry.grid(row=0, column=1, padx=5, pady=5)

        self.time_out_label = tk.Label(master, text="Time Out:")
        self.time_out_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.time_out_var = tk.StringVar()
        self.time_out_entry = tk.Entry(master, textvariable=self.time_out_var, state="disabled")
        self.time_out_entry.grid(row=1, column=1, padx=5, pady=5)

        self.time_in_button = tk.Button(master, text="Time In", command=self.record_time_in)
        self.time_in_button.grid(row=0, column=2, padx=5, pady=5)

        self.time_out_button = tk.Button(master, text="Time Out", command=self.record_time_out)
        self.time_out_button.grid(row=1, column=2, padx=5, pady=5)

        self.total_hours_label = tk.Label(master, text="Total Hours Worked:")
        self.total_hours_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.total_hours_var = tk.StringVar()
        self.total_hours_entry = tk.Entry(master, textvariable=self.total_hours_var, state="readonly")
        self.total_hours_entry.grid(row=2, column=1, padx=5, pady=5)

        self.total_hours = 0
        self.last_time_in = None

    def record_time_in(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.time_in_var.set(now)
        self.last_time_in = now

    def record_time_out(self):
        if self.last_time_in is None:
            return
        now = datetime.now().strftime("%H:%M:%S")
        self.time_out_var.set(now)
        time_in = datetime.strptime(self.last_time_in, "%H:%M:%S")
        time_out = datetime.strptime(now, "%H:%M:%S")
        hours_worked = (time_out - time_in).seconds / 3600
        self.total_hours += hours_worked
        self.total_hours_var.set("{:.2f}".format(self.total_hours))

def main():
    root = tk.Tk()
    app = TimeManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
