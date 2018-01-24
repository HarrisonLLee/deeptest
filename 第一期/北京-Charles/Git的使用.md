## Git的使用
### 1、查看本地关联的远程仓库地址
	git remote –v
### 2、从远程仓库（remote区）拉取全部代码
    git clone git@git.missfresh.cn:astest/astestautomation.git
### 3、在本地（workspace区）可对代码进行增删改等操作，然后提交到本地仓库
	git add order_list_test.py
	git commit -m 'add a case order_list_test'  (引号内备注语强制加一下哈，有好处)
### 4、将本地仓库代码提交至远程仓库GitLab（remote区）
	git push origin master
### 5、提交成功，即可在GitLab看到
	http://git.missfresh.cn/astest/astestautomation
### 6、若远程仓库更新了代码，需要将这些更新拉取本地
	git fetch origin master
### 7、在本地分支上合并远程分支
	git rebase origin/master
	若出现冲突，解决冲突后
	git add .
	git rebase --continue
	
### 注：在操作过程中，建议每一步后使用git status，关注当前状态；当前只有一个项目，暂不设置分支，若分支情况有问题，后续补充。

### 配图帮助理解：
![git版本控制](./images/git.png)
