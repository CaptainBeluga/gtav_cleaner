import os
import shutil
from datetime import datetime


important = [
    'gta5_cleaner.py',

    'bink2w64.dll',
    'common.rpf',
    'd3dcompiler_46.dll',
    'd3dcsx_46.dll',
    'GFSDK_TXAA.win64.dll',
    'GFSDK_ShadowLib.win64.dll',
    'GPUPerfAPIDX11-x64.dll',
    'GFSDK_TXAA_AlphaResolve.win64.dll',
    'GTAVLanguageSelect.exe',
    'GTA5.exe',
    'GTAVLauncher.exe',
    'NvPmApi.Core.win64.dll',
    'x64e.rpf',
    'x64a.rpf',
    'x64b.rpf',
    'x64c.rpf',
    'x64d.rpf',
    'PlayGTAV.exe',
    'x64f.rpf',
    'x64g.rpf',
    'x64h.rpf',
    'x64i.rpf',
    'x64j.rpf',
    'x64k.rpf',
    'x64l.rpf',
    'x64m.rpf',
    'x64n.rpf',
    'x64o.rpf',
    'x64p.rpf',
    'x64q.rpf',
    'x64r.rpf',
    'x64s.rpf',
    'x64t.rpf',
    'x64u.rpf',
    'x64v.rpf',
    'x64w.rpf',
    'update',
    'x64',
    'uninstall.exe',
    'version.txt',
    'ReadMe',
    'Redistributables',
    'index.bin',
    'fvad.dll',
    'libcurl.dll',
    'opus.dll',
    'opusenc.dll',
    'toxmod.dll',
    'zlib1.dll',
    'title.rgl',

    #EPIC GAMES
    '.egstore',
    'GPUPerfAPIDX11-x64.dll',
    'NvPmApi.Core.win64.dll',
    'version.txt',
    'ReadMe',
    'Redistributables',
    'EOSSDK-Win64-Shipping.dll',

    #STEAM FILES
    'steam_api64.dll',
    'steam_appid.txt',
    'installscript.vdf',
    'installscript_sdk.vdf',
    'EntryPoints.txt',
]

createDir = True
DIR = "..\\GTA5_MODS_STORE"

if(os.path.exists(DIR) == False):
    os.mkdir(DIR)

for l in os.listdir():
    if(l not in important):
        try:
            if createDir:
                d = datetime.now()
                dirname = f"{DIR}\\{d.hour}-{d.minute}-{d.second}"
                os.mkdir(dirname)

                createDir = False


            shutil.move(l,f"{DIR}\\{dirname}")

            print(f"[-] {l}")


        except Exception as e:
            print(e)

if(createDir==False):
    print(f"\n[!] MODS BACKUP saved in `{os.path.abspath(dirname)}`")

else:
    print("\n[+] You're are READY TO PLAY ! ")