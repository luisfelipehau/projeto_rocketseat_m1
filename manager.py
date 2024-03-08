tasks = []

while True:
    print("\nMenu do gerenciador de Lista de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    choice = input("Digite sua escolha: ")
    if choice == "1":
        task_name = input("Qual é o nome da tarefa que deseja adicionar? ")

        while True:
            try:
                # Tenta converter o input para inteiro
                task_number = int(task_name)
                print("Você digitou um número, por favor, insira um nome válido.")
                task_name = input(
                    "Qual é o nome da tarefa que deseja adicionar? "
                )  # Atualiza o valor de task_name
            except ValueError:
                # Se ocorrer uma ValueError (quando a conversão para int falha), o nome da tarefa é válido
                print("Tarefa adicionada:", task_name)
                break
            except Exception as e:
                # Qualquer outra exceção que ocorrer será tratada aqui
                print("Ocorreu um erro:", e)
                break

    elif choice == "6":
        break

print("Programa finalizado")
