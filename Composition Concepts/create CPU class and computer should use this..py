class CPU:
    def process(self):
        print("CPU is processing.")
class Computer:
    def start(self):
        self.cpu.process()
        print("Computer is running.")

    def __init__(self):
        self.cpu = CPU()      #Computer HAS-A CPU

c = Computer()
c.start()