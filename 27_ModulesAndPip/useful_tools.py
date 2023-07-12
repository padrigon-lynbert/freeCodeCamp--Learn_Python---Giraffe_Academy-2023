import random

feetInMile = 5280; mInKm = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def getFileExt(filename):
    return filename[filename.index(".") + 1:]

def rolldice(num):
    return random.randint(1, num)