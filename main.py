import flet as ft

def main(page: ft.Page):
    # Cria o campo de texto onde o usuário digita a tarefa
    texto = ft.TextField('Digite uma tarefa:', width=300)
    
    # Cria a coluna para listar as tarefas
    listar_tarefa = ft.Column()

    
    def adicionar_tarefas(e):
        if not texto.value:
            print('Nenhuma tarefa adicionada')
        else:
            print('Adicionar tarefa!')
            
            nova_tarefa = ft.Text(texto.value)
            
            listar_tarefa.controls.append(nova_tarefa)
            
            listar_tarefa.update()
            
            texto.value = ""
            texto.update()

    # Cria o botão 
    btn = ft.ElevatedButton('Adicionar Tarefa', on_click=adicionar_tarefas)

    
    page.add(
        texto,
        btn,
        listar_tarefa
    )


ft.app(main)


