# AmazingData Claude Code Skill

> 中国银河证券星耀数智 AmazingData 量化数据接口 Claude Code 集成

## 功能特性

- **股票数据**: A股、B股全市场覆盖
- **ETF数据**: 实时净值 IOPV、申购赎回
- **期货期权**: 商品期货、ETF期权、股票期权
- **指数数据**: 沪深300、中证500等主要指数
- **K线数据**: 日/周/月/季/年线及1/3/5/15/30/60分钟K线
- **财务数据**: 资产负债表、利润表、现金流量表
- **实时行情**: Level-1 快照订阅
- **特色数据**: 龙虎榜、融资融券、沪港通、概念板块

## 安装

### 方法一: 复制文件（推荐）

```bash
# 克隆到 skills 目录
git clone https://github.com/fanyichao1029-boop/amazing-data-skill.git ~/.claude/skills/amazing-data
```

### 方法二: 手动复制

1. 下载 `amazing-data.md`
2. 复制到 `~/.claude/skills/` 目录

## 配置凭证

首次使用时，在 Claude Code 中告诉 AI：

```
我想连接 AmazingData，我的账号是: xxx，密码是: xxx，服务器: xxx，端口: 8600
```

AI 会引导你完成配置。凭证会保存到 memory 中，下次使用无需重新输入。

## 使用前提

### 安装 AmazingData SDK

```bash
pip install AmazingData-1.1.6-cp312-none-any.whl
```

> SDK 下载地址请联系你的券商获取

## 快速开始

### 查询股票

```
帮我查一下贵州茅台的股价
```

```
获取平安银行的日K线
```

```
列出所有 ETF 代码
```

### 数据分析

```
帮我分析一下茅台的财务数据
```

```
获取比亚迪最近一个月的分钟K线
```

### 实时监控

```
监控中国石油的实时价格
```

## 示例命令

### 连接测试

```python
import AmazingData as ad
ad.login(username='你的账号', password='你的密码', host='服务器地址', port=8600)
print('连接成功')
```

### 查询数据

```python
import AmazingData as ad

# 获取股票列表
base_data = ad.BaseData()
stocks = base_data.get_code_list(security_type='EXTRA_STOCK_A')

# 获取K线
kline = base_data.get_kline(
    code='600519.SH',
    start_date=20260101,
    end_date=20260520,
    period=ad.constant.Period.day,
    adj='qfq'
)

# 财务数据
info_data = ad.InfoData()
financial = info_data.get_financial_index(['600519.SH'])
```

## 证券类型

| 类型 | 代码 | 说明 |
|------|------|------|
| A股 | `EXTRA_STOCK_A` | 沪深全市场 |
| A股(沪深) | `EXTRA_STOCK_A_SH_SZ` | 仅沪深主板 |
| ETF | `EXTRA_ETF` | 交易所交易基金 |
| 指数 | `EXTRA_INDEX_A` | A股指数 |
| 期货 | `EXTRA_FUTURE` | 商品/金融期货 |
| 期权 | `EXTRA_ETF_OP` | ETF期权 |
| 国债 | `EXTRA_GLRA` | 国债/利率债 |

## Period 常量

| 常量 | 周期 |
|------|------|
| `Period.min1` | 1分钟 |
| `Period.min5` | 5分钟 |
| `Period.min15` | 15分钟 |
| `Period.min30` | 30分钟 |
| `Period.min60` | 60分钟 |
| `Period.day` | 日线 |
| `Period.week` | 周线 |
| `Period.month` | 月线 |

## 注意事项

1. **需要有效账号**: 联系券商开通 AmazingData 服务
2. **网络要求**: 能够访问券商服务器地址
3. **权限说明**: 部分数据需要相应的订阅权限
4. **交易日**: 实时数据仅在交易日有效

## 故障排除

### 连接失败
- 检查用户名密码是否正确
- 确认服务器地址和端口
- 检查网络连接

### 数据为空
- 确认日期格式（YYYYMMDD整数）
- 检查股票代码是否正确
- 某些股票可能停牌

## 许可证

AGPL v3

## 获取帮助

- SDK 下载: 联系券商
- 技术支持: 联系券商客服
- Skill 问题: GitHub Issues