def launch_text_operators_lab():
    import subprocess
    subprocess.Popen(["python", "labs/text_operators_lab.py"])
def show_explanation(result, explanation):
    popup = tk.Toplevel()
    popup.title("نتيجة التجربة - Wael Style")
    popup.geometry("420x200")
    popup.configure(bg="#fff")

    tk.Label(popup, text="🔍 النتيجة:", font=("Arial", 14, "bold"), fg="#007acc", bg="#fff").pack(pady=(10, 0))
    tk.Label(popup, text=result, font=("Arial", 13), fg="#222", bg="#fff").pack()

    tk.Label(popup, text="📘 الشرح:", font=("Arial", 14, "bold"), fg="#cc00cc", bg="#fff").pack(pady=(15, 0))
    tk.Label(popup, text=explanation, font=("Arial", 12), fg="#444", bg="#fff", wraplength=380, justify="left").pack()

    tk.Button(popup, text="إغلاق", font=("Arial", 12), command=popup.destroy).pack(pady=10)

def apply_function(text, function_name, args):
    try:
        if function_name == "capitalize":
            return text.capitalize()
        elif function_name == "casefold":
            return text.casefold()
        elif function_name == "center":
            return text.center(int(args[0]))
        elif function_name == "count":
            return text.count(args[0])
        elif function_name == "encode":
            return text.encode().decode()
        elif function_name == "endswith":
            return str(text.endswith(args[0]))
        elif function_name == "expandtabs":
            return text.expandtabs(int(args[0]))
        elif function_name == "find":
            return text.find(args[0])
        elif function_name == "format":
            return text.format(*args)
        elif function_name == "format_map":
            return text.format_map(eval(args[0]))
        elif function_name == "index":
            return text.index(args[0])
        elif function_name == "isalnum":
            return str(text.isalnum())
        elif function_name == "isalpha":
            return str(text.isalpha())
        elif function_name == "isascii":
            return str(text.isascii())
        elif function_name == "isdecimal":
            return str(text.isdecimal())
        elif function_name == "isdigit":
            return str(text.isdigit())
        elif function_name == "isidentifier":
            return str(text.isidentifier())
        elif function_name == "islower":
            return str(text.islower())
        elif function_name == "isnumeric":
            return str(text.isnumeric())
        elif function_name == "isprintable":
            return str(text.isprintable())
        elif function_name == "isspace":
            return str(text.isspace())
        elif function_name == "istitle":
            return str(text.istitle())
        elif function_name == "isupper":
            return str(text.isupper())
        elif function_name == "join":
            return args[0].join(eval(text))
        elif function_name == "ljust":
            return text.ljust(int(args[0]))
        elif function_name == "lower":
            return text.lower()
        elif function_name == "lstrip":
            return text.lstrip(args[0])
        elif function_name == "maketrans":
            return str(text.maketrans(eval(args[0])))
        elif function_name == "pad_with_zeros":
            return text.zfill(int(args[0]))
        elif function_name == "partition":
            return str(text.partition(args[0]))
        elif function_name == "replace":
            return text.replace(args[0], args[1])
        elif function_name == "rfind":
            return text.rfind(args[0])
        elif function_name == "rindex":
            return text.rindex(args[0])
        elif function_name == "rjust":
            return text.rjust(int(args[0]))
        elif function_name == "rpartition":
            return str(text.rpartition(args[0]))
        elif function_name == "rsplit":
            return str(text.rsplit(args[0]))
        elif function_name == "rstrip":
            return text.rstrip(args[0])
        elif function_name == "split":
            return str(text.split(args[0]))
        elif function_name == "splitlines":
            return str(text.splitlines())
        elif function_name == "startswith":
            return str(text.startswith(args[0]))
        elif function_name == "strip":
            return text.strip(args[0])
        elif function_name == "swapcase":
            return text.swapcase()
        elif function_name == "title":
            return text.title()
        elif function_name == "translate":
            return text.translate(text.maketrans(eval(args[0])))
        elif function_name == "upper":
            return text.upper()
        elif function_name == "zfill":
            return text.zfill(int(args[0]))
        elif function_name == "reverse_text":
            return text[::-1]
        elif function_name == "remove_vowels":
            return ''.join([c for c in text if c.lower() not in "aeiou"])
        elif function_name == "add_wael_signature":
            return text + " ✍️ بإشراف وائل"
        elif function_name == "zfill_each_word":
            width = int(args[0])
            return ' '.join([word.zfill(width) for word in text.split()])
        elif function_name == "count_words":
            return str(len(text.split()))
        elif function_name == "highlight_keywords":
            keywords = args[0].split(",")
            for kw in keywords:
                text = text.replace(kw.strip(), f"[{kw.strip()}]")
            return text
        elif function_name == "emojiify_text":
            mapping = {
                "حب": "❤️",
                "مرح": "😄",
                "ذكاء": "🧠",
                "شمس": "☀️",
                "قمر": "🌙",
                "نجاح": "🏆",
                "نار": "🔥",
                "سلام": "🕊️"
            }
            for word, emoji in mapping.items():
                text = text.replace(word, f"{word} {emoji}")
            return text
        elif function_name == "find_all_positions":
            return [i for i in range(len(text)) if text.startswith(args[0], i)]
        elif function_name == "safe_index":
            try:
                return text.index(args[0])
            except ValueError:
                return f"❌ الكلمة '{args[0]}' غير موجودة في النص."
        elif function_name == "splitlines_clean":
            raw = text.encode().decode('unicode_escape').strip('"')
            return raw.splitlines()
        else:
            return "⚠️ دالة غير معروفة"
    except Exception as e:
        return f"⚠️ خطأ أثناء التنفيذ: {e}"