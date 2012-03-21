import pickle

def recover():
  with open("dbinfo","rb") as f:
    unpickler = pickle.Unpickler(f)

    info = unpickler.load()

    return info

def create():
  with open("dbinfo","wb") as f:
    pickler = pickle.Pickler(f)

    info = dict()

    info["host"] = raw_input("Enter your hostname: ")

    port = raw_input("Enter your port number (leave blank for 3306): ")
    info["port"] = 3306 if port == "" else int(port)

    info["user"] = raw_input("Enter your username: ")

    info["passwd"] = raw_input("Enter your password: ")

    info["db"] = raw_input("Enter your database: ")

    pickler.dump(info)

def main():
  create()

if __name__ == "__main__":
  main()