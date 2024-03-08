from functions.task_operations import (
    add_task,
    update_task,
    check_task,
    delete_tasks_checked,
)
from functions.task_utils import list_tasks


def print_menu():
    """Imprime o menu do gerenciador de Lista de Tarefas."""
    print("\nMenu do gerenciador de Lista de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")


def get_user_choice():
    """Obtém a escolha do usuário e a retorna."""
    return input("Digite sua escolha: ")


def handle_add_task(tasks):
    """Adiciona uma nova tarefa."""
    task_name = input("Qual é o nome da tarefa que deseja adicionar? ")
    task_description = input("Qual será a descrição da tarefa? ")
    return add_task(tasks, task_name, task_description)


def handle_update_task(tasks):
    """Atualiza uma tarefa existente."""
    list_tasks(tasks)
    task_index = input("\nDigite o número da tarefa: ")
    task_name = input("Digite o novo nome da tarefa: ")
    task_description = input("Digite a nova descrição da tarefa: ")
    return update_task(tasks, task_index, task_name, task_description)


def handle_check_task(tasks):
    """Marca uma tarefa como completa."""
    list_tasks(tasks)
    index = input("Digite o número da tarefa que deseja completar: ")
    return check_task(tasks, index)


def handle_delete_tasks_checked(tasks):
    """Deleta as tarefas completadas."""
    tasks = delete_tasks_checked(tasks)
    list_tasks(tasks)
    return tasks


def main():
    """Função principal do programa."""
    tasks = []
    while True:
        print_menu()
        choice = get_user_choice()
        if choice == "1":
            tasks = handle_add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            tasks = handle_update_task(tasks)
        elif choice == "4":
            tasks = handle_check_task(tasks)
        elif choice == "5":
            tasks = handle_delete_tasks_checked(tasks)
        elif choice == "6":
            break
    print("Programa finalizado")


if __name__ == "__main__":
    main()
