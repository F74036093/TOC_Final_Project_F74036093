# TOC_Final_Project F74036093

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

第一步先輸入任意的文字並送出，bot就會送出歡迎訊息：

```sh
嗨～我這裡有一些漂亮的圖片！ 想看“卡通角色”還是“狗狗”或是“鳥兒”呢？
```

輸入“”內的選項，就會轉換到不同的state並且給出不同的訊息

在接下來只要輸入括號內的文字就可以看到圖片

bot輸出圖片後就會回到一開始的state並等待使用者輸入任意文字
