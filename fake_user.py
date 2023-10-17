from faker import Faker


class FakeUserGenerator:
    # Генерация случайных пользовательских данных
    def __init__(self):
        self.fake = Faker()
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.postcode = self.fake.postcode()


def generate_fake_user():
    # Генерация пользовательских данных
    generated_user = FakeUserGenerator()
    return generated_user
