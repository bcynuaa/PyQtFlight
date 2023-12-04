from PySide2.QtWidgets import QApplication
from pglive.sources.data_connector import DataConnector
from pglive.sources.live_plot import LiveVBarPlot, LiveLinePlot
from pglive.sources.live_plot_widget import LivePlotWidget
from pglive.sources.live_candleStickPlot import LiveCandleStickPlot

app = QApplication([])

bar_width: float = 10
bar_spacing: float = 5

n_bars: int = 20

first_bar_x_position: float = 0

import numpy as np

bars_x_positions: np.arange = np.arange(first_bar_x_position, first_bar_x_position + n_bars * (bar_width + bar_spacing), bar_width + bar_spacing)+bar_width/2

bars_x_ticks: list = [(bars_x_positions[i], "%d"%i) for i in range(n_bars)]

plot_widget = LivePlotWidget(title="TestCandleStickPlot")
candle_stick_plot = LiveVBarPlot(bar_width=bar_width, y0=0)
plot_widget.addItem(candle_stick_plot)

plot_widget.setBackground("w")

line_plot = LiveLinePlot(pen=({"color": "r", "width": 2}))

data_connector_line = DataConnector(line_plot, max_points=40)

plot_widget.addItem(line_plot)

data_connector_line.cb_set_data([0.5, 0.5], [bars_x_positions[0]-bar_width/2, bars_x_positions[-1]+bar_width/2])

data_connector = DataConnector(candle_stick_plot, max_points=40)

# x = np.arange(0, 40, 5)
# y = np.abs(np.sin(x))

y = np.abs(np.sin(bars_x_positions))

axis = plot_widget.getAxis('bottom')
axis.setTicks([bars_x_ticks])

data_connector.cb_set_data(y, x=bars_x_positions)

# plot_widget.setXRange(x.min(), x.max(), padding=0.1)



plot_widget.show()

app.exec_()