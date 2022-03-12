documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_doc_num():
    return input('Введи номер документа: ')


def choose_shelf():
    return input('Введи целевую полку для размещения: ')


def get_name_by_docs_number():
    """Команда, которая спросит номер документа и выведет имя человека"""
    docs_num = get_doc_num()
    flag = None  # 0, None, False
    for i in documents:
        if docs_num == i['number']:
            flag = False  # 1, True, 'fdsfsd'
            print(i['name'])

    # Аналогично: if flag == True, if flag is True
    if flag:
        print('Успешно!')

    # Аналогично: if flag == False, if flag is False
    if not flag:
        print('не то ввел')


def get_index_by_docs_number(docs_num=None):
    """Команда, которая спросит номер документа и выведет номер полки."""
    if not docs_num:
        docs_num = get_doc_num()

    flag = False
    for i, j in directories.items():
        if docs_num in j:
            flag = True
    if not flag:
        print('не то ввёл')
    return flag


def get_list_doc():
    """команда, которая выведет список всех документов."""
    for i in documents:
        print(i['type'], i['number'], i['name'])


def add_docs():
    """команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и
    номер полки, на котором он будет храниться. """
    add_shelf = str(int(input('Введи номер полки: ')))
    if directories.get(add_shelf):
        docs_num = get_doc_num()
        add_type = input('Введи тип документа: ')
        add_name = input('Введи имя: ')
        docs_list = directories[add_shelf]
        docs_list.append(docs_num)
        new_dict = {}
        new_dict.update({"type": add_type, "number": docs_num, "name": add_name})
        documents.append(new_dict)
        print(documents)
    else:
        print('не та полка')


def del_docs():
    """команда, которая спросит номер документа и удалит его из каталога и из перечня полок."""
    docs_num = get_doc_num()
    flag = False
    count_index = None
    for index, i in enumerate(documents):
        if docs_num == i['number']:
            flag = True
            count_index = index
    if count_index is not None:
        documents.pop(count_index)
        for i, j in directories.items():
            if docs_num in j:
                j.remove(docs_num)
                print('удалил')
        if not flag:
            print('не то ввёл')
    if not flag:
        print('не то ввел')


def move_docs():
    """команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую."""
    docs_num = get_doc_num()
    if get_index_by_docs_number(docs_num):

        for i, j in directories.items():
            # добавляем документ на новую полку.

            if docs_num in j:
                choose_shelf_temp = choose_shelf()
                if choose_shelf != i:
                    j.remove(docs_num)
                    print('удалил документ из старого списка')
                    directories.update({choose_shelf_temp: [docs_num]})
                    print(directories)
                else:
                    print('Документ уже есть на этой полке')
                break


def add_shelf_by_docs():
    choose_shelf_temp = choose_shelf()
    if not directories.get(choose_shelf_temp):
        directories.update({choose_shelf_temp: []})
        print(directories)
    #     хз что с этим ещё делать. Надо или нет добавлять просто номер документа на суще
    else:
        print('Не могу добавить в существующую полку')


function_map = {
    'p': get_name_by_docs_number,
    's': get_index_by_docs_number,
    'l': get_list_doc,
    'a': add_docs,
    'd': del_docs,
    'm': move_docs,
    'as': add_shelf_by_docs,
}


if __name__ == 'main':
    print(__name__)
    user_com = input('Введи команду: ')
    function = function_map.get(user_com)
    # 1 вариант вызова
    if function:
        function()

        # 2 вариант вызова
        # if user_com in function_map:
        #     function_map[user_com]()
    else:
        print('Не знаю такую команду')