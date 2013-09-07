多层前馈网络
=================================


多层前馈网络
----------------------------------

这个与人大脑皮层的结构也类似。

.. graphviz::

    digraph grph{
    rankdir=LR;
    node [shape = none];
    x1;
    x2;
    xx[label="1"];
    y;
    node [shape = circle];
    {rank=same;
    h11[label="a1"] h12[label="a2"] h13[label="a3"]; 
    h14[label="1"];
    };
    x1 -> h11;x2->h11;xx->h11;
    x1 -> h12;x2->h12;xx->h12;
    x1 -> h13;x2->h13;xx->h13;
    h11->h14 [style=invis]

    h21[label="b1"] h22[label="b2"] h23[label="b3"] h24[label="1"];

    h11->h21;h12->h21;h13->h21;
    h11->h22;h12->h22;h13->h22;
    h11->h23;h12->h23;h13->h23;
    h14->h21;h14->h22;h14->h23;
    h21->y;
    h22->y;h23->y;h24->y;
    }


后向传播算法计算梯度
----------------------------------------

导数计算中的链式法则

.. math::
    
    \frac{dx}{dy}=\frac{dx}{dz}\frac{dz}{dy}


.. math::

    \frac{dx}{dy}=\frac{dx}{dz_1}\frac{dz_1}{dy}+\frac{dx}{dz_2}\frac{dz_2}{dy}
