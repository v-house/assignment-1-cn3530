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
    (52.3785, 4.9, 'DataCamp Limited'),
    (50.0879, 14.4208, 'DataCamp Limited'),
    (49.4478, 11.0683, 'Core-Backbone GmbH'),
    (45.4643, 9.1885, 'MIX S.r.L. - Milan Internet eXchange'),
    (43.7175, 10.9414, 'Leonet4Cloud srl')
]

linec1 = [
    '0',
    '0',
    '0',
    '0'
]

line3 = [
    (52.3785, 4.9, 'DataCamp Limited'),
    (50.0879, 14.4208, 'Unknown'),
    (48.8591, 2.2935, 'Cogent Communications Inc.'),
    (43.2629, -2.9254, 'Cogent Communications Inc.'),
    (38.881, -77.1043, 'Cogent Communications Inc.'),
    (33.7488, -84.3875, 'Newfold Digital'),
    (30.1911, -81.493, 'Newfold Digital'),
    (30.3321, -81.6557, 'WebsiteWelcome.com')
]

linec3 = [
    '0',
    '0',
    '0',
    '0',
    '0',
    '0',
    '0'
]

line4 = [
    (52.3785, 4.9, 'DataCamp Limited'),
    (49.4478, 11.0683, 'Core-Backbone GmbH'),
    (45.4643, 9.1885, 'MIX S.r.L. - Milan Internet eXchange'),
    (43.7175, 10.9414, 'Leonet4Cloud srl')
]

linec4 = [
    '0',
    '0',
    '0'
]

line5 = [
    (52.3785, 4.9, 'DataCamp Limited'),
    (51.5308, 4.4654, 'NForce Entertainment B.V.'),
    (37.7757, -122.3952, 'CloudFlare Inc.')
]

linec5 = [
    '0',
    '0',
    '0'
]

line6 = [
    (52.3785, 4.9, 'DataCamp Limited'),
    (50.0879, 14.4208, 'DataCamp Limited'),
    (53.3442, -6.2672, 'Amazon Technologies Inc.'),
    (47.6275, -122.3462, 'Amazon Technologies Inc.'),
]

linec6 = [
    '0',
    '0',
    '0'
]

line7 = [
    (52.3785, 4.9, 'DataCamp Limited'),
    (51.5308, 4.4654, 'NForce Entertainment B.V.'),
    (51.5085, -0.1257, 'NTT America Inc.'),
    (40.7323, -74.1736, 'NTT America Inc.'),
    (39.0395, -77.4918, 'NTT America Inc.'),
    (34.0526, -118.2439, 'NTT America Inc.'),
    (47.6829, -122.1209, 'NTT America Inc.'),
    (40.7132, -74.0061, 'NTT America Inc.'),
    (35.6895, 139.6923, 'NTT Resonant Incorporate')
]


linec7 = [
    '0',
    '0',
    '0',
    '0',
    '0',
    '0',
    '0',
    '0',
    '0',
    '0',
    '0'
]

additional_points = [
    (45.4643, 9.1885, 'MIX S.r.L. - Milan Internet eXchange')
]

lines = [line1, line3, line4, line5, line6, line7]
line_comments = [linec1, linec3, linec4, linec5, linec6, linec7]

custom_map = CustomMap(lines, line_comments, additional_points)
m = custom_map.create_map()
map_filename = 'understanding_3.html'
m.save(map_filename)

with open(map_filename, 'r') as f:
    html_content = f.read()
