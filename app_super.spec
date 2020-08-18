# -*- mode: python -*-

block_cipher = None


a = Analysis(['app_super.py'],
             pathex=['/media/nanfe/D66E07B96E079183/Users/admin/Documents/facultad/5toSemestre_2018,5/5toSemestre_2018,5/Paradigmas/ProyectoHernan/Estacionamiento2.1_InterfazGrafica'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='app_super',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='app_super')
