from git import Repo

git_dir = 'ssh://git@git.sankuai.com/data/datalink.git'
source_dir = '/tmp/datalink'
tag_or_branch='DLS-1.2.1-QA'
repo = Repo.clone_from(git_dir, source_dir, branch=tag_or_branch)
# 重新设置 git 的 head
tag_we_use = repo.create_head('tag_we_use', tag_or_branch)
repo.head.reference = tag_we_use
# 下面这句很重要，不然代码是 master 分支的
repo.head.reset(index=True, working_tree=True)
