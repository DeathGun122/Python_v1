def get_phone(country, area, first, last):
    return f"+{country}-{area}-{first}-{last}"

phone_number = get_phone(country=1, area=800, first=555, last=1234)
print(phone_number)