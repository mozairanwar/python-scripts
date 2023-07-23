def defangIPaddr(address: str) -> str:
    return address.replace(".","[.]")

address = "255.100.50.0"
print(defangIPaddr(address))