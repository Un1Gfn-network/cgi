#!/bin/python3

import datetime
import pprint
import re
import requests
import subprocess
import sys
import yt_dlp

# JSON = "/tmp/ytdlp.json"

ytdlpobj = None
BROWSER = 'chromium'

def eprint(*x):

    print(*x,file=sys.stderr)


def canonicalize(url):

    assert type(url) == str

    # https://docs.python.org/3/library/re.html#regular-expression-syntax

    # video id only
    if re.match(r"^[A-Za-z0-9_-]{11}\Z", url):
        return f"https://www.youtube.com/watch?v={url}"

    # full url
    if (False
        or re.match(r"^https://youtu.be/[A-Za-z0-9_-]{11}\Z", url)
        or re.match(r"^https://www.youtube.com/watch\?v=[A-Za-z0-9_-]{11}\Z", url)
    ):
        return url

    return str("")


def ipapi():

    with requests.get("https://ipinfo.io") as r:
        j = r.json()
    pprint.pprint(j, stream=sys.stderr)
    return j['ip']


def hls2ip(s):

    regex = "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/[0-9]+/ei/[-0-9A-Z_a-z]+/ip/" + \
            "(" + r"[0-9]+\." * 3 \
                + "[0-9]+" + \
            ")" + "/"
    return re.search(regex, s).group(1)


def watch(fmt: dict, url: str):

    global ytdlpobj
    assert ytdlpobj
    # with contextlib.redirect_stdout(sys.stderr):
    i = ytdlpobj.extract_info(url, download=False)
    print()
    eprint()

    if (False
        or not i['is_live']
        or i['was_live']
        or i['live_status'] != "is_live"
    ):
        print("not live\n")
        return

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
            assert f.items() >= fmt.items()
            m3u8 = f['url']
            break
    assert 10 <= len(m3u8)

    # https://pythonguides.com/python-epoch-to-datetime/
    start = datetime.datetime.fromtimestamp(i['release_timestamp'])
    mins = int((datetime.datetime.now() - start).total_seconds() / 60)
    eprint(f":: {mins} min, since {start}", "\n")

    args = ["/usr/bin/mpv",
            "--pause",
            "--no-resume-playback",
            "--hwdec=vaapi",
            # "--vo=vaapi", "--no-osc", "--no-osd-bar",
            f"--title=tv",
            m3u8]
    eprint(":;", *args, "\n")

    if (hls2ip(m3u8), None) != (ipapi(), eprint()):
        raise ValueError(f"ip mismatch, try playing {url} in {BROWSER} for a short while beforing launching")

    subprocess.run(args, stdout=sys.stderr)


def init():

    global ytdlpobj
    # with contextlib.redirect_stdout(sys.stderr):
    ytdlpobj = yt_dlp.YoutubeDL(params={
        'verbose': True,
        'quiet': False,
        'no_warnings': False,
        'cookiesfrombrowser': (BROWSER,)
    },auto_init=True)


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
#     u = canonicalize(sys.argv[1])
#     if u:
#         watch(y, u)
# else:
#     assert 1 == len(sys.argv)
#     while True:
#         try:
#             u = canonicalize(input("youtube_url> "))
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
