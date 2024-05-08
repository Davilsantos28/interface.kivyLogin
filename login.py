from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
from functools import partial
from kivy.uix.modalview import ModalView


class Login(BoxLayout):
    def __init__(self, arg1=None, arg2=None, **kwargs):
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__(**kwargs)
        self.arg1 = arg1
        self.arg2 = arg2
        Window.clearcolor = ("#f0ebbb")
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        self.add_widget(Image(source='data:image/jpeg;base64,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'))
        
        self.add_widget(Label(text="LOGIN", font_size=40, font_name='Georgia', color=get_color_from_hex('#623ecc')))

        
        self.username_input = TextInput(hint_text="Nome de usuário",halign='center')
        self.senha_input = TextInput(hint_text="Digite sua senha",halign='center', password=True)
        1

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#623ecc'), font_size=25))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#623ecc'), font_size=25))
        self.add_widget(self.senha_input)
        
        
        self.cadastrar_button = Button(text="Entrar", background_color=(0, 1, 0, 0.75))
        self.login_button = Button(text="Não possui uma conta? Cadastre-se", background_color=(1, 0, 0))
        self.login_button.bind(on_release=partial(self.create_new_window, self.arg1, self.arg2))
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

    def create_new_window(self, arg1, arg2, instance):
            new_window = NewWindow(arg1, arg2)
            new_window.open()
            Window.clearcolor = (1, 1, 1, 1)

    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class NewWindow(BoxLayout):
    def __init__(self, arg1, arg2, **kwargs):
        Window.clearcolor = (1, 0, 0)
        super().__init__(**kwargs)
        self.arg1 = 'value1'
        self.arg2 = 'value2'
        self.orientation = 'vertical'
        self.padding = [120, 120]
        self.spacing = 10

        self.add_widget(Label(text='Tela Cadastro', font_size=40, font_name='Georgia', color=get_color_from_hex('#623ecc')))
        Window.clearcolor = ("#f0ebbb")

        self.username_input = TextInput(hint_text="Nome de usuário",halign='center')
        self.email_input = TextInput(hint_text="Digite seu email",halign='center')
        self.celular_input = TextInput(hint_text="Digite o número do seu celular",halign='center')
        self.senha_input = TextInput(hint_text="Digite sua senha", password=True,halign='center')

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#cc623f'), font_size=20))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#cc623f'), font_size=25))
        self.add_widget(self.email_input)
        self.add_widget(Label(text="Celular:", font_name='Arial', color=get_color_from_hex('#cc623f'), font_size=25))
        self.add_widget(self.celular_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#cc623f'), font_size=25))
        self.add_widget(self.senha_input)

        self.button_cadastrar = Button(text='Cadastrar', background_color=(0, 1, 0, 0.75))
        self.button_cadastrar.bind(on_release=partial(self.entrar_interface_login, self.arg1, self.arg2))
        self.add_widget(self.button_cadastrar)

    def entrar_interface_login(self, arg1, arg2, instance):
            entrar_login = Login(arg1, arg2)
            entrar_login.open()
            Window.clearcolor = ("#f0ebbb")


    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()
