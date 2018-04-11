import os
import shutil

toolsdir     = os.path.dirname(os.path.abspath(__file__))
base_path    = os.path.split(toolsdir)[0]
datadir      = '_repo'
toolsdir     = "_tools"
output       = os.path.join(base_path, datadir)
#print 'Output directory is %s'% output

wslivetv     = 'https://github.com/welwel2/wslivetv.git#dev'
#wslivetv     = 'https://github.com/welwel2/wslivetv.git:plugin.video.wslivetv'
wslivestream = 'https://github.com/welwel2/wslivestream.git:plugin.video.wslivestream'
wsteledunet  = 'https://github.com/welwel2/wsteledunet.git:plugin.video.wsteledunet'
wsrepo       = 'https://github.com/welwel2/wsrepo.git:_repo/repository.wsrepo'
addons = [wslivetv, wslivestream, wsteledunet, wsrepo]
addons_str = ''.join('%s '%addon for addon in addons)

def update_remote(repo_path, rm='origin'):
    # the objective here is to develp code to push the wsrepo changes to the server
    # the steps requied are:
    # 1. commit the changes locally
    # 2. push changes to server
    
    from git import Repo
    repo = Repo(repo_path)       # instantiate the repo
    assert not repo.bare         # ensure that the repo is not empty
    if repo.is_dirty():          # check if there is changes that needs to be commited
        # commit changes
    
    #    master = repo.heads.master
    #    repo.head.reference = master  # switch to master branch
        #git.checkout('--', '*.py[oc]')
        index = repo.index
        #for (path, stage), entry in index.entries.items():
        #    print path, stage
        #repo.index.rm('*')
        repo.index.add('*')
        repo.index.add(repo.untracked_files)
        repo.index.commit("commit changes")
        print 'commited changes'
    else:
        print "repo is clean no changes to commit"
    
    remote = eval('repo.remotes.%s'%rm)
    assert remote.exists()
    try:
       remote.push()
    except:
        import push
        pp = push.PushProject()
        pp.get_git()
    print 'pushed changes'

#print 'addons paths are %s'%addons_str

def delete_output():
    if os.path.exists(output):
        shutil.rmtree(output)
    os.chdir(os.path.join(base_path, toolsdir))

if __name__ ==  "__main__":
    delete_output()
    os.system(r'py -3 create_repository.py --datadir=%s %s'%(output, addons_str))
    update_remote(base_path)



