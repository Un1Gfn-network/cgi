#!/bin/bash

S="httpd"

function httpd_miniserve {
  sudo miniserve -D -g -H -l -q -r -v -z -i 192.168.0.223 -p 80 -- ~/cgi/
  exit
}

function httpd_busybox {

  cd /home/darren/cgi || { echo "cannot change directory"; read -r; exit 1; }

  sudo /bin/true || { echo "cannot gain root privilege"; read -r; exit 1; }

  if [ -e index.html ]; then
    grep -qFe 'by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro' index.html \
      || { echo "ill tree"; read -r; exit 1; }
    # echo -n "  overwrite index.html? "
    # read -r
  fi

  ./cgi-bin/00_redir.sh

  printf "\e]0;%s\a" httpd

  # https://unix.stackexchange.com/questions/87468/is-there-an-easy-way-to-programmatically-extract-ip-address
  IP="$(ip -4 address show wlp2s0 | grep -Po 'inet \K[\d.]+')"
  [ 192.168.0.223 = "$IP" ] || { echo "ill IP"; read -r; exit 1; }
  URL="http://$IP/index.html"

  echo
  echo "  (1) Turn off proxy"
  echo "  (2) Visit $URL"

  echo
  qrencode -tUTF8 "$URL"

  echo
  sudo busybox httpd -f -vv -p "$IP":80 -u darren:darren -h /home/darren/cgi -c /etc/httpd.conf

  printf "\e]0;%s\a" Alacritty
  exit

}

function help2 {
  echo "  $0 [-b]"
  echo "  $0 -m"
  echo "  $0 -h"
  read -r
  exit
}

{ 

  [ -v TMUX ] || { 
    # tmux has-session -t "$S" && {
    #   echo "restart"
    #   tmux send -t "$S":0 "C-c" &>/dev/null || true
    # }
    CMD=(bash "$0" "$@")
    echo "#${CMD[*]}#"
    tmux new -A -s "$S" "${CMD[*]}"
    tmux ls
    exit
  }

  X=($(/bin/getopt -o 'mbh' -n 'httpd.sh' -- "$@"))

  for x in "${X[@]}"; do case x"$x" in
    x'-b') httpd_busybox; exit;;
    x'-m') httpd_miniserve; exit;;
    x'-h') help2; exit;;
    x''|x'--') ;;
    *) echo "err: unrecognized arg '$x'"; read -r; exit 1;;
  esac; done

  # default
  httpd_busybox

}; exit
