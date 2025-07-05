from faker import Faker #tentar entender o por que esta alertando sobre a importação do Faker


fake = Faker()
names = set()
while len(names) < 250:
    names.add(fake.name())

for name in names:
    print(name)

print("Total names generated:", len(names))