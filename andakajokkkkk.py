import tkinter as tk
from tkinter import ttk
 
LARGEFONT = ("Verdana", 35)
 
class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)  
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}  
        for F in (ความเร็ว, เวลา, อุณภูมิ, พื้นที่, ความดัน, calculate):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(calculate)
 
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
 
class calculate(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label5 = ttk.Label(self, text="Calculate", font=LARGEFONT)
        label5.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="เวลา", command=lambda: controller.show_frame(เวลา))
        button1.grid(row=1, column=1, padx=10, pady=10)
        button2 = ttk.Button(self, text="ความเร็ว", command=lambda: controller.show_frame(ความเร็ว))
        button2.grid(row=2, column=1, padx=10, pady=10)
        button3 = ttk.Button(self, text="พื้นที่", command=lambda: controller.show_frame(พื้นที่))
        button3.grid(row=3, column=1, padx=10, pady=10)
        button4 = ttk.Button(self, text="ความดัน", command=lambda: controller.show_frame(ความดัน))
        button4.grid(row=4, column=1, padx=10, pady=10)
        button5 = ttk.Button(self, text="อุณภูมิ", command=lambda: controller.show_frame(อุณภูมิ))
        button5.grid(row=5, column=1, padx=10, pady=10)
 
class ความเร็ว(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="ความเร็ว",font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)




        get=ttk.Entry(self,font=('Arial',12))
        get.grid(row=1, column=4, padx=10, pady=10)





        speed_cata= ttk.Combobox(self,values=['km/h','m/s','mph','tons'])
        speed_cata.grid(row=2, column=4, padx=10, pady=10)

        label1 = ttk.Label(self, text="เเปลงเป็น")
        label1.grid(row=3, column=4, padx=10, pady=10)

        speed_want= ttk.Combobox(self,values=['km/h','m/s','mph','tons'])
        speed_want.grid(row=4, column=4, padx=10, pady=10)

        

        label3 = ttk.Button(self, text="ผลลัพ")
        label3.grid(row=5, column=4, padx=10, pady=10)



        


       
        
       
        button_back = ttk.Button(self, text="กลับ", command=lambda: controller.show_frame(calculate))
        button_back.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
 
    def calculate_speed(self):
        try:
            distance = float(self.entry_distance.get())
            time = float(self.entry_time.get())
            if time != 0:
                speed = distance / time
                self.result_label.config(text=f"ผลลัพธ์: {speed:.2f} เมตร/วินาที")
            else:
                self.result_label.config(text="ข้อผิดพลาด: เวลาไม่สามารถเป็นศูนย์ได้")
        except ValueError:
            self.result_label.config(text="ข้อผิดพลาด: โปรดป้อนตัวเลขที่ถูกต้อง")
 
