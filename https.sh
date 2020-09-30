#!/dev/null

function quit {
  sudo iptables -F INPUT
  sudo killall stunnel
  sudo killall busybox
  exit 0
}

trap quit SIGINT

cd /home/darren/cgi

if [ -e index.html ]; then
  echo
  echo -n "  overwrite index.html? "
  read -r
fi

./cgi-bin/00_redir.sh

echo -e "\033]0;https\007"

sudo /bin/true

sudo iptables -A INPUT -p tcp --dport 80 ! -s 127.0.0.1 -j DROP

parallel --line-buffer ::: 'sudo busybox httpd -f -vv -p 127.0.0.1:80 -u darren:darren -h /home/darren/cgi -c /etc/httpd.conf' 'sudo stunnel /etc/stunnel/stunnel.conf'

echo -e "\033]0;Alacritty\007"
