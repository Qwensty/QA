from address import Address
from mailing import Mailing

# Создание адресов
to_address = Address('230000', 'Калининград', 'Майский переулок', '2', '333')
from_address = Address('190000', 'Санкт-Петербург', 'Невский пр.', '10', '5')

# Создание экземпляра Mailing
mailing = Mailing(to_address, from_address, 6000, '12345TRACK12345')

# Вывод информации о почтовом отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")