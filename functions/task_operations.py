def add_task(tasks, task_name, task_description):
    """
    Adiciona uma nova tarefa à lista de tarefas.

    Args:
        tasks (list): Lista de tarefas existentes.
        task_name (str): Nome da nova tarefa a ser adicionada.
        task_description (str): Descrição da nova tarefa.

    Returns:
        list: Lista de tarefas atualizada após a adição da nova tarefa.
    """
    # Estrutura da tarefa: keys -> name, description e status
    task = {"name": task_name, "status": False, "description": task_description}
    tasks.append(task)
    print(f"Tarefa {task_name} adicionada com sucesso!")
    return tasks


def update_task(tasks: list, index: int, task_name: str, task_description: str) -> list:
    """
    Atualiza uma tarefa existente na lista de tarefas.

    Args:
        tasks (list): Lista de tarefas existentes.
        index (int): Índice da tarefa a ser atualizada na lista.
        task_name (str): Novo nome da tarefa.
        task_description (str): Nova descrição da tarefa.

    Returns:
        list: Lista de tarefas atualizada após a atualização da tarefa.
    """
    index = int(index) - 1
    if index >= 0 and index < len(tasks):
        tasks[index]["name"] = task_name
        tasks[index]["description"] = task_description
        print(f"Tarefa {index+1} atualizada para {task_name}")
        return tasks
    else:
        print("Índice de tarefas inválido.")
        return tasks
