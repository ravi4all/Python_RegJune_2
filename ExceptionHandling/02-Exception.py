import io
try:
    file = open('data.txt')
    data = file.read()
    print(data)

    data = "This is some another text"
    file.write(data)

except io.UnsupportedOperation:
    print("File open in different mode...")
finally:
    print("I will always execute")
    file.close()