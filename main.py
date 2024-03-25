from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter.constants import END

# Словарь для кодирования и декодирования
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}

decrypt = {'•—': 'a', '—•••': 'b', '—•—•': 'c', '—••': 'd',
           '•': 'e', '••—•': 'f', '——•': 'g', '••••': 'h',
           '••': 'i', '•———': 'j', '—•—': 'k', '•—••': 'l',
           '——': 'm', '—•': 'n', '———': 'o', '•——•': 'p',
           '——•—': 'q', '•—•': 'r', '•••': 's', '—': 't',
           '••—': 'u', '•••—': 'v', '•——': 'w', '—••—': 'x',
           '—•——': 'y', '——••': 'z'}

# Функция для кодирования текста в азбуку Морзе
def to_morse(s):
    return ' '.join(morze.get(i.lower(), '') for i in s)

# Функция для декодирования текста из азбуки Морзе
def from_morse(s):
    return ''.join(decrypt.get(i, '') for i in s.split())

# Функция для записи зашифрованного пароля в файл
def save_password(password):
    with open("password.txt", "w") as f:
        f.write(password)

# Функция для обработки нажатия кнопки "Регистрация"
def register():
    password = entry_password.get()
    encrypted_password = to_morse(password)
    save_password(encrypted_password)
    messagebox.showinfo("Регистрация", "Регистрация прошла успешно!")

# Функция для обработки нажатия кнопки "Вход"
def login():
    entered_text = entry_password.get()
    with open("password.txt", "r") as f:
        encrypted_text = f.read()
    decrypted_text = from_morse(encrypted_text)
    if decrypted_text == entered_text:
        messagebox.showinfo("Вход", "Вход выполнен успешно!")
    else:
        messagebox.showerror("Ошибка", "Неверный пароль!")

# Создание основного окна
root = Tk()
root.title("Авторизация")

# Создание элементов управления
label_password = Label(root, text="Введите пароль:")
label_password.grid(row=0, column=0, padx=5, pady=5)

entry_password = Entry(root, width=30, show="*")
entry_password.grid(row=0, column=1, padx=5, pady=5)

register_button = Button(root, text="Регистрация", command=register)
register_button.grid(row=1, column=0, padx=5, pady=5)

login_button = Button(root, text="Войти", command=login)
login_button.grid(row=1, column=1, padx=5, pady=5)

# Запуск основного цикла
root.mainloop()