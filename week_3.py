import plotly.plotly as py
import plotly.graph_objs as go
import openpyxl
import sys

if len(sys.argv)!=4:
	print("Please input filename , line number and plot title")
	sys.exit(0)

workbook=openpyxl.load_workbook(sys.argv[1])
data_list=[[],[],[],[]]

# sheet=workbook.get_sheet_by_name("Sheet1")

# wb=workbook.active
workbook_rows=tuple(workbook.active.rows)
for i in workbook_rows:
	if(i[int(sys.argv[2])]value!='/'):
		data_list[i[0].value-1].append(i[int(sys.argv[2])].value)
	
data=[]
for i in range(4):
	data.append(go.Box(
	y=data_list[i],
	name='method_'+str(i+1),
	boxpoints='all',
    jitter=0.3,
    pointpos=-1.8,
    boxmean=True
))
	
layout = go.Layout(
	title=sys.argv[3],
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig)

# Toluene
# Aniline
# Total Benzoic acid