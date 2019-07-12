# Celery - 分布式任务队列
-  Celery
   是一个简单、灵活且可靠的，处理大量消息的分布式系统，并且提供维护这样一个系统的必需工具。
-  它是一个专注于实时处理的任务队列，同时也支持任务调度。 
## 何为任务队列？
任务队列是一种在线程或机器间分发任务的机制。

消息队列的输入是工作的一个单元，称为任务，独立的职程（Worker）进程持续监视队列中是否有需要处理的新任务。

Celery 用消息通信，通常使用中间人（Broker）在客户端和职程间斡旋。这个过程从客户端向队列添加消息开始，之后中间人把消息派送给职程。

Celery 系统可包含多个职程和中间人，以此获得高可用性和横向扩展能力。

Celery 是用 Python 编写的，但协议可以用任何语言实现。迄今，已有 Ruby 实现的[
RCelery](http://leapfrogdevelopment.github.com/rcelery/) 、node.js 实现的
[node-celery](https://github.com/mher/node-celery) 以及一个
[PHP 客户端](https://github.com/gjedeer/celery-php) ，语言互通也可以通过
[using webhooks](http://docs.jinkan.org/docs/celery/userguide/remote-tasks.html#guide-webhooks) 实现。

