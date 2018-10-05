month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
s = [int(i) for i in input().split()]
print(week[(sum(month[:s[0]-1])+s[1])%7])