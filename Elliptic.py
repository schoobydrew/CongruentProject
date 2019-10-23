import argparse
def squaresModM(m):
    squares = []
    for i in range(m):
        squares.append((i**2)%m)
    return squares
def ellipticOutput(a, b, m):
    output = []
    for i in range(m):
        output.append((i**3 + a*i + b)%m)
    return output
def genPoints(squares, curve):
    points = []
    for idx, c in enumerate(curve):
        possibilities = [i for i,j in enumerate(squares) if j==c]
        for p in possibilities:
            points.append((idx,p))
    return points
#main
ap = argparse.ArgumentParser()
ap.add_argument("--a", required=True, type=int)
ap.add_argument("--b", required=True, type=int)
ap.add_argument("--field", required=True, type=int)
args = vars(ap.parse_args())
#print info
print("y^2 = x^3 + {}x + {} | over field mod {}".format(args["a"], args["b"], args["field"]))
print("-"*5)
print("Squares in the field are:")
squares = squaresModM(args["field"])
for i, j in enumerate(squares):
    print("\t{}: {}".format(i,j))
print("-"*5)
print("y^2 values for the function are:")
ellipticValues = ellipticOutput(args["a"], args["b"], args["field"])
for i, j in enumerate(ellipticValues):
    print("\t{}: {}".format(i,j))
print("The points on the curve are:")
points = genPoints(squares, ellipticValues)
for p in points:
    print("({}, {})".format(p[0], p[1]))
