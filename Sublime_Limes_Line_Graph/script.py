import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# Create a figure with two subplots to visualize monthly visits and lime sales
plt.figure(figsize=(12, 8))
ax1 = plt.subplot(1, 2, 1)
x_values = range(len(months))
plt.plot(x_values, visits_per_month, color='r', marker='o')
plt.title('Monthly Visits in 2023')
plt.xlabel('Month of the year')
plt.ylabel('Visits on the site')
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)

ax2 = plt.subplot(1, 2, 2)
lime_data = {'Key limes': ('red', key_limes_per_month), 'Persian limes': ('green', persian_limes_per_month), 'Blood limes': ('yellow', blood_limes_per_month)}
for lime, (color, data) in lime_data.items():
    lime_data = {'Key limes': ('red', key_limes_per_month), 'Persian limes': ('green', persian_limes_per_month), 'Blood limes': ('yellow', blood_limes_per_month)}
for lime, (color, data) in lime_data.items():
    plt.plot(x_values, data, color=color, marker='o', label='{} sold'.format(lime))
# plt.plot(x_values, key_limes_per_month, color='red', marker='o', label='Key limes sold')
# plt.plot(x_values, persian_limes_per_month, color='green', marker='o', label='Persian limes sold')
# plt.plot(x_values, blood_limes_per_month, color='yellow', marker='o', label='Blood limes sold')
plt.title('Products sold monthly in 2023')
plt.xlabel('Month of the year')
plt.ylabel('Products sold')
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.legend()
plt.savefig('sublime_limes_sales_2023.png')
plt.show()
