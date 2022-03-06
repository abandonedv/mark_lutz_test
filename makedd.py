from marc58 import Person, Manager
import shelve

db = shelve.open("persondb")
wdyw = int(input("Введите 0, если хотите очистить...\n"))
if wdyw == 0:
    db.clear()
    print("cleared")
elif wdyw == 1:
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=10000)
    tom = Manager("Tom Jones", 50000)
    for obj in (bob, sue, tom):
        db[obj.name] = obj
    print("filled")
elif wdyw == 2:
    for key in sorted(db):
        print(key, "\t=>", db[key])

    sue = db["Sue Jones"]
    sue.giveraise(13)
    db["Sue Jones"] = sue
db.close()
