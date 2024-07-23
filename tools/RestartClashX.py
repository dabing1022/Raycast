#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title RestartClashX
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName Developer

# Documentation:
# @raycast.description 重启 ClashX
# @raycast.author ChildhoodAndy
# @raycast.authorURL https://raycast.com/andy_childhoody

import subprocess

subprocess.run('pkill -9 -f /Applications/ClashX.app/Contents/MacOS/ClashX', shell=True)
subprocess.run('open /Applications/ClashX.app', shell=True)

# use AppleScript to notification
cmd = 'osascript -e \'display notification "ClashX restarted" with title "ClashX"\''
subprocess.run(cmd, shell=True)
