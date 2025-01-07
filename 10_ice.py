import math

def get_circle_length(radius):
    """Calculates the circumference of a circle given its radius."""
    result = 2 * math.pi * radius
    return round(result, 2)

def get_circle_area(radius):
    """Calculates the area of a circle given its radius."""
    result = math.pi * radius ** 2
    return round(result, 2)

# Example usage
print(f'Circle length (radius=10): {get_circle_length(10)}')
print(f'Circle area (radius=10): {get_circle_area(10)}')

def test(a, b, c, key=100):
    """Demonstrates argument passing."""
    print(a, b, c, key)

test(1, 2, 3)
test(1, 2, 3, key=10)

def get_icecream(volume, flavour='Vanilka'):
    """Prints the ice cream flavour and volume."""
    print(f'{flavour} Icecream {volume}')

get_icecream(100)
get_icecream(100, flavour='Chocolate')

# Print value of pi
print(f'Math pi value: {math.pi}')
