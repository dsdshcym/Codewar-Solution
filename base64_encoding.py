import string

BASE64_INDEX_TABLE = ''.join([string.ascii_uppercase,
                              string.ascii_lowercase,
                              string.digits,
                              '+',
                              '/'])

def int_to_n_bits(n):
    def f(x):
        return bin(x)[2:].rjust(n, '0')
    return f

def split_string_in_fixed_length(length):
    def f(string):
        return [string[i: i+length] for i in range(0, len(string), length)]
    return f

def encode_bit_pattern(length, encode_function):
    def f(bit_pattern):
        return ''.join(map(encode_function,
                           split_string_in_fixed_length(length)(bit_pattern)))
    return f

def encode(string, split_function, to_bit_pattern, encode_function):
    string_groups = split_function(string)
    bit_patterns = [''.join(map(to_bit_pattern, group))
                    for group in string_groups]
    return ''.join(map(encode_function, bit_patterns))


def _plain_char_to_bit_pattern(char):
    return int_to_n_bits(8)(ord(char))

def _bit_pattern_to_encoded_char(bits):
    return BASE64_INDEX_TABLE[int(bits.ljust(6, '0'), 2)]

def to_base_64(string):
    return encode(string,
                  split_string_in_fixed_length(3),
                  _plain_char_to_bit_pattern,
                  encode_bit_pattern(6,
                                     _bit_pattern_to_encoded_char))

def _encoded_char_to_bit_pattern(char):
    return int_to_n_bits(6)(BASE64_INDEX_TABLE.index(char))

def _bit_pattern_to_decoded_char(bits):
    if len(bits) != 8:
        return ""
    return chr(int(bits, 2))

def from_base_64(string):
    return encode(string,
                  split_string_in_fixed_length(4),
                  _encoded_char_to_bit_pattern,
                  encode_bit_pattern(8,
                                     _bit_pattern_to_decoded_char))
