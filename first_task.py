import time

class WashingMachine():
    def start(self):
        print("Пральна машина запущена.")
        self.state = "Заповнення водою"
        self.fill_water()
        
    def fill_water(self):
        print(f"Стан: {self.state}: Машина заповнюється водою.")
        time.sleep(3)
        self.state = "Прання"
        self.wash()

    def wash(self):
        print(f"Стан: {self.state}: Прання в процесі.")
        time.sleep(5)
        self.state = "Полоскання"
        self.rinse()

    def rinse(self):
        print(f"Стан: {self.state}: Полоскання в процесі.")
        time.sleep(4)
        self.state = "Віджимання"
        self.spin()

    def spin(self):
        print(f"Стан: {self.state}: Віджимання в процесі.")
        time.sleep(3)
        self.finish()

    def finish(self):
        self.state = "Завершено"
        print("Прання завершено.")
        self.restart_option()

    def restart_option(self):
        while True:
            choice = input("Чи бажаєте запустити машину знову? (так/ні): ").strip().lower()
            if choice == "так":
                self.start()
                break
            elif choice == "ні":
                print("Машина зупинена.")
                break
            else:
                print("Невірний вибір. Будь ласка, введіть 'так' або 'ні'.")

washing_machine = WashingMachine()
washing_machine.start()