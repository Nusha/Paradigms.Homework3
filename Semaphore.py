import threading


class TrainStation:
    def __init__(self):
        self.semaphore = threading.BoundedSemaphore(value=2)

    def arrive_train(self, train_name):
        self.semaphore.acquire()
        print(f'Поезд {train_name} прибыл на станцию')

    def depart_train(self, train_name):
        print(f'Поезд {train_name} ушел со станции')
        self.semaphore.release()


if __name__ == '__main__':
    station = TrainStation()
    threading.Thread(target=station.arrive_train, args=('A',)).start()
    threading.Thread(target=station.arrive_train, args=('B',)).start()
    threading.Thread(target=station.arrive_train, args=('C',)).start()
    threading.Thread(target=station.depart_train, args=('A',)).start()
    threading.Thread(target=station.depart_train, args=('B',)).start()
