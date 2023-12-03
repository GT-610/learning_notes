## 1. 单词计数

大致思路是：用一个数组，统计每个字母、数字出现的次数，还是比较简单的。

```c
#include<stdio.h>
#include<string.h>
int main(){
    int alphabet[63]={0};
    char ch;
    
    while ((ch = getchar()) != '\n') {
        if (ch != ' ') {
            if (ch >= '0' && ch <= '9')
                alphabet[ch - 48]++;
            else if (ch >= 'A' && ch <= 'Z')
                alphabet[ch - 55]++;
            else if (ch >= 'a' && ch <= 'z')
                alphabet[ch - 60]++;
        }
    }

    for(int i=0;i<10;++i)
        if(alphabet[i]!=0)
            printf("%c %d\n", i+48,alphabet[i]);

    for(int i=10;i<36;++i)
        if(alphabet[i]!=0)
            printf("%c %d\n", i+55, alphabet[i]);
    
    for(int i=37;i<63;++i)
        if(alphabet[i]!=0)
            printf("%c %d\n", i+60, alphabet[i]);

    return 0;
}
```

2. 
而题目要求是循环输入直到遇到换行符为止，结合循环中给出的 `!='\n'` 可知，这里是要填一个输入的。但是要注意， 非 (`!`) 的优先级是高于 赋值(`=`) 运算符的，所以我们要在输入 `cx=getchar()` 这里添加括号，让它先执行。

然后下面是让我们遇到连续空格的时候只输出一个。这道题用 `front` 定义输入位置的前一个字符，然后加入输入的是一个空格，那我就看前面一个是不是空格，如果是，那就不输出；如果不是，那我就需要输出了。所以第二个空是 `cx!=front` 即当前输入的字符和前面一个比较。

第三个空就是当输入的那个字符不是空格，我要做的事情，那就是直接输出了。

```c
#include<stdio.h>
int main(){
    char cx, front='\0';
    while((cx=getchar())!='\n'){ // 空 1
        if(cx!=' ')putchar(cx);
        if(cx==' ')
            if(cx!=front) // 空 2
                putchar(cx); // 空 3
        front=cx;
    }
    return 0;
}
```

3. 
```cpp
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int main(){
    int n;cin >> n;
    bool cmp(string,string);
    string number[n];
    for(int i=0;i<n;++i)
        cin >> number[i];

    sort(number,number+n,cmp);

    for(int i=0;i<n;++i)
        cout << number[i];
    cout << endl;
    return 0;
}

bool cmp(string a,string b){
    return a+b>b+a;
}
```

4.这个就按照题目中的意思去累加就可以了，分子用一个变量控制，分母用另一个变量控制。

