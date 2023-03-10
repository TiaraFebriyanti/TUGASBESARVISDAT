
"""finalproject_visdat.ipynb


---



---

**FINAL PROJECT VISUALISASI DATA**


Disusun oleh: 


*   Tiara Febriyanti ( 1301194309 ) 
*   Kamalludin Hanif Farisi ( 1301190360 )
*   Bagas Millen A ( 1301180184 )

---
link deployment html: https://tiarafebriyanti.github.io/TUGASBESARVISDAT/covid19-bokeh.html


---
"""

# Import semua Dependencies
import numpy as np
import pandas as pd
import bokeh
from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource, CustomJS, DatetimeTickFormatter
from bokeh.models.widgets.sliders import DateRangeSlider
from bokeh.layouts import row, column, gridplot, layout
from bokeh.models import Slider, Select
from bokeh.io import output_file, output_notebook, curdoc
from bokeh.models.widgets import Tabs, Panel

# Versi Module
print('Bokeh  Version  : {}'.format(bokeh.__version__))
print('Pandas Version  : {}'.format(pd.__version__))
print('Numpy  Version  : {}'.format(np.__version__))

# Membaca Dataset Covid 19 
data = pd.read_csv("covid19.csv", parse_dates=['date'])
data.head()

# Menambah Tabel Baru 
data["Name"] = "DataCovid"
data

data['Name'].unique()

newDS1 = data
newDS1 = newDS1.sort_values(['date', 'Name'])
newDS1.head()

DataCovid = newDS1[newDS1['Name'] == 'DataCovid']
output_notebook()

DataCovid

# Theme Layout 
curdoc().theme = "dark_minimal"

output_notebook()

# Resource Data
output_file('covid19-bokeh.html',
            title='data terkonfirmasi positif berdasarkan kurun waktu')
dt_covid = ColumnDataSource(DataCovid)


# Untuk Hover
tooltips = [('Name', '@Name'), ('acc_confirmed', '@acc_confirmed'), ('new_confirmed', '@new_confirmed'),('acc_negative', '@acc_negative')]
tool=[('new_tested','@new_tested'), ('acc_tested','@acc_tested'),  ('being_checked','@being_checked'),  ('isolated','@isolated')]


# Untuk Visualisasi Data Figure Plot 
covidFig = figure(x_axis_type= 'datetime',
                  plot_height=500, plot_width=1000,
                  title='Data Covid 19', 
                  x_axis_label='Tanggal', y_axis_label='acc confirmed',  tooltips=tooltips)

covidFig2 = figure(x_axis_type= 'datetime',
                  plot_height=500, plot_width=1000,
                  title='Data Covid 19', 
                  x_axis_label='Tanggal', y_axis_label='new confirmed',  tooltips=tooltips)

covidFig3 = figure(x_axis_type= 'datetime',
                  plot_height=500, plot_width=1000,
                  title='Data Covid 19', 
                  x_axis_label='Tanggal', y_axis_label='acc negative',  tooltips=tooltips)

covidFig4 = figure(x_axis_type= 'datetime',
                  plot_height=500, plot_width=1000,
                  title='Data Covid 19', 
                  x_axis_label='Tanggal', y_axis_label='Covid Value',  tooltips=tool)

# Untuk Visualisasi Data Figure dalam bentuk Garis

covidFig.line('date', 'acc_confirmed', 
         color='red', legend_label='Data Covid 19 - acc_confirmed',
         line_width=2, 
         source=dt_covid)

covidFig2.line('date', 'new_confirmed', 
         color='yellow', legend_label='Data Covid 19 - new_confirmed',
         line_width=2, 
         source=dt_covid)

covidFig3.line('date', 'acc_negative', 
         color='green', legend_label='Data Covid 19 - acc_negative',
         line_width=2, 
         source=dt_covid)


# Visualisasi Data untuk Interactive Select List atau Dropdown
plot_1 = covidFig4.line(x='date', y='new_tested',  color='blue', legend_label='Data Covid 19 - new_tested', line_width=2, source=dt_covid )
plot_2 = covidFig4.line(x='date', y='acc_tested',  color='orange', legend_label='Data Covid 19 - acc_tested', line_width=2, source=dt_covid )
plot_3 = covidFig4.line(x='date', y='being_checked',  color='green', legend_label='Data Covid 19 - being_checked', line_width=2, source=dt_covid )
plot_4 = covidFig4.line(x='date', y='isolated',  color='red', legend_label='Data Covid 19 - isolated', line_width=2, source=dt_covid )

