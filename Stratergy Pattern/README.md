References:

- https://refactoring.guru/design-patterns/strategy
- https://www.youtube.com/watch?v=0mcP8ZpUR38
- https://github.com/ArjanCodes/2021-composition-vs-inheritance/blob/main/with_composition.py

## Why Stratergy Pattern?

In a sample population

Let's assume that they have three religions:

- A
- B
- C

each religion has a `pray method`

Let's assume that they have three job roles:

- Job1
- Job2
- Job3

each job has a `pay` method

Each person is associated with a religion and a job.
For each and every case we have to create a new object for every possible case.
Ex:

- A -> Job1. (A_With_Job1)
- A -> Job2. (A_With_Job2)
- B -> Job3. (B_With_Job3)
- C -> Job1. (C_With_Job1)

> What if we want to cover all the possible combinations ?
>
> What if there is a new Job4 (or) Jobless (or) a new religion (or) people are becoming atheist ?

See the [example.py](./example.py) for more clear understanding

Obeserve that we didn't need to create a new class for every possible combination, we use the classes that we need and construct our object followingly. This is called favour composition over inheritance.This can also be seen as dependency injection which can make our code decoupled and is easy to test.
