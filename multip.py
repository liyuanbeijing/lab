import multiprocessing
import os

print(f'Process {os.getpid()} start...')

def func():
    print(f'Process {os.getpid()} start...')

p = multiprocessing.Process(target=func)
p.start()
p.join()

class MyProcess(multiprocessing.Process):
    def run(self):
        func()

p = MyProcess()
p.start()
p.join()