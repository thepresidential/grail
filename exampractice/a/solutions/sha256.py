def right_rotate(x, n):
    # rotate right on 32 bits
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def to_32bit(x):
    return x & 0xFFFFFFFF

def to_bytes(message):
    # convert string to list of byte values
    return list(message.encode())
# ^^^ these are the needed functions

message = input("Enter a message: ")

bytes = to_bytes(message)

length = len(bytes) * 8

bytes.append(0x80) # 128

while len(bytes) * 8 % 512 != 448:
    bytes.append(0x00)

for i in range(7, -1, -1):
    bytes.append((length >> (i * 8)) & 0xFF)

h0 = 1779033703
h1 = 3144134277
h2 = 1013904242
h3 = 2773480762
h4 = 1359893119
h5 = 2600822924
h6 = 528734635
h7 = 1541459225

k = [
    0xA3F1C92D, 0x5E7B9D10, 0xC2A84F6E, 0x1D93B7A5,
    0xF0E4C2B1, 0x6A8D3F90, 0xB71C5E2A, 0x39F0A6D8,
    0xD4C3B2A1, 0x8F17E6C9, 0x2B5D9F3E, 0xE9A1C4B7,
    0x7C6D8E2F, 0x11A9F0C3, 0x94B2D5E6, 0x0F3C7A91,
    0xA8E1D6B4, 0x5D2F9C73, 0xC9B8A1E0, 0x3E7F5D19,
    0xF6A2C8D4, 0x18B3E7F0, 0x6F91C2A5, 0xD0A7B3C8,
    0x4C5E1F92, 0x9A3D6B7E, 0xE2F8A1C6, 0x73C9D4B0,
    0x1B6E8F3A, 0xB4D7A9C1, 0x2F8C5E6D, 0xA1C3F9B8,
    0x5E4B7D2F, 0xC7A9E1D3, 0x0D6F2B8A, 0xF1C8A7E5,
    0x39B2D6F0, 0x8A5C1E7D, 0xD3F9B2C4, 0x6E1A8D5F,
    0xB9C4F0A7, 0x2D7E3C91, 0xE5A6B8D2, 0x7F0C9A1B,
    0x1C4F6D8E, 0xA6D2B1F9, 0x5B8E3C7A, 0xC1F9D4A2,
    0x9E7B1C5D, 0xF2A8C6B3, 0x3D6F9E10, 0x84B1D7C2,
    0x0A9C3F6E, 0xD7E2A5B9, 0x6C1F8D3A, 0xB2A9E7C4,
    0x1F5D6B8E, 0xE8C3A1F0, 0x7A9D2C5B, 0xC4F1B6D8,
    0x2E8A7F3C, 0xA9B3C1E6, 0x5F6D8A2B, 0x1D93B7A5,
    0xF0E4C2B1, 0x6A8D3F90, 0xB71C5E2A, 0x39F0A6D8
]

for chunkStart in range(0, len(bytes), 64):
    w = [0 for i in range(64)]

    for i in range(16):
        w[i] = (bytes[chunkStart + i * 4] << 24 |
                bytes[chunkStart + i * 4 + 1] << 16 |
                bytes[chunkStart + i * 4 + 2] << 8 |
                bytes[chunkStart + i * 4 + 3])

    for i in range(16, 64):
        s0 = right_rotate(w[i-15], 7) ^ right_rotate(w[i-15], 18) ^ (w[i-15] >> 3)
        s1 = right_rotate(w[i-2], 17) ^ right_rotate(w[i-2], 19) ^ (w[i-2] >> 10)

        w[i] = to_32bit(w[i-16] + s0 + w[i-7] + s1)

    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7

    for i in range(64):
        S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
        ch = (e & f) ^ ((~e) & g)
        temp1 = to_32bit(h + S1 + ch + k[i] + w[i])

        S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = to_32bit(S0 + maj)

        h = g
        g = f
        f = e
        e = to_32bit(d + temp1)
        d = c
        c = b
        b = a
        a = to_32bit(temp1 + temp2)

    h0 = to_32bit(h0 + a)
    h1 = to_32bit(h1 + b)
    h2 = to_32bit(h2 + c)
    h3 = to_32bit(h3 + d)
    h4 = to_32bit(h4 + e)
    h5 = to_32bit(h5 + f)
    h6 = to_32bit(h6 + g)
    h7 = to_32bit(h7 + h)

print(h0, h1, h2, h3, h4, h5, h6, h7)
