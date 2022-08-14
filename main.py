import email
from http import client
from turtle import position
from unicodedata import name
from attr import field
from setuptools import Command
import sys
import csv
import os

CLIENT_TABLE = ".clients.csv"
CLIENT_SCHEMA = ['name','company','email','position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENT_TABLE)

    os.rename(tmp_table_name, CLIENT_TABLE)


"""
clients = [
    {
        "name": "Pablo",
        "company": "Google",
        "email": "pablo@google.com",
        "position": "software engineer",
    },
    {
        "name": "Ricardo",
        "company": "Facebook",
        "email": "ricardo@facebook.com",
        "position": "data engineer",
    }
]
"""

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
        print("{uid} | {name} | {company} | {email} | {position}".format(
            uid=idx,
            name=client["name"],
            company=client["company"],
            email=client["email"],
            position=client["position"]
        ))
#    global clients
#    print(clients)


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
#        clients = clients.replace(client_name + ",", updated_client_name + ",")
    else:
        print("client is not in clients list")


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
#        clients = clients.replace(client_name + ",", "")
    else:
        print("client is not in clients list")


def search_client(client_name):
#    clients_list = clients.split(",")

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


#def _add_comma():
#    global clients
#    clients += ","


def _print_welcome():
    print("Welcome to platzi ventas")
    print("*" * 50)
    print("what would you like to do today?")
    print("[C]reate client")
    print("[L]ist clients")
    print("[D]elete client")
    print("[U]pdate client")
    print("[S]earch client")


def _get_client_field(field_name):
    field = None

    while not field:
        field = input("What is the client {}?".format(field_name))
    return field


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
    _initialize_clients_from_storage()

    _print_welcome()

    Command = input()
    Command = Command.upper()

    if Command == "C":
        client = {
            "name": _get_client_field("name"),
            "company": _get_client_field("company"),
            "email": _get_client_field("email"),
            "position": _get_client_field("position"),
        }

#        client_name = _get_client_name()
        create_client(client)
#        list_clients()
    elif Command == "L":
        list_clients()
    elif Command == "D":
        client_name = _get_client_name()
        delete_client(client_name)
#        list_clients()
    elif Command == "U":
        client_name = _get_client_name()
        updated_client_name = input("what is the updated client name? ")
        update_client(client_name, updated_client_name)
#        list_clients()
    elif Command == "S":
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print("The client is in the client's list")
        else:
            print("the client: {} is not in our cient's list", format(client_name))
    else:
        print("Invalid command")

    _save_clients_to_storage()