def get_todos(filepath=r"C:\Users\rodho\PycharmProjects\PyCharm-Library\app1\todo_list.txt"):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=r"C:\Users\rodho\PycharmProjects\PyCharm-Library\app1\todo_list.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
