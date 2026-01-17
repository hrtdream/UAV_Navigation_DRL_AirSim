import airsim
import time

print("开始连接...")
client = airsim.MultirotorClient()

# ping() 会返回 True 如果连接成功，不会无限卡死
if client.ping():
    print("✅ 连接成功！AirSim 正常工作。")
    client.confirmConnection()
    print("API 控制权已获取。")
else:
    print("❌ 连接失败。请检查：")
    print("1. UE4 是否正在播放？")
    print("2. settings.json 是否为 Multirotor？")