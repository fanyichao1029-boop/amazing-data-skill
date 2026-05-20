# AmazingData Claude Code Skill

中国银河证券星耀数智 AmazingData 金融数据服务的 Claude Code 集成。

## 功能

- A股、ETF、期货、期权数据查询
- 实时行情订阅
- K线数据获取
- 财务数据、指标数据查询

## 安装

### 方法一：直接复制

1. 复制 `amazing-data.md` 到 `~/.claude/skills/`

### 方法二：从 GitHub 安装

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/amazing-data-skill.git ~/.claude/skills/amazing-data
```

## 配置

首次使用时，Skill 会引导你输入 AmazingData 凭证：

- **用户名**：你的券商账号
- **密码**：你的账号密码
- **服务器地址**：券商提供的服务器IP或域名
- **端口**：服务商提供的端口（通常 8600）

凭证会保存到 memory 中，下次使用无需重新输入。

## 使用前提

### 1. 安装 AmazingData SDK

```bash
pip install AmazingData-1.1.6-cp38-none-any.whl
```

或联系你的券商获取最新版本的 SDK 安装包。

### 2. 配置凭证

在 Claude Code 中说"连接 AmazingData"，Skill 会引导你配置。

## 示例

### 查询茅台股价

```
"帮我查一下茅台今天的价格"
```

### 获取K线

```
"获取茅台最近一个月的日K线"
```

### 查看A股列表

```
"列出所有A股代码"
```

## 注意事项

- 需要有效的 AmazingData 账号
- 部分数据需要相应的订阅权限
- 网络需要能够访问券商服务器

## 许可证

AGPL v3

## 获取帮助

联系你的券商获取 AmazingData 服务支持和 SDK。