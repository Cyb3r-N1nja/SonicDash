import tkinter as tk
from tkinter import messagebox


class MyFirstGUI(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        master.title("Timer")

        self.Canvas_Timer_x = 460
        self.Canvas_Timer_y = 460
        self.minutes_default = 15
        self.seconds_default = 0



        self.temp = 0
        self.Hold = False
        self.tempstart = 1
        self.tempcurrent = 0
        self.Wiget_x = int((self.Canvas_Timer_x * 0.3333))
        self.Wiget_y = int((self.Canvas_Timer_y * 0.1666))

        self.Circle_Timer_x = int((self.Canvas_Timer_x * 0.2667))
        self.Circle_Timer_y = int((self.Canvas_Timer_y * 0.5))
        self.Canvas_hight = int((self.Canvas_Timer_y * 0.43))
        self.Canvas_wight = int((self.Canvas_Timer_x * 0.43))

        self.Circle_Diameter = int((self.Canvas_Timer_x * 0.2))
        self.Circle_Boarder = int((self.Canvas_Timer_x * 0.167))

        self.Entry_x = int((self.Canvas_Timer_x * 0.3333))
        self.Entry_y = int((self.Canvas_Timer_y * 0.0555))

        self.minute = tk.StringVar()
        self.second = tk.StringVar()

        self.minute.set(str(self.minutes_default))
        self.second.set(str(self.seconds_default))

        self.minuteEntry = tk.Entry(master, width=3, font=("Arial", 18, ""),
                                    textvariable=self.minute)
        self.minuteEntry.place(x=self.Entry_x, y=self.Entry_y)

        self.secondEntry = tk.Entry(master, width=3, font=("Arial", 18, ""),
                                    textvariable=self.second)
        self.secondEntry.place(x=(self.Entry_x + 50), y=self.Entry_y)

        self.btn = tk.Button(master, text='Countdown', bd='5',
                             command=self.Countdown)
        self.btn.place(x=self.Wiget_x, y=self.Wiget_y)
        self.btn_reset = tk.Button(master, text='RESET', bd='5',
                                   command=self.reset)
        self.btn_reset.place(x=self.Wiget_x, y=(self.Wiget_y + 30))
        self.btn_stop = tk.Button(master, text='STOP', bd='5',
                                  command=self.stop)
        self.btn_stop.place(x=self.Wiget_x, y=(self.Wiget_y + 60))
        self.btn_restart = tk.Button(master, text='Restart', bd='5',
                                     command=self.restart)
        self.btn_restart.place(x=self.Wiget_x, y=(self.Wiget_y + 90))

        self.timer = None

    def Countdown(self):

        try:
            self.temp = int(self.minute.get()) * 60 + int(self.second.get())
            self.tempstart = self.temp

        except:
            print("Please input the right value")

        self.set_display()

        if not self.timer:
            self.timer = self.after(1000,self.update)

    def set_display(self):
        mins = str(self.minutes_default)
        mins, secs = divmod(self.temp, 60)
        self.minute.set("{0:2d}".format(mins))
        self.second.set("{0:2d}".format(secs))

    def update(self):
        if (self.temp > -1) and (self.Hold == False):
            self.set_display()
            
            if self.temp == 0:
                messagebox.showinfo("Time Countdown", "Time's up ")
            self.temp -= 1
            self.tempcurrent = self.temp
        self.timer = self.after(1000,self.update)

    def reset(self):

        self.minute.set(str(self.minutes_default))
        self.second.set("00")
        self.Hold = False
        self.Countdown()
        return

    def stop(self):
        self.Hold = True
        self.Countdown()
        return

    def restart(self):

        self.update()
        self.Hold = False
        self.Countdown()
        return



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    my_gui = MyFirstGUI(root)
    my_gui2 = MyFirstGUI(tk.Toplevel(root))
    my_gui3 = MyFirstGUI(tk.Toplevel(root))

    
    root.mainloop()