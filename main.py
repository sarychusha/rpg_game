"""Текстовая игра "Герой и чудовища"."""
import random

global hp
global attack
global monster_counter

hp = random.randint(20, 40)
attack = random.randint(10, 25)
monster_counter = 0


def check_input(value: int) -> None:
    """Проверка, что пользователь ввел с клавиатуры."""
    if value == 1:
        print("Вы настоящий герой!")
    else:
        if value == 2:
            print("Это страх или тактика?")
        else:
            print(
                "Вы ввели неверное значение! Коль не трус ты, нажми 1 и сразись, а если хочешь сбежать - нажми 2"
            )
            new_value = int(input())
            check_input(new_value)


def fight(hp: int, attack: int) -> None:
    """Сцена боя."""
    hp_m = random.randint(7, 20)
    attack_m = random.randint(5, 10)

    print(
        "БОЙ! Вы встретили чудовище со здоровьем равным",
        hp_m,
        "и с силой удара",
        attack_m,
        "Коль не трус ты, нажми 1 и сразись, а если хочешь сбежать - нажми 2",
    )
    flag = int(input())
    check_input(flag)

    if flag == 1:
        while hp > 0 and hp_m > 0:
            hp -= attack_m
            hp_m -= attack

        if hp <= 0:
            print("ПОРАЖЕНИЕ! Может тебе пойти в ученики мага?")
            exit(0)

        global monster_counter

        if hp_m <= 0:
            monster_counter += 1
            print(
                "Ты победил монстра! Счетчик поверженных монстров равен",
                monster_counter,
            )

        if monster_counter == 10:
            print("ПОБЕДА! Ты выполнил свое задание, ты настоящий рыцарь!")
            exit(0)


def apple(hp: int) -> None:
    """Поедание яблока = добавление здоровья."""
    hp_apple = random.randint(5, 15)
    hp += hp_apple
    print("Ты нашел яблоко. Оно даст", hp_apple, "здоровья")
    print("Твое здоровье теперь равно", hp)


def sword(attack: int) -> None:
    """Нахождение нового меча."""
    sword_attack = random.randint(15, 49)
    print(
        "Ты нашел МЕЧ, он даст тебе",
        sword_attack,
        "атаки. Если хочешь забрать его, нажми 1, а если хочешь оставить - нажми 2",
    )
    flag = int(input())
    check_input(flag)
    if flag == 1:
        attack = sword_attack
        print("Твоя аттака теперь равна", attack)


def game() -> None:
    """Главная функция, сама игра."""
    print(
        "Приветствую, рыцарь. Твоя главная цель - защитить наше королевство и победить 10 монстров!"
    )
    print("Твое здоровье равно", hp)
    print("Твоя аттака равна", attack)

    while monster_counter < 10 and hp > 0:
        action = random.choice([fight, apple, sword])
        if action == fight:
            fight(hp, attack)

        if action == apple:
            apple(hp)

        if action == sword:
            sword(attack)


game()
