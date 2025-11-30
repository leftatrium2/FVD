# 登录

+ /login

+ POST

+ 参数

  ```json
  {
    "user_name":"",
    "password":""
  }
  ```

  

+ 返回值

  ```json
  {
      "code": 0,
      "data": {
          "token": "fc69182939dba5ab697302bacc0408b7"
      },
      "message": "successful"
  }
  ```


+ 注册后，token放入HEADER

  ```html
  X-IVD-TOKEN: fc69182939dba5ab697302bacc0408b7
  ```

  



# 修改密码

+ /login/change

+ POST

+ 参数

  ```json
  {
    "user_name":"",
    "password":"",
    "new_password":""
  }
  ```

  

+ 返回值

  ```json
  {
      "code": 0,
      "data": {
          "token": "fc69182939dba5ab697302bacc0408b7"
      },
      "message": "successful"
  }
  ```


# 首页列表

+ /index

+ GET

+ 参数

  ```html
  /list?medialib=xxx&page=1
  ```

  

+ 返回值

  ```json
  {
  "code":0,
  "msg":"successful",
  "data":
  {
  }
  }
  ```



# 媒体库列表

+ /medialib

+ GET

+ 参数

  ```html
  /medialib_list?page=1
  ```

  

+ 返回值

  ```json
  {
  "code":0,
  "msg":"successful",
  "data":
  {
  }
  }
  ```

  

# 任务检测

+ /task/check

+ POST

+ 参数

```
{
"url":"https://www.youtube.com/watch?v=ir6ndUQ2pS4"
}
```

+ 返回值

```
{
"code":0,
"msg":"successful",
"data":
{
}
}
```

  

# 添加任务

+ /task/add

+ POST

+ 参数

  ```json
  {
    
  }
  ```

  

+ 返回值

  ```json
  {
  "code":0,
  "msg":"successful",
  "data":
  {
  }
  }
  ```

# 任务列表

+ /task/list

+ GET

+ 参数

```json
/task/list?page=0&num=20&keyword=
```

+ 返回值

  
```
{
"code":0,
"msg":"successful",
"data":
{
}
}
```


# 设置 - 普通 - 列表

# 设置 - 普通 - 提交



# 设置 - VPN

# 设置 - VPN - 提交

# 设置 - 日志查看

# 设置 - 升级到专业版

