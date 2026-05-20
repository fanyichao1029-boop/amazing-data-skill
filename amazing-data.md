---
name: amazing-data
description: AmazingData financial data service SDK for Chinese quantitative trading. Use when user asks about Chinese stocks, A-shares, futures, options, ETF data, or uses AmazingData API. Triggers on: "股票", "A股", "茅台", "K线", "行情", "AmazingData".
version: 1.1
updated: 2026-05-20
---

# AmazingData 金融数据服务

中国银河证券星耀数智 AmazingData 金融数据服务，支持A股、ETF、期货、期权等数据查询。

## 首次使用

### 第一步：安装 SDK

从中国银河证券获取 SDK 下载地址，安装 Python 包：

```bash
pip install AmazingData-1.1.6-cp38-none-any.whl
```

或者联系你的券商获取最新版本。

### 第二步：配置凭证

**Skill 会引导你输入以下信息：**
- 用户名
- 密码
- 服务器地址
- 端口

这些凭证会保存到 memory 中，下次使用无需重新输入。

### 第三步：测试连接

```python
import AmazingData as ad

ad.login(
    username='你的用户名',
    password='你的密码',
    host='服务器地址',
    port=端口
)
print('连接成功！')
```

---

## 快速查询示例

### 查看股票列表

```python
base_data = ad.BaseData()

# A股（沪深）
stock_list = base_data.get_code_list(security_type='EXTRA_STOCK_A_SH_SZ')
print(f'A股数量: {len(stock_list)}')

# 找特定股票（如茅台）
maotai = [s for s in stock_list if '600519' in s][0]
print(f'茅台代码: {maotai}')
```

### 获取实时行情（快照）

```python
sub_data = ad.SubscribeData()

@sub_data.register(code_list=['600519.SH'], period=ad.constant.Period.snapshot)
def on_snapshot(data, period):
    print(f'最新价: {data.price}')
    print(f'今开: {data.open}')
    print(f'最高: {data.high}')
    print(f'最低: {data.low}')
    print(f'成交量: {data.volume}')

sub_data.run()
```

### 获取 K 线数据

```python
from datetime import datetime

kline = base_data.get_kline(
    code='600519.SH',
    start_date=20260101,
    end_date=20260520,
    period=ad.constant.Period.kline_1day.value,
    adj='qfq'  # 前复权
)
print(kline)
```

---

## 证券类型常量

| 常量 | 含义 |
|------|------|
| `EXTRA_STOCK_A` | A股 |
| `EXTRA_STOCK_A_SH_SZ` | A股（沪深） |
| `EXTRA_ETF` | ETF |
| `EXTRA_INDEX_A` | A股指数 |
| `EXTRA_FUTURE` | 期货 |
| `EXTRA_ETF_OP` | ETF期权 |
| `EXTRA_GLRA` | 国债/利率 |

---

## 核心对象

| 对象 | 用途 |
|------|------|
| `ad.BaseData()` | 基础数据（代码列表、日历、复权因子） |
| `ad.InfoData()` | 信息数据（股票基本信息、财务数据） |
| `ad.SubscribeData()` | 实时订阅（快照、K线） |

---

## Period 常量（K线周期）

| Period | 含义 |
|--------|------|
| `Period.min1` | 1分钟 |
| `Period.min5` | 5分钟 |
| `Period.min15` | 15分钟 |
| `Period.min30` | 30分钟 |
| `Period.min60` | 60分钟 |
| `Period.day` | 日线 |
| `Period.week` | 周线 |
| `Period.month` | 月线 |

---

## 常见查询

### 股票基本信息

```python
info_data = ad.InfoData()
basic = info_data.get_stock_basic(['600519.SH'])
```

### 财务数据

```python
financial = info_data.get_financial_index(
    ['600519.SH'],
    start_date=20260101,
    end_date=20260401,
    retrench_type='basic'
)
```

### 指标数据

```python
indicator = info_data.get_indicator(['600519.SH'])
```

### 概念板块

```python
concepts = info_data.get_concept_index()
```

---

## 注意事项

1. **必须先登录**：`ad.login()` 成功后才能调用其他API
2. **端口是int类型**：`port=8600`，不是字符串 `"8600"`
3. **订阅是阻塞的**：`sub_data.run()` 会一直运行，需要单独线程
4. **网络超时**：设置 `socket.setdefaulttimeout(15)` 避免长时间等待

---

## 数据类型

- `Snapshot` - 快照（股价、成交量、买卖盘）
- `SnapshotIndex` - 指数快照
- `SnapshotFuture` - 期货快照
- `SnapshotETF` - ETF快照