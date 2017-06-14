import os
import shutil

base_path    = r'C:\Users\220554\Documents\GitHub\wsrepo'
datadir      = '_repo'
toolsdir     = "_tools"
output       = os.path.join(base_path, datadir)
print 'Output directory is %s'% output

wslivetv     = 'https://github.com/welwel2/wslivetv.git#dev'
#wslivetv     = 'https://github.com/welwel2/wslivetv.git:plugin.video.wslivetv'
wslivestream = 'https://github.com/welwel2/wslivestream.git:plugin.video.wslivestream'
wsteledunet  = 'https://github.com/welwel2/wsteledunet.git:plugin.video.wsteledunet'
wsrepo       = 'https://github.com/welwel2/wsrepo.git:_repo/repository.wsrepo'

addons = [wslivetv, wslivestream, wsteledunet, wsrepo]

addons_str = ''.join('%s '%addon for addon in addons)
print 'addons paths are %s'%addons_str

if os.path.exists(output):
    shutil.rmtree(output)
os.chdir(os.path.join(base_path, toolsdir))

os.system(r'py -3 create_repository.py --datadir=%s %s'%(output, addons_str))
