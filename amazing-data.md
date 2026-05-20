---
name: amazing-data
description: AmazingData 中国银河证券金融数据服务。支持 A股、ETF、期货、期权、指数、K线、财务数据、实时行情订阅等。查询茅台股价、K线数据、股票列表、财务报表、龙虎榜、融资融券、沪港通等。
version: 2.0
updated: 2026-05-20
---

# AmazingData 金融数据服务

中国银河证券星耀数智 AmazingData 量化数据接口，支持全市场 A股、ETF、期货、期权、指数等金融数据查询。

## 一键安装

### Step 1: 配置凭证

在 Claude Code 对话框输入以下内容，替换为你的信息：

```
用户名: 你的用户名
密码: 你的密码
服务器: 服务器地址
端口: 8600
```

### Step 2: 安装 SDK

```bash
# 从券商获取 SDK 下载地址，安装命令类似：
pip install AmazingData-1.1.6-cp312-none-any.whl
```

### Step 3: 测试连接

```python
import AmazingData as ad
import socket
socket.setdefaulttimeout(15)

ad.login(username='你的用户名', password='你的密码', host='服务器地址', port=8600)
print('连接成功！')

# 获取数据
base_data = ad.BaseData()
stocks = base_data.get_code_list(security_type='EXTRA_STOCK_A')
print(f'A股数量: {len(stocks)}')
```

---

## 核心对象速查

| 对象 | 创建方式 | 用途 |
|------|----------|------|
| 基础数据 | `ad.BaseData()` | 代码列表、日历、K线、复权因子 |
| 信息数据 | `ad.InfoData()` | 财务、指标、股东、板块 |
| 实时订阅 | `ad.SubscribeData()` | 快照、K线订阅 |

---

## 证券类型常量

```python
'EXTRA_STOCK_A'        # A股
'EXTRA_STOCK_A_SH_SZ'  # A股（沪深）
'EXTRA_ETF'            # ETF
'EXTRA_INDEX_A'        # A股指数
'EXTRA_FUTURE'         # 期货
'EXTRA_ETF_OP'         # ETF期权
'EXTRA_GLRA'           # 国债/利率
'EXTRA_STOCK_B'        # B股
'EXTRA_CNC'            # 沪股通/深股通
```

---

## 登录与认证

```python
import AmazingData as ad

# 登录
ad.login(username='用户名', password='密码', host='服务器IP', port=8600)

# 登出
ad.logout(username='用户名')

# 修改密码
ad.update_password(username='用户名', old_password='旧密码', new_password='新密码')
```

---

## 代码列表查询

```python
base_data = ad.BaseData()

# A股列表
stocks = base_data.get_code_list(security_type='EXTRA_STOCK_A')

# ETF列表
etf_list = base_data.get_code_list(security_type='EXTRA_ETF')

# 指数列表
index_list = base_data.get_code_list(security_type='EXTRA_INDEX_A')

# 期货列表
future_list = base_data.get_future_code_list(security_type='EXTRA_FUTURE')

# 期权列表
option_list = base_data.get_option_code_list(security_type='EXTRA_ETF_OP')

# 找特定股票（如茅台）
maotai = [s for s in stocks if '600519' in s][0]
print(f'茅台: {maotai}')  # 600519.SH
```

---

## 股票基本信息

```python
info_data = ad.InfoData()

# 基本信息
basic = info_data.get_stock_basic(['600519.SH', '000858.SZ'])

# 买卖队列（Level-2）
order_book = info_data.get_order_book(['600519.SH'])

# 股东户数
holder_num = info_data.get_holder_num(['600519.SH'])

# 股本结构
equity = info_data.get_equity_structure(['600519.SH'])

# 限售股解禁
equity_restricted = info_data.get_equity_restricted(['600519.SH'])

# 股权质押
equity_pledge = info_data.get_equity_pledge_freeze(['600519.SH'])
```

---

## 财务数据

```python
# 资产负债表
balance = info_data.get_balance_sheet(['600519.SH'])

# 利润表
income = info_data.get_income(['600519.SH'])

# 现金流量表
cash_flow = info_data.get_cash_flow(['600519.SH'])

# 财务指标
financial = info_data.get_financial_index(
    ['600519.SH'],
    start_date=20260101,
    end_date=20260401,
    retrench_type='basic'  # basic=基础财务, fanal=完整财务
)

# 业绩快报
profit_notice = info_data.get_profit_notice(['600519.SH'])

# 业绩预告
profit_express = info_data.get_profit_express(['600519.SH'])
```

