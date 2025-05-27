import flet as ft

def main(page: ft.Page):
    # Cria o campo de texto onde o usuário digita a tarefa
    texto = ft.TextField('Digite uma tarefa:', width=300)
    
    # Cria a coluna onde as tarefas vão ser listadas
    listar_tarefa = ft.Column()

    # Função que será chamada quando o botão for clicado
    def adicionar_tarefas(e):
        # Verifica se o campo de texto está vazio
        if not texto.value:
            print('Nenhuma tarefa adicionada')
        else:
            print('Adicionar tarefa!')
            # Cria um novo texto com o conteúdo digitado
            nova_tarefa = ft.Text(texto.value)
            # Adiciona esse texto à lista de tarefas
            listar_tarefa.controls.append(nova_tarefa)
            # Atualiza a lista para aparecer na tela
            listar_tarefa.update()
            # Limpa o campo de texto
            texto.value = ""
            texto.update()

    # Cria o botão e associa a função de clique
    btn = ft.ElevatedButton('Adicionar Tarefa', on_click=adicionar_tarefas)

    # Adiciona os elementos na página
    page.add(
        texto,
        btn,
        listar_tarefa
    )

# Executa a aplicação
ft.app(target=main)


