import tkinter as tk
from tkinter import ttk


class VKeyboard(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        #super().__init__(parent)
        # Don't show the 'Toplevel' at instantiation
#        super().withdraw()

        #self.title('On Screen Keyboard')

        #self.geometry('1385x320')  # Window size
        #self.maxsize(width=1385, height=320)
        #self.minsize(width=1385, height=320)

        self.style = ttk.Style()
        #self.configure(bg='gray27')
        self.style.configure('TButton', background='gray21')
        self.style.configure('TButton', foreground='white')

        self.theme = "light"

        # entry box
        self.equation = tk.StringVar()
        Dis_entry = ttk.Entry(self, state='readonly', textvariable=self.equation)
        Dis_entry.grid(rowspan=1, columnspan=100, ipadx=999, ipady=20)

        # showing all data in display
        self.exp = " "
        self.is_shift = False

        self.display()

# Necessary functions

    def press(self,  num):
        self.exp = self.exp + str(num)
        self.equation.set(self.exp)

    def backspace(self):
        self.exp = self.exp[:-1]
        self.equation.set(self.exp)

    def shift(self):
        self.is_shift = not self.is_shift
        self.display()

    def clear(self):
        self.exp = " "
        self.equation.set(self.exp)

    def theme(self):
        if self.theme == "dark":
            self.configure(bg='gray27')
            self.style.configure('TButton', background='gray21')
            self.style.configure('TButton', foreground='white')
            self.theme = "light"
        elif self.theme == "light":
            self.configure(bg='gray99')
            self.style.configure('TButton', background='azure')
            self.style.configure('TButton', foreground='black')
            self.theme = "dark"

    def display(self):
        if self.is_shift:
            # Adding keys line wise
            # First Line Button
            tilda = ttk.Button(self, text='~', width=6, command=lambda: self.press('~'))
            tilda.grid(row=1, column=0, ipadx=6, ipady=10)

            num1 = ttk.Button(self, text='!', width=6, command=lambda: self.press('!'))
            num1.grid(row=1, column=1, ipadx=6, ipady=10)

            num2 = ttk.Button(self, text='@', width=6, command=lambda: self.press('@'))
            num2.grid(row=1, column=2, ipadx=6, ipady=10)

            num3 = ttk.Button(self, text='#', width=6, command=lambda: self.press('#'))
            num3.grid(row=1, column=3, ipadx=6, ipady=10)

            num4 = ttk.Button(self, text='$', width=6, command=lambda: self.press('$'))
            num4.grid(row=1, column=4, ipadx=6, ipady=10)

            num5 = ttk.Button(self, text='%', width=6, command=lambda: self.press('%'))
            num5.grid(row=1, column=5, ipadx=6, ipady=10)

            num6 = ttk.Button(self, text='^', width=6, command=lambda: self.press('^'))
            num6.grid(row=1, column=6, ipadx=6, ipady=10)

            num7 = ttk.Button(self, text='&', width=6, command=lambda: self.press('&'))
            num7.grid(row=1, column=7, ipadx=6, ipady=10)

            num8 = ttk.Button(self, text='*', width=6, command=lambda: self.press('*'))
            num8.grid(row=1, column=8, ipadx=6, ipady=10)

            num9 = ttk.Button(self, text='(', width=6, command=lambda: self.press('('))
            num9.grid(row=1, column=9, ipadx=6, ipady=10)

            num0 = ttk.Button(self, text=')', width=6, command=lambda: self.press(')'))
            num0.grid(row=1, column=10, ipadx=6, ipady=10)

            under = ttk.Button(self, text='_', width=6, command=lambda: self.press('_'))
            under.grid(row=1, column=11, ipadx=6, ipady=10)

            plus = ttk.Button(self, text='+', width=6, command=lambda: self.press('+'))
            plus.grid(row=1, column=12, ipadx=6, ipady=10)

            backspace = ttk.Button(
                self, text='<---', width=6, command=self.backspace)
            backspace.grid(row=1, column=13, ipadx=6, ipady=10)

            # Second Line Buttons

            tab_button = ttk.Button(self, text='Tab', width=6,
                                    command=lambda: self.press('\t'))
            tab_button.grid(row=2, column=0, columnspan=2, ipadx=55, ipady=10)

            Q = ttk.Button(self, text='Q', width=6, command=lambda: self.press('Q'))
            Q.grid(row=2, column=2, ipadx=6, ipady=10)

            W = ttk.Button(self, text='W', width=6, command=lambda: self.press('W'))
            W.grid(row=2, column=3, ipadx=6, ipady=10)

            E = ttk.Button(self, text='E', width=6, command=lambda: self.press('E'))
            E.grid(row=2, column=4, ipadx=6, ipady=10)

            R = ttk.Button(self, text='R', width=6, command=lambda: self.press('R'))
            R.grid(row=2, column=5, ipadx=6, ipady=10)

            T = ttk.Button(self, text='T', width=6, command=lambda: self.press('T'))
            T.grid(row=2, column=6, ipadx=6, ipady=10)

            Y = ttk.Button(self, text='Y', width=6, command=lambda: self.press('Y'))
            Y.grid(row=2, column=7, ipadx=6, ipady=10)

            U = ttk.Button(self, text='U', width=6, command=lambda: self.press('U'))
            U.grid(row=2, column=8, ipadx=6, ipady=10)

            I = ttk.Button(self, text='I', width=6, command=lambda: self.press('I'))
            I.grid(row=2, column=9, ipadx=6, ipady=10)

            O = ttk.Button(self, text='O', width=6, command=lambda: self.press('O'))
            O.grid(row=2, column=10, ipadx=6, ipady=10)

            P = ttk.Button(self, text='P', width=6, command=lambda: self.press('P'))
            P.grid(row=2, column=11, ipadx=6, ipady=10)

            curly_l = ttk.Button(
                self, text='{', width=6, command=lambda: self.press('{'))
            curly_l.grid(row=2, column=12, ipadx=6, ipady=10)

            curly_r = ttk.Button(self, text='}', width=6,
                                 command=lambda: self.press('}'))
            curly_r.grid(row=2, column=13, ipadx=6, ipady=10)

            # Third Line Buttons

            A = ttk.Button(self, text='A', width=6, command=lambda: self.press('A'))
            A.grid(row=3, column=0, ipadx=6, ipady=10)

            S = ttk.Button(self, text='S', width=6, command=lambda: self.press('S'))
            S.grid(row=3, column=1, ipadx=6, ipady=10)

            D = ttk.Button(self, text='D', width=6, command=lambda: self.press('D'))
            D.grid(row=3, column=2, ipadx=6, ipady=10)

            F = ttk.Button(self, text='F', width=6, command=lambda: self.press('F'))
            F.grid(row=3, column=3, ipadx=6, ipady=10)

            G = ttk.Button(self, text='G', width=6, command=lambda: self.press('G'))
            G.grid(row=3, column=4, ipadx=6, ipady=10)

            H = ttk.Button(self, text='H', width=6, command=lambda: self.press('H'))
            H.grid(row=3, column=5, ipadx=6, ipady=10)

            J = ttk.Button(self, text='J', width=6, command=lambda: self.press('J'))
            J.grid(row=3, column=6, ipadx=6, ipady=10)

            K = ttk.Button(self, text='K', width=6, command=lambda: self.press('K'))
            K.grid(row=3, column=7, ipadx=6, ipady=10)

            L = ttk.Button(self, text='L', width=6, command=lambda: self.press('L'))
            L.grid(row=3, column=8, ipadx=6, ipady=10)

            colon = ttk.Button(self, text=':', width=6,
                               command=lambda: self.press(':'))
            colon.grid(row=3, column=9, ipadx=6, ipady=10)

            quotation = ttk.Button(self, text='"', width=6,
                                   command=lambda: self.press('"'))
            quotation.grid(row=3, column=10, ipadx=6, ipady=10)

            pipe = ttk.Button(self, text='|', width=6, command=lambda: self.press('|'))
            pipe.grid(row=3, column=11, ipadx=6, ipady=10)

            enter = ttk.Button(self, text='Enter', width=6,
                               command=lambda: self.press('\n'))
            enter.grid(row=3, column=12, columnspan=2, ipadx=55, ipady=10)

            # Fourth line Buttons

            shift = ttk.Button(self, text='Shift', width=6, command=self.shift)
            shift.grid(row=4, column=0, columnspan=2, ipadx=55, ipady=10)

            Z = ttk.Button(self, text='Z', width=6, command=lambda: self.press('Z'))
            Z.grid(row=4, column=2, ipadx=6, ipady=10)

            X = ttk.Button(self, text='X', width=6, command=lambda: self.press('X'))
            X.grid(row=4, column=3, ipadx=6, ipady=10)

            C = ttk.Button(self, text='C', width=6, command=lambda: self.press('C'))
            C.grid(row=4, column=4, ipadx=6, ipady=10)

            V = ttk.Button(self, text='V', width=6, command=lambda: self.press('V'))
            V.grid(row=4, column=5, ipadx=6, ipady=10)

            B = ttk.Button(self, text='B', width=6, command=lambda: self.press('B'))
            B.grid(row=4, column=6, ipadx=6, ipady=10)

            N = ttk.Button(self, text='N', width=6, command=lambda: self.press('N'))
            N.grid(row=4, column=7, ipadx=6, ipady=10)

            M = ttk.Button(self, text='M', width=6, command=lambda: self.press('M'))
            M.grid(row=4, column=8, ipadx=6, ipady=10)

            ang_l = ttk.Button(self, text='<', width=6, command=lambda: self.press('<'))
            ang_l.grid(row=4, column=9, ipadx=6, ipady=10)

            ang_r = ttk.Button(self, text='>', width=6, command=lambda: self.press('>'))
            ang_r.grid(row=4, column=10, ipadx=6, ipady=10)

            question = ttk.Button(self, text='?', width=6,
                                  command=lambda: self.press('?'))
            question.grid(row=4, column=11, ipadx=6, ipady=10)

            clear = ttk.Button(self, text='Clear', width=6, command=self.clear)
            clear.grid(row=4, column=12, columnspan=2, ipadx=55, ipady=10)

            # Fifth Line Buttons

            space = ttk.Button(self, text='Space', width=6,
                               command=lambda: self.press(' '))
            space.grid(row=5, column=2, columnspan=8, ipadx=350, ipady=10)

            theme = ttk.Button(self, text='Theme', width=6, command=self.theme)
            theme.grid(row=5, column=12, columnspan=2, ipadx=55, ipady=10)

        else:
            # Adding keys line wise
            # First Line Button
            tick = ttk.Button(self, text='`', width=6, command=lambda: self.press('`'))
            tick.grid(row=1, column=0, ipadx=6, ipady=10)

            num1 = ttk.Button(self, text='1', width=6, command=lambda: self.press('1'))
            num1.grid(row=1, column=1, ipadx=6, ipady=10)

            num2 = ttk.Button(self, text='2', width=6, command=lambda: self.press('2'))
            num2.grid(row=1, column=2, ipadx=6, ipady=10)

            num3 = ttk.Button(self, text='3', width=6, command=lambda: self.press('3'))
            num3.grid(row=1, column=3, ipadx=6, ipady=10)

            num4 = ttk.Button(self, text='4', width=6, command=lambda: self.press('4'))
            num4.grid(row=1, column=4, ipadx=6, ipady=10)

            num5 = ttk.Button(self, text='5', width=6, command=lambda: self.press('5'))
            num5.grid(row=1, column=5, ipadx=6, ipady=10)

            num6 = ttk.Button(self, text='6', width=6, command=lambda: self.press('6'))
            num6.grid(row=1, column=6, ipadx=6, ipady=10)

            num7 = ttk.Button(self, text='7', width=6, command=lambda: self.press('7'))
            num7.grid(row=1, column=7, ipadx=6, ipady=10)

            num8 = ttk.Button(self, text='8', width=6, command=lambda: self.press('8'))
            num8.grid(row=1, column=8, ipadx=6, ipady=10)

            num9 = ttk.Button(self, text='9', width=6, command=lambda: self.press('9'))
            num9.grid(row=1, column=9, ipadx=6, ipady=10)

            num0 = ttk.Button(self, text='0', width=6, command=lambda: self.press('0'))
            num0.grid(row=1, column=10, ipadx=6, ipady=10)

            minus = ttk.Button(self, text='-', width=6, command=lambda: self.press('-'))
            minus.grid(row=1, column=11, ipadx=6, ipady=10)

            equal = ttk.Button(self, text='=', width=6, command=lambda: self.press('='))
            equal.grid(row=1, column=12, ipadx=6, ipady=10)

            backspace = ttk.Button(
                self, text='<---', width=6, command=self.backspace)
            backspace.grid(row=1, column=13, ipadx=6, ipady=10)

            # Second Line Buttons

            tab_button = ttk.Button(self, text='Tab', width=6,
                                    command=lambda: self.press('\t'))
            tab_button.grid(row=2, column=0, columnspan=2, ipadx=55, ipady=10)

            Q = ttk.Button(self, text='q', width=6, command=lambda: self.press('q'))
            Q.grid(row=2, column=2, ipadx=6, ipady=10)

            W = ttk.Button(self, text='w', width=6, command=lambda: self.press('w'))
            W.grid(row=2, column=3, ipadx=6, ipady=10)

            E = ttk.Button(self, text='e', width=6, command=lambda: self.press('e'))
            E.grid(row=2, column=4, ipadx=6, ipady=10)

            R = ttk.Button(self, text='r', width=6, command=lambda: self.press('r'))
            R.grid(row=2, column=5, ipadx=6, ipady=10)

            T = ttk.Button(self, text='t', width=6, command=lambda: self.press('t'))
            T.grid(row=2, column=6, ipadx=6, ipady=10)

            Y = ttk.Button(self, text='y', width=6, command=lambda: self.press('y'))
            Y.grid(row=2, column=7, ipadx=6, ipady=10)

            U = ttk.Button(self, text='u', width=6, command=lambda: self.press('u'))
            U.grid(row=2, column=8, ipadx=6, ipady=10)

            I = ttk.Button(self, text='i', width=6, command=lambda: self.press('i'))
            I.grid(row=2, column=9, ipadx=6, ipady=10)

            O = ttk.Button(self, text='o', width=6, command=lambda: self.press('o'))
            O.grid(row=2, column=10, ipadx=6, ipady=10)

            P = ttk.Button(self, text='p', width=6, command=lambda: self.press('p'))
            P.grid(row=2, column=11, ipadx=6, ipady=10)

            sq_l = ttk.Button(self, text='[', width=6, command=lambda: self.press('['))
            sq_l.grid(row=2, column=12, ipadx=6, ipady=10)

            sq_r = ttk.Button(self, text=']', width=6, command=lambda: self.press(']'))
            sq_r.grid(row=2, column=13, ipadx=6, ipady=10)

            # Third Line Buttons

            A = ttk.Button(self, text='a', width=6, command=lambda: self.press('a'))
            A.grid(row=3, column=0, ipadx=6, ipady=10)

            S = ttk.Button(self, text='s', width=6, command=lambda: self.press('s'))
            S.grid(row=3, column=1, ipadx=6, ipady=10)

            D = ttk.Button(self, text='d', width=6, command=lambda: self.press('d'))
            D.grid(row=3, column=2, ipadx=6, ipady=10)

            F = ttk.Button(self, text='f', width=6, command=lambda: self.press('f'))
            F.grid(row=3, column=3, ipadx=6, ipady=10)

            G = ttk.Button(self, text='g', width=6, command=lambda: self.press('g'))
            G.grid(row=3, column=4, ipadx=6, ipady=10)

            H = ttk.Button(self, text='h', width=6, command=lambda: self.press('h'))
            H.grid(row=3, column=5, ipadx=6, ipady=10)

            J = ttk.Button(self, text='j', width=6, command=lambda: self.press('j'))
            J.grid(row=3, column=6, ipadx=6, ipady=10)

            K = ttk.Button(self, text='k', width=6, command=lambda: self.press('k'))
            K.grid(row=3, column=7, ipadx=6, ipady=10)

            L = ttk.Button(self, text='l', width=6, command=lambda: self.press('l'))
            L.grid(row=3, column=8, ipadx=6, ipady=10)

            semi_co = ttk.Button(self, text=';', width=6,
                                 command=lambda: self.press(';'))
            semi_co.grid(row=3, column=9, ipadx=6, ipady=10)

            quotation = ttk.Button(self, text="'", width=6,
                                   command=lambda: self.press('"'))
            quotation.grid(row=3, column=10, ipadx=6, ipady=10)

            back_slash = ttk.Button(self, text='\\', width=6,
                                    command=lambda: self.press('\\'))
            back_slash.grid(row=3, column=11, ipadx=6, ipady=10)

            enter = ttk.Button(self, text='Enter', width=6,
                               command=lambda: self.press('\n'))
            enter.grid(row=3, column=12, columnspan=2, ipadx=55, ipady=10)

            # Fourth line Buttons

            shift = ttk.Button(self, text='Shift', width=6, command=self.shift)
            shift.grid(row=4, column=0, columnspan=2, ipadx=55, ipady=10)

            Z = ttk.Button(self, text='z', width=6, command=lambda: self.press('z'))
            Z.grid(row=4, column=2, ipadx=6, ipady=10)

            X = ttk.Button(self, text='x', width=6, command=lambda: self.press('x'))
            X.grid(row=4, column=3, ipadx=6, ipady=10)

            C = ttk.Button(self, text='c', width=6, command=lambda: self.press('c'))
            C.grid(row=4, column=4, ipadx=6, ipady=10)

            V = ttk.Button(self, text='v', width=6, command=lambda: self.press('v'))
            V.grid(row=4, column=5, ipadx=6, ipady=10)

            B = ttk.Button(self, text='b', width=6, command=lambda: self.press('b'))
            B.grid(row=4, column=6, ipadx=6, ipady=10)

            N = ttk.Button(self, text='n', width=6, command=lambda: self.press('n'))
            N.grid(row=4, column=7, ipadx=6, ipady=10)

            M = ttk.Button(self, text='m', width=6, command=lambda: self.press('m'))
            M.grid(row=4, column=8, ipadx=6, ipady=10)

            comma = ttk.Button(self, text=',', width=6, command=lambda: self.press(','))
            comma.grid(row=4, column=9, ipadx=6, ipady=10)

            dot = ttk.Button(self, text='.', width=6, command=lambda: self.press('.'))
            dot.grid(row=4, column=10, ipadx=6, ipady=10)

            slash = ttk.Button(self, text='/', width=6, command=lambda: self.press('/'))
            slash.grid(row=4, column=11, ipadx=6, ipady=10)

            clear = ttk.Button(self, text='Clear', width=6, command=self.clear)
            clear.grid(row=4, column=12, columnspan=2, ipadx=55, ipady=10)

            # Fifth Line Buttons

            space = ttk.Button(self, text='Space', width=6,
                               command=lambda: self.press(' '))
            space.grid(row=5, column=2, columnspan=8, ipadx=350, ipady=10)

            theme = ttk.Button(self, text='Theme', width=6, command=self.theme)
            theme.grid(row=5, column=12, columnspan=2, ipadx=55, ipady=10)


if __name__ == '__main__':
    root = tk.Tk()
    VKeyboard(root).pack()
    root.mainloop()
