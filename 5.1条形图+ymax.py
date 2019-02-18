from pyecharts import Overlap, Bar, Line, Grid

grid = Grid()

attr = ["{}月".format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

bar = Bar(title="Overlap+Grid 示例", title_pos="40%")
bar.add("蒸发量", attr, v1)
bar.add(
    "降水量",
    attr,
    v2,
    yaxis_formatter=" ml",
    yaxis_max=250,
    legend_pos="85%",
    legend_orient="vertical",
    legend_top="45%",
)
line = Line()
line.add("平均温度", attr, v3, yaxis_formatter=" °C")
overlap = Overlap(width=1200, height=600)
overlap.add(bar)
overlap.add(line, is_add_yaxis=True, yaxis_index=1)

grid.add(overlap, grid_right="20%")
grid.render()
