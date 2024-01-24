variables = {}


def get_instruction(code_line: str) -> dict:
    instruction = {}

    # Если в строке кода содержится оператор присваивания
    if ":=" in code_line:
        # Разрезаем строку кода по пробелам
        # Затем извлекаем из неё имя переменной и значение
        components = code_line.split(" ")
        variable_name = components[0]
        value = int(components[2])
        instruction = {"operation": "assign", "variable_name": variable_name, "value": value}
    elif ">" in code_line or "<" in code_line or "==" in code_line or "!=":
        result = False
        left = components[0]
        right = components[2]
        if components[1] == ">":
            result = left > right
            compare_type = 'greater' 
        elif components[1] == "<":
            result = left < right
            compare_type = 'less'
        elif components[1] == "==":
            result = left == right
            compare_type = 'equal'
        elif components[1] == "!=":
            result = left != right
            compare_type = 'not_equal' 
            
            
    
    instruction = {"operation": "compare", "compare_type": compare_type, "result": result }
    return instruction


def execute(code_line: str) -> None:
    instruction = get_instruction(code_line)

    # Если операция - присваивание
    if instruction["operation"] == "assign":
        # Достаём из массива имя переменной и значение
        variable_name = instruction["variable_name"]
        value = instruction["value"]

        # Обращаемся к глобальному словарю переменных, 
        # записываем по имени переменной соответствующее значение
        variables[variable_name] = value


if __name__ == '__main__':
    print("Вас приветствует консоль! Удивительно, не правда ли? Вводите команды.")
    # Бесконечно просим пользователя вводить команды и исполняем их
    while True:
        command = input(">>> ")
        execute(command)
