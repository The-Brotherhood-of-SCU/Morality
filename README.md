# Morality-Review-Material
思想道德与法治复习资料

### [点击此处查看网页版](https://the-brotherhood-of-scu.github.io/Morality-Review-Material/)
### [点击此处查看Github版](https://github.com/The-Brotherhood-of-SCU/Morality-Review-Material/blob/gh-pages/index.md)

# Contribute
文档规范

文件均使用markdown格式编写
子章节应放在章节对应的文件夹下

如：`第一章`->`1.马克思主义关于人的本质的认识.md`
子章节也应写上编号，防止整合的时候顺序错乱

**特别注意**

在markdown文件中，请不要使用#、##这样的一级、二级标题

因为自动化脚本会将所有文件合并，自动化脚本会自动将章节、子章节设为一级、二级标题

# 自动化逻辑

依赖Github-Action运行python脚本`Generate.py`（pull,push的时候触发）

脚本逻辑如下

    创建一个新markdown文件`index.md`
    将文件夹名设为一级标题,文件夹内部的文件名(不包括.md)设为二级标题，内容直接复制

将`index.md`部署到`gh-page`分支上，这时Github Pages会构建部署静态网站，将`index.md`构建为`index.html`

