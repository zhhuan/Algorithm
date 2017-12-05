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

