# 遠距教學課堂筆記 CH13

###### tags: `遠距教學`

> Lesson: `Linux 系統實務`
> Author: `U108B124 Xin-You Tsai`
> Date: `110.05.20`, `110.05.27`

## 利用指令建立使用者帳號

### 超級使用者(root)與一般使用者的差異

| | 超級使用者 | 一般使用者 |
| -------- | -------- | -------- |
| 帳號名稱 | root | 使用者名稱 |
| 家目錄位置 | /root | /home/使用者名稱 |
| 檔案權限 | 對所有磁碟內的檔案目錄都有讀寫及修改權限 | 僅能讀寫及修改有授權的檔案及目錄 |
| 指令權限 | 皆可執行 | 僅能執行有權限授權的指令 |



### 在終端機建立使用者

#### 手動新增

檢查使用者帳號是否存在
```bash 
finger <使用者名稱>
```

:::info
若需要安裝套件，輸入以下指令安裝：
`sudo apt install finger`
:::

建立使用者帳號
```bash
sudo useradd <使用者名稱>
```
更改使用者密碼: 
```bash
sudo passwd <使用者名稱>
```
在終端機切換使用者
```bash
su <使用者名稱>
```

#### 透過useradd指令
```bash 
sudo adduser <使用者名稱>
```

- 使用這個指令，會自動建立全新且完整的使用者帳號（包含家目錄、命令殼層、使用者權限...等等），但不需要手動設定，總體而言，比手動新增還方便許多。
- 使用新建立的帳號登入圖形界面時，若發現到所有語系以及設定檔全都跑掉，必須重新設定一遍。

輸出視窗
```bash 
正在新增使用者 'XXX' ...
增加新群組 'XXX' (XXXX) ...
正在新增使用者 'XXX' (UID XXXX) 到群組 'XXX' ...
正在新增家目錄 'home/XXX' ...
正在從 '/etc/skel' 複製檔案 ...
新 密碼: (輸入密碼)
再次輸入新的 密碼: (輸入密碼)
請輸入新值，或直接按 ENTER 鍵使用預設值
    全名[]: 
    房間號碼[]:
    工作電話[]:
    家用電話[]:
    其他[]:
以上輸入的資料正確嘛？[Y/n]
```

### 可以在`/home`目錄手動建立使用者資料夾嘛？
不行。每個資料夾都有給對應的使用者權限。即使你使用系統管理員建立了資料夾，使用者的權限依舊為root所有。

### 訪客帳號？
跟windows一樣，在系統內都有一個共用帳號`guest`(預設是關閉)，可以給臨時需要電腦的人士使用。但這種帳號通常都沒有密碼，常會被有心人士利用破壞系統。

:::info
如何查看自己的電腦有無開啟訪客帳號：
`cat /etc/passwd | grep guest`
若沒有看到任何輸出訊息，代表這個帳號是預設關閉的，你的電腦是安全的。
若有，可以輸入以下指令取消密碼：
`sudo passwd -d guest`
:::

## passwd 和 shadow 

### 觀察passwd權限
下方指令擇一即可：
```bash 
ls -al /etc/passwd

ll /etc/passwd
```
輸出視窗
```bash 
-rw-r--r-- 1 root root 1934  5月 20 09:30 /etc/passwd
```

可以利用`nano`或者`cat`查看/etc/passwd裡面的內容
```
minexo79:x       :1000      :1000    :THIS IS USER:/home/minexo79:/bin/zsh
使用者名稱 使用者密碼 使用者識別碼 群組識別碼 使用者資訊    使用者家目錄     使用者終端機環境
```

### 觀察shadow權限
下方指令擇一即可：
```bash 
ls -al /etc/shadow

ll /etc/passwd
```
輸出視窗
```bash 
-r-------- 1 root root 1274  5月 20 09:30 /etc/shadow
```

## 最高管理者（ROOT）
- 安裝好Linux系統之後，系統會預設建立root帳號，這是在系統中最高級權限的帳號。因此，在維護root帳號的安全，則格外的重要。
- 大部分的Linux系統在安裝過程中，會要求使用者建立root帳號的密碼，以及自己使用者帳號的密碼，防止外人對系統進行攻擊。

### 切換成root帳號
```bash 
sudo su
```
輸出訊息
```bash
root@<主機名稱>:<目前工作目錄># 
```

### 切換其他使用者

若加上減號以及使用者名稱，則切換之後會將工作目錄切成該帳號對應的家目錄：
```bash  
sudo su -                  # 預設切換成root帳號

sudo su - <其他使用者名稱>    # 切換成指定的帳號
```

輸出訊息
```bash
root@<主機名稱>:~#             # root帳號

<其他使用者名稱>@<主機名稱>:~$    # 其他帳號
```
此時可以利用`pwd`查看目前的所在目錄。

## 維護模式

### 只能允許root登入的維護模式
先在`/etc`目錄中輸入`touch nologin`，使其產生檔名為`nologin`的檔案。
鍵入`Alt+F1` ~ `Alt+F6`，進入純文字模式，若登入一般的使用者帳號，則會被攔截而無法登入。（訊息如下）
```bash 
Login incorrect
```
此舉用於系統維護相關動作。當按下重新開機之後，`nologin`將會被自動刪除，可以再次鍵入`Alt+F1` ~ `Alt+F6`進入純文字模式，透過一般使用者登入進行操作。

