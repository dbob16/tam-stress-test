import mariadb
import os
from getpass import getpass
from configparser import ConfigParser

config = ConfigParser()

def init():
    host = input("Please insert hostname: [localhost] ")
    if host == "":
        host = "localhost"
    port = input("Please insert port number: [3306] ")
    if port == "":
        port = 3306
    else:
        try:
            port = int(port)
        except:
            print("Port is not a valid integer.")
            quit()
    user = input("Please insert username: ")
    password = getpass("Please insert password: ")
    database = input("Please insert database: ")
    config["database"] = {
        "host": host,
        "port": port,
        "user": user,
        "password": password,
        "database": database
    }

    try:
        global conn
        conn = mariadb.connect(
            host=config["database"]["host"],
            port=int(config["database"]["port"]),
            user=config["database"]["user"],
            password=config["database"]["password"],
            database=config["database"]["database"]
        )
        global cur
        cur = conn.cursor()
        with open("config.ini", "w") as file:
            config.write(file)
    except:
        print("Connection didn't work.")
        quit()

if os.path.isfile("config.ini"):
    try:
        config.read("config.ini")
        global conn
        conn = mariadb.connect(
            host=config["database"]["host"],
            port=int(config["database"]["port"]),
            user=config["database"]["user"],
            password=config["database"]["password"],
            database=config["database"]["database"]
        )
        global cur
        cur = conn.cursor()
    except:
        print("No/invalid config detected, let's try to create one.")
        init()
else:
    print("No/invalid config detected, let's try to create one.")
    init()

