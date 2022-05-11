#!/bin/python3

import datetime
import os
import pprint
import pwd
import re
import subprocess
import sys
import yt_dlp

# JSON = "/tmp/ytdlp.json"

ytdlpobj = None
USER = "darren"

PROXY = "http://127.0.0.1:8080"
PROXYENV = {
    'all_proxy': PROXY,
    'ALL_PROXY': PROXY,
    'http_proxy': PROXY,
    'HTTP_PROXY': PROXY,
    'https_proxy': PROXY,
    'HTTPS_PROXY': PROXY,
    'no_proxy': "localhost,127.0.0.1,localaddress,.localdomain.com",
}

def eprint(*x):

    print(*x,file=sys.stderr)

def run_as_user(args):

    r = pwd.getpwnam(USER)

    # https://stackoverflow.com/a/6037494/
    # https://docs.python.org/3/library/subprocess.html#subprocess.Popen
    # process = subprocess.Popen(args=args, preexec_fn=demote(r.pw_uid, r.pw_gid), cwd="/tmp", env=dict())

    g0, u0 = os.getgid(), os.getuid()
    os.setgid(r.pw_gid)
    os.setuid(r.pw_uid)
    os.environ.clear()
    newenv = {
        'DISPLAY': ":0.0",
        'HOME': f"/home/{USER}",
        'LOGNAME': USER,
        'PWD': "/tmp",
        'USER': USER,
        'XDG_RUNTIME_DIR': f"/run/user/{r.pw_uid}"
    }
    newenv.update(PROXYENV)
    eprint(newenv)
    subprocess.run(args=args, stdout=sys.stderr, stderr=sys.stderr, cwd="/tmp", env=newenv)
    os.setgid(g0)
    os.setuid(u0)


def validate(url: str):

    # video id only
    if bool(re.match(r"^[A-Za-z0-9_-]{11}$", url)):
        return f"https://www.youtube.com/watch?v={url}"

    # full-blown url
    if (False
        or bool(re.match(r"^https://youtu.be/[A-Za-z0-9_-]{11}$", url))
        or bool(re.match(r"^https://www.youtube.com/watch\?v=[A-Za-z0-9_-]{11}$", url))
    ):
        return url

    return False


def watch(fmt: dict, url: str):

    global ytdlpobj
    assert ytdlpobj
    # with contextlib.redirect_stdout(sys.stderr):
    i = ytdlpobj.extract_info(url, download=False)

    assert i['is_live']
    assert i['live_status'] == "is_live"
    assert not i['was_live']

    if 'thumbnails' in i:
        i['thumbnails'] = { "...": "..." }

    m3u8 = ""
    for f in i['formats']:
        if f['format_id'] == fmt['format_id']:
            # for i in fmt:
            #     if fmt[i] != f[i]:
            #         eprint(f"{i}, {fmt[i]}, {f[i]}")
            #         assert False
            # https://stackoverflow.com/questions/9323749/how-to-check-if-one-dictionary-is-a-subset-of-another-larger-dictionary
            assert fmt.items() <= f.items()
            m3u8 = f['url']
            break
    assert 10 <= len(m3u8)

    # https://pythonguides.com/python-epoch-to-datetime/
    start = datetime.datetime.fromtimestamp(i['release_timestamp'])
    mins = int((datetime.datetime.now() - start).total_seconds() / 60)
    eprint(f":: {mins} min, since {start}")
    eprint()

    args = ["/usr/bin/mpv",
            "--hwdec=vaapi",
            "--vo=vaapi", "--no-osc", "--no-osd-bar",
            f"--title=tv",
            m3u8]
    eprint(":;", *args, "")
    run_as_user(args)

    # https://stackoverflow.com/questions/13432717/enter-interactive-mode-in-python
    # code.interact(local=locals())


def init():

    os.environ.update(PROXYENV)

    global ytdlpobj
    # with contextlib.redirect_stdout(sys.stderr):
    ytdlpobj = yt_dlp.YoutubeDL(params={
        'verbose': True,
        'quiet': False,
        'no_warnings': False,
        'cookiesfrombrowser': ('chromium',)
    },auto_init=True)


# def get_device():

#     global device
#     if 'DISPLAY' in os.environ:
#         assert os.environ['DISPLAY'] == ":0.0" or ":0"
#         assert os.environ['XDG_RUNTIME_DIR'] == "/run/user/1000"
#         device = '820g3'
#     else:
#         device = 'x200'

#     print("device "+device)


# def garbage():

# jq -C </tmp/ytdlp.json | less -RM +%
# jq -C </tmp/ytdlp.json 'del(.formats[].fragments)' | less -RM +%
# https://stackoverflow.com/a/35876912/8243991
# jq -C </tmp/ytdlp.json ' .formats[].fragments |= [.[0],.[-1]] ' | less -RM +%

# pydoc -n pydoc.localdomain -p 33423 -b

# InfoExtractors

# with open("/tmp/ytdlp.txt", "w") as t:
    # pprint.pprint(object=i,
                  # stream=t,
                  # indent=2,
                  # width=16384,
                  # depth=None)

# with open(JSON, 'w') as j:
#     json.dump(obj=i,
#               fp=j,
#               skipkeys=False,
#               ensure_ascii=False,
#               check_circular=True,
#               allow_nan=False,
#               indent=None,
              
#               separators=(',', ': '),
#               # separators=(',', ':'),
#               default=None,
#               # sort_keys=True,
#               cls=None,
#               # )
#     print(f":: written to {JSON}")
#     print()

# if 2 == len(sys.argv):
#     u = validate(sys.argv[1])
#     if u:
#         watch(y, u)
# else:
#     assert 1 == len(sys.argv)
#     while True:
#         try:
#             u = validate(input("youtube_url> "))
#         except EOFError:
#             print()
#             print()
#             break
#         except KeyboardInterrupt:
#             print()
#             continue
#         if u:
#             watch(y, u)
#             print()

# if 'fragments' in f:
#     assert 'n_fragment' not in f
#     f['n_fragment'] = len(f['fragments'])
#     del f['fragments']
