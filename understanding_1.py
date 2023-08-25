import folium
from folium import plugins
from geopy.distance import geodesic


class CustomMap:
    def __init__(self, lines, line_comments, additional_points=None):
        self.lines = lines
        self.line_comments = line_comments
        self.additional_points = additional_points or []

    def create_map(self):
        m = folium.Map(location=[0, 0], zoom_start=2,
                       tiles='CartoDB positron', control_scale=True)
        ant_path_data = []

        for line_data, line_comment in zip(self.lines, self.line_comments):
            line_coordinates = []
            ant_path_data = []
            for i, (lat, lon, label) in enumerate(line_data):
                if isinstance(lat, (float, int)) and isinstance(lon, (float, int)):
                    popup = folium.Popup(label)
                    line_coordinates.append((lat, lon))
                    ant_path_data.append((lat, lon))

                    if i == 0:
                        marker_color = 'green'
                    elif i == len(line_data) - 1:
                        marker_color = 'red'
                    else:
                        marker_color = 'yellow'

                    folium.CircleMarker(
                        [lat, lon],
                        radius=5,
                        popup=popup,
                        color=marker_color,
                        fill=True,
                        fill_color=marker_color,
                        fill_opacity=1,
                        prefix="custom-icon blink"
                    ).add_to(m)

            shortest_path = self.get_shortest_path(line_coordinates)
            ant_path = plugins.AntPath(ant_path_data, dash_array=[
                                       10, 20], weight=1, color='blue')
            m.add_child(ant_path)

            for i in range(len(shortest_path) - 1):
                start_coord = shortest_path[i]
                end_coord = shortest_path[i + 1]
                folium.PolyLine([start_coord, end_coord],
                                color='green', weight=1, opacity=1).add_to(m)
            for lat, lon, label in self.additional_points:
                folium.CircleMarker(
                    [lat, lon],
                    radius=5,
                    popup=label,
                    color='yellow',
                    fill=True,
                    fill_color='yellow',
                    fill_opacity=1,
                    prefix="custom-icon blink"
                ).add_to(m)
                folium.Marker(
                    [lat, lon],
                    icon=None,
                    tooltip=label,
                    popup=label,
                ).add_to(m)

        return m

    def get_shortest_path(self, coordinates):
        shortest_path = [coordinates[0]]
        for i in range(1, len(coordinates)):
            dist1 = geodesic(shortest_path[-1], coordinates[i]).kilometers
            dist2 = geodesic(shortest_path[-1], coordinates[-1]).kilometers
            if dist1 < dist2:
                shortest_path.append(coordinates[i])
            else:
                break
        return shortest_path


line1 = [
    (19.076, 72.8774, 'Krunalshah Software Private Limited'),
    (28.6668, 77.2167, 'National Internet Exchange of India'),
    (37.406, -122.0785, 'Google LLC')
]

linec1 = [
    '3',
    '2'
]

line2 = [
    (52.525, 5.718, 'Serverius Holding B.V.'),
    (51.845, 4.3287, 'LayerSwitch B.V.'),
    (37.3394, -121.895, 'Oath Holdings Inc.'),
    (41.2586, -95.9378, 'Oath Holdings Inc.'),
    (40.7313, -73.9901, 'Oath Holdings Inc.')
]

linec2 = [
    '1',
    '0',
    '0',
    '0'
]

line3 = [
    (19.076, 72.8774, 'Krunalshah Software Private (Mumbai)'),
    (50.1109, 8.682, 'DE-CIX Management GmbH (Germany)'),
    (55.7523, 37.6155, 'Yandex LLC (Moscow)')
]

linec3 = [
    '0',
    '0'
]

line4 = [
    (19.076, 72.8774, 'Krunalshah Software Private (Mumbai)'),
    (13.0879, 80.2785, 'CloudFlare Inc.'),
    (37.7757, -122.3952, 'CloudFlare Inc.')
]

linec4 = [
    '0',
    '0'
]

line5 = [
    (19.076, 72.8774, 'Krunalshah Software Private Limited'),
    (28.6668, 77.2167, 'National Internet Exchange of India'),
    (37.4369, -122.1936, 'Facebook Inc.')
]

linec5 = [
    '0',
    '0'
]

line6 = [
    (19.076, 72.8774, 'Krunalshah Software Private (Mumbai)'),
    (28.6668, 77.2167, 'National Internet Exchange (Delhi)'),
    (37.406, -122.0785, 'Google LLC (California)'),
    (39.0997, -94.5786, 'Google LLC (Missouri, US)')
]

linec6 = [
    '0',
    '0',
    '0'
]

line7 = [
    (19.076, 72.8774, 'Krunalshah Software Private Limited'),
    (47.6829, -122.1209, 'Microsoft Corporation')
]


linec7 = [
    '0'
]

lines = [line1, line3, line4, line5, line6, line7]
line_comments = [linec1, linec3, linec4, linec5, linec6, linec7]


additional_points = [
    (50.1109, 8.682, 'DE-CIX Deutscher Commercial Internet Exchange - IXP'),
    (28.6668, 77.2167, 'National Internet Exchange of India - IXP')
]

custom_map = CustomMap(lines, line_comments, additional_points)
m = custom_map.create_map()
map_filename = 'understanding_1.html'
m.save(map_filename)

with open(map_filename, 'r') as f:
    html_content = f.read()
