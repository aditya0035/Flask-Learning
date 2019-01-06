def CharacterLimit(string,noOfCharacterreq=10):
    if len(string)>11:
        return f'{string[0:(noOfCharacterreq+1)]}...'
    else:
        return string