---

## 分红送股

```python
# 分红
dividend = info_data.get_dividend(['600519.SH'])

# 配股
right_issue = info_data.get_right_issue(['600519.SH'])
```

---

## K线数据

```python
base_data = ad.BaseData()

# 日K线
daily_kline = base_data.get_kline(
    code='600519.SH',
    start_date=20260101,
    end_date=20260520,
    period=ad.constant.Period.day,  # 日线
    adj='qfq'  # qfq=前复权, hfq=后复权, none=不复权
)

# 分钟K线
min1_kline = base_data.get_kline(
    code='600519.SH',
    start_date=20260520,
    end_date=20260520,
    period=ad.constant.Period.min1,  # 1分钟
    adj='none'
)

# 5分钟K线
min5_kline = base_data.get_kline(
    code='600519.SH',
    start_date=20260520,
    end_date=20260520,
    period=ad.constant.Period.min5,
    adj='none'
)
```

### Period 常量

```python
ad.constant.Period.min1    # 1分钟
ad.constant.Period.min3    # 3分钟
ad.constant.Period.min5    # 5分钟
ad.constant.Period.min15   # 15分钟
ad.constant.Period.min30   # 30分钟
ad.constant.Period.min60   # 60分钟
ad.constant.Period.day     # 日线
ad.constant.Period.week    # 周线
ad.constant.Period.month   # 月线
ad.constant.Period.season  # 季线
ad.constant.Period.year    # 年线
```

---

## 实时行情订阅

```python
sub_data = ad.SubscribeData()

@sub_data.register(code_list=['600519.SH'], period=ad.constant.Period.snapshot)
def on_snapshot(data, period):
    print(f'代码: {data.code}')
    print(f'最新价: {data.price}')
    print(f'今开: {data.open}')
    print(f'最高: {data.high}')
    print(f'最低: {data.low}')
    print(f'成交量: {data.volume}')
    print(f'成交额: {data.amount}')
    print(f'时间: {data.time}')

# 运行订阅（会阻塞）
sub_data.run()
```

### Snapshot 字段

```python
data.code           # 证券代码
data.price          # 最新价
data.open           # 今开
data.high           # 最高
data.low            # 最低
data.volume         # 成交量
data.amount         # 成交额
data.time           # 时间
data.pre_close      # 昨收
data.high_limited   # 涨停价
data.low_limited    # 跌停价
data.num_trades     # 成交笔数
# 买卖盘
data.ask_price1    # 卖一价
data.ask_volume1    # 卖一量
data.bid_price1     # 买一价
data.bid_volume1    # 买一量
# ... 还有买卖2-5档
```

### 指数快照

```python
@sub_data.register(code_list=['000001.SH'], period=ad.constant.Period.snapshot)
def on_index(data, period):
    print(f'指数: {data.code}')
    print(f'最新: {data.price}')
    print(f'涨跌: {data.change}')
    print(f'涨跌幅: {data.change_pct}%')
```

---

## 指标数据

```python
info_data = ad.InfoData()

# 技术指标
indicator = info_data.get_indicator(['600519.SH'])
```

---

## 概念板块

```python
# 概念指数列表
concept_index = info_data.get_concept_index()

# 概念成分股
concept_stocks = info_data.get_concept_stocks(concept_code='BK0001')

# 行业列表
industry_info = info_data.get_industry_base_info()

# 行业成分股
industry_stocks = info_data.get_industry_constituent(industry_list)

# 行业权重
industry_weight = info_data.get_industry_weight(industry_list)
```

---

## 指数数据

```python
# 指数成分股
constituent = info_data.get_index_constituent(['000300.SH'])  # 沪深300

# 指数权重
weight = info_data.get_index_weight(['000300.SH', '000016.SH'])

# 沪股通/深股通
cnc_snapshot = info_data.get_cnc_snapshot()  # 沪港通快照
```

---

## 龙虎榜 & 融资融券

```python
# 融资融券汇总
margin_summary = info_data.get_margin_summary()

# 融资融券明细
margin_detail = info_data.get_margin_detail(['600519.SH'])

# 龙虎榜
long_hu_bang = info_data.get_long_hu_bang(['600519.SH'])
```

