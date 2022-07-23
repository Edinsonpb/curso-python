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


if __name__ == '__main__':
    _print_welcome()

    Command = input()

    if Command == "C":
        client_name = input("what is the client name? ")
        create_client(client_name)
        list_clients()
    elif Command == "D":
        pass
    else:
        print("Invalid command")