import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


class VKeyboard(ttk.Frame):
    def __init__(self, parent,
                 target: ttk.Entry = None, **kwargs):
        super().__init__(parent, **kwargs)

        self.target = target
        self.is_shift = False

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

        all_properties = {"padx": 2,
                          "pady": 2,
                          "ipadx": 6,
                          "ipady": 10}

        if self.is_shift:
            # Adding keys line wise
            # First Line Button

            num1 = ttk.Button(self, text='!', width=6, command=lambda: self.press('!'))
            num1.grid(all_properties, row=0, column=1)

            num2 = ttk.Button(self, text='@', width=6, command=lambda: self.press('@'))
            num2.grid(all_properties, row=0, column=2)

            num3 = ttk.Button(self, text='#', width=6, command=lambda: self.press('#'))
            num3.grid(all_properties, row=0, column=3)

            num4 = ttk.Button(self, text='$', width=6, command=lambda: self.press('$'))
            num4.grid(all_properties, row=0, column=4)

            num5 = ttk.Button(self, text='%', width=6, command=lambda: self.press('%'))
            num5.grid(all_properties, row=0, column=5)

            num6 = ttk.Button(self, text='^', width=6, command=lambda: self.press('^'))
            num6.grid(all_properties, row=0, column=6)

            num7 = ttk.Button(self, text='&', width=6, command=lambda: self.press('&'))
            num7.grid(all_properties, row=0, column=7)

            num8 = ttk.Button(self, text='*', width=6, command=lambda: self.press('*'))
            num8.grid(all_properties, row=0, column=8)

            num9 = ttk.Button(self, text='(', width=6, command=lambda: self.press('('))
            num9.grid(all_properties, row=0, column=9)

            num0 = ttk.Button(self, text=')', width=6, command=lambda: self.press(')'))
            num0.grid(all_properties, row=0, column=10)

            # Second Line Buttons

            Q = ttk.Button(self, text='Q', width=6, command=lambda: self.press('Q'))
            Q.grid(all_properties, row=1, column=1)

            W = ttk.Button(self, text='W', width=6, command=lambda: self.press('W'))
            W.grid(all_properties, row=1, column=2)

            E = ttk.Button(self, text='E', width=6, command=lambda: self.press('E'))
            E.grid(all_properties, row=1, column=3)

            R = ttk.Button(self, text='R', width=6, command=lambda: self.press('R'))
            R.grid(all_properties, row=1, column=4)

            T = ttk.Button(self, text='T', width=6, command=lambda: self.press('T'))
            T.grid(all_properties, row=1, column=5)

            Z = ttk.Button(self, text='Y', width=6, command=lambda: self.press('Y'))
            Z.grid(all_properties, row=1, column=6)

            U = ttk.Button(self, text='U', width=6, command=lambda: self.press('U'))
            U.grid(all_properties, row=1, column=7)

            I = ttk.Button(self, text='I', width=6, command=lambda: self.press('I'))
            I.grid(all_properties, row=1, column=8)

            O = ttk.Button(self, text='O', width=6, command=lambda: self.press('O'))
            O.grid(row=1, column=9)

            P = ttk.Button(self, text='P', width=6, command=lambda: self.press('P'))
            P.grid(all_properties, row=1, column=10)

            # Third Line Buttons

            A = ttk.Button(self, text='A', width=6, command=lambda: self.press('A'))
            A.grid(all_properties, row=2, column=1)

            S = ttk.Button(self, text='S', width=6, command=lambda: self.press('S'))
            S.grid(all_properties, row=2, column=2)

            D = ttk.Button(self, text='D', width=6, command=lambda: self.press('D'))
            D.grid(all_properties, row=2, column=3)

            F = ttk.Button(self, text='F', width=6, command=lambda: self.press('F'))
            F.grid(all_properties, row=2, column=4)

            G = ttk.Button(self, text='G', width=6, command=lambda: self.press('G'))
            G.grid(all_properties, row=2, column=5)

            H = ttk.Button(self, text='H', width=6, command=lambda: self.press('H'))
            H.grid(all_properties, row=2, column=6)

            J = ttk.Button(self, text='J', width=6, command=lambda: self.press('J'))
            J.grid(all_properties, row=2, column=7)

            K = ttk.Button(self, text='K', width=6, command=lambda: self.press('K'))
            K.grid(all_properties, row=2, column=8)

            L = ttk.Button(self, text='L', width=6, command=lambda: self.press('L'))
            L.grid(all_properties, row=2, column=9)

            backspace = ttk.Button(
                self, text='<---', width=6, command=self.backspace)
            backspace.grid(all_properties, row=2, column=10)

            # Fourth line Buttons

            shift = ttk.Button(self, text='Shift', width=6, command=self.shift)
            shift.grid(all_properties, row=3, column=1)

            Y = ttk.Button(self, text='Z', width=6, command=lambda: self.press('Z'))
            Y.grid(all_properties, row=3, column=2)

            X = ttk.Button(self, text='X', width=6, command=lambda: self.press('X'))
            X.grid(all_properties, row=3, column=3)

            C = ttk.Button(self, text='C', width=6, command=lambda: self.press('C'))
            C.grid(all_properties, row=3, column=4)

            V = ttk.Button(self, text='V', width=6, command=lambda: self.press('V'))
            V.grid(all_properties, row=3, column=5)

            B = ttk.Button(self, text='B', width=6, command=lambda: self.press('B'))
            B.grid(all_properties, row=3, column=6)

            N = ttk.Button(self, text='N', width=6, command=lambda: self.press('N'))
            N.grid(all_properties, row=3, column=7)

            M = ttk.Button(self, text='M', width=6, command=lambda: self.press('M'))
            M.grid(all_properties, row=3, column=8)

            dot = ttk.Button(self, text='.', width=6, command=lambda: self.press('.'))
            dot.grid(all_properties, row=3, column=9)

            # Fifth Line Buttons

            space = ttk.Button(self, text='Space', width=6,
                               command=lambda: self.press(' '))
            space.grid(row=4, column=2, columnspan=8, padx=2, pady=2, ipadx=350, ipady=10)

        else:
            # Adding keys line wise
            # First Line Button

            num1 = ttk.Button(self, text='1', width=6, command=lambda: self.press('1'))
            num1.grid(all_properties, row=0, column=1)

            num2 = ttk.Button(self, text='2', width=6, command=lambda: self.press('2'))
            num2.grid(all_properties, row=0, column=2)

            num3 = ttk.Button(self, text='3', width=6, command=lambda: self.press('3'))
            num3.grid(all_properties, row=0, column=3)

            num4 = ttk.Button(self, text='4', width=6, command=lambda: self.press('4'))
            num4.grid(all_properties, row=0, column=4)

            num5 = ttk.Button(self, text='5', width=6, command=lambda: self.press('5'))
            num5.grid(all_properties, row=0, column=5)

            num6 = ttk.Button(self, text='6', width=6, command=lambda: self.press('6'))
            num6.grid(all_properties, row=0, column=6)

            num7 = ttk.Button(self, text='7', width=6, command=lambda: self.press('7'))
            num7.grid(all_properties, row=0, column=7)

            num8 = ttk.Button(self, text='8', width=6, command=lambda: self.press('8'))
            num8.grid(all_properties, row=0, column=8)

            num9 = ttk.Button(self, text='9', width=6, command=lambda: self.press('9'))
            num9.grid(all_properties, row=0, column=9)

            num0 = ttk.Button(self, text='0', width=6, command=lambda: self.press('0'))
            num0.grid(all_properties, row=0, column=10)

            # Second Line Buttons

            Q = ttk.Button(self, text='q', width=6, command=lambda: self.press('q'))
            Q.grid(all_properties, row=1, column=1)

            W = ttk.Button(self, text='w', width=6, command=lambda: self.press('w'))
            W.grid(all_properties, row=1, column=2)

            E = ttk.Button(self, text='e', width=6, command=lambda: self.press('e'))
            E.grid(all_properties, row=1, column=3)

            R = ttk.Button(self, text='r', width=6, command=lambda: self.press('r'))
            R.grid(all_properties, row=1, column=4)

            T = ttk.Button(self, text='t', width=6, command=lambda: self.press('t'))
            T.grid(all_properties, row=1, column=5)

            Y = ttk.Button(self, text='y', width=6, command=lambda: self.press('y'))
            Y.grid(all_properties, row=1, column=6)

            U = ttk.Button(self, text='u', width=6, command=lambda: self.press('u'))
            U.grid(all_properties, row=1, column=7)

            I = ttk.Button(self, text='i', width=6, command=lambda: self.press('i'))
            I.grid(all_properties, row=1, column=8)

            O = ttk.Button(self, text='o', width=6, command=lambda: self.press('o'))
            O.grid(all_properties, row=1, column=9)

            P = ttk.Button(self, text='p', width=6, command=lambda: self.press('p'))
            P.grid(all_properties, row=1, column=10)

            # Third Line Buttons

            A = ttk.Button(self, text='a', width=6, command=lambda: self.press('a'))
            A.grid(all_properties, row=2, column=1)

            S = ttk.Button(self, text='s', width=6, command=lambda: self.press('s'))
            S.grid(all_properties, row=2, column=2)

            D = ttk.Button(self, text='d', width=6, command=lambda: self.press('d'))
            D.grid(all_properties, row=2, column=3)

            F = ttk.Button(self, text='f', width=6, command=lambda: self.press('f'))
            F.grid(all_properties, row=2, column=4)

            G = ttk.Button(self, text='g', width=6, command=lambda: self.press('g'))
            G.grid(all_properties, row=2, column=5)

            H = ttk.Button(self, text='h', width=6, command=lambda: self.press('h'))
            H.grid(all_properties, row=2, column=6)

            J = ttk.Button(self, text='j', width=6, command=lambda: self.press('j'))
            J.grid(all_properties, row=2, column=7)

            K = ttk.Button(self, text='k', width=6, command=lambda: self.press('k'))
            K.grid(all_properties, row=2, column=8)

            L = ttk.Button(self, text='l', width=6, command=lambda: self.press('l'))
            L.grid(all_properties, row=2, column=9)

            backspace = ttk.Button(
                self, text='<---', width=6, command=self.backspace)
            backspace.grid(all_properties, row=2, column=10)

            # Fourth line Buttons

            shift = ttk.Button(self, text='Shift', width=6, command=self.shift)
            shift.grid(all_properties, row=3, column=1)

            Z = ttk.Button(self, text='z', width=6, command=lambda: self.press('z'))
            Z.grid(all_properties, row=3, column=2)

            X = ttk.Button(self, text='x', width=6, command=lambda: self.press('x'))
            X.grid(all_properties, row=3, column=3)

            C = ttk.Button(self, text='c', width=6, command=lambda: self.press('c'))
            C.grid(all_properties, row=3, column=4)

            V = ttk.Button(self, text='v', width=6, command=lambda: self.press('v'))
            V.grid(all_properties, row=3, column=5)

            B = ttk.Button(self, text='b', width=6, command=lambda: self.press('b'))
            B.grid(all_properties, row=3, column=6)

            N = ttk.Button(self, text='n', width=6, command=lambda: self.press('n'))
            N.grid(all_properties, row=3, column=7)

            M = ttk.Button(self, text='m', width=6, command=lambda: self.press('m'))
            M.grid(all_properties, row=3, column=8)

            dot = ttk.Button(self, text='.', width=6, command=lambda: self.press('.'))
            dot.grid(all_properties, row=3, column=9)

            minus = ttk.Button(self, text='-', width=6, command=lambda: self.press('-'))
            minus.grid(all_properties, row=3, column=10)

            # Fifth Line Buttons

            space = ttk.Button(self, text='Space', width=6,
                               command=lambda: self.press(' '))
            space.grid(row=4, column=2, columnspan=8, padx=2, pady=2, ipadx=350, ipady=10)


if __name__ == '__main__':
    style = Style()
    root = style.master
    root.title('On Screen Keyboard')
    root.geometry('800x480')  # Window size
    root.maxsize(width=800, height=480)
    root.minsize(width=800, height=480)
    VKeyboard(root).pack()
    root.mainloop()
