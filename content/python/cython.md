Title: 上天的Cython
Date: 2017.9.13
Summary: 了解到Cython
tags: Python

有个东西叫做`uvloop`, 使用了cython，最初以为用cython要写很多c代码所以不怎么在意这玩意。

然后今晚突发奇想: cython能不能编译原生python代码? 于是随手搜了一下，看到一个[Cython 的基础](https://moonlet.gitbooks.io/cython-document-zh_cn/content/ch1-basic_tutorial.html)。

What??? 还真能编译??!! 这就上天了。立马测试了一下`print('test')`，然后写了个`setup.py`

```
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('cp.pyx')
)
```

测试了一下: `python setup.py build_ext`，进去python console，`import cp`，还真成功了。

这。。。是不是意味着。。。用python写了CPU密集的东西后用cython编译一下就可以让性能有所提高? 想想都有点兴奋呢~
