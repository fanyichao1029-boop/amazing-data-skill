# -*- coding: utf-8 -*-
"""
AmazingData 快速测试脚本
测试连接和数据获取
"""

import AmazingData as ad
import socket

def test_connection(username: str, password: str, host: str, port: int):
    """测试 AmazingData 连接"""
    print("=" * 50)
    print("AmazingData 连接测试")
    print("=" * 50)

    # 设置超时
    socket.setdefaulttimeout(15)

    # 登录
    print(f"\n1. 登录到 {host}:{port}...")
    try:
        ad.login(username=username, password=password, host=host, port=port)
        print("   登录成功！")
    except Exception as e:
        print(f"   登录失败: {e}")
        return False

    # 获取数据
    base_data = ad.BaseData()

    # 2. A股列表
    print("\n2. 获取A股列表...")
    stocks = base_data.get_code_list(security_type='EXTRA_STOCK_A')
    print(f"   A股总数: {len(stocks)}")

    # 3. 找茅台
    print("\n3. 查找茅台...")
    maotai = [s for s in stocks if '600519' in s]
    if maotai:
        print(f"   茅台代码: {maotai[0]}")
    else:
        print("   未找到茅台")

    # 4. ETF列表
    print("\n4. 获取ETF列表...")
    etf = base_data.get_code_list(security_type='EXTRA_ETF')
    print(f"   ETF总数: {len(etf)}")

    print("\n" + "=" * 50)
    print("测试完成！")
    print("=" * 50)
    return True


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 5:
        username = sys.argv[1]
        password = sys.argv[2]
        host = sys.argv[3]
        port = int(sys.argv[4])
    else:
        print("用法: python quick-demo.py <用户名> <密码> <服务器> <端口>")
        print("示例: python quick-demo.py 11100066430 mypassword 120.86.124.106 8600")
        sys.exit(1)

    test_connection(username, password, host, port)