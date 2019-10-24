import argparse
def squaresModM(m):
    squares = [(i**2)%m for i in range(m)]
    return squares
def ellipticOutput(a, b, m):
    output = [(i**3 + a*i + b)%m for i in range(m)]
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
print("Determinant 4*{}^3 + 27*{}^2".format(args["a"], args["b"]))
assert (4*(args["a"]**3) + 27*(args["b"]**2))%args["field"], "Determinant failed"
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
print("-"*5)
print("The points on the curve are: \n\tInfinity")
points = genPoints(squares, ellipticValues)
for p in points:
    print("\t({}, {})".format(p[0], p[1]))
print("-"*5)
print("Outputting table to EllipticTableA_{}B_{}M_{}.csv".format(args["a"], args["b"], args["field"]))
# f = open("EllipticTableA_{}B_{}M_{}.csv".format(args["a"], args["b"], args["field"]), w+)
