from http import client
from setuptools import Command


clients = "pablo,ricardo,"


def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print("client already is in the client's list")


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ",", updated_client_name + ",")
    else:
        print("client is not in clients list")


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ","


def _print_welcome():
    print("Welcome to platzi ventas")
    print("*" * 50)
    print("what would you like to do today?")
    print("[C]reate client")
    print("[D]elete client")
    print("[U]pdate client")

def _get_client_name():
    return input("what is the client name? ")

if __name__ == '__main__':
    _print_welcome()

    Command = input()
    Command = Command.upper()

    if Command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif Command == "D":
        pass
    elif Command == "U":
        client_name = _get_client_name()
        updated_client_name = input("what is the updated client name? ")
        update_client(client_name, updated_client_name)
        list_clients()
    else:
        print("Invalid command")