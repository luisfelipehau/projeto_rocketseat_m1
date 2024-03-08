def list_tasks(tasks):
    print("\nLista de tarefas:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["status"] else "🚫"
        name = task["name"]
        description = (
            (" - " + task["description"])
            if "description" in task and task["description"]
            else ""
        )
        # print(f"{index}. [ {status} ] {name}")
        print(f"{index}. [ {status} ] {name}{description}")
