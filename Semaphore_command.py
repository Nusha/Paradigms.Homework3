# Команда (Command): превращает запрос в объект, содержащий информацию о запросе.
# Пример с желкзнодорожным семафором

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Классы конкретных команд
class RedLightCommand(Command):
    def __init__(self, semaphore):
        self.semaphore = semaphore

    def execute(self):
        self.semaphore.set_light("Остановка")


class YellowLightCommand(Command):
    def __init__(self, semaphore):
        self.semaphore = semaphore

    def execute(self):
        self.semaphore.set_light("Движение с малой скоростью")


class GreenLightCommand(Command):
    def __init__(self, semaphore):
        self.semaphore = semaphore

    def execute(self):
        self.semaphore.set_light("Движение без ограничений")


class Semaphore:
    def set_light(self, status):
        print("Семафор показывает: " + status)


class SemaphoreController:
    def __init__(self, green, yellow, red):
        self.green_light_command = green
        self.yellow_light_command = yellow
        self.red_light_command = red

    def set_green_light(self):
        self.green_light_command.execute()

    def set_yellow_light(self):
        self.yellow_light_command.execute()

    def set_red_light(self):
        self.red_light_command.execute()


if __name__ == '__main__':
    semaphore = Semaphore()

    red_light_command = RedLightCommand(semaphore)
    yellow_light_command = YellowLightCommand(semaphore)
    green_light_command = GreenLightCommand(semaphore)

    semaphore_controller = SemaphoreController(green_light_command, yellow_light_command, red_light_command)

    semaphore_controller.set_green_light()
    semaphore_controller.set_yellow_light()
    semaphore_controller.set_red_light()
