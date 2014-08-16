SYM_STAR = '*'
SYM_DOLLAR = '$'
SYM_CRLF = '\r\n'

def encode(value):
    "Return a bytestring representation of the value"
    if isinstance(value, str):
        return value
    if isinstance(value, float):
        value = repr(value)
    if not isinstance(value, basestring):
        value = str(value)
    if isinstance(value, unicode):
        value = value.encode('utf-8', 'strict')
    return value

def pack_command(*args):
    "Pack a series of arguments into a value Redis command"
    output = SYM_STAR + str(len(args)) + SYM_CRLF
    for enc_value in map(encode, args):
        output += SYM_DOLLAR
        output += str(len(enc_value))
        output += SYM_CRLF
        output += enc_value
        output += SYM_CRLF
    return output
