def add_task(tasks, task_name, task_description):
    # Estrutura da tarefa: keys -> name, description e status
    task = {"tarefa": task_name, "status": False, "descrição": task_description}
    tasks.append(task)
    print(f"Tarefa {task_name} adicionada com sucesso!")
    return tasks
