import re

def lambda_handler(event, context):
    idNum = event['queryStringParameters']['id_number']
    try:
        if (re.match(r"\d{13}$", idNum)):
            idNumList = list(map(int, idNum))
            checkSum = 10 - int(str((sum(idNumList[0:12:2])) + (sum(list(map(int, str(int("".join(map(str, idNumList[1::2]))) * 2))))))[1])
            if (checkSum == idNumList[12]):
                return ("valid")
        
        return ("invalid")
    
    except Exception as e:
        return ("invalid")