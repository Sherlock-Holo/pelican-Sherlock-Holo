Title: VLAN
Date: 2017.3.20
Summary: openwrt的VLAN
tag: openwrt

## 关
这个分组不使用这个接口

## 关联
这个就扣需要通过VLAN  ID来访问这个分组，端口之间通信无二层交换，而是冲突广播

## 不关联
这个接口被直接桥接到这个分组，即该端口作为本VLAN成员，进行二层交换

# 路由器上的VLAN
<img src="https://c2.staticflickr.com/4/3847/33375953332_49885c906e_o.png" width="1549" height="458" alt="2017-03-20 01-01-13 的屏幕截图">

2看起来像是eth0.2，也就是wan的

1看起来像是eth0.1，也就是lan的
