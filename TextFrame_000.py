import tkinter as tk

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





def main():
    root = tk.Tk()
    root.title("テキストフレーム")
    root.geometry("500x400")

    # フレームを一度だけ作成
    frame1 = TextFrame(root, x=10, y=50, width=480, height=300, font=("TkDefaultFont", 14))

    # 関数を使ってテキストを順に表示
    frame1.append_text("x,yz")
    frame1.append_text("OKです。")

    root.mainloop()

if __name__ == "__main__":
    main()
