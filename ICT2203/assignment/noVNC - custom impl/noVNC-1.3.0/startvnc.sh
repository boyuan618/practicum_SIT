env -u SESSION_MANAGER -u DBUS_SESSION_BUS_ADDRESS vncserver -depth 32 -geometry 1280x720 -localhost no
utils/novnc_proxy --vnc localhost:5901 --listen 0.0.0.0:80 &
