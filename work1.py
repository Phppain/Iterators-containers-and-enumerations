"""work1.py"""

def task1(arr: list) -> tuple:
    return {x: x**3 for x in arr if x % 2 != 0}

def task2(arr: list):
    return {x for x in arr if x % 2 == 0}

def task3():
    return [i * 10 for i in range(10)]

def task4(n: int):
    for i in range(0, n + 1):
        if i % 7 == 0:
            yield i 

if __name__ == "__main__":
    LST1 = [1, 2, 3, 4, 5, 6, 7]
    LST2 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
    print(task1(LST1), task2(LST2), task3(), sep="\n")
    N = int(input("Enter a num: "))
    for num in task4(N):
        print(num)
