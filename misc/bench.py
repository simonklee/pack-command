# -*- coding: utf-8 -*-

import pack_command
import pack_command_python

import timeit
import cProfile
import pstats
import pycallgraph

def format_time(seconds):
    v = seconds

    if v * 1000 * 1000 * 1000 < 1000:
        scale = u'ns'
        v = int(round(v*1000*1000*1000))
    elif v * 1000 * 1000 < 1000:
        scale = u'μs'
        v = int(round(v*1000*1000))
    elif v * 1000 < 1000:
        scale = u'ms'
        v = round(v*1000, 4)
    else:
        scale = u'sec'
        v = int(v)

    return u'{} {}'.format(v, scale)

# profiler size
number = 100000
sample = 7

# profiler type
profile = False
graph = False
timer = True

def runit():
    pack_command.pack_command("ZADD", "foo", 1369198341, 10000)

def runitp():
    pack_command_python.pack_command("ZADD", "foo", 1369198341, 10000)

if profile:
    pr = cProfile.Profile()
    pr.enable()

if graph:
    pycallgraph.start_trace()

if timer:
    for name, t in (("Python", runitp), ("cython", runit)):
        res = timeit.Timer(t).repeat(sample, number)
        min_run = min(res)
        per_loop = min_run/number

        print u'{}'.format(name)
        print u'{} total run'.format(format_time(min_run))
        print u'{} per/loop'.format(format_time(per_loop))
        #print u'{} per/friend'.format(format_time(per_loop/friends_cnt))
else:
    for j in xrange(number):
        runit()

if graph:
    pycallgraph.make_dot_graph('example.png')

if profile:
    pr.disable()
    ps = pstats.Stats(pr)
    sort_by = 'cumulative'
    ps.strip_dirs().sort_stats(sort_by).print_stats(20)
