# `typedef` 关键字
可以用它给类型取一个新的名字。

```c
typedef unsigned char BYTE;
```

当然你把 `BYTE` 换成别的也行，随你怎么取。

然后我们就可以把 `BYTE` 当成 `unsigned char` 去用啦：

```c
typedef unsigned char BYTE;
BYTE b1,b2; // b1 b2 都是 unsigned char 类型
```

`typedef` 也可以定义**结构体**。此时，定义的名字**可直接作为结构体类型使用**。

```c
typedef struct Books{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} Book;

Book book; // book 的类型是上面那个结构体
```

## `typedef` 与 `#define` 的区别
1. `typedef` 是**执行时解释**，`#define` 是**预处理**。
2. `typedef` 只能**为类型定义**符号名称，`#define` 不仅可以定义类型的别名，还能**为数值定义**别名。

```c
#define TRUE 1
#define FALSE 0
```

但是 `typedef` 是不能干上面这个的。