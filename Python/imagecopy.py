file = open("fil.jpg", "wb")
with open("fortnite.jpg", "rb") as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        file.write(byte)

