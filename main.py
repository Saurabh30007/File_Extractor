import PySimpleGUI as sg
from zip_extractor import extract_archive


sg.theme('Python')

label1 = sg.Text('Select Archive: ', tooltip='Select a compressed file to extract')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose', key='archive')

label2 = sg.Text('Select dest directory: ', tooltip='Select a destination folder for extraction')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='folder')

extract_button = sg.Button('Extract')
quit_button = sg.Button('Quit')
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('File Extractor',
                   [[label1, input1, choose_button1],
                    [label2, input2, choose_button2],
                    [extract_button, output_label, quit_button]])

while True:
    event, values = window.read()
    # print(1, event)
    # print(2, values)

    if event == 'Quit':
        break

    try:
        archivepath = values['archive']
        dest_folder = values['folder']
        extract_archive(archivepath, dest_folder)
        window['output'].update(value='File(s) has been extracted successfully!')

    except FileNotFoundError:
        window['output'].update(value='Choose a file and a folder to extract!!', text_color='yellow')

window.close()
