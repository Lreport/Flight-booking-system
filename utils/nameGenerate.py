from faker import Faker #tentar entender o por que esta alertando sobre a importação do Faker

def name_generate(quantity=250):
    fake = Faker()
    names = set()
    while len(names) < quantity:
        names.add(fake.name())

    return list(names)
