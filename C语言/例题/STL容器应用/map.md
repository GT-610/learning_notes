# `map` 的应用
1. 统计一段文本中各个单词的次数。
```cpp
#include<iostream>
#include<map>
#include<string>
#include<sstream>
using namespace std;

int main(){
    string text="hello world welcome to the c plus plus world";
    map<string, int> wordcount;

    stringstream ss(text);
    string word;
    while(ss>>word)wordcount[word]++;

    for(const auto &pair:wordcount)
        cout << pair.first << ": " << pair.second << " time(s)" << endl;
    
    return 0;
}
```
## 部分解释
### 第 11 行
```cpp
stringstream ss(text);
```

`stringstream` 这个类型，可以将一个字符串转变为一个输入/输出流。这样，你就可以把它当成类似 `cin` 和 `cout`，使用 `>>` 进行流式输入。

这条语句将字符串 `text` 的内容，传入 `stringstream` 对象 `ss` 的构造函数中，这样，当 `ss` 通过流输入至 `word` 时，对于字符串中的空格，编译器会使用一种与 `cin` 流式输入相同的处理方法去对待，也就是以空格去分隔单词。这样，每个单词自然而然地成为了每一个输入，我们不需要手动判断空格在哪里了。

需要引入头文件 `sstream`。 

## 第 15 行
```cpp
for (const auto& pair : wordCount){
    cout << pair.first << ": " << pair.second << " time(s)" << endl;
}
```
这里 `pair` 的类型是 `wordCount` 的**键值对**，即一开始定义的 `pair<const string, int>`。（~~能用 `auto` 就用不是更省事嘛~~）

`pair.first` 输出**键**，`pair.second` 输出**值**。


对于这道题，`map`的优势就体现的很明显：性能比传统数组很高，而且你可以直接调用现成的操作方式，不需要自己设计数据结构以及实现增删操作。