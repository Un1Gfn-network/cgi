#!/bin/python3

import os
import sys
import urllib.parse
import pprint

# sys.path.insert(1, '/path/to/application/app/folder')
import ytdlp2

HIST = "/tmp/holoplay"

print_html = print

# https://stackoverflow.com/a/15860483
# https://docs.python.org/3/library/functions.html#print
# https://docs.python.org/3/glossary.html#keyword-only-parameter
def print_server(*x):

    print(*x,file=sys.stderr)


def parse():

    # https://docs.python.org/3/tutorial/errors.html
    # https://stackoverflow.com/questions/4906977
    # print_server(f"REQUEST_URI  = '{os.environ['REQUEST_URI']}'")
    # print_server(f"QUERY_STRING = '{os.environ['QUERY_STRING']}'")
    return urllib.parse.parse_qs(
        qs=os.environ['QUERY_STRING'],
        keep_blank_values=True,
        strict_parsing=True,
        encoding='utf-8',
        errors='strict',
        max_num_fields=None,
        separator='&'
    )


def kill():

    ytdlp2.run_as_user(args=["/usr/bin/killall", "ffplay"])
    ytdlp2.run_as_user(args=["/usr/bin/killall", "mpv"])


def play(d):

    assert type(d) == dict
    assert len(d) == 2

    t = d['m346bpv6']       # get the name group containing resolution and url
    assert type(t) == list
    assert len(t) == 2

    # choose resolution
    fmt = { 'abr': 0,
            'dynamic_range': 'SDR',
            'ext': "mp4",
            'protocol': "m3u8_native",
            'video_ext': "mp4" }
    match t[0]:
        case "upcl8r46": fmt |= { 'format_id':  "91", 'width':  256, 'height':  144, 'fps': 30, 'vcodec': "avc1.4d400c", 'acodec': "mp4a.40.5" }
        case "b4bk2eut": fmt |= { 'format_id':  "92", 'width':  426, 'height':  240, 'fps': 30, 'vcodec': "avc1.4d4015", 'acodec': "mp4a.40.5" }
        case "28fh6pym": fmt |= { 'format_id':  "93", 'width':  640, 'height':  360, 'fps': 30, 'vcodec': "avc1.4d401e", 'acodec': "mp4a.40.2" }
        case "87spj9m8": fmt |= { 'format_id':  "94", 'width':  854, 'height':  480, 'fps': 30, 'vcodec': "avc1.4d401f", 'acodec': "mp4a.40.2" }
        case "q5vewy44": fmt |= { 'format_id': "300", 'width': 1280, 'height':  720, 'fps': 60, 'vcodec': "avc1.4d4020", 'acodec': "mp4a.40.2" }
        case "t2gic9ya": fmt |= { 'format_id': "301", 'width': 1920, 'height': 1080, 'fps': 60, 'vcodec': "avc1.4d402a", 'acodec': "mp4a.40.2" }
        case _: raise NotImplementedError
    fmt['resolution'] = f"{fmt['width']}x{fmt['height']}"
    fmt['format'] = f"{fmt['format_id']} - {fmt['resolution']}"

    # validate url
    u = t[1]
    assert type(u) == str
    u = ytdlp2.validate(u)
    assert u

    # start watching
    ytdlp2.init()
    print_server()
    with open(HIST, 'a') as f:
        print(u, file=f)
    ytdlp2.watch(fmt, u)


def main():

    # http header
    print_html("Content-Type: text/plain; charset=utf-8\n")
    # print_html('Hello 歡迎')

    print_server()

    d = parse()
    if "ef1lc1gh" in d:
        kill()
        print_server()
        return
    if "gf3dqjhn" in d:
        kill()
        print_server()
        with open(HIST, 'r') as f:
            d['m346bpv6'][1] = f.readlines()[-1]
            # print_server("A", d['m346bpv6'][1])
        play(d)
        return
    elif "sc40lpz5" in d:
        kill()
        print_server()
        play(d)
        print_server()
    else:
        raise NotImplementedError

if __name__ == "__main__":
    main()

# print_server(d)
# for i in d:
#     print_server(type(i))
#     print_server(f"###[{i[0]}]###")
#     print_server()
#     print_server(f"###{i[1]}###")
#     print_server()

# https://stackoverflow.com/q/5574702
# https://stackoverflow.com/a/37376668
# from os import write
# write(2,b"\n")
# write(2,d[0][0].encode())
# write(2,b"\n")
# write(2,d[0][1].encode())
# write(2,b"\n")
# write(2,b"\n")
