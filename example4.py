# for p in (True, False):
#     for q in (True, False):
#         print "%10s %10s %10s" % ( p, q, p and q)

for p in (True, False):
    for q in (True, False):
        print("{:10} {:10} {:10}".format(p, q, p and q))

# program ini memprint truth table dari p, q, p dan q

