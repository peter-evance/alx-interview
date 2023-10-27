#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that checks if a given data set represents a valid
    UTF-8 encoding.
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data is represented by a list of integers
    Each integer represents 1 byte of data, and you need to handle
    the 8 least significant bits of each integer
    """
    # Variable to keep track of the number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking if a byte is valid (Starts with 10)
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:

        byte_mask = 1 << 7

        if num_bytes == 0:
            # Count the number of bytes the UTF-8 character will have
            while byte_mask & byte:
                num_bytes += 1
                byte_mask = byte_mask >> 1

            # If the number of bytes did not increase, then it has 1 byte,
            # which is the same we are counting, so no need to check next bytes
            # for the current character
            if num_bytes == 0:
                continue

            # A character in UTF-8 can be 1 to 4 bytes long,
            # but 1 byte characters start with 0, so num_bytes should never
            # be 1
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Every byte that is not the first byte of a character should start
            # with 10, otherwise, it's not valid
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # If bytes of the character are valid, then the count will decrease with
        # each byte until a new character starts
        num_bytes -= 1

    # All characters were verified correctly with their proper byte count
    if num_bytes == 0:
        return True

    return False
