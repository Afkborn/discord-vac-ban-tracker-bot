


def splitTextByLength(text, length):
    textLen = len(text)
    if textLen <= length:
        return [text]
    lines = text.split("\n")
    returnList = []
    returnList.append(f"{lines[0]}\n")
    lineCounter = 0
    for index, line in enumerate(lines):
        if index == 0:
            continue
        else: 
            if (len(returnList[lineCounter]) + len(line) + 1) <= length:
                returnList[lineCounter] = returnList[lineCounter] + f"{line}\n"
            else:
                lineCounter += 1
                returnList.append('')
    return returnList