from smartphone import Smartphone

catalog = [
    Smartphone('Apple', 'iPhone 16', '+79161234567'),
    Smartphone('Samsung', 'Galaxy S24', '+79001234567'),
    Smartphone('Xiaomi', 'Redmi Note 12 pro', '+79876543210'),
    Smartphone('OnePlus', '9 Pro', '+79109876543'),
    Smartphone('Google', 'Pixel 6', '+79012345678')
]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}')