import flet as ft

def formulario(page: ft.Page):

    #Criar campo de texto e confirmação

    nome = ft.TextField(label='Digite seu nome: ')
    email = ft.TextField(label='Digite seu e-mail: ')
    msg = ft.TextField(label='Digite uma mensagem: ')
    confirmacao = ft.Text('')

    #Criar função e o botão.
   
    def btn_enviar(e):
        if nome.value and email.value and msg.value:
            confirmacao.value = 'Formulario enviado com sucesso'
        else:
            confirmacao.value('Preencha todos os campos')     
    btn = ft.ElevatedButton(text='Enviar', on_click=btn_enviar)

    #Adicionar as informações a página.
    page.add(
        nome,
        email,
        msg,
        btn,
        confirmacao
    )

ft.app(target=formulario)