class เวลา(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="เวลา", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
       
        label_distance = ttk.Label(self, text="ระยะทาง (เมตร):")
        label_distance.grid(row=1, column=1, padx=10, pady=10)
        self.entry_distance = ttk.Entry(self)
        self.entry_distance.grid(row=1, column=2, padx=10, pady=10)
       
        label_speed = ttk.Label(self, text="ความเร็ว (เมตร/วินาที):")
        label_speed.grid(row=2, column=1, padx=10, pady=10)
        self.entry_speed = ttk.Entry(self)
        self.entry_speed.grid(row=2, column=2, padx=10, pady=10)
       
        self.result_label = ttk.Label(self, text="ผลลัพธ์: ")
        self.result_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
       
        button_calculate = ttk.Button(self, text="คำนวณเวลา", command=self.calculate_time)
        button_calculate.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
       
        button_back = ttk.Button(self, text="กลับ", command=lambda: controller.show_frame(calculate))
        button_back.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
 
    def calculate_time(self):
        try:
            distance = float(self.entry_distance.get())
            speed = float(self.entry_speed.get())
            if speed != 0:
                time = distance / speed
                self.result_label.config(text=f"ผลลัพธ์: {time:.2f} วินาที")
            else:
                self.result_label.config(text="ข้อผิดพลาด: ความเร็วไม่สามารถเป็นศูนย์ได้")
        except ValueError:
            self.result_label.config(text="ข้อผิดพลาด: โปรดป้อนตัวเลขที่ถูกต้อง")
 
class อุณภูมิ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="อุณภูมิ", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
       
        label_celsius = ttk.Label(self, text="อุณหภูมิ (องศาเซลเซียส):")
        label_celsius.grid(row=1, column=1, padx=10, pady=10)
        self.entry_celsius = ttk.Entry(self)
        self.entry_celsius.grid(row=1, column=2, padx=10, pady=10)
       
        self.result_label = ttk.Label(self, text="ผลลัพธ์: ")
        self.result_label.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
       
        button_calculate = ttk.Button(self, text="แปลงเป็นฟาเรนไฮต์", command=self.convert_temperature)
        button_calculate.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
       
        button_back = ttk.Button(self, text="กลับ", command=lambda: controller.show_frame(calculate))
        button_back.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
 
    def convert_temperature(self):
        try:
            celsius = float(self.entry_celsius.get())
            fahrenheit = (celsius * 9/5) + 32
            self.result_label.config(text=f"ผลลัพธ์: {fahrenheit:.2f} °F")
        except ValueError:
            self.result_label.config(text="ข้อผิดพลาด: โปรดป้อนตัวเลขที่ถูกต้อง")
 
class พื้นที่(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="พื้นที่", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
       
        label_length = ttk.Label(self, text="ความยาว (เมตร):")
        label_length.grid(row=1, column=1, padx=10, pady=10)
        self.entry_length = ttk.Entry(self)
        self.entry_length.grid(row=1, column=2, padx=10, pady=10)
       
        label_width = ttk.Label(self, text="ความกว้าง (เมตร):")
        label_width.grid(row=2, column=1, padx=10, pady=10)
        self.entry_width = ttk.Entry(self)
        self.entry_width.grid(row=2, column=2, padx=10, pady=10)
       
        self.result_label = ttk.Label(self, text="ผลลัพธ์: ")
        self.result_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
       
        button_calculate = ttk.Button(self, text="คำนวณพื้นที่", command=self.calculate_area)
        button_calculate.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
       
        button_back = ttk.Button(self, text="กลับ", command=lambda: controller.show_frame(calculate))
        button_back.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
 
    def calculate_area(self):
        try:
            length = float(self.entry_length.get())
            width = float(self.entry_width.get())
            area = length * width
            self.result_label.config(text=f"ผลลัพธ์: {area:.2f} ตารางเมตร")
        except ValueError:
            self.result_label.config(text="ข้อผิดพลาด: โปรดป้อนตัวเลขที่ถูกต้อง")
 
class ความดัน(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="ความดัน", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
       
        label_force = ttk.Label(self, text="แรง (นิวตัน):")
        label_force.grid(row=1, column=1, padx=10, pady=10)
        self.entry_force = ttk.Entry(self)
        self.entry_force.grid(row=1, column=2, padx=10, pady=10)
       
        label_area = ttk.Label(self, text="พื้นที่ (ตารางเมตร):")
        label_area.grid(row=2, column=1, padx=10, pady=10)
        self.entry_area = ttk.Entry(self)
        self.entry_area.grid(row=2, column=2, padx=10, pady=10)
       
        self.result_label = ttk.Label(self, text="ผลลัพธ์: ")
        self.result_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
       
        button_calculate = ttk.Button(self, text="คำนวณความดัน", command=self.calculate_pressure)
        button_calculate.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
       
        button_back = ttk.Button(self, text="กลับ", command=lambda: controller.show_frame(calculate))
        button_back.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
 
    def calculate_pressure(self):
        try:
            force = float(self.entry_force.get())
            area = float(self.entry_area.get())
            if area != 0:
                pressure = force / area
                self.result_label.config(text=f"ผลลัพธ์: {pressure:.2f} ปาสกาล")
            else:
                self.result_label.config(text="ข้อผิดพลาด: พื้นที่ไม่สามารถเป็นศูนย์ได้")
        except ValueError:
            self.result_label.config(text="ข้อผิดพลาด: โปรดป้อนตัวเลขที่ถูกต้อง")
 
app = tkinterApp()
app.mainloop()