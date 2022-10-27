import tkinter as tk
from tkinter.ttk import Combobox, Frame, Scale, Style
from tkinter import StringVar, IntVar, DoubleVar

from testsFunctions import Spherical, Rastrigin, Ackley, Beale, Booth, Bukin, Three_humpCamel, Holder_table, McCormick, Shaffer

from PSO import Evolution

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Settings():
    def __init__(self):
        self.testFunction = Spherical()
        self.populationSize = 20
        self.iteration = 80
        self.params = ({'num_particles': self.populationSize,
                        'inertia': 0.8,
                        'cognition': 1.0,
                        'social_rate': 1.0,
                        'local_rate': 1.0,
                        'max_velocity': 1.0,
                        'max_epochs': 10000,
                        'num_neighbors': 0,
                        'fname': ''})
    def __str__(self):
        return f"""
    Количество частиц: {self.populationSize}
    Итераций: {self.iteration}
    Инерция: {self.params["inertia"]}
    Познание: {self.params["cognition"]}
    Соц скорость: {self.params["social_rate"]}
    Локал скорость: {self.params["local_rate"]}
    Макс скорость: {self.params["max_velocity"]}
    Соседей: {self.params["num_neighbors"]}"""

class InitGuiVar():
    def __init__(self, settings):
        self.settings = settings
        self.initGuiVar()

    def initGuiVar(self):
        self.varSelectTestFunction = StringVar()
        self.varSelectTestFunction.trace_add("write", self.changeTestFunction)
        
        self.varPopulationSize = IntVar()
        self.varPopulationSize.set(self.settings.populationSize)
        self.varPopulationSize.trace_add("write", self.changePopulationSize)

        self.varIteration = IntVar()
        self.varIteration.set(self.settings.iteration)
        self.varIteration.trace_add("write", self.changeIteration)

        self.varSliderEra = StringVar()
        self.varSliderEra.set("Поколение: ")

        # Новые переменные для пчелиного роя
        self.varInertia = DoubleVar()
        self.varInertia.trace_add("write", self.changePSOvariable)
        self.varInertia.set(self.settings.params["inertia"])

        self.varCognition = DoubleVar()
        self.varCognition.trace_add("write", self.changePSOvariable)
        self.varCognition.set(self.settings.params["cognition"])

        self.varSocial_rate = DoubleVar()
        self.varSocial_rate.trace_add("write", self.changePSOvariable)
        self.varSocial_rate.set(self.settings.params["social_rate"])

        self.varLocal_rate = DoubleVar()
        self.varLocal_rate.trace_add("write", self.changePSOvariable)
        self.varLocal_rate.set(self.settings.params["local_rate"])

        self.varMax_velocity = DoubleVar()
        self.varMax_velocity.trace_add("write", self.changePSOvariable)
        self.varMax_velocity.set(self.settings.params["max_velocity"])

        self.varNum_neighbors = DoubleVar()
        self.varNum_neighbors.trace_add("write", self.changePSOvariable)
        self.varNum_neighbors.set(self.settings.params["num_neighbors"])


    def changeTestFunction(self, v, i, m):
        value = self.varSelectTestFunction.get()
        print(value)

        if value == "Сферическая":
            self.settings.testFunction = Spherical()
            print("Выбрана функция сферическая")
        if value == "Растригина":
            self.settings.testFunction = Rastrigin()
            print("Выбрана функция растригина")
        if value == "Экли":
            self.settings.testFunction = Ackley()
        if value == "Била":
            self.settings.testFunction = Beale()
        if value == "Стенда":
            self.settings.testFunction = Booth()
        if value == "Букина":
            self.settings.testFunction = Bukin()
        if value == "Три горба":
            self.settings.testFunction = Three_humpCamel()
        if value == "Таблица Холдера":
            self.settings.testFunction = Holder_table()
        if value == "Кормика":
            self.settings.testFunction = McCormick()
        if value == "Шафера":
            self.settings.testFunction = Shaffer()
        
        self.updateEvolution()
        try:
            drawStartArea()
        except NameError:
            pass

        
    def changePopulationSize(self, v, i, m):
        self.settings.populationSize = self.varPopulationSize.get()
        self.settings.params['num_particles'] = self.varPopulationSize.get()
        print(self.settings.populationSize)
        self.updateEvolution()

    def changeIteration(self, v, i, m):
        self.settings.iteration = self.varIteration.get()
        print(self.settings.iteration)
        self.updateEvolution()


    # Обновляет скопом все переменные
    def changePSOvariable(self, v, i, m):
        try:
            self.settings.params['inertia'] = self.varInertia.get()
            self.settings.params['cognition'] = self.varCognition.get()
            self.settings.params['social_rate'] = self.varSocial_rate.get()
            self.settings.params['local_rate'] = self.varLocal_rate.get()
            self.settings.params['max_velocity'] = self.varMax_velocity.get()
            self.settings.params['num_neighbors'] = self.varNum_neighbors.get()
        except Exception as e:
            pass

        self.updateEvolution()


    def updateEvolution(self):
        global e
        e = Evolution(ss)



window = tk.Tk()
ss = Settings()
e = Evolution(ss)
s = InitGuiVar(ss)

window.style = Style()
#window.style.theme_use("alt")
window.option_add( "*font", "clearlyu 12" )
window.title("Лабораторная работа Сиренко В. Н. Алгоритм PSO")
window.geometry('1010x900')


titleFrame = Frame(window)
canvasFrame = Frame(window)
frame = Frame(titleFrame)

# Выбор тестовой функции
label = tk.Label(frame, text="Тестовая функция: ")
label.grid(column=0, row=0)


