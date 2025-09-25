import tkinter as tk
from tkinter import filedialog

class TextFrame(tk.Frame):
    def __init__(self, master=None, x=50, y=50, width=200, height=100, font=("TkDefaultFont", 12)):
        super().__init__(master, width=width, height=height)
        self.place(x=x, y=y, width=width, height=height)

        # スクロールバー付きテキストウィジェット
        self.text_widget = tk.Text(self, wrap="none", font=font)

        # スクロールバー（水平・垂直）
        x_scroll = tk.Scrollbar(self, orient="horizontal", command=self.text_widget.xview)
        y_scroll = tk.Scrollbar(self, orient="vertical", command=self.text_widget.yview)

        self.text_widget.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

        # 配置
        self.text_widget.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        # グリッドのリサイズ設定
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # テキストを追加表示する関数
    def append_text(self, text):
        self.text_widget.insert("end", text + "\n")
        self.text_widget.see("end")

# 新しい関数：指定した位置に指定したフォントでテキストを表示
def create_label(master, x, y, text, font=("TkDefaultFont", 12)):
    label = tk.Label(master, text=text, font=font)
    label.place(x=x, y=y)
    return label


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



# Folder選択
def select_folder():
    folder = filedialog.askdirectory()
    return folder

# File選択
def select_file():
    file_path = filedialog.askopenfilename()
    return file_path






def main():
    root = tk.Tk()
    root.title("テキストフレーム")
    root.geometry("500x400")

    # フレームを一度だけ作成
    frame1 = TextFrame(root, x=10, y=50, width=480, height=300, font=("TkDefaultFont", 14))

    # 関数を使ってテキストを順に表示
    frame1.append_text("x,yz")
    frame1.append_text("1,2,3")

    # 新しい関数を使って指定位置にテキストを表示
    create_label(root, x=200, y=10, text="入力", font=("TkDefaultFont", 16))

    # Button_clickクラスを使ってボタンを作成（押されたらframe1にOKを表示）
    button_click = Button_click(root, x=400, y=10, text="押す", command=lambda: frame1.append_text("OK"))

    button_folder = Button_click(root, x=400, y=10, text="押す", command=lambda: frame1.append_text("OK"))
    s_folder = select_folder()
    frame1.append_text(s_folder)

    s_folder = select_folder()
    frame1.append_text(s_folder)

    root.mainloop()

if __name__ == "__main__":
    main()
