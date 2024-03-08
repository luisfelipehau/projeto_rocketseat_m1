def list_tasks(tasks):
    """
    Lista as tarefas com seus respectivos índices, status, nome e descrição (se existir).

    Args:
        tasks (list): Lista de dicionários contendo informações das tarefas.
            Cada dicionário deve ter as chaves "name" e "status".
            A chave opcional "description" pode ser incluída para fornecer descrição da tarefa.
    """
    print("\nLista de tarefas:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["status"] else "-"
        name = task["name"]
        description = (" - " + task["description"]) if task.get("description") else ""
        print(f"{index}. [ {status} ] {name}{description}")
