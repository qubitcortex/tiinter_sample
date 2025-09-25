import tkinter as tk
from tkinter import filedialog, messagebox




# def select_folder():
#     folder_selected = filedialog.askdirectory()
#     if folder_selected:
#         entry.delete(0, tk.END)
#         entry.insert(0, folder_selected)

# def show_folder(entry,label_display):
#     folder_name = entry.get()
#     if folder_name:
#         label_display.config(text=f"選択されたフォルダー: {folder_name}")
#     else:
#         messagebox.showwarning("警告", "フォルダーが選択されていません")



def main():

    # メインウィンドウ作成
    root = tk.Tk()
    root.title("フォルダー選択GUI")
    root.geometry("500x400")



    def select_folder():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            entry.delete(0, tk.END)
            entry.insert(0, folder_selected)

    def show_folder():
        folder_name = entry.get()
        if folder_name:
            # ラベルにテキストを更新して即時反映
            label_display.config(text=f"選択されたフォルダー: {folder_name}")
            label_display.update_idletasks()
        else:
            messagebox.showwarning("警告", "フォルダーが選択されていません")





    # テキストボックス
    entry = tk.Entry(root, width=20)
    entry.place(x=80, y=50, width=400, height=30)
    #entry.pack(pady=5)


    # フォルダー選択ボタン
    btn_select = tk.Button(root, text="Folder", command=select_folder)
    btn_select.place(x=20, y=50, width=50, height=30)
    #btn_select.pack(pady=5)


    # 表示ボタン
    btn_show = tk.Button(root, text="表示", command=show_folder)
    btn_show.place(x=50, y=200, width=50, height=30)
    #btn_show.pack(pady=5)


    # ラベル（フォルダー名表示用）
    label_display = tk.Label(root, text="AAA", fg="blue")
    label_display.place(x=50, y=300, width=500, height=30)
    #label_display.pack(pady=10)


    # メインループ
    root.mainloop()


if __name__ == "__main__":
    main()