combo1 = Combobox(frame, textvariable=s.varSelectTestFunction)
combo1['values'] = ["Сферическая", "Растригина", "Экли", "Била", "Стенда", "Букина", "Три горба", "Таблица Холдера", "Кормика", "Шафера"]
combo1.current(0)
combo1.grid(column=1, row=0)



# Количество частиц
label2 = tk.Label(frame, text="Количество частиц: ")
label2.grid(column=3, row=0, padx=5)

ePopulationSize = tk.Entry(frame, width=30, textvariable=s.varPopulationSize)
ePopulationSize.grid(column=4, row=0)

# Итераций
label3 = tk.Label(frame, text="Шаг: ")
label3.grid(column=3, row=1, padx=5)

eIteration = tk.Entry(frame, width=30, textvariable=s.varIteration)
eIteration.grid(column=4, row=1)


# Выбор метода мутации
mutationFrame = Frame(titleFrame)

label5 = tk.Label(mutationFrame, textvariable=s.varSliderEra)
label5.grid(column=2, row=0, pady=5)

#*************
# Параметры добавленные под PSO
framePSOParams = Frame(titleFrame)

#PARAM inertia
labelInertia = tk.Label(framePSOParams, text="Инерция: ")
labelInertia.grid(column=1, row=1, padx=5)

eInertia = tk.Entry(framePSOParams, width=20, textvariable=s.varInertia)
eInertia.grid(column=2, row=1)

#PARAM cognition
labelcognition = tk.Label(framePSOParams, text="Познание: ")
labelcognition.grid(column=1, row=2, padx=5)

ecognition = tk.Entry(framePSOParams, width=20, textvariable=s.varCognition)
ecognition.grid(column=2, row=2)

#PARAM social_rate
labelsocial_rate = tk.Label(framePSOParams, text="Общественаня скорость: ")
labelsocial_rate.grid(column=1, row=3, padx=5)

esocial_rate = tk.Entry(framePSOParams, width=20, textvariable=s.varSocial_rate)
esocial_rate.grid(column=2, row=3)

#PARAM local_rate
labelLocal_rate = tk.Label(framePSOParams, text="Локальная скорость: ")
labelLocal_rate.grid(column=3, row=1, padx=5)

eLocal_rate = tk.Entry(framePSOParams, width=20, textvariable=s.varLocal_rate)
eLocal_rate.grid(column=4, row=1)

#PARAM max_velocity
labelMax_velocity = tk.Label(framePSOParams, text="Максимальная скорость: ")
labelMax_velocity.grid(column=3, row=2, padx=5)

eMax_velocity = tk.Entry(framePSOParams, width=20, textvariable=s.varMax_velocity)
eMax_velocity.grid(column=4, row=2)

#PARAM num_neighbors
labelNum_neighbors = tk.Label(framePSOParams, text="Количество соседей: ")
labelNum_neighbors.grid(column=3, row=3, padx=5)

eNum_neighbors = tk.Entry(framePSOParams, width=20, textvariable=s.varNum_neighbors)
eNum_neighbors.grid(column=4, row=3)

########### Отображение графиков ошибок

def showGeneralErrors():
    global e
    fig = e.showGlobalErrorGraphs()
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    # canvas = FigureCanvasTkAgg(e.drawHromoByStep(), canvasFrame)
    canvas = FigureCanvasTkAgg(fig, canvasFrame)
    canvas.get_tk_widget().pack()

def showBestParticles():
    global e
    fig = e.showGlobalXYGraphs()
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    # canvas = FigureCanvasTkAgg(e.drawHromoByStep(), canvasFrame)
    canvas = FigureCanvasTkAgg(fig, canvasFrame)
    canvas.get_tk_widget().pack()

btnStartEvolution = tk.Button(framePSOParams,
                              text="Общий ошибок",
                              command=showGeneralErrors)
btnStartEvolution.grid(column=5, row=1, padx=20)

btnStartEvolution = tk.Button(framePSOParams,
                              text="Лучшей частицы",
                              command=showBestParticles)
btnStartEvolution.grid(column=5, row=2, padx=20)

# Другие параметры
frame.grid(column=0, row=0, pady=5)

##########


##### код эволюции
def runEvolution():
    global e
    print("===НАСТРОЙКИ===")
    print(ss)
    print("Старт эволюции!")
    e.run()

canvas = None
def drawStartArea():
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    # canvas = FigureCanvasTkAgg(e.drawHromoByStep(), canvasFrame)
    canvas = FigureCanvasTkAgg(e.drawInitArea(), canvasFrame)
    canvas.get_tk_widget().pack()

def updateSlider(arg):
    #print(arg)
    step = int((ss.iteration / 100)  * float(arg))
    #print(f"Slider! {step}")
    s.varSliderEra.set("Поколение: "+str(step))
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    canvas = FigureCanvasTkAgg(e.drawHromoByStep(
        step
    ), canvasFrame)
    canvas.get_tk_widget().pack()

btnStartEvolution = tk.Button(titleFrame,
                              text="Запустить PSO",
                              command=runEvolution)
btnStartEvolution.grid(column=1, row=0, padx=20)

frameSlider=Frame(titleFrame)
slider=Scale(frameSlider, from_=0, to=100, orient='horizontal', length = 980,
             command=updateSlider)
slider.grid(column=0, row=0)
lSlider=tk.Label(frameSlider, text="0..100")

mutationFrame.grid(column=0, row=1, sticky=tk.W+tk.E, columnspan=3)
framePSOParams.grid(column=0, row=2, sticky=tk.W+tk.E, columnspan=3)
frameSlider.grid(column=0, row=3, sticky=tk.W+tk.E, columnspan=3)

titleFrame.grid(column=0, row=0)
canvasFrame.grid(column=0, row=1)

# AFter-init
drawStartArea()
window.mainloop()