### 單人模式（也稱救援模式）
單人模式(Single User Mode)，也稱救援模式(Rescue Mode)是最精簡的開機模式，系統在開機時不會啟用網路卡、顯示卡等硬體配備，也不會執行使用者認證的機制。
如果忘記`root`帳號的密碼, 可以使用單人模式來重新設定密碼。

相關教學：https://blog.gtwang.org/linux/linux-grub-change-root-password/

:::spoiler 還沒試過，別點開來看
```
好喔，你點進來了xdd
```

更改`/etc/default/grub`內的內容
```
sudo nano /etc/default/grub
```

在`GRUB_CMDLINE_LINUX_DEFAULT`中加入`single`這個參數。之後更新grub開機選單。

```bash 
sudo update-grub
```

之後重新開機，便可進入單人模式。

若更改完畢root帳號的密碼，可以鍵入`init 3`進入多人文字模式，或者是`init 5`進入多人圖形模式。也可進入`/etc/default/grub`，在`GRUB_CMDLINE_LINUX_DEFAULT`中加入`single`這個參數移除，更新grub開機選單，之後重開機即可。

:::

## 刪除與停用使用者帳號

### 停用使用者帳號

進入`/etc/passwd`檔案
```bash 
sudo nano /etc/passwd
```

將該使用者的密碼欄位由`'X'`改成`'*'`
```bash 
minexo79:x:1000:1000:THIS IS USER:/home/minexo79:/bin/zsh <更改前>
minexo79:*:1000:1000:THIS IS USER:/home/minexo79:/bin/zsh <更改後>
```

### 刪除使用者帳號

刪除使用者帳號比停用帳號還麻煩許多，步驟如下
#### 刪除背景執行程式
為了避免使用者有程式遺留在系統中，利用下列指令檢查背景執行的程式，並把在背景中執行的程式刪除。
```bash 
sudo ps -u <使用者名稱>
```
輸出視窗顯示出目前正在背景執行的程式：
```bash 
    PID TTY          TIME CMD
   1160 ?        00:00:00 systemd
   1161 ?        00:00:00 (sd-pam)
   1171 ?        00:00:00 gnome-keyring-d
   1175 tty2     00:00:00 gdm-x-session
   1177 tty2     00:02:56 Xorg
   1194 ?        00:00:02 dbus-daemon
   1196 tty2     00:00:00 gnome-session-b
   1215 ?        00:00:00 gvfsd
   1220 ?        00:00:00 gvfsd-fuse
   1224 ?        00:00:00 at-spi-bus-laun
   1233 ?        00:00:00 dbus-daemon
...
```
需要刪除這些程式，可以利用`kill`指令：
```bash 
sudo kill -0 1177 (正常關閉程式)
sudo kill -9 1177 (強制關閉程式)
```
#### 刪除排程工作
利用下方指令檢查排程工作
```bash 
crontab -u <使用者名稱> -l
```
輸出畫面顯示出目前在背景執行的排程工作
```bash 
0, 30 * * * * date -> (每當整點30分，在背景執行date指令)
```
此時可以用下方指令刪除該使用者所制定的所有排程工作
```bash 
crontab -u <使用者名稱> -r
```
#### 刪除使用者的帳號與檔案
使用下方指令檢查並刪除使用者所建立的檔案
```bash 
sudo find / -user <使用者名稱> -print -exec rm -rf () \; -> 刪除屬於該使用者的全部檔案
```
#### 刪除使用者
如果做完上述步驟，並且都沒有發生錯誤，最後就能放心的，輸入下方指令從系統中完整移除使用者
```bash 
sudo userdel <使用者名稱>
```

## 使用者群組
為了方便管理系統各個使用者的權限，Linux有群組的功能，可將每個使用者透過群組分開權限去做管理，省去每個使用者逐個分配相對應的權限。
系統中除了`root`帳號的`root`群組，及一般使用者的`users`群組之外，還有許多其他的群組，詳細內容都記錄在`/etc/group`檔案中。
```bash 
root:x:0:root
adm:x:999:daemon
wheel:x:998:minexo79
kmem:x:997:
tty:x:5:
utmp:x:996:
...
minexo79:x:1000:
```
特別注意到，群組編號為0代表超級使用者`(root)`，代號1000之前代表系統及應用程式所屬的群組，代號1000之後則是代表一般使用者的群組。

### 自訂群組

#### 建立群組

使用`groupadd`命令建立群組
```bash 
sudo groupadd -g <群組編號> <群組名稱>
```
可以利用`cat`檢查群組有沒有建立成功
```bash 
cat /etc/group
```
輸出視窗
```bash 
root:x:0:root
adm:x:999:daemon
wheel:x:998:minexo79
kmem:x:997:
tty:x:5:
utmp:x:996:
...
minexo79:x:1000:
mine0853:x:1100: -> 假設這是我剛剛新增的群組
```

#### 變更所屬群組
若要更動已存在的使用者帳號所隸屬的群組，可直接編輯`/etc/passwd`檔案
```bash 
minexo79:x:1000:1000:'minexo79':/home/minexo79:/bin/zsh (更改前)
minexo79:x:1000:1100:'mine0853':/home/minexo79:/bin/zsh (更改後)
```

接著鍵入`chown`命令, 改變使用者家目錄及檔案所隸屬的群組
```bash 
sudo chown -R .mine0853 /home/minexo79 -> 把minexo79的家目錄及目錄下所有的檔案，更改成mine0853這個群組可以存取
```

#### 刪除群組
當這個群組不再使用，可以鍵入`groupdel`命令刪除群組
```bash 
sudo groupdel <群組名稱>
```