import tkinter as tk
from tkinter import filedialog



def entry_texbox(master, x, y, width, height, text=None):
    entry = tk.Entry(master)
    entry.place(x=x, y=y, width=width, height=height)
    if text!=None:
        entry.insert(0,text)
    return entry

def entry_textbox_write(entry, text):
    entry.delete(0, tk.END)
    entry.insert(0, text)


# Folder選択
def select_folder():
    folder = filedialog.askdirectory()
    return folder


def on_click(entry):
    folder = select_folder()
    entry_textbox_write(entry,folder)



# 新しいクラス：ボタンクリック用
class Button_click(tk.Frame):
    def __init__(self, master=None, x=0, y=0, text="押す", command=None):
        super().__init__(master)
        self.command = command
        self.button = tk.Button(master, text=text, command=self.on_click)
        self.button.place(x=x, y=y)

    def on_click(self):
        if self.command:
            self.command()




def main():
    root = tk.Tk()
    root.title("テキストフレーム")
    root.geometry("500x400")


    # テキストボックスにフォルダー名を入力する。
    # Entryの位置とサイズを指定
    entry = tk.Entry(root)
    entry.delete(0, tk.END)
    entry.insert(0, "入力してください")
    entry.place(x=50, y=50, width=300, height=30)


    # 表示用ラベル
    label = tk.Label(root, text="")
    label.pack(pady=10)

    # 入力されているフォルダー名を取得して表示する関数
    def show_folder_name():
        folder_name = entry.get()
        label.config(text=f"入力されたフォルダー名: {folder_name}")

    # ボタン（押すとフォルダー選択ダイアログが開き、選択したパスをentryに表示）
    #button = tk.Button(root, text="フォルダー選択", command=lambda: on_click(entry))
    #button.pack(pady=5)


    a=Button_click(root, x=400, y=100, text="押す", command=lambda: on_click(entry))


    folder_name = entry.get()
    label.config(text=f"入力されたフォルダー名: {folder_name}")


    root.mainloop()

if __name__ == "__main__":
    main()
