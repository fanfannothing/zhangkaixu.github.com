<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link href="http://jasonm23.github.com/markdown-css-themes/foghorn.css" rel="stylesheet"></link>

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<title>中文分词模型简介</title>

#中文分词模型简介
*   本文基于作者的学位论文的引言部分，是对当前常用的一套分词模型的介绍和梳理。
*   如果对文字有任何疑问或意见，欢迎[在此留言](http://cws.miniban.cn/)，或联系[作者](http://weibo.com/zhangkaixu)。
*   想了解更多？请参考[中文分词文献列表](http://zhangkaixu.github.com/bibpage/cws.html)。

##最优化问题建模

设$X$是需要分词的原始句子，例如

>   `材料利用率高`

设$Y$是分好词的分词结果，例如

>   `材料 利用率 高`

我们知道一个原始句子可能的分词结果不止一种， 设$X$对应的所有可能的分词结果为$\text{Gen}(X)$， 那么有$Y\in\text{Gen}(X)$。

分词模型的任务，就是对于给定的输入$X$， 从所有可能的分词结果中， 找到一个最好的分词结果$\hat{Y}$， 可以形式化为：

$$\hat{Y}=\arg\max_{Y\in \text{Gen}(X)}f(Y,\Lambda)$$

这里的$f$可称为<a name="object">目标函数</a>， 代表着分词模型的结构、机制， $\Lambda$是一个参数向量， 代表着模型的参数。 一个分词模型就是由$f$和$\Lambda$确定的。

##目标函数线性分解

下面深入到模型的设计部分，而这部分只与通用的机器学习算法有关，与分词这个具体问题无关。

通常，会将一个[目标函数](#object)分解成一个特征向量与模型参数向量的点积：

$$f(Y,\Lambda)=\Phi(Y) ^ T \cdot \Lambda$$

为了方便起见，不妨将向量的定义做一个等价的扩展，传统的向量的下标是从$1$开始的连续自然数，在此，向量的下标可以是任意多元组。（只要这种多元组的数量是有限的，就与传统的向量等价。）

而一个关于$Y$的特征向量$\Phi(Y)$，可以通过如下方式计算得到：

>   `1: set` $\Phi(Y)=\mathbf{0}$  
>   `2: for` $\text{feature}$ `in` $\text{features_of}(Y)$:  
>   `3: - - ` $\Phi(Y)[\text{feature}]=\Phi(Y)[\text{feature}]+1$  

这里函数$\text{features_of}(Y)$负责生成与$Y$有关的所有特征。

##分词特征设计

这部分讨论针对分词任务设计的特征。

为了便于表述，在此定义$x _ i$为原始句子$X$第$i+1$个字，如当$X$为“`材料利用率高`”时，$x _ 0 =\text{材}$，$x _ 3 = \text{用}$。$a _ i$表示分词结果$Y$中第$i$个字与后一个字之间是否是词的边界（是用$\text{s}$表示，否用$\text{c}$表示），如当$Y$为“`材料 利用率 高`”时，$a _ 1 = \text{c}$， $a _ 2 =\text{s}$。

这里给出一组特征的设计，作为函数$\text{features_of}(Y)$返回的结果：

>   $(1,x _ i,a _ i,a _ {i+1})$, $i\in \[0\dots |X|)$<br/>
>   $(2,x _ {i-1},a _ i,a _ {i+1})$, $i\in \[0\dots |X|)$<br/>
>   $(3,x _ {i+1},a _ i,a _ {i+1})$, $i\in \[0\dots |X|)$<br/>
>   $(4,x _ {i-2}, x _ {i-1},a _ i,a _ {i+1})$, $i\in \[0\dots |X|)$<br/>
>   $(5,x _ {i-1}, x _ {i},a _ i,a _ {i+1})$, $i\in \[0\dots |X|)$<br/>
>   $(6,x _ {i}, x _ {i+1},a _ i,a _ {i+1})$, $i\in \[0\dots |X|)$<br/>
>   $(7,x _ {i+1}, x _ {i+2},a _ i,a _ {i+1})$, $i\in \[0\dots |X|)$<br/>
>   $(8,a _ {i-1},a _ i,a _ {i+1})$, $i\in \[0\dots |X|)$<br/>

还是以$Y$为“`材料 利用率 高`”时为例，此时$\Phi(Y)[ (1,\text{料},\text{c},\text{s}) ] = 1$，而$\Phi(Y)[ (8,\text{s},\text{s},\text{s}) ] = 0$，注意，向量某些维的分量可以大于$1$。

这样，对于任意分词结果$Y$，可以通过以上定义的函数$\text{features_of}(Y)$确定特征向量$\Phi(Y)$，然后乘以$\Lambda$就可以得到目标函数的值，以此来判断分词结果的好坏。

##模型参数学习

以上的讨论已经将模型的特征向量确定下来，接下来，讨论如何确定参数向量$\Lambda$。

为了确定参数向量，需要一个训练集$\\{(X _ i, Y^* _ i)| i = 1 \dots N \\}$，也就是一个原始句子的集合，其中的句子$X _ i$所对应的正确的分词结果$Y _ i$是已知的（这也就是基于统计的经验主义方法的哲学）。

然后使用一种算法学习参数向量，在此给出一种叫做“平均感知器”的学习算法：
>   `1: set` $\Lambda=\mathbf{0}$<br/>
>   `2: for` $t$ `in` $[0,T)$:<br/>
>   `3: - - ` `for` $i$ `in` $[1, N ] $:<br/>
>   `4: - - - - ` $\hat{Y} _ i=\arg\max{f(Y,\Lambda)}$<br/>
>   `5: - - - - ` $\Lambda=\Lambda - \Phi(\hat{Y} _ i) + \Phi(Y^ * _ i)$<br/>
>   `6: - - - - ` $\Lambda _ {t,i}=\Lambda$<br/>
>   `7: return` $\overline{\Lambda _ {t,i}}$

##模型评价

以上已经讨论了分词模型的构造和通过训练集进行参数学习的算法。当模型的结构和参数都已经确定之后，还需要评价其分词的效果。

这时候，需要一个测试集，其形式与训练集相同，即原始句子和对应的标准分词结果的集合，但为了公平起见，训练集和测试集中的句子应该没有交集的。

通用的评价指标是采用基于词的精确率、召回率以及F1。

精确率和召回率定义为

$$p=\frac{\text{输出中正确的总词数} }{ \text{输出中的总词数} } $$

$$r=\frac{\text{输出中正确的总词数} }{ \text{标准答案中的总词数} } $$

F1是精确率和召回率的调和平均
$$\text{F1}=\frac{2pr}{p+r}$$

F1的范围在$[0,1]$之间，越大越好，现在中文分词模型的效果在大多数常用的训练集、测试集下能够达到$0.96$甚至更高。
