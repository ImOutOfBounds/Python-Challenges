import json

# Open JSON with morse dictionary
with open('./morse.json', 'r') as arquivo:
    data = json.load(arquivo)


message = input("insert message to be encoded: ")

if message == "":
    # This will be shown if the input is null.
    message = "sou uma frase morse"

messageList = message.split(" ")
res = ""

for i in range(len(messageList)):
    currentWord = list(messageList[i])
    for j in currentWord:
        res += data["encode"][j] + " "
        
    res += "  "

print("your message: " + message + " means: " + res)