HEX_COLORS = {'absolutezero': '#0048ba', 'acidgreen': '#b0bf1a', 'aliceblue': 'f0f8ff',
              'bitterlemon': '#cae00d', 'bittersweet': '#fe6f5e', 'camel': '#c19a6b', 'candyapplered': '#ff0800',
              'daffodil': '#ffff31', 'dimgray': '#696969', 'eggshell': '#f0ead6'}

print(HEX_COLORS)
hex_color = input("Enter color name: ").lower()
while hex_color != "":
    try:
        print(hex_color, "is", HEX_COLORS[hex_color])
    except KeyError:
        print("Invalid short state")
    hex_color = input("Enter short state: ").lower()
