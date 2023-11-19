# `list` 的应用
1. 给定一个整数数组，将其中的奇数倒序排在前面，偶数正序排在后面。

```cpp
#include<iostream>
#include<list>
using namespace std;
int main(){
    list<int> input={1,2,3,4,5,6,7,8,9,10};
    list<int> result;
    for(int num:input){
        if(num%2==0)result.push_back(num);
        else result.push_front(num);
    }

    for(int num:result)cout << num << " ";
    cout << endl;
    return 0;
}
```

2. 实现一个简单的任务调度器，假设有一组任务，每个任务又一个名称和一个优先级（用整数表示）。我们需要按照任务的优先级来进行调度。

由于每个任务有两个属性，这里用**结构体**定义每个任务会更加方便操作。

```cpp
#include<iostream>
#include<list>
#include<algorithm>
#include <string>

using namespace std;

struct Task{
    string name;
    int priority;

    Task(const string &n, int p): name(n), priority(p) {}
};

bool comparePriority(const Task &t1, const Task &t2){
    return t1.priority<t2.priority;
}

void scheduleTasks(list<Task> &tasks){
    tasks.sort(comparePriority);
}

int main(){
    list<Task> tasks = {{"TaskA", 3}, {"TaskB", 1}, {"TaskC", 2}, {"TaskD", 5}};  
    scheduleTasks(tasks);
    for(const auto &task:tasks)
        cout << "Task: " << task.name << ", Priority: " << task.priority << endl;
    return 0;
}
```

## 部分解释
### 第 12 行
```cpp
Task(const std::string& n, int p) : name(n), priority(p) {}
```

这条语句是用来**构造函数**的，作用是创建对象时**顺便进行初始化操作**。其中，`: name(n), priority(p)` 是**成员初始化列表**，用来对 `Task` 结构体中的 `name` 和 `priority` 进行初始化。

这样，当我们创建一个 `Task` 类型的结构体时，我们可以直接通过**提供值**来对该结构体进行初始化。

```cpp
list<Task> tasks = {{"TaskA", 3}, {"TaskB", 1}, {"TaskC", 2}, {"TaskD", 5}};
```

如果没有这条语句，编译器会使用默认的函数进行初始化，我们无法直接在定义的时候就初始化，必须另外赋值了。

### 第 15 行
```cpp
bool comparePriority(const Task &t1, const Task &t2){
    // ...
}
```

这里在定义形参的时候，使用了 `&` 取地址符。这个表示**引用传递**。它是一种将参数的引用传递给函数的方法，它可以使函数**直接操作原始数据**，而不是一般形参的创建副本，以此提高效率并允许函数内部修改参数的值。

1. 避免了参数的拷贝：使用引用传递可以避免在调用函数时对参数进行拷贝，节省了内存和时间的开销，特别是当参数是大型对象时。

2. 可以修改参数的值：通过引用传递，函数内部对参数的修改会直接反映到调用函数时的原始数据上，而不是在函数内部操作参数的副本。

3. 方便传递可变数量的参数：通过引用传递，可以方便地传递多个参数给函数，而不需要指定参数的个数。

