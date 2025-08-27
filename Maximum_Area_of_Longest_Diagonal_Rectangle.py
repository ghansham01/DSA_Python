dimensions = [[9, 3], [8, 6], [10, 1]]

max_dig =0
max_area = 0
for l,w in dimensions:
    diag_sq = l*l +w*w
    area = l*w

    if diag_sq > max_dig:
        max_dig = diag_sq
        max_area = area
    elif diag_sq == max_dig:
        max_area = max(max_area,area)

print(f"The area of the rectangle with the maximum diagonal is: {max_area}")

