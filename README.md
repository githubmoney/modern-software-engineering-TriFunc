# 现代软件工程
## 总体设计
### 三角函数计算器总体设计

* 顶层模块
 * 角度弧度转换模块
   * `角度转弧度`函数
 * 三角函数计算模块
   * `sin`函数
   * `cos`函数
   * `arcsin`函数
   * `arctan`函数
 * 界面显示模块
   * `用户输入`模块
   * `计算`模块
   * `结果输出`模块
 * 测试模块


## 详细设计
具体功能实现方法及具体数据结构
* 数据结构约束
  * 角度弧度值均采用`float`型数据，保留小数点后`9`位
* 三角函数计算算法
  * 具体实现:计算过程利用函数实现,函数名统一为`小写三角函数名`,如`sin、cos`,输入输出遵循数据结构约束,且函数输入为`弧度`，函数名统一命名为其相应的三角函数名，如`def sin(input)`，方便主函数进行相关调用。
* 界面显示
  * 通过在`界面类`里定义相应方法，对需要进行计算的函数进行调用计算，然后通过将此方法与按钮事件相连接，最终在界面上输出显示计算结果。


## 计算模块文件命名规则
* 三角函数模块文件：`Func_`加上各自对应的三角函数名称（首字母大写）,如`Func_Sin`
* 角度转弧度模块文件命名为：`Func_Angle2Radian`


## 测试模块
* 测试模块不单独编写函数进行实现，而是采用在各函数内部进行测试的方式，通过在`循环内生成随机数`并各自计算 `编写的函数值`与`python提供的内置方法`所计算的函数值进行`减法运算`，通过事先确定的`阈值`与`差值`进行比较来确定编写的函数是否正确及可用。用户可通过在界面上输入`想要测试的值`并通过`test`按钮进行相关测试，测试结果将输出到界面上。


## Display
* 对应整个显示模块,使用PyQt进行开发
* ![image](https://user-images.githubusercontent.com/57553584/160834662-907762d2-21c2-4842-a074-d413037c45d0.png)


## 角度转弧度函数
* 函数命名为`angle2radian`；参数为angle，即输入的角度值
* 弧度(radian)=角度(angle)*π(pi)/180
* 根据公式计算得到转换后的弧度值，返回该弧度值
* 函数的部分测试结果如下图：
* ![image](https://user-images.githubusercontent.com/97205517/161012380-5a3e996f-ae68-444f-87c2-6b688e27d814.png)


## sin函数计算模块
* 测试结果
* ![image](https://user-images.githubusercontent.com/57553584/161010282-e7fcc91f-1e0c-4112-af6f-b06c267be64a.png)


## cos函数计算模块
* 函数实现思想是通过泰勒公式展开，在一定的取值范围内进行收敛;
* 输入数值范围为弧度制浮点数-1到1;
* 精度范围为小数点后六位;
* 测试函数予以验证是否满足精度要求(满足要求返回值为True,否则为False);
* cos函数计算模块测试结果:
* ![image](https://user-images.githubusercontent.com/57553584/161010402-b31ba88d-2573-4db8-8a26-1bb4d9049ed2.png)


## arcsin函数计算模块
* 使用泰勒级数展开逼近
* 输入范围从-1到1
* 精度范围为小数点后九位
* arcsin函数计算模块测试结果
* ![1648643010(1)](https://user-images.githubusercontent.com/101335052/160833494-2e083cb4-7c97-41ab-8f5e-c7f8c4571534.png)


## arctan函数计算模块
* 使用泰勒级数展开逼近
* arctan函数是正切函数y=tanx在开区间（x∈(-π/2,π/2)）的反函数，记作y=arctanx 或 y=tan-1x，叫做反正切函数。它表示(-π/2,π/2)上正切值等于 x 的那个唯一确定的角，即tan(arctan x)=x;
* 反正切函数的定义域为R即(-∞，+∞);
* 值 域：(-π/2,π/2);
* 函数实现思想是通过泰勒公式展开，在一定的取值范围内进行收敛;
* 结果保留小数点后９位;
* 测试函数予以验证是否满足精度要求(满足要求返回值为True,否则为False).
* 经测试，当循环取到100000000时，arctan(1)无法得出结果。
* 测试结果：
* ![arctan](https://github.com/yanghaan/picture/blob/main/2.png)
  


