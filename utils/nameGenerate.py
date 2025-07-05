from faker import Faker #tentar entender o por que esta alertando sobre a importação do Faker

def name_generate():
    fake = Faker()
    names = set()
    while len(names) < 250:
        names.add(fake.name())

    return list(names)
