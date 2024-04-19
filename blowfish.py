import struct

def generate_subkeys(key):
    # Initialize P-box and S-boxes
    P = [0] * 18
    S = [[0] * 256 for _ in range(4)]

    # Load P-box with initial P-array values
    for i in range(18):
        P[i] = struct.unpack(">I", key[4 * i % len(key): 4 * i % len(key) + 4].ljust(4, b'\0'))[0]

    # Load S-boxes with the base64-derived values
    base64_values = [
        0x243f6a88, 0x85a308d3, 0x13198a2e, 0x03707344,
        0xa4093822, 0x299f31d0, 0x082efa98, 0xec4e6c89,
        0x452821e6, 0x38d01377, 0xbe5466cf, 0x34e90c6c,
        0xc0ac29b7, 0xc97c50dd, 0x3f84d5b5, 0xb5470917
    ]

    for i in range(4):
        for j in range(256):
            S[i][j] = (base64_values[i] >> (24 - (j % 4) * 8)) & 0xFF

    # Initialize the three key-dependent 32-bit Blowfish S-boxes
    return P, S

# Dynamic input
key = b"my32bitkey"

P, S = generate_subkeys(key)

print("P-box:", P)
print("S-boxes:")
for i, sbox in enumerate(S):
    print("S-box", i, ":", sbox)
