def distance(feet):
    inches = feet * 12
    yards = feet * 0.333333333
    miles = feet * 0.000189393939

    return inches, yards, miles

def start():
    while True:
        feet = float(input("Введіть відстань у футах: "))
        
        inches, yards, miles = distance(feet)

        print(f"{feet} футів = {inches} дюймів, {yards} ярдів та {miles} миль.")
        
        choice = input("Чи бажаєте конвертувати ще одну відстань? (так/ні): ").strip().lower()
        if choice == "ні":
            print("Конвертацію завершено.")
            break
        elif choice != "так":
            print("Невірний вибір. Конвертацію завершено.")
            break

start()