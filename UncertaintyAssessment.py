#不确定性计算
from scipy.stats import norm

#风数据不确定性计算
def Wind_data():
    #定义全局变量wind_data
    global wind_data
    print('开始风资源数据不确定性计算，各参考参数如下！\n测风 2-5%\n长期订正 2-5%\n年际变化 2-6%\n未来气候变化 暂无确定值，可取2%\n其它 2%\n请分别输入上述参数取值，整数即可，以空格键隔开')
    while True:
        try:
            a,b,c,d,e = map(int,input().split())
            if a > 5 or a < 2:
                print('输入有误！请重新输入！')
                continue
            elif b > 5 or b < 2:
                print('输入有误！请重新输入！')
                continue
            elif c > 6 or c < 2:
                print('输入有误！请重新输入！')
                continue
            elif d > 10 or d < 0:
                print('输入有误！请重新输入！')
                continue
            elif e > 5 or e < 0:
                print('输入有误！请重新输入！')
                continue
            break
        except ValueError:
            print('输入有误！请重新输入')
    wind_data = (a**2 + b**2 + c**2 + d**2 + e**2)**0.5
    print('风数据不确定性为：{:.2f}%'.format(wind_data))

#风资源计算模型不确定性
def Wind_model():
    global wind_model
    print('\n开始风资源计算模型不确定性计算，各参考参数如下！\n垂直外推 0-5%\n水平外推 0-5%\n其它模型相关 无 可取值2%\n请分别输入上述参数取值，整数即可，以空格键隔开')
    while True:
        try:
            a,b,c = map(int,input().split())
            if a > 5 or a < 0:
                print('输入有误！请重新输入！')
                continue
            elif b > 5 or b < 0:
                print('输入有误！请重新输入！')
                continue
            elif c > 10 or c < 0:
                print('输入有误！请重新输入！')
                continue
            break
        except ValueError:
            print('输入有误！请重新输入')
    wind_model = (a**2 + b**2 + c**2)**0.5
    print('计算模型不确定性为：{:.2f}%'.format(wind_model))

#能量转换不确定性
def Power_conversion():
    global power_conversion

    print('\n开始能量转换不确定性计算，各参考参数如下！\n功率曲线 5-10%\n计量 0-2%\n其它AEP相关 无 可取值2%\n请分别输入上述参数取值，整数即可，以空格键隔开')
    while True:
        try:
            a,b,c = map(int,input().split())
            if a > 10 or a < 5:
                print('输入有误！请重新输入！')
                continue
            elif b > 2 or b < 0:
                print('输入有误！请重新输入！')
                continue
            elif c > 10 or c < 0:
                print('输入有误！请重新输入！')
                continue
            break
        except ValueError:
            print('输入有误！请重新输入')
    power_conversion = (a**2 + b**2 + c**2)**0.5
    print('能量转换不确定性为：{:.2f}%'.format(power_conversion))

#w尾流损失不确定性
def Loss():
    global wake_effects
    print('\n尾流不确定性参考计算结果，参考值5.2%\n请输入尾流损失不确定性:')
    while True:
        try:
            a = input()
            if a.isspace():
                print('输入有误，请重新输入！')
                continue
            elif float(a) > 12 or float(a) <0:
                print('超出计算范围，请重新输入！')
                continue
            break
        except ValueError:
            print('输入有误！请重新输入')
    wake_effects = float(a)
    print(wake_effects)

#所有不确定性之和
def All_un():
    global all_un
    all_un = (wind_data**2+wind_model**2+power_conversion**2+wake_effects**2)**0.5
    print('\n总不确定性为: {:.1f}%\n'.format(all_un))

#不确定性
def Reduction_factor():
    global P50,P75_S,P84_S,P90_S,P99_S
    P50 = 85/100
    P75_S = 75/100
    P84_S = 84/100
    P90_S = 90/100
    P99_S = 99/100
    print('P50 不确定性 ：{:.1f}%\n'.format(P50 * 100))
    P75 = (1 - all_un * norm.ppf(P75_S) / 100) * P50
    print('P75 不确定性 : {:.1f}%'.format(P75 * 100))
    P84 = (1 - all_un * norm.ppf(P84_S) / 100) * P50
    print('P84 不确定性 : {:.1f}%'.format(P84 * 100))
    P90 = (1 - all_un * norm.ppf(P90_S) / 100) * P50
    print('P90 不确定性 : {:.1f}%'.format(P90 * 100))
    P99 = (1 - all_un * norm.ppf(P99_S) / 100) * P50
    print('P99 不确定性 : {:.1f}%'.format(P99 * 100))

if __name__=='__main__':

    Wind_data()
    Wind_model()
    Power_conversion()
    Loss()
    All_un()
    Reduction_factor()
    input("按 'Enter' 退出 !")

