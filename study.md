# <center> study python </center>

## list的学习使用

### 1. 添加删除修改：

+ 插入： append(尾插法）； insert（注意必须包含插入的位置）
+ 删除修改： delete（知道索引）；pop（默认删除最后的一个，可以添加索引）；            remove（根据给定的值删除，只删除列表中的第一个）
+ 排序： sort（永久性排序）；sorted（暂时），可以通过添加参数进行反向排序         或者直接反向输出（reverse）

### 2. 列表学习使用：

+ for循环的遍历：注意python只靠缩进进行模块化，所以特别注意
+ 数值列表的创建：range（），使用list使得range创建的数字直接转化为列表，支持创建空列表 : exp[ ]，使用3 4 行代码，简洁易懂

>number = list(range(1,5))
>number = [1,2,3,4]

+ 简单的统计：max，min，sum
+ 通过列表解析创建列表: 与for循环合并
> squares = [value**2 for value in range(1,11)]
> squares = [1,4,9,16,25,36,49,64,81,100] 

+ 使用列表的部分: list[1:4]/[:4]/[1:] （记得负数索引是从列表末尾开始向前计数，所以[-3:]也正确
+ 使用列表的全部： list[:],只用：省略范围
+ 使用in可以检验元是否在列表中
> car = ["bmw", "benz", "other"]
> "bmw" in car  (true) // "dazhong" in car (false)
+ 使用len获取列表长度

### 3.元组学习使用：

+ <font color  = "red">元组<font color = "blue"><b>元素</b></font>不可以修改！！！</font>
+ 定义元组，使用的是dimension = （200,50）圆括号，访问依然是使用方括。可以只用dimension = （400,100）方式对元组变量进行修改

## if语句学习

### 基础的语法知识：

+ if； elif；...... else 在语句之后加<b><font color = "red" size = 5px > : </font></b>

## 字典学习

### 1.基础：

+ 使用dictionary_name = {"key" : value, }在其中键入 “键  ：值”一一对应.
+ 直接键入新的key-value进行添加，使用
> delete dictionary_name['key'] 删除
+ 遍历：
> 使用<font color = "red">item</font>遍历所有键对
> 使用<font color = "blue">keys</font>遍历所有键 ,用sorted(dictionary_name.keys()),使得按照键入的字典的顺序遍历所有值。
> 使用<font color = "green">value</font>遍历所有值，使用set(dictionary_name.values())剔除列表中的重复项。

### 2.嵌套：

+ 字典列表 ： （把字典存储在列表中）

> aline_0 : {"color":"red", "points" : 10 }
> alien_1 : {"color":"red", "points" : 13 }
> alien = [alien_0, alien_1]

+ 列表字典： （将列表存储到字典中）

> alien : {"color" : "red" , "interest" :<font color = "red">["football", "sing" , "dance"]</font> , }

+ 字典中存储字典:

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

<font color = "Red">注意：</font>尽量在每位用户的字典结构都保持相同，这样使得字典结构化较强，嵌套处理更容易（虽然python并没有特殊要求）

## 函数学习



