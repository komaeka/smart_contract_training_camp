from brownie import SimpleStorage

def read_contract():
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve("Alice"))

def main():
    read_contract()