import os
import pickle
products_in = [
    {
        "product":"Sichqoncha",
        "price":300000,
        "amount":100
    },
    {
        "product":"Keyboard",
        "price":160000,
        "amount":50
    },
    {
        "product":"Monitor",
        "price":1000000,
        "amount":80
    }
]

if not os.path.exists("database"):
    with open("database", "wb") as dfile:
        pickle.dump(products_in, dfile)


with open('database', "rb") as rfile:
    products_in = pickle.load(rfile)

def updateProductInfo():
    with open("database", "wb") as wfile:
        pickle.dump(products_in, wfile)


