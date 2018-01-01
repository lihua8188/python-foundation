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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
telemarketers_phonelist = []
check_list = set()

# creat the phone number checklist from calls and texts
for call in calls:
    check_list.add(call[1])

for text in texts:
    check_list.add(text[0])
    check_list.add(text[1])

# check and creat telemarketers phone codes_list
for call in calls:
    if call[0] not in check_list and call[0] not in telemarketers_phonelist:
        telemarketers_phonelist.append(call[0])
telemarketers_phonelist = sorted(telemarketers_phonelist)
print("these numbers could be telemarketers:")
for number in telemarketers_phonelist:
    print(number)
