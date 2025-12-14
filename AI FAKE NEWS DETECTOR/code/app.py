import tkinter as tk
from tkinter import messagebox
from detector import detect_fake_news  # Dependency injection for detection logic

def check_news():
    """Single Responsibility: Handles news verification workflow"""
    headline = entry.get()
    if headline.strip() == "":
        messagebox.showerror("Error", "Please enter a news headline.")
        return
    
    # Open/Closed Principle: Detection logic is separate and extensible
    result, confidence = detect_fake_news(headline)

    # Strategy Pattern: Different visual treatments for each result type
    if result == "Fake News":
        update_ui("❌", result, confidence, "#ff4d4d", "white", "#ff1a1a")
    elif result == "Real News":
        update_ui("✅", result, confidence, "#4CAF50", "white", "#2eb82e")
    else:
        update_ui("⚠️", result, confidence, "#ffcc00", "black", "#e6b800")

def update_ui(icon, result, confidence, bg, fg, bar_color):
    """Single Responsibility: Handles UI updates only"""
    result_box.config(text=f"{icon} {result}\nConfidence: {confidence:.1f}%", bg=bg, fg=fg)
    confidence_canvas.delete("bar")
    bar_width = (confidence / 100) * 250
    confidence_canvas.create_rectangle(0, 0, bar_width, 25, fill=bar_color, tags="bar")

def clear_all():
    """Single Responsibility: Resets all inputs and outputs"""
    entry.delete(0, tk.END)  # Clear input field
    result_box.config(text="", bg="white", fg="black")  # Reset result display
    confidence_canvas.delete("bar")  # Clear confidence bar

# GUI Factory: Creates and configures UI components
root = tk.Tk()
root.title("AI Fake News Detector")
root.geometry("500x400")
root.configure(bg="#f5f5f5")  # Consistent theme color

# Title Component
title_label = tk.Label(
    root, 
    text="📰 AI Fake News Detector", 
    font=("Arial", 18, "bold"), 
    bg="#ff5a5f",  # Primary color
    fg="white", 
    pady=10
)
title_label.pack(fill="x")  # Responsive design

# Input Component (Single Responsibility)
input_frame = tk.Frame(root, bg="#f5f5f5", pady=15)
input_frame.pack()

tk.Label(input_frame, text="Enter News Headline:", font=("Arial", 12, "bold"), bg="#f5f5f5").pack(pady=5)
entry = tk.Entry(
    input_frame, 
    font=("Arial", 12), 
    width=45, 
    relief="solid", 
    borderwidth=1
)
entry.pack(ipady=5)  # Improved touch target

# Button Container (Interface Segregation)
button_frame = tk.Frame(input_frame, bg="#f5f5f5")
button_frame.pack(pady=10)

# Command Pattern: Buttons trigger specific actions
check_btn = tk.Button(
    button_frame, 
    text="Check", 
    command=check_news,  # Loose coupling
    bg="#2196F3",  # Action color
    fg="white", 
    font=("Arial", 12, "bold"), 
    width=10, 
    relief="raised"
)
check_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_all,  # Single responsibility
    bg="#FF5722",  # Distinct secondary color
    fg="white",
    font=("Arial", 12, "bold"),
    width=10,
    relief="raised"
)
clear_btn.pack(side=tk.LEFT, padx=5)

# Result Display Component
result_box = tk.Label(
    root, 
    text="", 
    font=("Arial", 14, "bold"), 
    width=35, 
    height=3, 
    bg="white", 
    relief="groove"
)
result_box.pack(pady=10)

# Confidence Meter Component
tk.Label(root, text="Confidence Level", font=("Arial", 10, "bold"), bg="#f5f5f5").pack()
confidence_canvas = tk.Canvas(
    root, 
    width=250, 
    height=25, 
    bg="lightgray", 
    relief="ridge"
)
confidence_canvas.pack(pady=5)

# Main Loop (Controller)
root.mainloop()