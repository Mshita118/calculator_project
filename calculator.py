import tkinter as tk #Tkinterのインポート
import math


root = tk.Tk()
root.title("計算機") #タイトル
root.geometry("700x500") #画面サイズ

#計算結果エリア
display = tk.Label(root, text="0", font=("Arial", 24),anchor="e", bg="white", relief="sunken")
display.pack(fill="both", padx=10, pady=10)

#四則演算のボタン配置
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('リセット', 2,
    4),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
    ('税込', 1, 0), ('税抜', 1, 1), ('保存', 1, 2), ('合計', 1, 3), ('掛算', 1, 4), ('C', 1, 5)
]

for (text, row, col) in buttons: #text=ボタン、row=ボタンの配置行、col=ボタンの配置列 ('7'=ボタン, '1'=行, '0'=列)
    button = tk.Button(button_frame, text=text, font=("Arial", 18), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)


#ボタンの動作機能
current_input = "" #入力管理変数

def on_button_click(value): #ボタン押下処理
    global current_input
    if value == "C": #Cが押下された際に計算クリア
        current_input = ""
    elif value == "=":
        try:
            current_input = str(eval(current_input)) #計算実行
        except:
            current_input = "エラー"
    else:
        current_input += value
    display.config(text=current_input)


def tax_invluded():
    global current_input
    try:
        result = float(current_input) * 1.1
        current_input = str(result)
    except:
        current_input = "エラー"
    display.config(text=current_input)


def tax_excluded():
    global current_input
    try:
        result = float(current_input) / 1.1
        current_input = str(result)
    except:
        current_input = "エラー"
    display.config(text=current_input)


saved_numbers = []

def update_saved_display():
    saved_display.config(text="保存リスト: " + str(saved_numbers))

def save_number():
    global current_input
    try:
        number = float(current_input)
        saved_numbers.append(number)
        current_input = "0"
        update_saved_display()
    except:
        current_input = "エラー"
    display.config(text=current_input)


def sum_numbers():
    global current_input
    result = sum(saved_numbers)
    current_input = str(result)
    display.config(text=current_input)


def multiply_numbers():
    global current_input
    if saved_numbers:
        result = math.prod(saved_numbers)
        current_input = str(result)
    else:
        current_input = "0"
    display.config(text=current_input)


def reset_saved_numbers():
    global saved_numbers
    saved_numbers = []
    update_saved_display()


saved_display = tk.Label(root, text="保存リスト: []", font=("Arial", 14), anchor="w", bg="lightgray", relief="sunken")
saved_display.pack(fill="both", padx=10, pady=5)


for (text, row, col) in buttons: #ボタンをクリックした際に実行する
    if text == '税込':
        button = tk.Button(button_frame, text=text, font=("Arial", 18), width=5, height=2, command=tax_invluded)
    elif text == '税抜':
        button = tk.Button(button_frame, text=text, font=("Arial", 18), width=5, height=2, command=tax_excluded)
    elif text == '保存':
        button = tk.Button(button_frame, text=text, font=("Arial", 18), width=5, height=2, command=save_number)
    elif text == '合計':
        button = tk.Button(button_frame, text=text, font=("Arial", 18), width=5, height=2, command=sum_numbers)
    elif text == '掛算':
        button = tk.Button(button_frame, text=text, font=("Arial", 18), width=5, height=2, command=multiply_numbers)
    elif text == 'リセット':
        button = tk.Button(button_frame, text=text, font=("Arial", 18), width=5, height=2, command=reset_saved_numbers)
    else:
        button = tk.Button(button_frame, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, pady=5)



root.mainloop()
