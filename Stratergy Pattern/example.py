from dataclasses import dataclass
from datetime import date, datetime

from Religion import Religion
from Religion import AReligion, BReligion

from Job import Job
from Job import Job1, Job2


@dataclass
class Person:
    name: str
    date_of_birth: date
    religion: Religion
    job: Job

    def compute_pay(self) -> None:
        print(f"Paid to the employee: {self.job.pay()}")

    def pray(self) -> None:
        print(f"{self.religion.pray()}")


def pray_and_compute_pay(person: Person) -> None:
    person.pray()
    person.compute_pay()
    print()


def main() -> None:
    a_religion = AReligion()
    b_religion = BReligion()

    job_1 = Job1()
    job_2 = Job2()

    # Creating the person objects

    person1 = Person(
        name="1",
        date_of_birth=datetime(2023, 10, 20),
        religion=a_religion,
        job=job_1
    )

    person2 = Person(
        name="2",
        date_of_birth=datetime(2020, 11, 20),
        religion=b_religion,
        job=job_1
    )

    person3 = Person(
        name="3",
        date_of_birth=datetime(2021, 7, 11),
        religion=a_religion,
        job=job_2
    )

    for person in [person1, person2, person3]:
        pray_and_compute_pay(person)


if __name__ == "__main__":
    main()
