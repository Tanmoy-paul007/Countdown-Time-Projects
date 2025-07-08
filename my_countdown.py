from plyer import notification
from tkinter import messagebox
from tkinter import *
import time

# মূল উইন্ডো তৈরি
window = Tk()
window.geometry("600x400")
window.title("Countdown timer and notification")

# টাইমার ফাংশন
def timer():
    try:
        total_second = int(hour_entry.get()) * 3600 + int(min_entry.get()) * 60 + int(sec_entry.get())
    except:
        messagebox.showerror(message="Write valid number")
        return 

    if total_second > 0:
        while total_second >= 0:
            mins_val, secs_val = divmod(total_second, 60)
            hours_val, mins_val = divmod(mins_val, 60)

            hours.set(hours_val)
            mins.set(mins_val)
            secs.set(secs_val)

            time.sleep(1)
            window.update()
            total_second -= 1

        # টাইমার শেষে নোটিফিকেশন
        notification.notify(
            title="Time is up!",
            message="Have you finished your work?\nIf not, try again!",
            app_icon="bell.ico",     # Ensure 'bell.ico' file exists in the correct path
            timeout=30
        )

        messagebox.showinfo(message="Timer completed!")

# ক্লিক করলে ইনপুট ফিল্ড ক্লিয়ার হবে
def clean_hour(e): hour_entry.delete(0, 'end')
def clean_min(e): min_entry.delete(0, 'end')
def clean_sec(e): sec_entry.delete(0, 'end')

# টাইটেল লেবেল
Label(window, text="Simple countdown timer", font=("Arial", 12)).pack()
Label(window, text="Write 0 in the cells you do not use.", font=("Arial", 10)).pack()

# ইনপুট ভেরিয়েবল
hours = IntVar()
mins = IntVar()
secs = IntVar()

# ইনপুট বক্স
hour_entry = Entry(window, width=3, textvariable=hours, font=("Arial", 18))
min_entry = Entry(window, width=3, textvariable=mins, font=("Arial", 18))
sec_entry = Entry(window, width=3, textvariable=secs, font=("Arial", 18))

# ডিফল্ট মান
hour_entry.insert(0, 0)
min_entry.insert(0, 0)
sec_entry.insert(0, 0)

# অবস্থান
hour_entry.place(x=80, y=40)
min_entry.place(x=130, y=40)
sec_entry.place(x=180, y=40)

# ক্লিক করলে ক্লিয়ার
hour_entry.bind("<1>", clean_hour)
min_entry.bind("<1>", clean_min)
sec_entry.bind("<1>", clean_sec)

# বাটন
Button(window, text="Start the timer.", bg="green", fg="white", command=timer).pack(pady=40)

# GUI চালু
window.mainloop()
