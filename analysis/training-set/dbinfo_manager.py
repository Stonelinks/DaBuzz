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
    info["port"] = raw_input("Enter your port number: ")
    info["user"] = raw_input("Enter your username: ")
    info["password"] = raw_input("Enter your password: ")

    pickler.dump(info)

def main():
  create()

if __name__ == "__main__":
  main()