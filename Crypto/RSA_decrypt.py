import math

def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def main():

    p = 21094081
    q = 99363191
    ct = "875597732337885 1079270043421597 616489707580218 2010079518477891 1620280754358135 616660320758264 86492804386481 171830236437002 1500250422231406 234060757406619 1461569132566245 897825842938043 2010079518477891 234060757406619 1620280754358135 2010079518477891 966944159095310 1669094464917286 1532683993596672 171830236437002 1461569132566245 2010079518477891 221195854354967 1500250422231406 234060757406619 355168739080744 616660320758264 1620280754358135"
    ctr = ct.split()
    e = 5449
    n = p*q

    # compute n
    n = p * q

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    d = getModInverse(e, phi)

    print("n:  " + str(d))

    # Decrypt ciphertext
    res = "gigem{"
    for i in ctr:
        pt = pow(int(i), d, n)
        res = res + str(chr(pt))
    print("pt: " + res + "}")

if __name__ == "__main__":
    main()
