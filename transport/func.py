import json
#функ для добав клиента в список
def add_to_client_list(info):
    #чтение нынешнего списока клиентов из файла
    with open('transport/clients.json', "r", encoding='utf-8') as file:
        data = json.load(file)
        #добав новую инф о клиенте в список
    data.append(info)
    #Перезапись файла с обновленным списком клиентов
    with open('transport/clients.json', "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=True)
#функ для добавления транспорта в список транспорта
def add_to_transport_list(info):
    #чтение нынешнего списока транспорта из файла
    with open('transport/transport.json', "r", encoding='utf-8') as file:
        data = json.load(file)
         #добав новую инф о транспорте в список
    data.append(info)
    #Перезапись файла с обновленным списком транспорта
    with open('transport/transport.json', "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=True)
