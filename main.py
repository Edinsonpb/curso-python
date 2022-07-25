from http import client
from setuptools import Command
import sys

clients = ["pablo","ricardo"]


def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients.append(client_name)
#        clients += client_name
#        _add_comma()
    else:
        print("client already is in the client's list")


def list_clients():
    for idx, client in enumerate(clients):
        print("{}: {}".format(idx, client))
#    global clients
#    print(clients)


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ",", updated_client_name + ",")
    else:
        print("client is not in clients list")


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ",", "")
    else:
        print("client is not in clients list")



def search_client(client_name):
    clients_list = clients.split(",")

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


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
    print("[S]earch client")


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input("what is the client name? ")

        if client_name == "exit":
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name

if __name__ == '__main__':
    _print_welcome()

    Command = input()
    Command = Command.upper()

    if Command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif Command == "D":
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif Command == "U":
        client_name = _get_client_name()
        updated_client_name = input("what is the updated client name? ")
        update_client(client_name, updated_client_name)
        list_clients()
    elif Command == "S":
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print("The client is in the client's list")
        else:
            print("the client: {} is not in our cient's list", format(client_name))
    else:
        print("Invalid command")