def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f'{kwargs.get('street')} {kwargs.get('apt')}')
    elif "pobox" in kwargs:
        print(f'{kwargs.get('street')}')
        print(f'P.O. Box {kwargs.get('pobox')}')
    else:
        print(f'{kwargs.get('street')}')
    print(f'{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}')

shipping_label(
    "Dr.", "Spongebob", "Squarepants", "III", 
    street="123 Ocean Avenue",
    city="Bikini Bottom", 
    state="Pacific Ocean", 
    zip="12345"
)