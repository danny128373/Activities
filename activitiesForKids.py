def runs(*kids):
    for kid in kids:
        print(f'{kid} ran like a fool')


def swings(*kids):
    for kid in kids:
        print(f'{kid} swings like a fool')


def slides(*kids):
    for kid in kids:
        print(f'{kid} slides like a fool')


def hide_and_seeks(*kids):
    for kid in kids:
        print(f'{kid} hide and seeks like a fool')


runs("Joe", "Jenna")
slides("Joe", "Jenna")
swings("Joe", "Jenna")
hide_and_seeks("Joe", "Jenna")

runs("Pam", "Sam", "Andrea", "Will")
slides("Pam", "Sam", "Andrea", "Will")
swings("Pam", "Sam", "Andrea", "Will")
hide_and_seeks("Pam", "Sam", "Andrea", "Will")
