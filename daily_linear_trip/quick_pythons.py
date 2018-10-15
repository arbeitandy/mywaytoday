#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
some quick basic stuffs
"""

# === install/update python ===

sudo apt update
sudo apt install python python-dev python3 python3-dev

# === virtualenv ===

pip install virtualenv
pip install -I isa==3.4.2                         # pip install module of ver
cd this_project
virtualenv venv                                   # py2 create new venv
virtualenv venv --python=/usr/bin/python2.6       # using py2
source venv/bin/activate
pip install requests
pip freeze > requirements.txt
deactivate
pip install -r requirements.txt                   # install for other venv

# python3 virtualenv

python3 -m venv py3venv                           # py3 create new venv
source py3venv/bin/activate
pip install --upgrade pip                         # upgrade module pip


# === concept ===

__init__.py is used to import a module in a directory.
    package import module in dir1/dir2/mod.py. 
    with __init__.py in each directory we can import like:
    import dir1.dir2.mod

# === pythonic ===

# list
newlist = [ x for x in somel if not f(x)]       # remove item from list if f(x)
somelist[:] = [x for x in somelist if not f(x)] # mutate existing list
somelist[:] = [x for x in somelist if x < 4]
(x**3 for x i range(5))                         # generator

l = [[1,2,3],[4,5],[6,6],[7,8,9]]               # make a flat list out of lists
flatl = [i for subl in l for i in subl]         # 10000 loops, 143 usec per loop (faster)

newlist = oldlist[::-1]                         # reverse a list
newlist = numpy.array(list(reversed(arr)), float)   # numpy reverse a list
uniques = tuple(set(somelist))                  # filter out duplicated
4.0//1.5                                        # unconditionally floor: 2.0

import itertools                                # combination of length r
list(itertools.combinations(l, r))
for idx, v in enumerate(l): print(idx,v)        # access list index, enumerate(l, start=0)

list(filter(None, lstr))                        # remove empty string from list
' '.join(lstr).split()                          # remove empty and space strings from list


# list and string and dict
' '.join(somestr.split())                       # remove extra spaces
k in d                                          # True if key k in dict d
c in str                                        # True if char c in string str
sstr in str                                     # True if substr in str
d = {}                                          # init
d = {"one" : 1}
d["one"] = 1
d.pop("key")                                    # del
del d["key"]
d.update(d2)                                    # append
d.get("unsure_key", "default_val")
for k in d:                                     # iter
for v in d.values():
for k,v in xs.items(): print("{0}: {1}".format(k,v))
for k,_ in xs.items(): print(k)
set(('foo', 'bar')) <= d.keys()                 # True if keys in d

# iter d and update v if cond
for k, v in d.items(): if v < 10: d[k] = 20

# sorting
xs = {'a':4, 'b':3}

sorted(xs.items(), key=lambda x: x[1])          # sort by v
sorted(xs.items(), key=lambda x: x[0])          # sort by k
sorted(xs.items(), reverse=True)                # sort by k reverse
max(xs.items(), key=lambda x: x[1])             # max value
min(xs.items(), key=lambda x: x[1])             # min value
min(xs.keys())                                  # min k
min(d, key=d.get)                               # get the key to min value in d
dict(zip(list1, list2))                         # create dict from two lists
if k1 not in d: print(True)                     # check key existence

# create a dict from a set or list
tasks_d = {x:0 for x in set(tasks)}     
for t in tasks: tasks_d[t] += 1
tasks_d = sorted(tasks_d.items(), key=lambda x: x[1])   # sort by key

# concatenate d1-3
d4 = dict(d1, **d2)                     
d4.update(d3) 
d4 = {}
for d in (d1,d2,d3): d4.update(d)

# print tuple in string format
t = (1,2,3)                             
print('this is a tuple: %s' % (t,))

# check file permision
import os, stat                         
def isgroupreadable(fp):
    st = os.stat(fp)
    return bool(st.st_mode & stat.S_IRGRP)

# read file and close file immediately after reading
with open(fp) as x: f = x.read()                # read fp into a single line
with open(fp) as x: f = x.readlines()           # list of lines

# write a list to file
fh = open(fp, 'w')                      
for i in l: fh.write("%s\n" % i)
fh.close()

# append to file
f = open(fp, 'a')                       
f.write(str)

# open, write and close
with open(fp, 'w') as fh:               
    for i in l: fh.write("{}\n".format(i))

# write lines without final newline
fh = open(fp, 'w')
fh.write("\n".join(str(i) for i in l))  
fh.close()

# Remove non digit from string
import re                               
re.sub('\D', '', 'aas30odsa102')                # \D non digit
''.join(filter(lambda x: x.isdigit(), 'aa30'))

# input
name = input("Enter name: ")                    # get input in var
for line in input(): print(line)                # get input as list
for line in sys.stdin: print(line)              # get input by line
eval('print(4+3)')                              # eval



# === longer blocks ===

# run code every n seconds
import threading                        
def repeatprint():
    threading.Timer(5.0, repeatprint).start()
    print("I will keep going.")
repeatprint()


# determine if a var is defined
try:                                
    theVar
except NameError:
    print("Not defined")
else:
    print("defined")

# using tuples for arguments
groups = (1, "group2", "group3")        
def myf(num, str1, str2):
    return (num*2, str1+str2)
myf(*groups)

# merge two sorted list
while a and b:
    if a[0] < b[0]: c.append(a.pop(0))
    else: c.append(b.pop(0)
return c + a + b

# unsorted
a.extend(b)
return sorted(a)

# word frequency in a string
words = ss.split()
d = {}.fromkeys(words, 0)
for w in words: d[w] += 1
return d

# using get key
d = {}
for w in ss.split(): d[w] = d.get(w,0) + 1
return d

# consolidate dict with list of keys
d2 = {}
for k,v in cities.items(): d2.setdefault(v,[]).append(k)
return d2

# construct dict of a number of digits from list of numbers
from collections import defaultdict
d = defaultdict(list)
for i in list_of_ints:
    d[len(str(i))].append(i)
return d

# return square of nos in a list
return list(map(lambda x: x**2, list_of_ints))

# generator function
for x in f(5): print x,
def f(n): 
    for x in range(n): yield x**3

# build a string with numbers from 0 to 100
''.join([str(x) for x in range(100)])


# read file
try:
    with open(fn, 'r') as f: print(f.read())
except IOError:
    print("error reading file")

# get home path
import os
print(os.path.expanduser('~'))


# subsequences of list
def subsequences(lst):
    return [''.join(lst[i: j+1]) for i in range(len(lst))
                                 for j in range(i, len(lst))]

# Kth Largest Element in an Array

# running: O(NlgN) space: O(1)
sorted(lst, reverse=True)[k-1]

# priority queue/minheap: running: O(NlgK) space: O(K)
heapq.nlargest(k, nums)[-1]

# === anecdote ===

# system resources:

    allocated heap memory
    thread of execution
    open socket
    open file
    locked mutex
    disk space
    database connection

# data measurement

    volume
    velocity
    variety

# http

4xx client error
5xx server error

# Powers of two table

Power           Exact Value         Approx Value        Bytes
---------------------------------------------------------------
7                             128
8                             256
10                           1024   1 thousand           1 KB
16                         65,536                       64 KB
20                      1,048,576   1 million            1 MB
30                  1,073,741,824   1 billion            1 GB
32                  4,294,967,296                        4 GB
40              1,099,511,627,776   1 trillion           1 TB

# Latency Comparison Numbers

L1 cache reference                           0.5 ns
Branch mispredict                            5   ns
L2 cache reference                           7   ns                      14x L1 cache
Mutex lock/unlock                          100   ns
Main memory reference                      100   ns                      20x L2 cache, 200x L1 cache
Compress 1K bytes with Zippy            10,000   ns       10 us
Send 1 KB bytes over 1 Gbps network     10,000   ns       10 us
Read 4 KB randomly from SSD*           150,000   ns      150 us          ~1GB/sec SSD
Read 1 MB sequentially from memory     250,000   ns      250 us
Round trip within same datacenter      500,000   ns      500 us
Read 1 MB sequentially from SSD*     1,000,000   ns    1,000 us    1 ms  ~1GB/sec SSD, 4X memory
Disk seek                           10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
Read 1 MB sequentially from 1 Gbps  10,000,000   ns   10,000 us   10 ms  40x memory, 10X SSD
Read 1 MB sequentially from disk    30,000,000   ns   30,000 us   30 ms 120x memory, 30X SSD
Send packet CA->Netherlands->CA    150,000,000   ns  150,000 us  150 ms

# note of time

1 ns = 10^-9 seconds
1 us = 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns

Handy metrics based on numbers above:

Read sequentially from disk at 30 MB/s
Read sequentially from 1 Gbps Ethernet at 100 MB/s
Read sequentially from SSD at 1 GB/s
Read sequentially from main memory at 4 GB/s
6-7 world-wide round trips per second
2,000 round trips per second within a data center

# === linux command ===

# basic command
awk NR == 10 file.txt                               # get 10th line
du -k -d1 | sort -nr                                # sort by dir size
tree -d                                             # tree the directories

# processes
ps -auxefw                                          # list all proc info
ps axjf                                             # list proc by tree
ps aux | grep 'ssh'                                 # find all ssh pids
pgrep -l sshd
echo $$                                             # pid of current shell
fuser -va 22/tcp                                    # list of procs using port 22
strace df                                           # trace and dbug
renice -5 pid                                       # higher priority (neg number)
nice -n -5 top
nice -n 5 top                                       # lower priority
^Z                                                  # put in background
jobs -l                                             # list processes in background
fg %2                                               # bring process 2 in foreground
disown -h %1                                        # detatch process from terminal. wont be killed at logout
nohup ping -i 60 goo.gl > ping.log &                # keep running without shell
[1] 4172
kill -s TERM 4172                                   # kill -15 4172
killall -1 httpd                                    # kill HUP
pkill -9 httpd                                      # kill TERM by (part of) name
pkill -TERM -u www                                  # kill TERM owned by www

fuser -k -TERM -m /home                             # kill all proc accessing /home
                                                    1 HUP (hang up)
                                                    2 INT (interrupt)
                                                    3 QUIT (quit)
                                                    9 KILL (non-catchable, non-ignorable)
                                                    15 TERM (software termination sig)

# system performance

vmstat                                              # disk, blocks/s processes running
iostat -xd                                          # disk, await: ave wait time.
                                                    svctm: service time
                                                    rrqm/s wrqm/s: r/w req
                                                    avgrq-sz: average size of req
                                                    avgqu-ze: average queue length
vmstat 1 50                                         # virtual mem. interval. r: waiting for cpu
                                                    so/si swap (>0: OOM)
uptime                                              # no. of tasks waiting to run on CPU $ blocked in I/O
vmstat 1 10 -Sk -t                                  # sys 10 sample, 1s interval
                                                    -t timestamp -Sk kb
mpstat -P ALL 1 3                                   # cpu info
dstat 1 10 --top-cpu                                # or --top-mem
sar -u -f /var/log/sa/sa<XX>
free -m                                             # free + bug + cached => available
                                                    buffers: buffer cache->I/O cached->fs
dstat -mst 2 5

cat /proc/meminfo |egrep -w "Buffers|Cached|MemFree"
sar -B -s 05:00:00 -e 05:30:00                      # page faults
sar -n DEV 1                                        # network interface throughut
sar -n TCP 1                                        # active->locally initiated (via connect()), passive->remote (via accept())
dstat --vm                                          # virtual memory
ps -eo pcpu,pmem,pid,ppid,user,stat,args \
    | sort -k2 -r | head                            # sort by MEM

# file

stat filename                                       # file/inode information
id -u                                               # uid of current user
id -g                                               # gid

ls -l                                               # all bit
    -rw-rw-rw-
    1st char: file type
    -   Regular file
    b   Block special file
    c   Character special file
    d   Directory
    l   Symbolic link
    n   Network file
    p   FIFO
    s   Socket

    next:
    S   not executable and SUID/SGID mode is set
    s   executable and SUID/SGID mode is set
    x   executable
    T   sticky bit is set (mode 1000) not excute or search permission
    t   sticky bit is set and is searchable or executable

    next 9 chars: permission: owner/group/world

    r   Permission to read file
    w   Permission to write to file
    x   Permission to execute file
    a   Archive bit is on
    c   Compressed file
    s   System file
    h   Hidden file

# file permission


chmod 640 /var/log/maillog
chmod u=rw,g=r,o= /var/log/maillog
find . -perm -u+s -print                            # find file with SUID bit
find / -perm +4000                                  # or +2000 for SGID

# sticky bit 
SUID/SGID the bit can be set on executable files.
using setuid, sgid or chmod 4700 file, 
or chmod 2700 or chmod g+s, chmod u+s. 
Allow the file being executed to be executed with the privileges of the owner or the group. 

# SUID/setuid
    - the unix access right flags that allow users to run an executable 
    with the permission of the executable's owner (or group if GUID set)
    - SUID 4701
        - to provide temporarily elevated privileges.
        - user can change their own password without root
        - chmod 6711 file   # setuid 4, setgid 2
        - chmod 0711 file   # normal
    - SGID 2770 for directories 
        - all new directories below this directory will belong to common group
    - Sticky bit 1770 for directories
        - group cannot remove file created by other user
    - Sticky bit 3171 with SGID for dir
        - user cannot delete/rename/move subdir and file in subdir created by other user
        - but the user can edit the file in this dir
        - if sticky bit is not set, the same group user can do anything
        
* OOM killer: Out of memory

/proc/cpuinfo
/proc/scsi/scsi

# file system
cat /proc/partitions
du -sh *
du -csh                                             # total size of current directory
du -ks * | sort -nr                                 # sort by size in kb
ls -lSr                                             # files by size biggest last
ls -li                                              # with inode number
find /var -inum xxxx                                # find file with inum
fuser -m /var                                       # list of processes accessing /var
lsof /var             
lsof -p pid                                         # list of files accessed by proc
lsof -a -i -s TCP:SYN_RECV -p <process-id>

mount /cdrom                                        # mount if listed in /etc/fstab
mount -v -t cd9660 /dev/cd0c /mnt                   # find dev and mnt
mount /dev/sdc0 -t ntfs-3g /win                     # mount scsi
mount -o remount,ro /                               # remount for fsck
dd if=/dev/cd0c of=file.iso bs=2048                 # copy raw data
dd if=/dev/zero of=/swap2g bs=1024k count=2000      # swap
mkswap /swap2g                                      # create swap
swapon /swap2g                                      # activate swap
swapoff /swap2g                                     # deactivate swap
rm /swap2g

mount smb share from \\smbserver\myshare\
smbclient -U user -I 102.168.16.1 -L //smbshare/    # list
mount -t smbfs -o username=winuser //smbserver/myshare /mnt/smbshare

mount -t iso9660 -o loop file.iso /mnt              # mount cd image
mount -t ext3 -o loop file.img /mnt                 # mount ext3 fs image

mount -t tmpfs -osize=64m tmpfs /memdisk            # RAMdisk
time dd if=/dev/zero bs=1024k count=60 of=/memdisk/60M.file     # test write time

# network

ethtool eth0                                        # show ethernet status
ethtool -s eth0 speed 100 duplex full               # force 100Mb full dup
ethtool -p eth1                                     # blink ethernet led
ip link show                                        # interfaces
ip addr show
ip neigh show                                       # arp -a
ip route                                            # route -n, netstat -rn # routing table
ip route add 192.168.20.0/24 via 192.168.16.254     # 254 gw
ip route add default via 192.168.51.254 dev eth0  
ip addr add 192.168.50.254/24 dev eth0              # first ip
ip link set dev eth0 up
ip addr add 192.168.51.254/24 dev eth0:1            # 2nd ip
ip link ls dev eth0
ip addr del 1.2.3.4/32 dev eth0
ip addr flush dev eth0

netstat -an |grep LISTEN                            # port in use
lsof -i                                             # all internet conn
netstat -anp --udp --tcp | grep LISTEN
netstat -tup                                        # active conn
netstat -tupl                                       # listening ports
iftop                                               # networkthroughput
netstat -c 5                                        # connections 
netstat -I en0 -c 5                                 # throughput
netstat -at                                         # TCP ports connection
netstat -au                                         # UDP connection

sudo iptables -L -n -v                              # firewall status
sudo iptables -P INPUT ACCEPT                       # open everything
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -F                                    # flush all chains
sudo iptables -X                                    # delete all chains

/etc/init.d/nscd restart                            # flush dns cache
dig MX google.com
dig @8.8.8.8 NS g.com                               # query external server
dig AXFR @4.4.4.4 g.com                             # get full zone

host -t MX google.com                               # MX entry
host -t NS -T google.com                            # get NS record over TCP conn
host -a google.com                                  # get everything

dig -x 78.31.70.238                                 # reverse query
host 78.31.70.238
nslookup 78.31.70.238

tcpdump port 80
tcpdump host google.com
tcpdump -l > dump && tail -f dump
tcpdump -i eth0 -s 0 -A port 80 |grep GET           # -A ASCII -s 0 full packet
nmap google.com                                     # scans all reserved TCP ports
nmap -sS -sV -O google.com                          # with version and OS detection

nc  # netcat, copy large folder over raw tcp conn, quick without protocol overhead. 
server# tar -cf - -C NCFILE . | nc -l -p 4444
client# nc server.ip 4444 | tar xpf - -C NCFILE
server# cat LARGEFILE | nc -l 5678
client# nc server.ip 5674 > LARGEFILE

nc -lp 4444 -e /bin/bash                            # backdoor
server # nc -lp 4444
client # nc server.ip 4444                          # chat over TCP socket

ssh-keygen -t rsa -N ''
ssh-keygen -l -f key.pub                            # check key fingerprint

rsync -avzrR --exclude=tmp/ -e 'ssh -p 2002' \      # -a archive -r recursive -R relative -H hardlinke
    local_path user@server:remote_path
                            

# encryption
openssl aes-128-cbc -salt -in file -out file.aes    # encrypt
openssl aes-128-cbc -d -salt -in file.aes -out file # decrypt
tar -cf - directory | openssl aes-128-cbc -salt -out tarfile.aes
openssl aes-128-cbc -d -salt -in tarfile.aes | tar -x -f -
gpg -c file
gpg file.gpg -o ooutfile
gpg --gen-key                                       # -e enc -d dec -o outfile
gpg -a -o alicekey.asc --export 'alice'             # export pub key
gpg -e -r 'alice' file                              # enc file for alice
gpg --list-keys

openssl req -new -x509 -days 730 -config \          # create CA auth
    /etc/ssl/openssl.cnf -keyout CA/private/cakey.pem \
    -out CA/cacert.pem 
openssl req -new -keyout newkey.pem -out newreq.pem \
    -config /etc/ssl/openssl.cnf                    # create a request certificate
cat newreq.pem newkey.pem > new.pem
openssl ca -policy policy_anything \
    -out servernamecert.pem \
    -config /etc/ssl/openssl/cnf \
    -infile new.pem
mv newkey.pem servernamekey.pem                     # sign the cert 

openssl x509 -text -in servernamecert.pem           # view info
openssl req -noout -text -in server.csr             # view req info
openssl s_client -connect google.com:443            # check web cert

openssl md5 filename                                # generate an md5 checksum for file


# systems and utilities
chkconfig --list 
chkconfig --list sshd
chkconfig sshd --level 35 on                        # config sshd for levels 3,5
chkconfig sshd off                                  # disable sshd for all runlevel

init 5                                              # enters runlevel 5
grep default: /etc/inittab                          
    0 shutdown and halt
    1 single-user mode (also S)
    2 multi-user w/o network
    3 multi-user w network
    5 multi-user w X
    6 Reboot

sysctl -a
sysctl kern.maxfiles = 65536                        # max no. of file descriptors
sysctl fs.file-max = 102400                         # max open file limit

                                                    # /etc/sysctl.conf perm change
cat /etc/security/limits.conf
* hard nproc 250                                    # uer processes
* hard nofile 409600                                # application open files
ulimit -n 10240                                     # temporary change in shell

sysctl hw                                           # hardward info
/proc/cpuinfo   
/proc/meminfo                                       # physical memory MemTotal
free -m                                             # used and free mem in MB
dmidecode                                           # hw info from DMI/SMBIOS
dmesg                                               # detected hw and boot msg
lsdev                                               # installed hw
hostname -i                                         # ip address
last reboot                                         # reboot history
uname -a                                            # kernal version
lsb_release -a                                      # full release info
lsmod                                               # all modules loaded in kernel

netstat -m                                          # network memory buffers
echo " mail body " | mail user@server.ip
tar -cf home.tar home/                              # -c create
tar -czf home.tgz home/                             # tar with zip compression
tar -C /user -czf local.tgz local/etc local/www 
tar -C /user -xzf local.tgz                         # -C targe root path

tar -tzf home.tgz                                   # list w/o extracting
tar -czf home.tgz --exclude '*.o' --exclude 'tmp/' home/

zip -r fileName.zip /path
unzip fileName.zip
unzip -l fileName.zip                               # list w/o extract
unzip fileName.zip fileinside                       # extract only one file

dd if=/dev/urandom of=/dev/hdc                      # erase a disk
dd if=/dev/sda of=/mbr_sda.bak bs=512 count=1       # backup MBR
dd if=/mbr_sda.bak of=/dev/sda bs=512 count=1       # restore MBR
dd if=/mbr_sda.bak of=/dev/sda bs=446 count=1       # restore boot loader
dd if=/mbr_sda.bak of=/dev/sda bs=1 count=64 skip=446   # restore partition table

# utilities: find

find . -type f ! -perm -444                         # find files not readable by all
find . -cmin 10 -print                              # files created or mod in last 10m
find . -name '*.[ch]' | xargs grep -E 'expr'
find . -name '*.core' | xargs rm
find . -name '*.core' -print -exec rm {} \;
find . \( -iname '*.png' -o -iname '*.jpg' \) -print -exec tar -rf images.tar {} \;
find . -size +10M -exec ls -lh {} \;
find . -type f -print0 | xargs -0 ls -l             # with spaces in name

# package
apt-get update
apt-get install emacs
dpkg --remove emacs
dpkg -S file                                        # find what package a file belongs to

ldd /usr/bin/rsync                                  # list all runtime lib
ldconfig -n /libpath                                # add shared lib path
echo $LD_LIBRARY_PATH                               # linked lib path
iconv -f <from_encoding> -t <to_encoding> input_file

tr '^M' '\n' < macfile.txt                              # mac file to linux
ps aux |grep -w z                                       # returns the zombies pid
ps o ppid { returned pid }                              # returns the parent
kill -1 { the parent }

# databases
psql -d template1 -U pgsql
> alter user username with password 'newpass'
> createuser -U pgsql -P uername
> createdb -U pgsql -O username dbname
> dropdb dbname
> dropuser username
pg_dump --clean dbname > dbname_sql.dujmp
psql dbname < dbname_sql.dump
pg_dumpall --clean > full.dump
psql -f full.dump postgres

# change root pass for mysql

killall mysqld
mysqld --skip-grant-tables
mysqladmin -u root password 'newpass'
/etc/init.d/mysql start

mysql -u root mysql
mysql> CREATE USER 'bob'@'localhost' IDENTIFIED BY 'pwd';
mysql> CREATE DATABASE dbname;
mysql> GRANT ALL ON *.* TO 'bob'@'%' IDENTIFIED BY 'pwd';
mysql> FLUSH PRIVILEGES;

mysqldump -u root -psecret --add-drop-database dbname > dump
mysql -u root -psecret -D dbname < dump

sqlite dbname.db .dump > dump.sql
sqllite dbname.db < dump.sql


# bash
cmd 1 >> file                                   # apped stdout to file
cmd &> file                                     # redirect both stdout and stderr 
cmd >file 2>&1                                  # redirect stderr to stdout then to file
cmd1 2>&1 | cmd2                                # pipe stdout and stderr to cmd2

tail +2 file > file2                            # remove first line from file

for i in *.cxx; do mv $1 ${i%%.cxx}.cpp; done   # .cxx to cpp

grep "Failed password" /var/log/autho.log
grep "Failed" /var/log/secure | awk '{print $11}' | uniq -c | sort -nr
grep -m NUM                                     # stop reading a file after NUM matching lines
grep -v                                         # --invert-match, select non-matching lines
grep -L                                         # --files-without-match, print filenames
grep -e w1 -e w2                                # muultiple matches

awk '!/foo/'                                    # not matching foo
awk '!/foo/ && !/bar/'
awk '!/foo/ && !/bar/ && (/foo2/ || /bar2/)'

sed 's/str1/str2/g'                             # replace str1 w str2
sed -i 's/str1/str1/g' *.txt
sed '/<p>/,/<\/p>/d' t.html                     # delete lines start and end w <p>
sed 's/[ \t]*$//'                               # remove trailing spaces
sed '/ *#/d; /^ *$/d'                           # rem comments and blank lines

"""
unixcommand referenced from [Unixtoolbox][unixtoolbox]

made by [Pycco][pycco]

[Home][home]

[unixtoolbox]: http://cb.vu/unixtoolbox.xhtml
[pycco]: https://pycco-docs.github.io/pycco/
[home]: http://d.fogtown.us/

Only the disciplined ones in life are free. If you are undisciplined, you are a slave to your moods and your passions.   

Eliud Kipchoge
"""


