import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, question=None, zodiac=None):
        self.question = question
        self.zodiac = zodiac
        self.left = None
        self.right = None

def build_decision_tree():
    # Leaf nodes (12 zodiak)
    aries = Node(zodiac="Aries")
    taurus = Node(zodiac="Taurus")
    gemini = Node(zodiac="Gemini")
    cancer = Node(zodiac="Cancer")
    leo = Node(zodiac="Leo")
    virgo = Node(zodiac="Virgo")
    libra = Node(zodiac="Libra")
    scorpio = Node(zodiac="Scorpio")
    sagittarius = Node(zodiac="Sagittarius")
    capricorn = Node(zodiac="Capricorn")
    aquarius = Node(zodiac="Aquarius")
    pisces = Node(zodiac="Pisces")

    # Level 4 - pertanyaan terakhir
    q5_1 = Node(question="Apakah kamu optimis?")
    q5_1.left = sagittarius   # yes
    q5_1.right = capricorn    # no

    q5_2 = Node(question="Apakah kamu menyukai seni?")
    q5_2.left = libra         # yes
    q5_2.right = scorpio      # no

    q5_3 = Node(question="Apakah kamu mudah bergaul?")
    q5_3.left = gemini        # yes
    q5_3.right = cancer       # no

    q5_4 = Node(question="Apakah kamu perfeksionis?")
    q5_4.left = virgo         # yes
    q5_4.right = leo          # no

    # Level 3
    q4_1 = Node(question="Apakah kamu suka petualangan?")
    q4_1.left = q5_1
    q4_1.right = aquarius

    q4_2 = Node(question="Apakah kamu suka membantu orang lain?")
    q4_2.left = q5_2
    q4_2.right = pisces

    q4_3 = Node(question="Apakah kamu ekspresif?")
    q4_3.left = q5_3
    q4_3.right = taurus

    q4_4 = Node(question="Apakah kamu suka merencanakan?")
    q4_4.left = q5_4
    q4_4.right = aries

    # Level 2
    q3_1 = Node(question="Apakah kamu seorang pemimpin?")
    q3_1.left = q4_1
    q3_1.right = q4_2

    q3_2 = Node(question="Apakah kamu lebih suka stabilitas?")
    q3_2.left = q4_3
    q3_2.right = q4_4

    # Level 1 (root)
    root = Node(question="Apakah kamu lebih logis?")
    root.left = q3_1
    root.right = q3_2

    return root

# Traits kepribadian per zodiak
zodiac_traits = {
    "Aries": "Berani, energik, percaya diri.",
    "Taurus": "Sabar, setia, praktis.",
    "Gemini": "Cerdas, komunikatif, lincah.",
    "Cancer": "Peka, penyayang, protektif.",
    "Leo": "Kreatif, percaya diri, pemimpin.",
    "Virgo": "Analitis, perfeksionis, praktis.",
    "Libra": "Diplomatis, ramah, adil.",
    "Scorpio": "Intens, bersemangat, penuh misteri.",
    "Sagittarius": "Petualang, optimis, jujur.",
    "Capricorn": "Ambisius, disiplin, serius.",
    "Aquarius": "Inovatif, mandiri, progresif.",
    "Pisces": "Empati, artistik, intuitif."
}

def get_zodiac(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18): return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20): return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19): return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20): return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20): return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22): return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22): return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22): return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22): return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21): return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21): return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19): return "Capricorn"
    return None

