import numpy as np
import random
import time

cdata=open('C:/Users/lenovo/Desktop/classdata.txt')
cname=[]
cnt=0
for line in cdata:
    cname.append(line.strip())
    cnt=cnt+1

data1=open('C:/Users/lenovo/Desktop/数据库实验/data11.txt','w')
data2=open('C:/Users/lenovo/Desktop/数据库实验/data22.txt','w')
data3=open('C:/Users/lenovo/Desktop/数据库实验/data33.txt','w')
sid_list=[]
cid_list=[]
sc_set=set()
def random_s():
    sid=random.choice(['020','040','050','060','070','080','090'])
    for num in range(0,5):
        sid=sid+str(random.randint(0,9))
    return sid

def random_c():
    cid=random.choice(['CS','EE','ME','CE','IE','AE','BE','ChE','Chem','Phys','Econ','Bio','Math','Stat','Ling'])
    return cid+'-'+str(random.randint(0,9))+str(random.randint(0,9))
def random_name(jud):
    # 删减部分小众姓氏
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"
    # 百家姓中双姓氏
    firstName2="万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空亓官司寇仉督子颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁段干百里东郭南门呼延羊舌微生梁丘左丘东门西门南宫南宫"
    # 女孩名字
    girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
    # 男孩名字
    boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
    # 名
    name = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'
 
    # 10%的机遇生成双数姓氏
    if random.choice(range(100))>10:
        firstName_name =firstName[random.choice(range(len(firstName)))]
    else:
        i = random.choice(range(len(firstName2)))
        firstName_name =firstName2[i:i+2]
 
    sex = random.choice(range(2))
    name_1 = ""
    # 生成并返回一个名字
    if sex > 0:
        girl_name = girl[random.choice(range(len(girl)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        if jud==0:
            return firstName_name + name_1 + girl_name +"\t女"
        else:
            return firstName_name + name_1 + girl_name
    else:
        boy_name = boy[random.choice(range(len(boy)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        if jud==0:
            return firstName_name + name_1 + boy_name+"\t男"
        else:
            return firstName_name + name_1 + boy_name

def random_bdate():
    a1=(2000,1,1,0,0,0,0,0,0)    #设置开始日期时间元组（2000-01-01 00：00：00）
    a2=(2004,12,31,0,0,0,0,0,0)    #设置结束日期时间元组（2004-12-31 00：00：00）
    start=time.mktime(a1)
    end=time.mktime(a2)
    t=random.randint(start,end)
    date_touple=time.localtime(t)
    date_str=time.strftime("%Y-%m-%d %H:%M:%S",date_touple)
    return date_str

def random_height():
    height=random.uniform(1.40,2.00)
    return str(round(height,2))

def random_dorm():
    return random.choice('东南西北')+str(random.randint(1,25))+'舍'+str(random.randint(1,9))+str(random.randint(0,3))+str(random.randint(1,9))

def random_period():
    period=random.randint(1,10)
    return str(period*16)

def random_credit():
    return random.choice(['0.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0','9.5'])

def random_grade():
    if random.choice(range(100))<20: #20%概率不及格
        return str(round(random.uniform(0,59),1))
    else:
        return str(round(random.uniform(60,100),1))

a=int(input())
ca=a
b=int(input())
cb=b
c=int(input())
data1.write("s#\tsname\tsex\tbdate\theight\tdorm\n")
data2.write("c#\tcname\tperiod\tcredit\tteacher\n")
data3.write("s#\tc#\tgrade\n")
while ca>0:#生成学号
    nsid=random_s()
    if(nsid in sid_list):
        ca=ca+1
    else:
        sid_list.append(nsid)
    ca=ca-1
while a>0:#创建S742数据
    data1.write(sid_list[ca])
    ca=ca+1
    data1.write("\t")
    data1.write(random_name(0))
    data1.write("\t")
    data1.write(random_bdate())
    data1.write("\t")
    data1.write(random_height())
    data1.write("\t")
    data1.write(random_dorm())
    data1.write("\n")
    a=a-1
while cb>0:
    ncid=random_c()
    if(ncid in cid_list):
        cb=cb+1
    else:
        cid_list.append(ncid)
    cb=cb-1
while b>0:#创建C742数据
    data2.write(cid_list[cb])
    data2.write("\t")
    cb=cb+1
    data2.write(cname[random.randint(0,cnt-1)])
    data2.write("\t")
    data2.write(random_period())
    data2.write("\t")
    data2.write(random_credit())
    data2.write("\t")
    data2.write(random_name(1))
    data2.write("\n")
    b=b-1
while c>0:#创建SC742数据
    sid=random.choice(sid_list)
    cid=random.choice(cid_list)
    if(sid,cid) in sc_set:
        continue
    else:
        sc_set.add((sid,cid))
    data3.write(sid)
    data3.write("\t")
    data3.write(cid)
    data3.write("\t")
    data3.write(random_grade())
    data3.write("\n")
    c=c-1
data1.close()
data2.close()
data3.close()