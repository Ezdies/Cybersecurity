def get_points(a, b, p):
    points = []
    for x in range(p):
        for y in range(p):
            if (y**2) % p == (x**3 + a*x + b) % p:
                points.append((x, y))
    return points

def add_points(P, Q, a, p):
    # Punkt na nieskończoności (punkt zerowy)
    if P is None:
        return Q
    if Q is None:
        return P
    
    x1, y1 = P
    x2, y2 = Q

    # Jeśli punkty są przeciwne (ich suma to punkt na nieskończoności)
    if (x1 == x2) and (y1 == (-y2 % p)):
        return None
    
    # Jeśli punkty są różne
    if P != Q:
        try:
            # Oblicz nachylenie prostej s
            s = ((y2 - y1) * pow(x2 - x1, p - 2, p)) % p
        except ZeroDivisionError:
            return None  # Jeśli dzielenie przez zero, zwróć punkt na nieskończoności
        x3 = (s * s - x1 - x2) % p
        y3 = (s * (x1 - x3) - y1) % p
        return (x3, y3)
    
    # Jeśli punkty są takie same (podwojenie punktu)
    else:
        if y1 == 0:
            return None  # Punkt podwojony to punkt na nieskończoności
        # Oblicz nachylenie s dla podwojenia punktu
        s = ((3 * x1**2 + a) * pow(2 * y1, p - 2, p)) % p
        x3 = (s**2 - 2 * x1) % p
        y3 = (s * (x1 - x3) - y1) % p
        return (x3, y3)
        
        
    
            
print(get_points(2, 3, 13))
R1 = ((10,3), (12,0), 2, 13)
R2 = (None, None, 2, 13)
R3 = (None, (12,0), 2, 13)
R4 = ((10,3), None, 2, 13)
R5 = ((2,3), (2,3), 2, 13)
R6 = ((1,2), (1, -2 % 13), 2, 13)
print(add_points((10, 3), (12, 0), 2, 13))
print(add_points((3, 7), (4, 7), 2, 13))
print(add_points((7, 10), (3, 6), 2, 13))
print(add_points((0, 4), (11, 11), 2, 13))
print(add_points((6, 6), (6, 6), 2, 13))
print(add_points((6, 6), (11, 11), 2, 13))
print(add_points((7, 10), (7, 3), 2, 13))
print(add_points((9, 3), (9, 10), 2, 13))

