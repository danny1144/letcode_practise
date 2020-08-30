***as-if-serial语义的意思是:
不管怎么重排序(编译器和处理器为了提高并行度),(单线程)程序的执行结果不能被改变。编译器、runtime和处理器都必须遵守as-if-serial语义。 为了遵守as-if-serial语义,编译器和处理器不会对存在数据依赖关系的操作做重排序...***
- happens-before规则如下

**程序顺序规则**
对于单个线程中的每个操作，前继操作happens-before于该线程中的任意后续操作。
**监视器锁规则** 
对一个锁的解锁，hapens-before以及对随后这个锁的加锁
**volatile变量规则**
对一个volatile域的写，hapens-before于任意后续对这个volatile的读
**传递性**
如果 A happens-before B ,B happens-before C 那么A happens-before C
