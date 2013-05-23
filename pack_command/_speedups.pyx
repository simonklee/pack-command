cdef extern from "stdlib.h":
   void free(void* ptr)
   void* malloc(size_t size)
cdef extern from "string.h":
    void *memcpy(void *dest, const void *src, size_t n)
    size_t strlen(const char *s)
cdef extern from "stdio.h":
    int sprintf(char *str, const char *format, ...)

cdef char* encode(value):
    "Return a bytestring representation of the value"
    if isinstance(value, str):
        return <char*>value
    if isinstance(value, float):
        value = repr(value)
    if not isinstance(value, basestring):
        value = str(value)
    if isinstance(value, unicode):
        value = value.encode('utf-8', 'strict')
    return <char*>value

cdef int intlen(int i):
    cdef int n = 0

    if (i < 0): 
        n += 1
        i = -i

    n+=1
    i /= 10

    while i:
        n+=1
        i /= 10

    return n

cdef int bulklen(int n):
    return 1+intlen(n)+2+n+2

def pack_command(*args):
    "Pack a series of arguments into a value Redis command"
    cdef char *p
    cdef int argc = len(args)
    cdef int totlen = 1+intlen(argc)+2
    cdef int llen 
    cdef int pos
    cdef int i
    cdef int *argvlen = <int *>malloc(sizeof(int *) *argc)
    cdef char *cmd

    if not argvlen:
        raise MemoryError()

    try:
        for i in range(argc):
            p = encode(args[i])
            argvlen[i] = strlen(p)
            totlen += bulklen(argvlen[i])

        cmd = <char*>malloc(totlen+1)

        if not cmd:
            raise MemoryError()

        pos = sprintf(cmd, "*%d\r\n", argc)

        for i in range(argc):
            p = encode(args[i])
            llen = argvlen[i]
            pos += sprintf(cmd+pos,"$%zu\r\n",llen);
            memcpy(cmd+pos,p,llen);
            pos += llen;
            cmd[pos] = '\r';
            pos +=1
            cmd[pos] = '\n';
            pos +=1

        cmd[pos] = '\0';
        return cmd
    finally:
        if cmd:
            free(cmd)
        if argvlen:
            free(argvlen)