covidFig.legend.location = 'top_left'
covidFig.legend.click_policy = 'hide'

covidFig2.legend.location = 'top_left'
covidFig2.legend.click_policy = 'hide'

covidFig3.legend.location = 'top_left'
covidFig3.legend.click_policy = 'hide'

covidFig4.legend.location = 'top_left'
covidFig4.legend.click_policy = 'hide'



# Visualisas Data Slider tentang DateTime dari 02 Maret 2020 - 31 Maret 2020
date_slider_acc = DateRangeSlider(value=(min(newDS1['date']), max(newDS1['date'])),
                              start=min(newDS1['date']),end=max(newDS1['date']),width=300)
date_slider_acc.js_link('value', covidFig.x_range, 'start', attr_selector=0)
date_slider_acc.js_link('value', covidFig.x_range, 'end', attr_selector=1)

date_slider_new = DateRangeSlider(value=(min(newDS1['date']), max(newDS1['date'])),
                              start=min(newDS1['date']),end=max(newDS1['date']),width=300)
date_slider_new.js_link('value', covidFig2.x_range, 'start', attr_selector=0)
date_slider_new.js_link('value', covidFig2.x_range, 'end', attr_selector=1)

date_slider_neg = DateRangeSlider(value=(min(newDS1['date']), max(newDS1['date'])),
                              start=min(newDS1['date']),end=max(newDS1['date']),width=300)
date_slider_neg.js_link('value', covidFig3.x_range, 'start', attr_selector=0)
date_slider_neg.js_link('value', covidFig3.x_range, 'end', attr_selector=1)

date_slider_tes = DateRangeSlider(value=(min(newDS1['date']), max(newDS1['date'])),
                              start=min(newDS1['date']),end=max(newDS1['date']),width=300)
date_slider_tes.js_link('value', covidFig4.x_range, 'start', attr_selector=0)
date_slider_tes.js_link('value', covidFig4.x_range, 'end', attr_selector=1)


# Visualisasi Data Untuk Interactive Select List
select = Select(title="Plot to show:", value="new_tested", options=["new_tested", "acc_tested", "being_checked", "isolated"])
select.js_on_change("value", CustomJS(args=dict(new_tested=plot_1, acc_tested=plot_2, being_checked=plot_3,  isolated=plot_4, tooltips=tool), code="""

new_tested.visible = true
acc_tested.visible = true
being_checked.visible = true
isolated.visible = true

if (this.value === "new_tested") {
    acc_tested.visible = false 
    being_checked.visible = false 
    isolated.visible = false 
} else if (this.value === "acc_tested") {
    new_tested.visible = false
    being_checked.visible = false 
    isolated.visible = false 
} else if (this.value === "being_checked") {
    new_tested.visible = false
    acc_tested.visible = false 
    isolated.visible = false 
} else  {
    new_tested.visible = false
    acc_tested.visible = false 
    being_checked.visible = false 
}
    
""")
)

# Mengubah format datetime sumbu x setiap figure 
covidFig.xaxis.formatter = DatetimeTickFormatter(months="%b %Y", days="%d %b")
covidFig2.xaxis.formatter = DatetimeTickFormatter(months="%b %Y", days="%d %b")
covidFig3.xaxis.formatter = DatetimeTickFormatter(months="%b %Y", days="%d %b")
covidFig4.xaxis.formatter = DatetimeTickFormatter(months="%b %Y", days="%d %b")

# Membuat 4 layout atau layar terdiri dari masing-masing data covid 
layout1 = layout(date_slider_acc, covidFig)
layout2 = layout(date_slider_new, covidFig2)
layout3 = layout(date_slider_neg, covidFig3)
layout4 = layout(select, date_slider_tes, covidFig4)

# Membuat 4 Tabs untuk setiap data covid yang ditampilkan 
panel_1 = Panel(child= layout1, title='acc_confirmed')
panel_2 = Panel(child= layout2, title='new_confirmed')
panel_3 = Panel(child= layout3, title='acc_negative')
panel_4 = Panel(child= layout4, title='Data Lain')

tabs = Tabs(tabs=[panel_1, panel_2, panel_3, panel_4])

curdoc().add_root(tabs)
show(tabs)
