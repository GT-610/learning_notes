# `vector` 的应用
1. 给定一个整数数组，要求将数组中的所有偶数排在所有奇数的前面，而且偶数之间的相对顺序和奇数之间的相对顺序都不能改变。

```cpp
#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> even;
    vector<int> odd;
    vector<int> nums={1,1,4,5,1,4,1,9,1,9};


    for(int num:nums){
        if(num%2==0)even.push_back(num);
        if(num%2!=0)odd.push_back(num);
    }

    nums.clear();

    for(int num:even)nums.push_back(num);
    for(int num:odd)nums.push_back(num);

    for(int num:nums)cout << num << " ";
    cout << endl;

    return 0;
}
```

本题使用 `even` 和 `odd` 两个 `vector` 容器来保存奇数和偶数，利用 `vector` 的**动态扩展**特性，将奇数和偶数分别存储后再合并，实现奇数和偶数重新排列的效果。

本题也可以使用数组完成，但相比数组，容器的**动态扩展**功能使得我们**不需要手动预留空间**，既节省时间，也避免内存不足的问题。同时，我们可以直接 `push_back`，而不需要像数组一样去逐个赋值了。

2. 给定一个字符串，统计其中每个字符出现的次数，并按照字符顺序输出统计结果。

```cpp
#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main(){
    string input="Hello, world!";

    vector<int> count(256,0);

    for(char c:input)
        count[static_cast<int>(c)]++;

    for(int i=0;i<256;++i){
        if(count[i]>0)
            cout << "Char \'" << static_cast<char>(i) << "\' has appeared " << count[i] << " time(s)" << endl;
    }
    return 0;
}
```

这里面使用了一个 C++ 类型转换的方法 `static_cast<>()`。这是一个更加安全、灵活的强制类型转换，对于复杂的类型转换，更加推荐这个。
