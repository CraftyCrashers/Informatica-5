def yiq(rgb):
    y, i, q = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2], 0.596 * rgb[0] + (-0.274 * rgb[1]) + (-0.322 * rgb[2]),
               0.211 * rgb[0] - 0.523 * rgb[1] + 0.312 * rgb[2])
    y, i, q = round(y, 4), round(i, 4), round(q, 4)
    return y, i, q
