def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 20')
    btnsize = (6,3)
    layout = [
        [sg.Text(
        ' ',
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
