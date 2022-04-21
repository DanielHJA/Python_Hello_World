# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Person import Person


def print_hi(people):
    for person in people:
        print(person.firstname + " " + person.lastname)
        print(person.firstname + "'s age is" + " " + str(person.age))
        if person.age > 21:
            print("So old")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    person1 = Person("Harald", "Hammar", 22)
    person2 = Person("Sigge", "Ström", 23)
    person3 = Person("Sigurd", "Svensson", 24)
    people = [person1, person2, person3]
    print_hi(people)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
