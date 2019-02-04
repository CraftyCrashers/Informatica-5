huidig_invoer, queue = input('Geef het eerste invoer'), []
while huidig_invoer != 'STOP':
    if huidig_invoer == '?':
        if queue != []:
            print(queue[0])
            queue.pop(0)
    else:
        queue.append(huidig_invoer)
    huidig_invoer = input('Geef het invoer')
