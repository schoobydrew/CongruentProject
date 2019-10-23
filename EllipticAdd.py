def EllipticAddition(P1, P2, A, B, m):
    if P1 == "Inf":
        return P2
    if P2 == "Inf":
        return P1
    x1 = P1[0]
    y1 = P1[1]
    x2 = P2[0]
    y2 = P2[1]
    if (x1 == x2) and (y1 == -y2):
        return "Inf"
    #define lambda
    if (P1 == P2):
        num = 3*(x1**2) + A
        den = pow(2*y1, m-2, m)
        l = (num*den)%m
    else:
        num = y2-y1
        den = pow(x2-x1, m-2, m)
        l = (num*den)%m
    x3 = (l**2-x1-x2)%m
    y3 = (l*(x1-x3)-y1)%m
    return (x3, y3)
