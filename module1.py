def xor_uncipher(string:str, key: str)->str:
    """Kodeeritud text dekodeeritakse
    """
    result=''
    temp=[]
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i]=chr(ord(key[j])^ord(temp[i]))
        result +=temp[i]
    return result


