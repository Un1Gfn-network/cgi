#!/bin/python3

import os
import pprint
import pwd
import subprocess
import sys
import urllib.parse

# sys.path.insert(1, '/path/to/application/app/folder')
import ytdlp2

HIST = "/home/darren/.holoplay"
USER = "darren"

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


def dropuser():

    # https://stackoverflow.com/a/6037494/
    # https://docs.python.org/3/library/subprocess.html#subprocess.Popen
    g, u, r = os.getgid(), os.getuid(), pwd.getpwnam(USER)

    # drop privilege
    if (g, u) != (r.pw_gid, r.pw_uid):
        assert (g, u) == (0, 0)
        os.setgid(r.pw_gid)
        os.setuid(r.pw_uid)


def env():

    os.environ.clear()
    proxy = "http://127.0.0.1:8080"
    os.environ |= {
        'all_proxy': proxy,
        'ALL_PROXY': proxy,
        'http_proxy': proxy,
        'HTTP_PROXY': proxy,
        'https_proxy': proxy,
        'HTTPS_PROXY': proxy,
        'no_proxy': ','.join(["127.0.0.0/8",
                              "192.168.0.0/24",
                              "localaddress",
                              "localhost",
                              ".localdomain.com"])
    }
    os.environ |= {
        'DISPLAY': ":0.0",
        'HOME': f"/home/{USER}",
        'LOGNAME': USER,
        'PWD': "/tmp",
        'USER': USER,
        'XDG_RUNTIME_DIR': f"/run/user/{pwd.getpwnam(USER).pw_uid}"
    }


def kill():

   subprocess.run(["/usr/bin/killall", "ffplay"], stdout=sys.stderr)
   subprocess.run(["/usr/bin/killall", "mpv"], stdout=sys.stderr)


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
    url = ytdlp2.canonicalize(t[1])
    assert url

    # start watching
    ytdlp2.init()
    print_server()
    with open(HIST, 'a') as f:
        print(url, file=f)
    ytdlp2.watch(fmt, url)


def main():

    # http header
    print_html("Content-Type: text/plain; charset=utf-8\n")
    # print_html('Hello 歡迎')

    print_server()

    d = parse()
    dropuser()
    env()

    if "ef1lc1gh" in d:
        kill()
        print_server()
        return

    if "gf3dqjhn" in d:
        kill()
        print_server()
        # https://stackoverflow.com/a/54278929
        # https://stackoverflow.com/a/713814
        # with open(HIST, 'r') as f:
        #     d['m346bpv6'][1] = f.readlines()[-1]
        try:
            f = open(HIST, 'rb')
        except FileNotFoundError as fe:
            print(fe)
            return
        else:
            with f:
                f.seek(-1, os.SEEK_END)
                assert f.read(1) == b'\n'
                u = bytearray()
                while True:
                    try:
                        f.seek(-2, os.SEEK_CUR)
                    except OSError as oe:
                        assert oe.errno == 22
                        break
                    b = f.read(1)
                    if b == b'\n':
                        break
                    u = b + u
                d['m346bpv6'][1] = u.decode('utf-8')
                # print(f"..{u.decode('utf-8')}..")
        play(d)
        return

    if "sc40lpz5" in d:
        kill()
        print_server()
        play(d)
        print_server()
        return

    raise NotImplementedError


if __name__ == "__main__":
    main()


# if 'sz3nb58f' in d:
#     # https://stackoverflow.com/questions/51501029/how-to-run-part-of-code-as-different-user-in-linux-with-python
#     with UnixUser(1000):
#         with pulsectl.Pulse('hololive-pulse-client') as p:
#             s = p.sink_list()
#             assert len(s) == 1
#             s = s[0]
#             assert s.name == p.server_info().default_sink_name
#             print_html(p.volume_get_all_chans(s))
#             print(pulse.volume_get_all_chans(s))

# if 'sz3nb58f' in d:
# with UnixUser(1000):
#     with pulsectl.Pulse('hololive-pulse-client') as p:
#             # ...
#             pulse.volume_set_all_chans(s,0.78)

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
