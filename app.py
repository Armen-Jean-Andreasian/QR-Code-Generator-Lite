import PySimpleGUI as sg
import os
import qrcode


class QRGenerator:
    @staticmethod
    def qr_builder(message: str) -> None:
        data = message
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")


class GUI(QRGenerator):
    def __init__(self):
        icon_path = os.path.abspath(os.path.join(os.getcwd(), 'logo.ico'))
        sg.theme("DarkTeal")
        sg.set_options(icon=icon_path)

        input_box = sg.InputText(tooltip="Enter a link/message", size=32, key='input_box')

        add_button = sg.Button("Generate!")

        self.window = sg.Window("My Notes",
                                layout=[[input_box, add_button]],
                                font=('Helvetica', 12, 'bold'),
                                icon=icon_path)

    def app(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Generate!':
                text = values['input_box']
                QRGenerator.qr_builder(text)
                qr_code_folder = os.path.abspath(os.path.dirname(__file__))
                sg.popup_auto_close(f'QR code has been saved to: \n\n{qr_code_folder}\n\n',
                                    auto_close=False, title="Done!")

        self.window.close()


if __name__ == "__main__":
    qr_generator = GUI()
    qr_generator.app()
