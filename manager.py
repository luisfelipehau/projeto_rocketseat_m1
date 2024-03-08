from functions.task_operations import add_task, update_task
from functions.task_utils import list_tasks

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
    elif choice == "2":
        list_tasks(tasks)
    elif choice == "3":
        list_tasks(tasks)
        task_index = input("\nDigite o número da tarefa: ")
        task_name = input("Digite o novo nome da tarefa: ")
        task_description = input("Digite a nova descrição da tarefa: ")
        tasks = update_task(tasks, task_index, task_name, task_description)
    elif choice == "6":
        break

print("Programa finalizado")
