#!/usr/bin/python3
"""UTF-8 validation task for interview prep.
"""


def validUTF8(data):
    """validates a list of integers as UTF-8 codes.
    Resource <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    num_bytes = 0
    byte_7 = 1 << 7
    byte_6 = 1 << 6

    for num in data:
        byte_count = 1 << 7
        if num_bytes == 0:
            while byte_count & num:
                num_bytes += 1
                byte_count = byte_count >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num & byte_7 and not (num & byte_6)):
                return False
        num_bytes -= 1
    return num_bytes == 0
