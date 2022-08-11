def readFile(filename: str):
    with open(filename, "r") as newFile:
        return newFile.readlines()

def verifyStrings(filename: str):
    file = readFile(filename)
    file.pop(0)

    print(f"{filename.replace('.txt', '').capitalize()}")

    for line in file:
        line = line.replace("\n", "")

        index = 0
        isValid = False

        for letter in line:
            if letter == "a" or letter == "b":
                if letter == "a":
                    if index == len(line):
                        isValid = False
                        break

                    if line[index + 1] == "b" and line[index + 2] == "b":
                        isValid = True
                    else: 
                        isValid = False
                        break
            else:
                isValid = False
                break

            index += 1
            
        print(f"{line}: {'pertence' if isValid else 'não pertence'}")
    print("\n")

verifyStrings("entrada.txt")
verifyStrings("entrada2.txt")
verifyStrings("entrada3.txt")
