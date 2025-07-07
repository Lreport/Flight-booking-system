from faker import Faker

def name_generate(quantity=250):
    fake = Faker()
    names = set()
    while len(names) < quantity:
        names.add(fake.name())

    return list(names)
