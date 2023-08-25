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
    (-33.8678, 151.207, 'Resilans AB'),
    (45.4643, 9.1885, 'Venus Business Communications Limited'),
    (22.2855, 114.1577, 'Telstra Global'),
    (35.6895, 139.6923, 'Telstra Global')
]

linec1 = [
    '0',
    '0',
    '0',
    '0',
    '0'
]

line3 = [
    (-33.8678, 151.207, 'NetActuate Inc'),
    (-31.9522, 115.8614, 'Telstra Internet'),
    (22.2855, 114.1577, 'Reach Multi Media Satellite Services'),
    (37.4441, -122.1602, 'Reach Multi Media Satellite Services'),
    (45.5235, -122.6765, 'Amazon.com Inc.')
]

linec3 = [
    '0',
    '0',
    '0',
    '0'
]

line4 = [
    (-33.8678, 151.207, 'Resilans AB'),
    (45.4643, 9.1885, 'Venus Business Communications Limited'),
    (50.1109, 8.682, 'M247 Europe SRL'),
    (53.4809, -2.2374, 'M247 Europe SRL'),
    (37.7757, -122.3952, 'CloudFlare Inc.')
]

linec4 = [
    '0',
    '0',
    '0',
    '0',
    '0'
]

line5 = [
    (-33.8678, 151.207, 'NetActuate Inc'),
    (47.6024, -122.326, 'F5 Inc.'),
    (37.7749, -122.4194, 'PayPal Inc.'),
    (37.323, -122.0322, 'PayPal Inc.')
]

linec5 = [
    '0',
    '0',
    '0'
]

line6 = [
    (-33.8678, 151.207, 'OVH Australia Pty Ltd'),
    (-31.9522, 115.8614, 'They Call Me Joe'),
    (22.2855, 114.1577, 'OVH AP'),
    (47.6829, -122.1209, 'Microsoft Corporation')
]

linec6 = [
    '0',
    '0',
    '0'
]

line7 = [
    (-33.8678, 151.207, 'Amazon.com Inc.'),
    (-32.0077, 151.9633, 'Telstra Amazon'),
    (37.5483, -121.9886, 'Telstra Global'),
    (37.3394, -121.895, 'Tinet GmbH'),
    (40.7132, -74.0061, 'GTT Communications Inc.'),
    (38.8954, -77.0395, 'GTT'),
    (40.79, -74.0621, 'InterServer Inc.')
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
    (-33.8678, 151.207, 'Resilans AB'),
    (45.4643, 9.1885, 'Venus Business'),
    (50.1109, 8.682, 'M247 Europe SRL'),
    (53.4809, -2.2374, 'M247 Europe SRL'),
    (37.7757, -122.3952, 'Fastly Inc.')
]

lines = [line1, line3, line4, line5, line6, line7, line8]
line_comments = [linec1, linec3, linec4, linec5, linec6, linec7, linec7]


additional_points = [
    (50.1109, 8.682, 'DE-CIX Deutscher Commercial Internet Exchange - IXP')
]

custom_map = CustomMap(lines, line_comments, additional_points)
m = custom_map.create_map()
map_filename = 'understanding_4.html'
m.save(map_filename)

with open(map_filename, 'r') as f:
    html_content = f.read()
