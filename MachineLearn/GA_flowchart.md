```flow
st=>start: Start
cond=>condition: 车辆k是否运行?
op=>operation: ti=Tij
cond2=>condition: 车辆k是否与上
个工序车辆相同
op2=>operation: ti = t(i-1) + T'(i-1)j + Tji,同配送车辆的上个工序
op3=>operation: ti = t(i-1) + T'(i-1)j + Tji
e=>end: End

st->cond->op
cond(yes)->cond2
cond2(yes)->op3
cond2(no)->op2
cond(no)->op
op->e
op2->e
op3->e

```

```flow
st=>start: Start
sub=>subroutine: 计算预计到达时间RT
io=>inputoutput: RT
cond1=>condition: RT大于HT
cond2=>condition: RT小于LT
op1=>operation: real_time = RT
op2=>operation: real_time = LT

st->sub->io->cond1
cond1(no)->sub
cond1(yes)->cond2
cond2(no)->op1
cond2(yes)->op2

```

