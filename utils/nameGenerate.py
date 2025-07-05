from faker import Faker #tentar entender o por que esta alertando sobre a importação do Faker

def name_generate():
    fake = Faker()
    names = set()
    while len(names) < 250:
        names.add(fake.name())

    for name in names:
        print(name)

if __name__ == "__main__":
    name_generate()