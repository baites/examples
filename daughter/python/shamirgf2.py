import random
import argparse

# === Huffman Codebook ===
HUFFMAN_CODEBOOK = {
    'E': '001',
    ' ': '110',
    'R': '0000',
    'H': '0001',
    'S': '0100',
    'N': '0101',
    'I': '0110',
    'O': '0111',
    'A': '1010',
    'T': '1110',
    'L': '10001',
    'D': '10110',
    'P': '100000',
    'Y': '100110',
    'G': '100111',
    'F': '101110',
    'M': '101111',
    'W': '111100',
    'U': '111110',
    'C': '111111',
    'V': '1001011',
    'B': '1111011',
    '3': '10000101',
    '0': '10000110',
    '5': '10000111',
    '4': '10010000',
    '9': '10010001',
    '8': '10010010',
    '7': '10010011',
    '2': '10010100',
    '1': '10010101',
    '6': '11110100',
    'K': '11110101',
    'Z': '1000010000',
    'Q': '1000010001',
    'X': '1000010010',
    'J': '1000010011',
}
REVERSE_CODEBOOK = {v: k for k, v in HUFFMAN_CODEBOOK.items()}

# === Encoding and decoding ===
def encode(text: str) -> str:
    text = text.upper()
    try:
        return ''.join(HUFFMAN_CODEBOOK[ch] for ch in text)
    except KeyError as e:
        raise ValueError(f"Unsupported character: {e.args[0]}")

def decode(code: str) -> str:
    result = []
    buffer = ''
    for index in range(len(code)):
        buffer += code[index]
        if buffer in REVERSE_CODEBOOK:
            result.append(REVERSE_CODEBOOK[buffer])
            buffer = ''
    # Buffer is not reset and run through all message
    # means the code string is incomplete.
    if buffer != '' and index == len(code):
        raise ValueError("Incomplete code string: cannot fully decode.")
    return ''.join(result)

# === Secret sharing over GF(2) ===
def xor_strings(a: str, b: str) -> str:
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def pad_to_match_length(source: str, target_length: int) -> str:
    repeat_times = (target_length + len(source) - 1) // len(source)
    return (source * repeat_times)[:target_length]

def share_secret(secret: str, random_bits: str = None) -> tuple[str, str]:
    if random_bits is None:
        r = ''.join(random.choice('01') for _ in secret)
    else:
        r = pad_to_match_length(random_bits, len(secret))
    s2 = xor_strings(secret, r)
    return r, s2

def recover_secret(share1: str, share2: str) -> str:
    return xor_strings(share1, share2)

# === Main logic ===
def run_shamir_encoder(message1: str, message2: str = None):
    encoded1 = encode(message1)
    print(f"Original Message 1   : {message1}")
    print(f"Encoded Message      : {encoded1}")

    if message2:
        encoded2 = encode(message2)
        print(f"Original Message 2   : {message2}")
        print(f"Used as Random Binary: {encoded2}")
        share1, share2 = share_secret(encoded1, encoded2)
    else:
        share1, share2 = share_secret(encoded1)

    print(f"Share 1              : {share1}")
    print(f"Share 2              : {share2}")

    recovered = recover_secret(share1, share2)
    print(f"Recovered Binary     : {recovered}")

    decoded = decode(recovered)
    print(f"Decoded Message      : {decoded}")


# === CLI ===
def main():
    parser = argparse.ArgumentParser(description="Huffman + GF(2) Secret Sharing Encoder")
    parser.add_argument("message1", type=str, help="First message (secret)")
    parser.add_argument("message2", nargs="?", default=None, help="Optional second message to use as share (randomness)")
    args = parser.parse_args()

    run_shamir_encoder(args.message1, args.message2)

if __name__ == "__main__":
    main()
