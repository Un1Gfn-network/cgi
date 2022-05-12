#!/bin/python3

import datetime
import pprint
import re
import subprocess
import sys
import yt_dlp

# JSON = "/tmp/ytdlp.json"

ytdlpobj = None

def eprint(*x):

    print(*x,file=sys.stderr)


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
    eprint()

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
    eprint(f":: {mins} min, since {start}", "\n")

    args = ["/usr/bin/mpv",
            "--pause",
            "--no-resume-playback",
            "--hwdec=vaapi",
            "--vo=vaapi", "--no-osc", "--no-osd-bar",
            f"--title=tv",
            m3u8]
    eprint(":;", *args, "\n")
    subprocess.run(args, stdout=sys.stderr)

    # https://stackoverflow.com/questions/13432717/enter-interactive-mode-in-python
    # code.interact(local=locals())


def init():

    global ytdlpobj
    # with contextlib.redirect_stdout(sys.stderr):
    ytdlpobj = yt_dlp.YoutubeDL(params={
        'verbose': True,
        'quiet': False,
        'no_warnings': False,
        'cookiesfrombrowser': ('chromium',)
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
