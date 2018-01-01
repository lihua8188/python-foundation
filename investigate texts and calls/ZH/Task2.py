"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

phone_dict = {}
longest_time = 0
longest_phone_list = []

# creat a telephone dictionary with time spent
for call in calls:
    for i in range(2):
        if call[i] in phone_dict:
            phone_dict[call[i]] += int(call[3])
        else:
            phone_dict[call[i]] = int(call[3])

# get the longest time spend and phone list
for phone in phone_dict:
    if phone_dict[phone] > longest_time:
        longest_time = phone_dict[phone]
        longest_phone_list = []
        longest_phone_list.append(phone)
    elif phone_dict[phone] == longest_time:
        longest_phone_list.append(phone)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_phone_list, longest_time))
