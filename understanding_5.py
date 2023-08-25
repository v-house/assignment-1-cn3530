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
    (34.6942, 135.5022, 'xTom GmbH'),
    (34.6942, 139.6923, 'ntt.net Global IP Network'),
    (32.7831, -96.8065, 'NTT America Inc.'),
    (37.7757, -122.3952, 'CloudFlare Inc.')
]

linec1 = [
    '0',
    '0',
    '0',
    '0',
    '0'
]

line3 = [
    (34.6942, 135.5022, 'xTom GmbH'),
    (32.7831, -96.8065, 'NTT America Inc.'),
    (50.1109, 8.682, 'Lumen Technologies UK'),
    (49.4478, 11.0683, 'Core-Backbone GmbH'),
    (40.3779, 49.8919, 'Delta Telecom Ltd'),
    (35.6942, 51.4213, 'Abazarhaye Farsi Shabakeh')
]

linec3 = [
    '0',
    '0',
    '0',
    '0',
    '0',
    '0'
]

line4 = [
    (34.6942, 135.5022, 'xTom GmbH'),
    (32.7831, -96.8065, 'NTT America Inc.'),
    (47.6043, -122.3298, 'Arelion Sweden AB'),
    (41.8758, -87.6206, 'Arelion Sweden AB'),
    (52.4069, 16.93, 'Arelion Sweden AB'),
    (50.8508, 4.3488, 'Arelion Sweden AB'),
    (52.2298, 21.0118, 'Allegro Sp. Z o.o.')
]

linec4 = [
    '0',
    '0',
    '0',
    '0',
    '0',
    '0',
    '0'
]

line5 = [
    (34.6942, 135.5022, 'xTom GmbH'),
    (32.7831, -96.8065, 'NTT America Inc.'),
    (47.6043, -122.3298, 'NTT America Inc.'),
    (41.8758, -87.6206, 'Arelion Sweden AB'),
    (40.7132, -74.0061, 'Arelion Sweden AB'),
    (52.4069, 16.93, 'Arelion Sweden AB'),
    (50.8508, 4.3488, 'Arelion Sweden AB'),
    (52.2298, 21.0118, 'Arelion Sweden AB')
]

linec5 = [
    '0',
    '0',
    '0',
    '0',
    '0',
    '0',
    '0',
    '0'
]

line6 = [
    (34.6942, 135.5022, 'xTom GmbH'),
    (53.2192, 6.567, 'Marka')
]

linec6 = [
    '0',
    '0',
    '0'
]

line7 = [
    (34.6942, 135.5022, 'xTom GmbH'),
    (37.406, -122.0785, 'Spain info')
]


linec7 = [
    '0',
    '0',
    '0',
    '0',
    '0',
    '0',
    '0'
]

line8 = [
    (34.6942, 135.5022, 'xTom GmbH'),
    (35.6895, 139.6923, 'DataCamp Limited'),
    (50.0879, 14.4208, 'DataCamp Limited'),
    (51.5085, -0.1257, 'Vodafone Ltd'),
    (37.9576, -121.2907, 'Vodafone Ltd'),
    (45.4643, 9.1885, 'Vodafone Ltd'),
    (50.8508, 4.3488, 'Vodafone Ltd'),
    (37.9795, 23.7162, 'Vodafone-Panafon Hellenic')
]

lines = [line1, line3, line4, line5, line6, line7, line8]
line_comments = [linec1, linec3, linec4, linec5, linec6, linec7, linec7]


additional_points = [
    (50.1109, 8.682, 'DE-CIX Deutscher Commercial Internet Exchange - IXP')
]

custom_map = CustomMap(lines, line_comments, additional_points)
m = custom_map.create_map()
map_filename = 'understanding_5.html'
m.save(map_filename)

with open(map_filename, 'r') as f:
    html_content = f.read()
