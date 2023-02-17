total_min = int(input("минуты"))
total_sms = int(input("смс"))
total_sum = 15
if total_min > 50:
    total_sum = total_sum + (total_min - 50) * 0.25
if total_sms < 50:
    total_sum = total_sum + (total_sms - 50) * 0.25
print(total_sum)
