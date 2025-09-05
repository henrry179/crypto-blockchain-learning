# Git 配置与推送完整教程

*最后更新时间：2025-09-05 15:38:00*

本教程将指导您如何配置 Git 并将本地代码推送到远程仓库。

## Git 基本配置

您的 Git 已经配置了用户信息，但为了保护隐私，建议使用匿名化处理。

可以通过以下命令查看配置信息：
```bash
git config --global --list
```

### 隐私保护配置

为了保护您的私人信息（如邮箱），建议使用以下配置：

```bash
# 设置用户名
git config --global user.name "YourGitHubUsername"

# 设置隐私保护邮箱（使用GitHub提供的noreply邮箱）
git config --global user.email "YourGitHubID+username@users.noreply.github.com"
```

## 推送代码到远程仓库

### 1. 检查仓库状态

```bash
git status
```

### 2. 添加更改到暂存区

```bash
git add .
```

### 3. 提交更改

```bash
git commit -m "提交信息说明"
```

### 4. 推送到远程仓库

```bash
git push origin master
```

## 常见问题及解决方案

### 网络连接问题

如果遇到以下错误：
```
fatal: unable to access 'https://github.com/用户名/仓库名.git/': Recv failure: Connection was reset
```

可能的解决方案：

1. 检查网络连接
2. 如果使用代理，配置 Git 代理：
   ```bash
   git config --global http.proxy http://代理地址:端口
   git config --global https.proxy https://代理地址:端口
   ```

3. 更换为 SSH 方式（推荐）：
   ```bash
   git remote set-url origin git@github.com:用户名/仓库名.git
   ```

### 身份验证问题

如果推送时需要身份验证，可以：

1. 使用个人访问令牌（推荐）：
   ```bash
   git remote set-url origin https://用户名:个人访问令牌@github.com/用户名/仓库名.git
   ```

2. 或者使用 SSH 密钥认证（更安全）：
   - 生成 SSH 密钥：
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
     ```
   - 将公钥添加到 GitHub 账户
   - 更改远程仓库 URL 为 SSH 格式

## 完整推送流程示例

```bash
# 1. 检查状态
git status

# 2. 添加所有更改
git add .

# 3. 提交更改
git commit -m "Update files"

# 4. 推送到远程仓库
git push origin master
```

## 隐私保护最佳实践

1. 使用 GitHub 提供的隐私邮箱：
   - 格式：`ID+username@users.noreply.github.com`
   - 在 GitHub 设置中可以找到您的隐私邮箱

2. 避免在公共仓库中提交包含个人信息的文件：
   - 使用 [.gitignore](file:///e:/其他文件/crypto-blockchain-learning/.gitignore) 文件忽略敏感文件
   - 不要在代码中硬编码个人凭证

3. 定期检查提交历史：
   ```bash
   git log --oneline
   ```

## 项目时间维护规则

为确保项目中所有文档的时间一致性，特制定以下时间维护规则：

1. 所有文档的最后更新时间应使用本机电脑当前的实时时间
2. 时间格式统一为：`YYYY-MM-DD HH:MM:SS`
3. 每次修改文档时，应同步更新文档顶部的最后更新时间
4. 对于新增文档，应添加最后更新时间标记

## 参考文档

- [Git 官方文档](https://git-scm.com/doc)
- [GitHub 推送指南](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository)
- [GitHub 隐私设置](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address)