---

## ETF 数据

```python
# ETF 实时净值
iopv = info_data.get_fund_iopv(['516850.SH'])

# ETF 净值
nav = info_data.get_fund_nav(['516850.SH'])

# ETF 份额变动
share = info_data.get_fund_share(['516850.SH'])

# ETF 申购赎回
purchase = info_data.get_etf_purchase_redemption(['516850.SH'])
```

---

## 可转债数据

```python
# 可转债基本信息
kzz_basic = info_data.get_kzz_issuance(['113050.SH'])

# 可转债转股
kzz_conv = info_data.get_kzz_conv(['113050.SH'])

# 可转债赎回
kzz_call = info_data.get_kzz_call(['113050.SH'])

# 可转债回售
kzz_put = info_data.get_kzz_put(['113050.SH'])

# 可转债转股变动
kzz_change = info_data.get_kzz_conv_change(['113050.SH'])

# 可转债暂停转股
kzz_suspend = info_data.get_kzz_suspend(['113050.SH'])
```

---

## 期权数据

```python
# 期权基本信息
option_basic = info_data.get_option_basic_info(['10004633.SH'])

# 月期权合约要素
option_std = info_data.get_option_std_ctr_specs('10004633.SH')

# 商品期权合约要素
option_com = info_data.get_option_mon_ctr_specs('CU')

# 期权希腊值
kzz_corr = info_data.get_kzz_corr(['10004633.SH'])
```

---

## 国债收益率

```python
# 国债收益率曲线
treasury = info_data.get_treasury_yield(['m3', 'm6', 'y1', 'y2', 'y3', 'y5', 'y7', 'y10', 'y30'])
```

---

## 复权因子

```python
base_data = ad.BaseData()

# 获取复权因子
adj_factor = base_data.get_adj_factor(
    ['600519.SH'],
    local_path='D:/data/',
    is_local=False
)

# 获取后复权因子
backward_factor = base_data.get_backward_factor(
    ['600519.SH'],
    local_path='D:/data/',
    is_local=False
)
```

---

## 历史数据

```python
# 获取某日期区间的代码列表
all_codes = base_data.get_hist_code_list(
    security_type='EXTRA_STOCK_A_SH_SZ',
    start_date=20260101,
    end_date=20260520
)

# 历史股票状态
history_status = info_data.get_history_stock_status(['600519.SH'])

# 大宗交易
block_trading = info_data.get_block_trading(['600519.SH'])
```

---

## 常见问题

### Q: 登录失败？
- 检查用户名密码是否正确
- 检查服务器地址和端口是否正确
- 检查网络是否能访问服务器

### Q: 订阅没有数据？
- 账户可能没有实时行情权限
- 某些数据需要在交易日才能获取
- 尝试设置 `socket.setdefaulttimeout(15)`

### Q: K线数据为空？
- 检查日期格式是否为 YYYYMMDD 整数
- 检查股票代码是否正确（如 600519.SH）
- 某些股票可能停牌

---

## 数据类型速查

| 类型 | 说明 |
|------|------|
| Snapshot | 股票快照 |
| SnapshotIndex | 指数快照 |
| SnapshotFuture | 期货快照 |
| SnapshotETF | ETF快照 |
| SnapshotHKT | 沪深港通快照 |
| SnapshotOption | 期权快照 |

---

## 完整示例：查询茅台

```python
import AmazingData as ad
import socket
socket.setdefaulttimeout(15)

# 登录
ad.login(username='你的用户名', password='你的密码', host='服务器', port=8600)

# 创建数据对象
base_data = ad.BaseData()
info_data = ad.InfoData()

# 找茅台
stocks = base_data.get_code_list(security_type='EXTRA_STOCK_A')
maotai = '600519.SH'

# 基本信息
basic = info_data.get_stock_basic([maotai])

# 日K线（最近30天）
daily = base_data.get_kline(
    code=maotai,
    start_date=20260420,
    end_date=20260520,
    period=ad.constant.Period.day,
    adj='qfq'
)

# 财务数据
financial = info_data.get_financial_index(
    [maotai],
    start_date=20260101,
    end_date=20260401,
    retrench_type='basic'
)

print(f'股票: {maotai}')
print(f'K线数据: {len(daily)} 条')
print(f'财务数据: {len(financial)} 条')
```