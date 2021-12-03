import time as t
import subprocess as sb
import os
import fnmatch


vid = input("Que quiere ver zarshisa?")

bool=sb.run(["youtube-dl","ytsearch:"+vid, "-q"], check = True)

if bool != 0:
	vido = [f for f in os.listdir(os.getcwd()) if fnmatch.fnmatch(f, '*.mp4')]
	vido = str(vido[0])
	print('Señoras y señores, les presentamos el futuro...')
	t.sleep(1)
	print('el pasado')
	t.sleep(1)
	print('... y el PRESENTE')
	t.sleep(2)
	sb.run(["clear"])
	t.sleep(1)
	print(' / ||__  ||_  )/ |\n | |  / /  / / | |\n |_| /_/  /___||_|')
	t.sleep(3)
	sb.run(["clear"])
	t.sleep(4)
	print('   _________ .__                    __________ ____ ______________________    _________\n   \_   ___ \|  |__   ____ ________ \______   \    |   \__    ___/\_____  \  /   _____/    \n   /    \  \/|  |  \_/ __ \\___   /  |     ___/    |   / |    |    /   |   \ \_____  \     \n   \     \___|   Y  \  ___/ /    /   |    |   |    |  /  |    |   /    |    \/        \    \n /\ \______  /___|  /\___  >_____ \  |____|   |______/   |____|   \_______  /_______  / /\ \n \/        \/     \/     \/      \/                                       \/        \/  \/ ')
	t.sleep(1)
	print('PRESENTA')
	t.sleep(3)
	sb.run(["clear"])
	t.sleep(1)
	sb.run(["python3", "video-to-ascii", "-f",vido])
else:
	print('Hez')

