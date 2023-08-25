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
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (16.5033, 80.6465, 'Reliance Jio Infocomm Limited'),
    (1.2929, 103.8547, 'Telstra Global'),
    (22.2578, 114.1657, 'Telstra Global'),
    (22.2578, 114.1657, 'Level 30, Tower 1'),
    (34.7732, 113.722, 'China Mobile Communications Group Co., Ltd.')
]

linec1 = [
    '0',
    '0',
    '0',
    '0',
    '0',
    '0'
]

line3 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (37.751, -97.822, 'GOOGLE'),
    (40.3913, -74.3247, 'GOOGLE')
]

linec3 = [
    '0',
    '0'
]

line4 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (16.5033, 80.6465, 'Reliance Jio Infocomm Limited (Vijayawada)'),
    (35.6966, 139.656, 'Yahoo Japan')
]

linec4 = [
    '0',
    '0'
]

line5 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (19.0748, 72.8856, 'Reliance Jio Infocomm Limited'),
    (37.751, -97.822, 'FACEBOOK')
]

linec5 = [
    '0',
    '0'
]

line6 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (16.5033, 80.6465, 'Reliance Jio Infocomm Limited'),
    (21.9974, 79.0011, 'Tata Communications Ltd.'),
    (-33.8601, 151.2101, 'Tata Communications Ltd.'),
    (37.751, -97.822, 'Globo Comunicacao e Participacoes SA')
]

linec6 = [
    '0',
    '0',
    '0',
    '0',
    '0'
]

line7 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (16.5033, 80.6465, 'Reliance Jio Infocomm Limited'),
    (21.9974, 79.0011, 'Reliance Jio Infocomm Pte Ltd Singapore'),
    (34.0544, -118.2441, 'LEVEL3'),
    (37.751, -97.822, 'NTT-LTD-2914'),
    (35.6897, 139.6895, 'NTT-LTD-2914'),
    (35.7277, 139.8964, 'NTT Communications Corporation'),
    (35.1926, 136.906, 'NTT Communications Corporation')
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

additional_points = [
    (28.6668, 77.2167, 'National Internet Exchange of India - IXP')
]

lines = [line1, line3, line4, line5, line6, line7]
line_comments = [linec1, linec3, linec4, linec5, linec6, linec7]

custom_map = CustomMap(lines, line_comments, additional_points)
m = custom_map.create_map()
map_filename = 'understanding_2.html'
m.save(map_filename)

with open(map_filename, 'r') as f:
    html_content = f.read()
