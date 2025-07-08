# প্রয়োজনীয় লাইব্রেরি ইমপোর্ট
from plyer import notification        # ডেস্কটপ নোটিফিকেশন দেখাতে ব্যবহৃত
from tkinter import messagebox        # পপ-আপ বার্তা দেখানোর জন্য
from tkinter import *                 # GUI তৈরি করার জন্য Tkinter
import time              

# মেইন উইন্ডো তৈরি করি
window = Tk()
window.geometry("300x200")            # উইন্ডোর প্রস্থ ও উচ্চতা নির্ধারণ
window.title("কাউন্টডাউন টাইমার")    # উইন্ডোর উপরের শিরোনাম

# টাইমার চালু করার ফাংশন
def timer():

    try:
        # ঘন্টা, মিনিট, সেকেন্ডকে সেকেন্ডে রূপান্তর
        total_seconds = int(hour_entry.get()) * 3600 + int(min_entry.get()) * 60 + int(sec_entry.get())
    except:
        messagebox.showerror(message="সঠিক সংখ্যা লিখুন")  # ভুল ইনপুট হলে বার্তা
        return

    # যদি ইনপুট সময় ০-এর বেশি হয়
    if total_seconds > 0:
        while total_seconds >= 0:
            mins, secs = divmod(total_seconds, 60)       # সেকেন্ড থেকে মিনিট ও সেকেন্ডে ভাগ
            hours_val, mins = divmod(mins, 60)            # মিনিট থেকে ঘন্টায় ভাগ

            # GUI এর ইনপুট ফিল্ড আপডেট করি
            hours.set(hours_val)
            minutes.set(mins)
            seconds.set(secs)

            time.sleep(1)       # ১ সেকেন্ড অপেক্ষা করি
            window.update()     # GUI রিফ্রেশ করি
            total_seconds -= 1  # ১ সেকেন্ড কমাই

        # টাইমার শেষ হলে ডেস্কটপ নোটিফিকেশন দেখাই
        notification.notify(
            title="টাইম শেষ!",
            message="আপনি কি আপনার কাজ শেষ করেছেন?\nনা হলে আবার চেষ্টা করুন!",
            app_icon="bell.ico",     # নিজের আইকন ফাইলের ঠিকানা দিন (অপশনাল)
            timeout=30               # ৩০ সেকেন্ড পর নোটিফিকেশন অটো বন্ধ হবে
        )

        # GUI তে একটি ইনফো বক্স দেখানো
        messagebox.showinfo(message="টাইমার সম্পন্ন হয়েছে!")

# ইনপুট ফিল্ডে ক্লিক করলে ডিফল্ট মান মুছে ফেলার ফাংশন
def clear_hour(e): 
    hour_entry.delete(0, 'end')
def clear_min(e): 
    min_entry.delete(0, 'end')
def clear_sec(e): 
    sec_entry.delete(0, 'end')

# লেবেল তৈরি (শিরোনাম দেখানোর জন্য)
Label(window, text="সাধারণ কাউন্টডাউন টাইমার", font=("Arial", 12)).pack()
Label(window, text="যে ঘর ব্যবহার করবেন না, সেখানে ০ লিখুন", font=("Arial", 10)).pack()

# ইনপুট ভেরিয়েবল তৈরি (GUI এর সাথে সংযুক্ত ভেরিয়েবল)
hours = IntVar()
minutes = IntVar()
seconds = IntVar()

# ইনপুট ফিল্ড (ঘন্টা, মিনিট, সেকেন্ড)
hour_entry = Entry(window, width=3, textvariable=hours, font=("Arial", 18))
min_entry = Entry(window, width=3, textvariable=minutes, font=("Arial", 18))
sec_entry = Entry(window, width=3, textvariable=seconds, font=("Arial", 18))

# ডিফল্ট মান প্রবেশ করানো
hour_entry.insert(0, 0)
min_entry.insert(0, 0)
sec_entry.insert(0, 0)

# ইনপুট বক্সের অবস্থান নির্ধারণ (x = বাম থেকে, y = উপরে থেকে)
hour_entry.place(x=80, y=40)
min_entry.place(x=130, y=40)
sec_entry.place(x=180, y=40)

# ফিল্ডে ক্লিক করলে ডিফল্ট মান মুছে যাবে
hour_entry.bind("<1>", clear_hour)
min_entry.bind("<1>", clear_min)
sec_entry.bind("<1>", clear_sec)

# বাটন তৈরি - ক্লিক করলে টাইমার চালু হবে
Button(window, text="টাইমার চালু করুন", bg="red", fg="white", command=timer).pack(pady=40)

# GUI চালু রাখার জন্য mainloop()
window.mainloop()

