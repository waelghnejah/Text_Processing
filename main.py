import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime
from functions import apply_function

# Load metadata
with open("metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)

# Initialize window
root = tk.Tk()
root.title("مختبر وائل للنصوص – النسخة الذكية")
root.geometry("700x550")

# 🧡 Wael's signature
tk.Label(root, text="🧠 بإشراف: وائل", anchor="w", fg="gray", font=("Arial", 10)).pack(fill="x", padx=10, pady=(5, 0))

# Input: text
tk.Label(root, text="📝 أدخل الجملة:").pack()
entry_text = tk.Entry(root, width=70)
entry_text.pack(pady=5)

# Input: function selection
tk.Label(root, text="🧠 اختر الدالة:").pack()
selected_function = tk.StringVar()
combo = ttk.Combobox(root, textvariable=selected_function, values=list(metadata.keys()), width=30)
combo.pack(pady=5)

# Dynamic argument fields
arg_frame = tk.Frame(root)
arg_frame.pack()
arg_entries = []

def update_args(*args):
    for widget in arg_frame.winfo_children():
        widget.destroy()
    arg_entries.clear()

    func = selected_function.get()
    if func in metadata:
        arg_labels = metadata[func].get("arg_labels", [])
        for i, label in enumerate(arg_labels):
            tk.Label(arg_frame, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=2)
            entry = tk.Entry(arg_frame, width=30)
            entry.grid(row=i, column=1, pady=2)
            arg_entries.append(entry)

combo.bind("<<ComboboxSelected>>", update_args)

# Output: result
label_result = tk.Label(root, text="📤 النتيجة: ", fg="blue", wraplength=650, justify="left")
label_result.pack(pady=5)

# Output: explanation
label_explain = tk.Label(root, text="📚 الشرح: ", wraplength=650, justify="left")
label_explain.pack(pady=5)

# Log box
log_box = tk.Text(root, height=10, width=80)
log_box.pack(pady=10)
log_box.insert(tk.END, "📜 سجل التجارب:\n")
log_box.config(state="disabled")

# 🔍 Show all functions window
def show_all_functions():
    win = tk.Toplevel(root)
    win.title("📋 قائمة كل الدوال")
    win.geometry("400x500")

    tk.Label(win, text="🧠 الدوال المتاحة:", font=("Arial", 12, "bold")).pack(pady=10)

    listbox = tk.Listbox(win, width=50, height=25)
    listbox.pack(padx=10, pady=5)

    for func in sorted(metadata.keys()):
        listbox.insert(tk.END, func)

# Execute function
def execute():
    text = entry_text.get()
    func = selected_function.get()
    args = [e.get() for e in arg_entries]

    if func in metadata:
        result = apply_function(text, func, args)
        desc = metadata[func]["description"]
        example = metadata[func]["example"]

        label_result.config(text=f"📤 النتيجة: {result}")
        label_explain.config(text=f"📚 الشرح: {desc}\n🧪 مثال: {example}")

        log_line = f"[{datetime.now().strftime('%H:%M:%S')}] {func}({', '.join(args)}) على \"{text}\" → {result}\n"
        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(log_line)

        log_box.config(state="normal")
        log_box.insert(tk.END, log_line)
        log_box.config(state="disabled")
def run_function(func_name):
    text = entry_text.get()
    args = [e.get() for e in arg_entries]
    result = apply_function(text, func_name, args)

    label_result.config(text=f"📤 النتيجة: {result}")
    label_explain.config(text=f"📚 الشرح: هذه الدالة تعرض كل المواقع التي يظهر فيها الجزء المطلوب من النص.")

    log_line = f"[{datetime.now().strftime('%H:%M:%S')}] {func_name}({', '.join(args)}) على \"{text}\" → {result}\n"
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_line)

    log_box.config(state="normal")
    log_box.insert(tk.END, log_line)
    log_box.config(state="disabled")

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="✅ نفّذ", command=execute, width=20).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="🚪 خروج", command=root.destroy, width=10).grid(row=0, column=1)
tk.Button(btn_frame, text="📋 عرض كل الدوال", command=show_all_functions, width=20).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="🔍 مواقع كل ظهور", command=lambda: run_function("find_all_positions"), width=20).grid(row=0, column=3, padx=10)
tk.Button(btn_frame, text="🛡️ موقع الكلمة (آمن)", command=lambda: run_function("safe_index"), width=20).grid(row=2, column=1, padx=10, pady=5)
from functions import launch_text_operators_lab

tk.Button(root, text="🧪 تجربة العوامل النصية", command=launch_text_operators_lab).pack(pady=5)
root.mainloop()