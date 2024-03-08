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
    task = {"tarefa": task_name, "status": False, "descrição": task_description}
    tasks.append(task)
    print(f"Tarefa {task_name} adicionada com sucesso!")
    return tasks
