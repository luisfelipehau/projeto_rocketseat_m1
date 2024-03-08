from functions.add_task import add_task

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
        task_description = input("Qual será a descrição da tarefa?")
        tasks = add_task(tasks, task_name, task_description)

    elif choice == "6":
        break

print("Programa finalizado")
