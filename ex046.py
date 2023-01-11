from time import sleep
print('A contagem regressiva vai começar!!')
sleep(1)
for c in range(10, -1, -1):
    print('{}'.format(c))
    sleep(1)