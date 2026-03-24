import tkinter as tk
from tkinter import messagebox
import auth_module
import menu_module


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("АИС Отдел кадров")
        self.root.geometry("350x250")

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(expand=True)

        tk.Label(self.frame, text="Авторизация", font=("Arial", 12)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.frame, text="Логин:").grid(row=1, column=0, sticky="e")
        self.u_entry = tk.Entry(self.frame)
        self.u_entry.grid(row=1, column=1)
        tk.Label(self.frame, text="Пароль:").grid(row=2, column=0, sticky="e")
        self.p_entry = tk.Entry(self.frame, show="*")
        self.p_entry.grid(row=2, column=1)
        tk.Button(self.frame, text="Вход", width=10, command=self.login).grid(row=3, column=0, columnspan=2, pady=15)

    def login(self):
        auth = auth_module.AuthService()
        rights = auth.check_auth(self.u_entry.get(), self.p_entry.get())

        if rights is not None:
            self.frame.destroy()
            self.build_ui(rights)
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")

    def build_ui(self, rights):
        ms = menu_module.MenuService()
        items = ms.build_menu_data(user_rights=rights)

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        submenus = {}
        for item in items:
            st = "disabled" if item['disabled'] else "normal"
            if item['level'] == 0:
                if item['method'] is None:
                    sub = tk.Menu(menubar, tearoff=0)
                    menubar.add_cascade(label=item['name'], menu=sub, state=st)
                    submenus[item['name']] = sub
                else:
                    menubar.add_command(label=item['name'], state=st,
                                        command=lambda n=item['name']: messagebox.showinfo("Ок", n))
            elif item['level'] == 1 and submenus:
                list(submenus.values())[-1].add_command(label=item['name'], state=st,
                                                        command=lambda n=item['name']: messagebox.showinfo("Ок", n))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
