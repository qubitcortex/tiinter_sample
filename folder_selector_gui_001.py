import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry.delete(0, tk.END)
        entry.insert(0, folder_selected)

def show_folder():
    folder_name = entry.get()
    if folder_name:
        label_display.config(text=f"選択されたフォルダー: {folder_name}")
    else:
        messagebox.showwarning("警告", "フォルダーが選択されていません")

# メインウィンドウ作成
root = tk.Tk()
root.title("フォルダー選択GUI")

# フォルダー選択ボタン
btn_select = tk.Button(root, text="フォルダーを選択", command=select_folder)
btn_select.pack(pady=5)

# テキストボックス
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# 表示ボタン
btn_show = tk.Button(root, text="フォルダー名を表示", command=show_folder)
btn_show.pack(pady=5)

# ラベル（フォルダー名表示用）
label_display = tk.Label(root, text="", fg="blue")
label_display.pack(pady=10)

# メインループ
root.mainloop()
