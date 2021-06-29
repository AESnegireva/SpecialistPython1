promt="если хочешь прекратить мою работу введи stop"
message=""
while message!='stop':
    message=input(promt)
    if message != 'stop':
        print(message)
