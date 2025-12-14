import tkinter as tk
from tkinter import messagebox
from detector import detect_fake_news  # Import your logic

def check_news():
    headline = entry.get()
    if headline.strip() == "":
        messagebox.showerror("Error", "Please enter a news headline.")
        return
    result, confidence = detect_fake_news(headline)

    # Update result box style
    if result == "Fake News":
        result_box.config(text=f"❌ {result}\nConfidence: {confidence:.1f}%", bg="#ff4d4d", fg="white")
        confidence_canvas.delete("bar")
        confidence_canvas.create_rectangle(0, 0, (confidence / 100) * 250, 25, fill="#ff1a1a", tags="bar")
    elif result == "Real News":
        result_box.config(text=f"✅ {result}\nConfidence: {confidence:.1f}%", bg="#4CAF50", fg="white")
        confidence_canvas.delete("bar")
        confidence_canvas.create_rectangle(0, 0, (confidence / 100) * 250, 25, fill="#2eb82e", tags="bar")
    else:
        result_box.config(text=f"⚠️ {result}\nConfidence: {confidence:.1f}%", bg="#ffcc00", fg="black")
        confidence_canvas.delete("bar")
        confidence_canvas.create_rectangle(0, 0, (confidence / 100) * 250, 25, fill="#e6b800", tags="bar")

# GUI Setupv
root = tk.Tk()
root.title("AI Fake News Detector")
root.geometry("500x400")
root.configure(bg="#f5f5f5")

# Title
title_label = tk.Label(root, text="📰 AI Fake News Detector", font=("Arial", 18, "bold"), bg="#ff5a5f", fg="white", pady=10)
title_label.pack(fill="x")

# Input section
input_frame = tk.Frame(root, bg="#f5f5f5", pady=15)
input_frame.pack()

tk.Label(input_frame, text="Enter News Headline:", font=("Arial", 12, "bold"), bg="#f5f5f5").pack(pady=5)
entry = tk.Entry(input_frame, font=("Arial", 12), width=45, relief="solid", borderwidth=1)
entry.pack(ipady=5)

check_btn = tk.Button(input_frame, text="Check", command=check_news, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), width=10, relief="raised")
check_btn.pack(pady=10)

# Result section
result_box = tk.Label(root, text="", font=("Arial", 14, "bold"), width=35, height=3, bg="white", relief="groove")
result_box.pack(pady=10)

# Confidence bar
tk.Label(root, text="Confidence Level", font=("Arial", 10, "bold"), bg="#f5f5f5").pack()
confidence_canvas = tk.Canvas(root, width=250, height=25, bg="lightgray", relief="ridge")
confidence_canvas.pack(pady=5)

root.mainloop()