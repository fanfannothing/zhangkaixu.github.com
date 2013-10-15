
深度学习资源
================================


教程
-------------------

Ng 有一个wiki网站介绍 深度学习 和 无监督特征学习：  http://ufldl.stanford.edu/wiki/index.php/UFLDL_Tutorial

已经被翻译成中文： http://ufldl.stanford.edu/wiki/index.php/UFLDL%E6%95%99%E7%A8%8B

该教程介绍了多层前传神经网络的基本知识、 自动编码器、 深度学习的核心方法。 读了这个教程， 就可以回答什么是深度学习和无监督特征学习了。

theano工具包
-----------------------------------

还有一个教程在这里 http://deeplearning.net/tutorial/contents.html ， 它的特点是配合深度学习知识的介绍， 还同步提供了theano的源代码。 theano是一个基于python的工具包， 可以方便地进行符号计算（从此妈妈再也不用担心我求错偏导了）， 可利用GPU加速神经网络计算， 非常适合用于深度学习模型的建模。

基于这个教程学习了theano， 就可以很容易实现深度学习的相关模型了。



进行word embedding的word2vec工具包
-----------------------------------------------------------------------------

https://code.google.com/p/word2vec/

一个用c++编写的代码非常短小的工具包， 方便使用神经网络语言模型进行word embedding。 速度非常快。

word embedding是将神经网络用于自然语言的基础， 有了这个工具包， 就可以使用现有的state-of-the-art的方法快速地进行word embedding了。


Tutorials
------------------------------------

Ronan Collobert and Jason Weston【NIPS'09】Deep Learning for Natural Language Processing

Richard Socher, et al.【NAACL'13】【ACL'12】Deep Learning for NLP

YoshuaBengio【ICML'12】Representation Learning

Leon Bottou, Natural language processing and weak supervision

YoshuaBengio最新AAAI 2013 tutorial：http://www.iro.umontreal.ca/~bengioy/talks/aaai2013-tutorial.pdf

(摘自 http://www.cipsc.org.cn/hytx/15.html#41 ）

NLP相关论文推荐
-----------------------------------------------------

一种word embedding方法 【ACL'07】Fast Semantic Extraction Using a Novel Neural Network Architecture

在word embedding基础上进行各种NLP任务的尝试 【ICML'08】A unified architecture for natural language processing: deep neural networks with multitask learning

综述与比较各种Word representations 【ACL'10】Word representations：A simple and general method for semi-supervised learning

用于情感分析 【EMNLP'11】Semi-supervised recursive autoencoders for predicting sentiment distributions

【NAACL'13】 Discourse Connectors for Latent Subjectivity in Sentiment Analysis

用于句法分析 【ACL'13】 Parsing with Compositional Vector Grammars

用于paraphrase Dynamic Pooling and Unfolding Recursive Autoencoders for Paraphrase Detection

用于语义分析 Joint Learning of Words and Meaning Representations for Open-Text Semantic Parsing

用于中文分词词性标注 [EMNLP'13] Deep Learning for Chinese Word Segmentation and POS Tagging

用于机器翻译的词对齐 【ACL'13】 Word Alignment Modeling with Context Dependent Deep Neural Network

用于机器翻译的调序 [EMNLP'13] Recursive Autoencoders for ITG-Based Translation

（参考 http://www.xperseverance.net/blogs/2013/07/2124/）