# Fungsi visualisasi tree dengan wrapping text supaya rapi
def draw_tree(canvas, node, x, y, dx, dy, path_nodes):
    if node is None:
        return
    r = 25
    color = "lightgreen" if node in path_nodes else "lightblue"
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="black")

    # Teks node wrap manual supaya muat
    text = node.question if node.question else node.zodiac
    wrapped = wrap_text(text, 14)
    for i, line in enumerate(wrapped):
        canvas.create_text(x, y - 10 + i * 15, text=line, font=("Arial", 9))

    # Anak kiri
    if node.left:
        canvas.create_line(x, y + r, x - dx, y + dy - r, width=2)
        draw_tree(canvas, node.left, x - dx, y + dy, dx // 2, dy, path_nodes)

    # Anak kanan
    if node.right:
        canvas.create_line(x, y + r, x + dx, y + dy - r, width=2)
        draw_tree(canvas, node.right, x + dx, y + dy, dx // 2, dy, path_nodes)

def wrap_text(text, length):
    words = text.split()
    lines = []
    current_line = ""
    for w in words:
        if len(current_line + " " + w) <= length:
            current_line += " " + w if current_line else w
        else:
            lines.append(current_line)
            current_line = w
    if current_line:
        lines.append(current_line)
    return lines

class ZodiacApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kuis Kepribadian dan Tebak Zodiak (Binary Tree)")
        self.root.geometry("720x650")

        self.tree_root = build_decision_tree()
        self.current_node = self.tree_root
        self.path = [self.tree_root]

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="", font=("Arial", 14), wraplength=600)
        self.label.pack(pady=10)

        self.btn_yes = tk.Button(self.frame, text="Ya", width=15, command=lambda: self.answer(True))
        self.btn_yes.pack(side="left", padx=20)

        self.btn_no = tk.Button(self.frame, text="Tidak", width=15, command=lambda: self.answer(False))
        self.btn_no.pack(side="right", padx=20)

        self.show_question()

    def show_question(self):
        if self.current_node.question:
            self.label.config(text=self.current_node.question)
        else:
            self.label.config(
                text=f"Hasil zodiak dari kuis: {self.current_node.zodiac}\n\nKepribadian: {zodiac_traits.get(self.current_node.zodiac, 'Tidak diketahui.')}"
            )
            self.btn_yes.pack_forget()
            self.btn_no.pack_forget()

            self.btn_check = tk.Button(self.frame, text="Cek Zodiak (Tanggal Lahir)", command=self.open_date_input)
            self.btn_check.pack(side="left", padx=20, pady=10)

            self.btn_view_tree = tk.Button(self.frame, text="Lihat Tree", command=self.open_tree_window)
            self.btn_view_tree.pack(side="right", padx=20, pady=10)

    def answer(self, yes):
        if yes:
            self.current_node = self.current_node.left
        else:
            self.current_node = self.current_node.right
        self.path.append(self.current_node)
        self.show_question()

    def open_date_input(self):
        self.frame.pack_forget()
        self.date_frame = tk.Frame(self.root)
        self.date_frame.pack()

        tk.Label(self.date_frame, text="Masukkan Tanggal Lahir:", font=("Arial", 12)).pack(pady=5)
        frame_input = tk.Frame(self.date_frame)
        frame_input.pack()

        tk.Label(frame_input, text="Tanggal:").grid(row=0, column=0, padx=5)
        self.entry_day = tk.Entry(frame_input, width=5)
        self.entry_day.grid(row=0, column=1, padx=5)

        tk.Label(frame_input, text="Bulan:").grid(row=0, column=2, padx=5)
        self.entry_month = tk.Entry(frame_input, width=5)
        self.entry_month.grid(row=0, column=3, padx=5)

        self.result_label = tk.Label(self.date_frame, text="", font=("Arial", 12), justify="center")
        self.result_label.pack(pady=10)

        btn_show = tk.Button(self.date_frame, text="Tampilkan Zodiak", command=self.show_result)
        btn_show.pack(pady=10)

    def show_result(self):
        try:
            day = int(self.entry_day.get())
            month = int(self.entry_month.get())
            if not (1 <= day <= 31 and 1 <= month <= 12):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Masukkan tanggal dan bulan yang valid!")
            return

        zodiac_from_date = get_zodiac(day, month)
        if zodiac_from_date is None:
            self.result_label.config(text="Tanggal tidak valid untuk zodiak.")
            return

        traits = zodiac_traits.get(zodiac_from_date, "Kepribadian tidak diketahui.")
        self.result_label.config(text=f"Zodiak dari tanggal lahir: {zodiac_from_date}\nKepribadian: {traits}")

    def open_tree_window(self):
        # Jendela baru untuk visualisasi tree
        tree_win = tk.Toplevel(self.root)
        tree_win.title("Visualisasi Binary Tree Decision (Kuis Kepribadian)")
        tree_win.geometry("900x600")

        canvas = tk.Canvas(tree_win, width=880, height=560, bg="white")
        canvas.pack(padx=10, pady=10)

        # Gambarkan tree, highlight jalur yang dipilih saat kuis
        draw_tree(canvas, self.tree_root, 440, 40, 180, 90, self.path)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZodiacApp(root)
    root.mainloop()
