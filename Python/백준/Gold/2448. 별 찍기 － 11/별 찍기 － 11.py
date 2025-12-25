N = int(input())

stars = [
    "  *  ",
    " * * ",
    "*****"
]

while len(stars) < N:
    height = len(stars)
    padding = ' ' * height
    top = [padding + star + padding for star in stars]
    bottom = [star + ' ' + star for star in stars]
    stars = top + bottom

print('\n'.join(stars))