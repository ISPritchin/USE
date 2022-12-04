import doctest

def process_string(s):
    """
    >>> process_string("AAC")
    1
    >>> process_string("AACAAC")
    2
    >>> process_string("DAACAAC")
    2
    >>> process_string("DAACOACAAC")
    3
    >>> process_string("AADAACOACAAC")
    4
    >>> process_string("AAAACAACAACCAACAACAACA")
    3
    """
    binary = ""
    for c in s:
        binary += '0' if c in 'AO' else '1'

    max_seq = 0
    for start in range(0, 3):
        cur_seq = 0
        for j in range(start, len(s), 3):
            if binary[j:j + 3] == '001':
                cur_seq += 1
                max_seq = max(max_seq, cur_seq)
            else:
                cur_seq = 0

    return max_seq

doctest.testmod()