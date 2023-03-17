import PySimpleGUI as sg
import random
#you don't need this part i'm just trying themes and you can chang the theme list by changeng the thms_menu list 
thms = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark',
        'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 
        'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 
        'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 
        'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 
        'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 
        'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 
        'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 
        'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 
        'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 
        'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 
        'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 
        'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 
        'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 
        'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 
        'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 
        'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 
        'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 
        'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 
        'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 
        'Purple', 'Python', 'PythonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 
        'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 20')
    btnsize = (6,3)
    layout = [
        [sg.Text(
        'Output',
        expand_x=True,
        expand_y=True, 
        font='Franklin 26',
        justification='right',
        pad=(10,20),
        right_click_menu = thms_menu,
        key ='-screen-')],
        [sg.Button('CLEAR',expand_x=True),sg.Button('ENTER',expand_x=True)],
        [sg.Button(7,size = btnsize),sg.Button(8,size = btnsize),sg.Button(9,size = btnsize),sg.Button('*',size = btnsize)],
        [sg.Button(4,size = btnsize),sg.Button(5,size = btnsize),sg.Button(6,size = btnsize),sg.Button('/',size = btnsize)],
        [sg.Button(1,size = btnsize),sg.Button(2,size = btnsize),sg.Button(3,size = btnsize),sg.Button('-',size = btnsize)],
        [sg.Button(0,expand_x=True,expand_y=True),sg.Button('.',size = btnsize),sg.Button('+',size = btnsize)]
    ]
    return sg.Window('Calculator', layout)
thms_menu = ['menu',['LightGrey','Topanga','LightGreen6','BluePurple','random']]
window = create_window('LightGrey1')
current_num = ['']
operation =[]
while True:
    event , value = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in thms_menu[1]:
        window.close()
        window = create_window(event)
    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-screen-'].update(num_string)
    if event in ['+','-','*','/']:
        operation.append(''.join(current_num))
        current_num =[]
        operation.append(event)
        window['-screen-'].update(event)
    if event == 'ENTER':
        operation.append(''.join(current_num))
        result = eval(''.join(operation))
        window['-screen-'].update(result)
        operation = []
    if event == 'CLEAR':
        current_num =[]
        operation =[]
        window['-screen-'].update(" ")
window.close()

