# SSH密钥生成与GitHub配置完整指南

*最后更新时间：2025-09-05 15:40:00*

本指南将帮助您生成SSH密钥并配置GitHub，以解决HTTPS连接问题，实现更稳定的代码推送。

## 为什么使用SSH？

使用SSH方式连接GitHub相比HTTPS有以下优势：
1. 连接更稳定，不易出现网络中断
2. 无需每次输入用户名和密码
3. 更安全的身份验证方式

## SSH密钥生成步骤

### Windows系统

#### 方法一：使用Git Bash（推荐）

1. 打开Git Bash终端
2. 生成SSH密钥对：
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
3. 按提示操作：
   - 选择保存位置（直接回车使用默认位置）
   - 设置密码（可选，但推荐设置）

#### 方法二：使用Windows PowerShell

1. 打开PowerShell
2. 生成SSH密钥对：
   ```powershell
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

### macOS/Linux系统

1. 打开终端
2. 生成SSH密钥对：
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

## SSH密钥配置

### 1. 启动SSH代理

#### Windows (Git Bash)
```bash
eval "$(ssh-agent -s)"
```

#### Windows (PowerShell)
```powershell
Get-Service -Name ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent
```

#### macOS/Linux
```bash
eval "$(ssh-agent -s)"
```

### 2. 添加SSH密钥到代理

```bash
ssh-add ~/.ssh/id_rsa
```

### 3. 复制公钥内容

#### Windows (Git Bash)
```bash
cat ~/.ssh/id_rsa.pub
```

#### Windows (PowerShell)
```powershell
Get-Content ~/.ssh/id_rsa.pub
```

#### macOS/Linux
```bash
cat ~/.ssh/id_rsa.pub
```

### 4. 在GitHub中添加SSH密钥

1. 登录GitHub账户
2. 点击右上角头像，选择"Settings"
3. 在左侧菜单中选择"SSH and GPG keys"
4. 点击"New SSH key"
5. 填写标题（如："My Laptop"）
6. 将复制的公钥内容粘贴到"Key"区域
7. 点击"Add SSH key"

## 验证SSH连接

### 测试SSH连接

```bash
ssh -T git@github.com
```

如果看到类似以下信息，表示连接成功：
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

## 切换远程仓库URL

如果您之前使用HTTPS方式，需要切换为SSH方式：

```bash
# 查看当前远程仓库URL
git remote -v

# 切换为SSH方式
git remote set-url origin git@github.com:用户名/仓库名.git

# 验证更改
git remote -v
```

## 常见问题及解决方案

### Permission denied (publickey)

1. 确保SSH密钥已正确生成
2. 确保公钥已添加到GitHub账户
3. 确保SSH代理正在运行且已添加私钥

### SSH密钥密码忘记

重新生成SSH密钥对并重新添加到GitHub。

### Windows系统特殊注意事项

1. 确保Git已正确安装
2. 推荐使用Git Bash而非Windows CMD
3. 如遇到换行符问题，可配置：
   ```bash
   git config --global core.autocrlf true
   ```

## 完整推送流程

完成SSH配置后，正常推送流程如下：

```bash
# 1. 检查状态
git status

# 2. 添加更改
git add .

# 3. 提交更改
git commit -m "提交信息"

# 4. 推送到远程仓库
git push origin master
```

## 参考文档

- [GitHub SSH连接官方文档](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [生成新的SSH密钥](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [将SSH密钥添加到GitHub账户](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)