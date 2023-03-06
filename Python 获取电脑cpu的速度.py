'''
cpu的速度用时钟频率来衡量，它是1秒内发生的同步脉冲数，单位是Hz（赫兹），通常来说，频率越大，cpu的性能越强劲，以3个最常用的系统为目标，研究一下，如何用python来获取电脑的cpu频率。
程序应当可以识别出不同的操作系统，并根据操作系统的不同来采用对应的方法获取cpu的速度，标准模块platform 可以获取平台的信息，platform.system() 可以获取操作系统的名称，下面是该方法在各个操作系统下执行时返回的名称

mac 上返回 Darwin
linux 上返回 Linux
windows 上返回 Windows 或者 Win32
'''
import platform
import subprocess
import fileinput


def get_mac_cpu_speed():
    commond = 'system_profiler SPHardwareDataType | grep "Processor Speed" | cut -d ":" -f2'
    proc = subprocess.Popen([commond], shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    output = output.decode()   # bytes 转str
    speed = output.lstrip().rstrip('\n')
    return speed


def get_linux_cpu_speed():
    for line in fileinput.input('/proc/cpuinfo'):
        if 'MHz' in line:
            value = line.split(':')[1].strip()
            value = float(value)
            speed = round(value / 1024, 1)
            return "{speed} GHz".format(speed=speed)


def get_windows_cpu_speed():
    import winreg
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
    speed, type = winreg.QueryValueEx(key, "~MHz")
    speed = round(float(speed)/1024, 1)
    return "{speed} GHz".format(speed=speed)


def get_cpu_speed():
    osname = platform.system()  # 获取操作系统的名称
    speed = ''
    if osname == "Darwin":
        speed = get_mac_cpu_speed()
    if osname == "Linux":
        speed = get_linux_cpu_speed()
    if osname in ["Windows", "Win32"]:
        speed = get_windows_cpu_speed()

    return speed

print(get_cpu_speed())