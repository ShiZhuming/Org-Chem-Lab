import plotly.plotly as py
import plotly.graph_objs as go
import openpyxl

workbook=openpyxl.load_workbook("week_2_data.xlsx")

sheet=workbook.get_sheet_by_name("Sheet1")

data_list=[[],[],[],[]]



workbook=openpyxl.load_workbook("2018.xlsx")
sheet=workbook.get_sheet_by_name("Sheet1")

wb=workbook.active
wp=tuple(wb.rows)
for i in wp:
	data_list[i[0].value-1].append(i[1].value)
	# if i[0].value==1:
		# data_list.append(i[1].value)
	# elif i[0]	
# print("fileend")

# x = [ '甲苯', '甲苯', '甲苯', '甲苯', '甲苯', '甲苯', '甲苯', '甲苯',
# 	 '苯胺', '苯胺', '苯胺', '苯胺', '苯胺', '苯胺', '苯胺', '苯胺',
# 	 '苯甲酸', '苯甲酸', '苯甲酸', '苯甲酸', '苯甲酸', '苯甲酸', '苯甲酸', '苯甲酸']

method_1 = go.Box(
	y=data_list[0],
	name='method_1'
)

method_2 = go.Box(
	y=data_list[1],
	name='method_2'
)

method_3 = go.Box(
	y=data_list[2],
	name='method_3'
)

method_4 = go.Box(
	y=data_list[3],
	name='method_4'
)

# method_2 = go.Box(
# 	y=[3.53,8.20,10.53,10.79,7.53,8.02,12.67,8.75,10.59],
# 	name='method_2'
# )

data =[method_1,method_2,method_3,method_4]
py.plot(data)