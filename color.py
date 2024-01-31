def hex_to_rgb(value):
  value = value.lstrip('#')
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(value):
  return '#%02x%02x%02x' % value



hex = input('Enter hex: ').lstrip('#')
rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

new_hex = '#%02x%02x%02x' % rgb

print(f'Hex: {new_hex}')