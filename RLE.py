from itertools import chain, repeat

def batched(iterable, n):
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]


#helper for the decode function to add escape character requirement
def escapeSequence(st):
    st = st.replace('##', '\x00')

    #handle case when # has a number after it
    st = ''.join([ch if ch != '#' else ' ' for ch in st])

    st = st.replace('\x00', '#')

    return st


def decodeRLE(iterable, *, length_first=True):
    #input validation: check if its even
    if len(iterable) % 2 != 0:
        raise ValueError("RLE decoding not implemented for odd numbers")

    iterable = escapeSequence(iterable)

    return ''.join(
        ''.join(repeat(b, int(a))) if length_first else ''.join(repeat(a, int(b)))
        for a, b in batched(iterable, 2)
    )


# fulfills activity requirement to check if the string has numbers
def hasNumbers(st):
    return any(char.isdigit() for char in st)


def printRLE(st):
    #remove whitespace from string
    st = st.replace(" ", "")

    if st.startswith("##00"):
        print("Decoding RLE: ")
        decodedRLE = decodeRLE(st[4:])
        print(decodedRLE)
    elif hasNumbers(st):
        print("Decoding RLE: ")
        decodedRLE = decodeRLE(st)
        print(decodedRLE)
    else:
        print("This is your string in RLE format: ")
        n = len(st)
        i = 0

        #check if string is empty
        if n == 0:
            print("You didn't enter anything!")
            return

        rle = "##00"
        while i < n:
            count = 1
            while(i < n - 1 and st[i] == st[i + 1]):
                count += 1
                i += 1
            if count > 1:
                rle += st[i] + str(count)
            #if there is only one instance on a character, just print it out
            else:
                rle += st[i]

            i += 1
        print(rle)


if __name__ == "__main__":
    st = input("Enter a string with repeated characters: ")
    printRLE(st)
