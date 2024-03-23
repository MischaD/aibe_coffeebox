import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


class VKeyboard(ttk.Frame):
    def __init__(self, parent,
                 target: ttk.Entry = None, **kwargs):
        super().__init__(parent, **kwargs)

        self.target = target
        self.is_shift = False
        self.window_height = parent.winfo_screenwidth()
        self.window_width = parent.winfo_screenwidth()

        self.display()

    def change_target(self, target: ttk.Entry = None):
        self.target = target

    def press(self,  num):
        self.target.insert("end", str(num))

    def backspace(self):
        index = self.target.index("end")-1
        self.target.delete(index)

    def shift(self):
        self.is_shift = not self.is_shift
        self.display()

    def clear(self):
        pass

    def display(self):

        all_properties = {"padx": 1,
                          "pady": 1,
                          "ipadx": 10,
                          "ipady": 15}

        space_button_width = self.window_width/4
        button_width = 4

        if self.is_shift:
            # Adding keys line wise
            # First Line Button

            num1 = ttk.Button(self, text='!', width=button_width, command=lambda: self.press('!'))
            num1.grid(all_properties, row=0, column=1)

            num2 = ttk.Button(self, text='@', width=button_width, command=lambda: self.press('@'))
            num2.grid(all_properties, row=0, column=2)

            num3 = ttk.Button(self, text='#', width=button_width, command=lambda: self.press('#'))
            num3.grid(all_properties, row=0, column=3)

            num4 = ttk.Button(self, text='$', width=button_width, command=lambda: self.press('$'))
            num4.grid(all_properties, row=0, column=4)

            num5 = ttk.Button(self, text='%', width=button_width, command=lambda: self.press('%'))
            num5.grid(all_properties, row=0, column=5)

            num6 = ttk.Button(self, text='^', width=button_width, command=lambda: self.press('^'))
            num6.grid(all_properties, row=0, column=6)

            num7 = ttk.Button(self, text='&', width=button_width, command=lambda: self.press('&'))
            num7.grid(all_properties, row=0, column=7)

            num8 = ttk.Button(self, text='*', width=button_width, command=lambda: self.press('*'))
            num8.grid(all_properties, row=0, column=8)

            num9 = ttk.Button(self, text='(', width=button_width, command=lambda: self.press('('))
            num9.grid(all_properties, row=0, column=9)

            num0 = ttk.Button(self, text=')', width=button_width, command=lambda: self.press(')'))
            num0.grid(all_properties, row=0, column=10)

            # Second Line Buttons

            q = ttk.Button(self, text='Q', width=button_width, command=lambda: self.press('Q'))
            q.grid(all_properties, row=1, column=1)

            w = ttk.Button(self, text='W', width=button_width, command=lambda: self.press('W'))
            w.grid(all_properties, row=1, column=2)

            e = ttk.Button(self, text='E', width=button_width, command=lambda: self.press('E'))
            e.grid(all_properties, row=1, column=3)

            r = ttk.Button(self, text='R', width=button_width, command=lambda: self.press('R'))
            r.grid(all_properties, row=1, column=4)

            t = ttk.Button(self, text='T', width=button_width, command=lambda: self.press('T'))
            t.grid(all_properties, row=1, column=5)

            z = ttk.Button(self, text='Z', width=button_width, command=lambda: self.press('Z'))
            z.grid(all_properties, row=1, column=6)

            u = ttk.Button(self, text='U', width=button_width, command=lambda: self.press('U'))
            u.grid(all_properties, row=1, column=7)

            i = ttk.Button(self, text='I', width=button_width, command=lambda: self.press('I'))
            i.grid(all_properties, row=1, column=8)

            o = ttk.Button(self, text='O', width=button_width, command=lambda: self.press('O'))
            o.grid(row=1, column=9)

            p = ttk.Button(self, text='P', width=button_width, command=lambda: self.press('P'))
            p.grid(all_properties, row=1, column=10)

            # Third Line Buttons

            a = ttk.Button(self, text='A', width=button_width, command=lambda: self.press('A'))
            a.grid(all_properties, row=2, column=1)

            s = ttk.Button(self, text='S', width=button_width, command=lambda: self.press('S'))
            s.grid(all_properties, row=2, column=2)

            d = ttk.Button(self, text='D', width=button_width, command=lambda: self.press('D'))
            d.grid(all_properties, row=2, column=3)

            f = ttk.Button(self, text='F', width=button_width, command=lambda: self.press('F'))
            f.grid(all_properties, row=2, column=4)

            g = ttk.Button(self, text='G', width=button_width, command=lambda: self.press('G'))
            g.grid(all_properties, row=2, column=5)

            h = ttk.Button(self, text='H', width=button_width, command=lambda: self.press('H'))
            h.grid(all_properties, row=2, column=6)

            j = ttk.Button(self, text='J', width=button_width, command=lambda: self.press('J'))
            j.grid(all_properties, row=2, column=7)

            k = ttk.Button(self, text='K', width=button_width, command=lambda: self.press('K'))
            k.grid(all_properties, row=2, column=8)

            ll = ttk.Button(self, text='L', width=button_width, command=lambda: self.press('L'))
            ll.grid(all_properties, row=2, column=9)

            backspace = ttk.Button(
                self, text='<---', width=button_width, command=self.backspace)
            backspace.grid(all_properties, row=2, column=10)

            # Fourth line Buttons

            shift = ttk.Button(self, text='Shift', width=button_width, command=self.shift)
            shift.grid(all_properties, row=3, column=1)

            y = ttk.Button(self, text='Y', width=button_width, command=lambda: self.press('Y'))
            y.grid(all_properties, row=3, column=2)

            x = ttk.Button(self, text='X', width=button_width, command=lambda: self.press('X'))
            x.grid(all_properties, row=3, column=3)

            c = ttk.Button(self, text='C', width=button_width, command=lambda: self.press('C'))
            c.grid(all_properties, row=3, column=4)

            v = ttk.Button(self, text='V', width=button_width, command=lambda: self.press('V'))
            v.grid(all_properties, row=3, column=5)

            b = ttk.Button(self, text='B', width=button_width, command=lambda: self.press('B'))
            b.grid(all_properties, row=3, column=6)

            n = ttk.Button(self, text='N', width=button_width, command=lambda: self.press('N'))
            n.grid(all_properties, row=3, column=7)

            m = ttk.Button(self, text='M', width=button_width, command=lambda: self.press('M'))
            m.grid(all_properties, row=3, column=8)

            dot = ttk.Button(self, text='.', width=button_width, command=lambda: self.press('.'))
            dot.grid(all_properties, row=3, column=9)

            # Fifth Line Buttons

            space = ttk.Button(self, text='Space', width=button_width,
                               command=lambda: self.press(' '))
            space.grid(row=4, column=2, columnspan=8, padx=2, pady=2, ipadx=space_button_width, ipady=10)

        else:
            # Adding keys line wise
            # First Line Button

            num1 = ttk.Button(self, text='1', width=button_width, command=lambda: self.press('1'))
            num1.grid(all_properties, row=0, column=1)

            num2 = ttk.Button(self, text='2', width=button_width, command=lambda: self.press('2'))
            num2.grid(all_properties, row=0, column=2)

            num3 = ttk.Button(self, text='3', width=button_width, command=lambda: self.press('3'))
            num3.grid(all_properties, row=0, column=3)

            num4 = ttk.Button(self, text='4', width=button_width, command=lambda: self.press('4'))
            num4.grid(all_properties, row=0, column=4)

            num5 = ttk.Button(self, text='5', width=button_width, command=lambda: self.press('5'))
            num5.grid(all_properties, row=0, column=5)

            num6 = ttk.Button(self, text='6', width=button_width, command=lambda: self.press('6'))
            num6.grid(all_properties, row=0, column=6)

            num7 = ttk.Button(self, text='7', width=button_width, command=lambda: self.press('7'))
            num7.grid(all_properties, row=0, column=7)

            num8 = ttk.Button(self, text='8', width=button_width, command=lambda: self.press('8'))
            num8.grid(all_properties, row=0, column=8)

            num9 = ttk.Button(self, text='9', width=button_width, command=lambda: self.press('9'))
            num9.grid(all_properties, row=0, column=9)

            num0 = ttk.Button(self, text='0', width=button_width, command=lambda: self.press('0'))
            num0.grid(all_properties, row=0, column=10)

            # Second Line Buttons

            q = ttk.Button(self, text='q', width=button_width, command=lambda: self.press('q'))
            q.grid(all_properties, row=1, column=1)

            w = ttk.Button(self, text='w', width=button_width, command=lambda: self.press('w'))
            w.grid(all_properties, row=1, column=2)

            e = ttk.Button(self, text='e', width=button_width, command=lambda: self.press('e'))
            e.grid(all_properties, row=1, column=3)

            r = ttk.Button(self, text='r', width=button_width, command=lambda: self.press('r'))
            r.grid(all_properties, row=1, column=4)

            t = ttk.Button(self, text='t', width=button_width, command=lambda: self.press('t'))
            t.grid(all_properties, row=1, column=5)

            z = ttk.Button(self, text='z', width=button_width, command=lambda: self.press('z'))
            z.grid(all_properties, row=1, column=6)

            u = ttk.Button(self, text='u', width=button_width, command=lambda: self.press('u'))
            u.grid(all_properties, row=1, column=7)

            i = ttk.Button(self, text='i', width=button_width, command=lambda: self.press('i'))
            i.grid(all_properties, row=1, column=8)

            o = ttk.Button(self, text='o', width=button_width, command=lambda: self.press('o'))
            o.grid(all_properties, row=1, column=9)

            p = ttk.Button(self, text='p', width=button_width, command=lambda: self.press('p'))
            p.grid(all_properties, row=1, column=10)

            # Third Line Buttons

            a = ttk.Button(self, text='a', width=button_width, command=lambda: self.press('a'))
            a.grid(all_properties, row=2, column=1)

            s = ttk.Button(self, text='s', width=button_width, command=lambda: self.press('s'))
            s.grid(all_properties, row=2, column=2)

            d = ttk.Button(self, text='d', width=button_width, command=lambda: self.press('d'))
            d.grid(all_properties, row=2, column=3)

            f = ttk.Button(self, text='f', width=button_width, command=lambda: self.press('f'))
            f.grid(all_properties, row=2, column=4)

            g = ttk.Button(self, text='g', width=button_width, command=lambda: self.press('g'))
            g.grid(all_properties, row=2, column=5)

            h = ttk.Button(self, text='h', width=button_width, command=lambda: self.press('h'))
            h.grid(all_properties, row=2, column=6)

            j = ttk.Button(self, text='j', width=button_width, command=lambda: self.press('j'))
            j.grid(all_properties, row=2, column=7)

            k = ttk.Button(self, text='k', width=button_width, command=lambda: self.press('k'))
            k.grid(all_properties, row=2, column=8)

            ll = ttk.Button(self, text='l', width=button_width, command=lambda: self.press('l'))
            ll.grid(all_properties, row=2, column=9)

            backspace = ttk.Button(
                self, text='<---', width=button_width, command=self.backspace)
            backspace.grid(all_properties, row=2, column=10)

            # Fourth line Buttons

            shift = ttk.Button(self, text='Shift', width=button_width, command=self.shift)
            shift.grid(all_properties, row=3, column=1)

            y = ttk.Button(self, text='y', width=button_width, command=lambda: self.press('y'))
            y.grid(all_properties, row=3, column=2)

            x = ttk.Button(self, text='x', width=button_width, command=lambda: self.press('x'))
            x.grid(all_properties, row=3, column=3)

            c = ttk.Button(self, text='c', width=button_width, command=lambda: self.press('c'))
            c.grid(all_properties, row=3, column=4)

            v = ttk.Button(self, text='v', width=button_width, command=lambda: self.press('v'))
            v.grid(all_properties, row=3, column=5)

            b = ttk.Button(self, text='b', width=button_width, command=lambda: self.press('b'))
            b.grid(all_properties, row=3, column=6)

            n = ttk.Button(self, text='n', width=button_width, command=lambda: self.press('n'))
            n.grid(all_properties, row=3, column=7)

            m = ttk.Button(self, text='m', width=button_width, command=lambda: self.press('m'))
            m.grid(all_properties, row=3, column=8)

            dot = ttk.Button(self, text='.', width=button_width, command=lambda: self.press('.'))
            dot.grid(all_properties, row=3, column=9)

            minus = ttk.Button(self, text='-', width=button_width, command=lambda: self.press('-'))
            minus.grid(all_properties, row=3, column=10)

            # Fifth Line Buttons

            space = ttk.Button(self, text='Space', width=button_width,
                               command=lambda: self.press(' '))
            space.grid(row=4, column=2, columnspan=8, padx=2, pady=2, ipadx=space_button_width, ipady=10)


if __name__ == '__main__':
    style = Style()
    root = style.master
    root.title('On Screen Keyboard')
    root.attributes("-fullscreen", True)
    VKeyboard(root).pack()
    root.mainloop()
