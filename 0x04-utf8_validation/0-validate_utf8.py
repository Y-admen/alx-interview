#!/usr/bin/python3
"UTF-8 Validation"

def validUTF8(data):
    """determines if a given data set
    represents a valid UTF-8 encoding."""
    num_byte = 0
    for i in data:
        mask = 1 << 7

        if num_byte == 0:
            while i & mask:  # counting num of bytes
                num_byte += 1
                mask = mask >> 1

            if num_byte == 0:  # check if num of bytes still 0
                continue

            # check if num of bytes > 4 bytes or 1
            if num_byte == 1 or num_byte > 4:
                return False
        else:
            # Check Continuation Bytes 01
            if not ((i & (1 << 7)) and not (i & (1 << 6))):
                return False
        num_byte -= 1
    return num_byte == 0
