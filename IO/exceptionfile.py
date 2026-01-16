try:
    with open("dat.txt", "r") as file:
        data = file.read()
        print(data)

except IOError as e:
    print("file not found",e)
finally:
    print("executed succesfully")

