import  time
import  pygame


path="/Users/zzs/Downloads/iOSProject-master/iOSProject/iOSProject/Classes/QQ音乐/QQResources/MP3s/235319.mp3"

# 初始化
pygame.mixer.init()
# 加载音乐
track=pygame.mixer.music.load(path)
# 播放
pygame.mixer.music.play()

time.sleep(10)
#停止
pygame.mixer.music.stop()
# 暂停
# pygame.mixer.music.pause()