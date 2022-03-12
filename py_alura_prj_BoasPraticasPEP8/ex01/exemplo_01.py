from typing_extensions import Self


class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def from_fullname(cls, fullname: str) -> Self:
        firstname, lastname = fullname.split(' ', 1)
        return cls(firstname, lastname)


def main():
    a1 = Person("Eduardo", "Ferreira")
    print(a1, a1.firstname)
    a2 = Person.from_fullname("Eduardo Ferreira")
    print(a2, a2.firstname)


if __name__ == '__main__':
    main()
