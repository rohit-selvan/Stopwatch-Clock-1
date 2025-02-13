import tkinter as tk 
class RTC: 
def _init_(self): 
self.seconds = 0 
self.minutes = 0 
self.hours = 0 
self.is_running = False 
def update(self): 
if self.is_running: 
self.seconds += 1 
if self.seconds == 60: 
self.seconds = 0 
self.minutes += 1 
if self.minutes == 60: 
self.minutes = 0 
self.hours += 1 
if self.hours == 24: 
self.hours = 0 
def start_clock(self): 
self.is_running = True 
def stop_clock(self): 
self.is_running = False 
def reset_clock(self): 
self.seconds = 0 
self.minutes = 0 
self.hours = 0 
class ClockApp: 
def _init_(self, root): 
self.rtc = RTC() 
root.title("Real-Time Clock") 
root.geometry("400x200") 
self.label = tk.Label(root, font=('Helvetica', 36), fg="black") 
self.label.pack(pady=20) 
self.start_button = tk.Button(root, text="Start", command=self.start_clock, bg="#4CAF50", fg="white", padx=15, pady=10) 
self.start_button.pack(side-tk.LEFT, padx=10) 
self.stop_button = tk.Button(root, text="Stop", command=self.stop_clock, state=tk.DISABLED, bg="#FF5733", fg="white", padx=15, pady=10) 
self.stop_button.pack(side=tk. LEFT, padx=10) 
self.reset_button = tk.Button(root, text="Reset", command=self.reset_clock, bg="#4A90E2", 
fg="white", padx=15, pady=10) 
self.reset_button.pack(side-tk.RIGHT, padx=10) 
self.update_clock() 
def update_clock(self): 
self.rtc.update() 
time_str = f"{self.rtc.hours:02d}:{self.rtc.minutes:02d}:{self.rtc.seconds:02d}" 
self.label.config(text=time_str) 
self.label.after(1000, self.update_clock) 
def start_clock(self): 
self.rtc.start_clock() 
self.start_button.config(state-tk.DISABLED) 
self.stop_button.config(state-tk.NORMAL) 
self.reset_button.config(state-tk.DISABLED) 
def stop_clock(self): 
self.rtc.stop_clock() 
self.start_button.config(state-tk.NORMAL) 
self.stop_button.config(state-tk.DISABLED) 
self.reset_button.config(state-tk.NORMAL) 
def reset_clock(self): 
self.rtc.reset_clock() 
self.label.config(text="00:00:00") 
self.start_button.config(state-tk.NORMAL) 
self.stop_button.config(state=tk.DISABLED) 
if __name__ == "_main_": 
root = 
tk.Tk() 
app = ClockApp(root) 
root.mainloop()
