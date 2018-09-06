# <center> study python </center>

## list��ѧϰʹ��

### 1. ���ɾ���޸ģ�

+ ���룺 append(β�巨���� insert��ע�������������λ�ã�
+ ɾ���޸ģ� delete��֪����������pop��Ĭ��ɾ������һ�������������������            remove�����ݸ�����ֵɾ����ֻɾ���б��еĵ�һ����
+ ���� sort�����������򣩣�sorted����ʱ��������ͨ����Ӳ������з�������         ����ֱ�ӷ��������reverse��

### 2. �б�ѧϰʹ�ã�

+ forѭ���ı�����ע��pythonֻ����������ģ�黯�������ر�ע��
+ ��ֵ�б�Ĵ�����range������ʹ��listʹ��range����������ֱ��ת��Ϊ�б�֧�ִ������б� : exp[ ]��ʹ��3 4 �д��룬����׶�

>number = list(range(1,5))
>number = [1,2,3,4]

+ �򵥵�ͳ�ƣ�max��min��sum
+ ͨ���б���������б�: ��forѭ���ϲ�
> squares = [value**2 for value in range(1,11)]
> squares = [1,4,9,16,25,36,49,64,81,100] 

+ ʹ���б�Ĳ���: list[1:4]/[:4]/[1:] ���ǵø��������Ǵ��б�ĩβ��ʼ��ǰ����������[-3:]Ҳ��ȷ
+ ʹ���б��ȫ���� list[:],ֻ�ã�ʡ�Է�Χ
+ ʹ��in���Լ���Ԫ�Ƿ����б���
> car = ["bmw", "benz", "other"]
> "bmw" in car  (true) // "dazhong" in car (false)
+ ʹ��len��ȡ�б���
+ <font color  = "red">forѭ���еĵ�������</font>�� for index in range(len(numbers)): ���������������������Ҫ�õ�len����������ĳ��ȣ���range������������

### 3.Ԫ��ѧϰʹ�ã�

+ <font color  = "red">Ԫ��<font color = "blue"><b>Ԫ��</b></font>�������޸ģ�����</font>
+ ����Ԫ�飬ʹ�õ���dimension = ��200,50��Բ���ţ�������Ȼ��ʹ�÷���������ֻ��dimension = ��400,100����ʽ��Ԫ����������޸�

## if���ѧϰ

### �������﷨֪ʶ��

+ if�� elif��...... else �����֮���<b><font color = "red" size = 5px > : </font></b>

## �ֵ�ѧϰ

### 1.������

+ ʹ��dictionary_name = {"key" : value, }�����м��� ����  ��ֵ��һһ��Ӧ.
+ ֱ�Ӽ����µ�key-value������ӣ�ʹ��
> delete dictionary_name['key'] ɾ��
+ ������
> ʹ��<font color = "red">item</font>�������м���
> ʹ��<font color = "blue">keys</font>�������м� ,��sorted(dictionary_name.keys()),ʹ�ð��ռ�����ֵ��˳���������ֵ���������ʱ�򲻴���׺��Ĭ�ϵ��ڱ���keys
> ʹ��<font color = "green">value</font>��������ֵ��ʹ��set(dictionary_name.values())�޳��б��е��ظ��

### 2.Ƕ�ף�

+ �ֵ��б� �� �����ֵ�洢���б��У�

> aline_0 : {"color":"red", "points" : 10 }
> alien_1 : {"color":"red", "points" : 13 }
> alien = [alien_0, alien_1]

+ �б��ֵ䣺 �����б�洢���ֵ��У�

> alien : {"color" : "red" , "interest" :<font color = "red">["football", "sing" , "dance"]</font> , }

+ �ֵ��д洢�ֵ�:

> users = {
    'ss' : {
       'first' : "shuang",
       'last' : "song",
       'local' : "shuifu",
    },
   'zyh' : {
        'first' : "yuehang",
        'last' : "zhang",
        'local' : "yunnan",
    },    
}

<font color = "Red">ע�⣺</font>������ÿλ�û����ֵ�ṹ��������ͬ������ʹ���ֵ�ṹ����ǿ��Ƕ�״�������ף���Ȼpython��û������Ҫ��

## ����ѧϰ

### 1.��������

+ λ��ʵ��
> def animal_name(animal_type, pet_name):

ʹ��ʱ��animal_name(dog, xiamai)���������˳����ʵ���л��������

+ �ؼ���ʵ��
> def animal_name(animal_type, pet_name):

ʹ��ʱ��animal_name(animal_type = "dog", pet_name = "xiamai")
���߿���������animal_name(pet_name = "xiaoai", animal_name = "dog")

+ ʹ��Ĭ���β�
> def animal_name(pet_name, animal_name = "dog")
�ȿ�����ʽ�ĸ������ṩʵ�Σ�Ҳ��ʹ�ú�����Ĭ���β�

�磺animal_name("xiaoai") ����  animal_name("xiaoai", "cat")

+ �����б��б���������֣����ֻ����ֵ䣬��Ȼ�ں������޸��б�֮���ı��б�����ݣ���������޸��б����ݣ�����ʹ�����·�����
> def function(formal_par):  #����ʵ��
���ã�function(list_name[:]) #�������ݸ���

+ �������������ββ��ҽ��ʹ��λ���β�
> def function(first, second, **other):  #����ʵ��
�ڶ���������ͺ�����ʱ�򣬱��뽫���������������βη������python��ƥ��λ���βκ͹ؼ����βΣ����ʣ���ʵ�ζ��ռ�������һ���β��С�
