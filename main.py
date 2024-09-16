from uu import Error

import PySimpleGUI as sg
import threading

sg.theme("DarkRed")

layout = [  [sg.Text("1 тело"), sg.Text("Масса:"), sg.InputText(), sg.Text("Координаты X:"), sg.InputText(), sg.Text("Координаты Y:"), sg.InputText()],
            [sg.Text("2 тело"), sg.Text("Масса:"), sg.InputText(), sg.Text("Координаты X:"), sg.InputText(), sg.Text("Координаты Y:"), sg.InputText()],
            [sg.Text("3 тело"), sg.Text("Масса:"), sg.InputText(), sg.Text("Координаты X:"), sg.InputText(), sg.Text("Координаты Y:"), sg.InputText()],
            [sg.Button("Вжух")],
            [sg.Graph((1250, 1000), (0, 1000), (1250, 0), background_color="blue", key="-GRAPH-")]
            ]

# Создаем окно
window = sg.Window("Planar 3 Body Problem", layout)
window.finalize()


def draw(values):
    global window
    G = 6.6743015 * 10**(-11)
    min_mas = 999999999
    for i in range(len(values)-1):
        if i % 3 == 0:
            values[i] = values[i] * G
            if min_mas > values[i]:
                min_mas = values[i]
    for i in range(len(values)-1):
        if i % 3 == 0:
            values[i] /= min_mas

    for i in range(100):
        window["-GRAPH-"].draw_point((i, i), 2, color="black")


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Отмена':
        break
    if event == "Вжух":
        fl = "False"
        for i in range(len(values)-1):
            try:
                values[i] = int(values[i])
            except Exception:
                if values[i] == "":
                    fl = "True"
                else:
                    fl = "Error"
                break

        if fl == "True" or fl == "Error":
            info = ""
            if fl == "True":
                info = "Введите всю информацию"
            else:
                info = "Необходимо ввести только числа"

            layout_temporary = [ [sg.Text(info)],
                                 [sg.Button("OK")]
                                 ]
            window_temporary = sg.Window("Temporary", layout_temporary)
            event_temporary, values_temporary = window_temporary.read()
            window_temporary.close()
            continue

        thread = threading.Thread(target=draw(values), name="draw")

    print('Молодец, ты справился с вводом', values[0])


window.close()
