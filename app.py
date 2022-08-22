import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text("Peso (KG): "), sg.Input(key='-PESO-')],
         [sg.Text("Altura (CM): "), sg.Input(key='-ALTURA-')],
         [sg.Text("Resultado: "), sg.Text(size=(30,1), key="-OUTPUT-")],
         [sg.Button('Calcular'), sg.Button('Sair')],
         [sg.Text("Fonte: Tua Saúde - tuasaude.com")]]

window = sg.Window('IMC', layout)

def imc(p, a):
    a = a / 100
    res = p / (a * a)
    res = round(res, 2)
    if res < 18.5:
        return f"{res} - Magreza"
    elif res >= 18.5 and res < 24.9:
        return f"{res} - Saudável"
    elif res >= 25.0 and res < 29.9:
        return f"{res} - Sobrepeso"
    elif res >= 30.0 and res < 34.9:
        return f"{res} - Obesidade Grau I"
    elif res >= 35.0 and res < 39.9:
        return f"{res} - Obesidade Grau II"
    else:
        return f"{res} - Obesidade Grau III"

while True:  # Event Loop
    event, values = window.read()
    a = values["-PESO-"]
    b = values["-ALTURA-"]
    if a.isnumeric() == True and b.isnumeric() == True:
        a = float(a)
        b = float(b)
        if event == 'Calcular':
            window['-OUTPUT-'].update(imc(a, b))
    else:
        if event == 'Calcular':
            window['-OUTPUT-'].update("Valores inválidos!")
    if event == sg.WIN_CLOSED or event == 'Sair':
        break