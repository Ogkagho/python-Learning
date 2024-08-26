# Mercator projection

#1.2.28

lambda_0 = int(input())
longitude = int(input())
latitude = int(input())

x = longitude - lambda_0
y = math.log((1 + math.sin(latitude)) / (1 - math.sin(latitude))) * 0.5

print(f'projection: (x, y) = ({x}, {y})')
