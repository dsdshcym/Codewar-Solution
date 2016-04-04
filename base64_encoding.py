import string

BASE64_INDEX_TABLE = ''.join([string.ascii_uppercase,
                              string.ascii_lowercase,
                              string.digits,
                              '+',
                              '/'])

def int_to_n_bits(x, n):
    return bin(x)[2:].rjust(n, '0')

def plain_char_to_bit_pattern(char):
    return int_to_n_bits(ord(char), 8)

def split_string_in_fixed_length(string, length):
    return [string[i: i+length] for i in range(0, len(string), length)]

def bit_pattern_to_encoded_char(bits):
    return BASE64_INDEX_TABLE[int(bits, 2)]

def bits_to_base_64(bits):
    padded_bits = bits.ljust(24, '0')
    results = ''.join(map(bit_pattern_to_encoded_char,
                          split_string_in_fixed_length(padded_bits, 6)))
    equal_sign_counts = (len(padded_bits) - len(bits)) // 6
    return ''.join(results[:len(results)-equal_sign_counts])

def to_base_64(string):
    bit_pattern = ''.join(map(plain_char_to_bit_pattern,
                              string))
    return ''.join(map(bits_to_base_64,
                       split_string_in_fixed_length(bit_pattern, 24)))

def encoded_char_to_bit_pattern(char):
    return int_to_n_bits(BASE64_INDEX_TABLE.index(char), 6)

def decode_8_bits(bits):
    if len(bits) != 8:
        return ""
    return chr(int(bits, 2))

def decode_4_chars(encoded_4_chars):
    encoded_chars = encoded_4_chars.replace("=", "")
    bit_pattern = ''.join(map(encoded_char_to_bit_pattern,
                              encoded_chars))
    return ''.join(map(decode_8_bits,
                       split_string_in_fixed_length(bit_pattern, 8)))

def from_base_64(string):
    return ''.join(map(decode_4_chars,
                       split_string_in_fixed_length(string, 4)))
