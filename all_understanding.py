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


l1 = [
    (19.076, 72.8774, 'Krunalshah Software Private Limited'),
    (28.6668, 77.2167, 'National Internet Exchange of India'),
    (37.406, -122.0785, 'Google LLC')
]


l2 = [
    (52.525, 5.718, 'Serverius Holding B.V.'),
    (51.845, 4.3287, 'LayerSwitch B.V.'),
    (37.3394, -121.895, 'Oath Holdings Inc.'),
    (41.2586, -95.9378, 'Oath Holdings Inc.'),
    (40.7313, -73.9901, 'Oath Holdings Inc.')
]


l3 = [
    (19.076, 72.8774, 'Krunalshah Software Private (Mumbai)'),
    (50.1109, 8.682, 'DE-CIX Management GmbH (Germany)'),
    (55.7523, 37.6155, 'Yandex LLC (Moscow)')
]


l4 = [
    (19.076, 72.8774, 'Krunalshah Software Private (Mumbai)'),
    (13.0879, 80.2785, 'CloudFlare Inc.'),
    (37.7757, -122.3952, 'CloudFlare Inc.')

]

l5 = [
    (19.076, 72.8774, 'Krunalshah Software Private Limited'),
    (28.6668, 77.2167, 'National Internet Exchange of India'),
    (37.4369, -122.1936, 'Facebook Inc.')
]


l6 = [
    (19.076, 72.8774, 'Krunalshah Software Private (Mumbai)'),
    (28.6668, 77.2167, 'National Internet Exchange (Delhi)'),
    (37.406, -122.0785, 'Google LLC (California)'),
    (39.0997, -94.5786, 'Google LLC (Missouri, US)')
]


l7 = [
    (19.076, 72.8774, 'Krunalshah Software Private Limited'),
    (47.6829, -122.1209, 'Microsoft Corporation')
]

l8 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (16.5033, 80.6465, 'Reliance Jio Infocomm Limited'),
    (1.2929, 103.8547, 'Telstra Global'),
    (22.2578, 114.1657, 'Telstra Global'),
    (22.2578, 114.1657, 'Level 30, Tower 1'),
    (34.7732, 113.722, 'China Mobile Communications Group Co., Ltd.')
]


l9 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (37.751, -97.822, 'GOOGLE'),
    (40.3913, -74.3247, 'GOOGLE')
]


l10 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (16.5033, 80.6465, 'Reliance Jio Infocomm Limited (Vijayawada)'),
    (35.6966, 139.656, 'Yahoo Japan')
]


l11 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (19.0748, 72.8856, 'Reliance Jio Infocomm Limited'),
    (37.751, -97.822, 'FACEBOOK')
]


l12 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (16.5033, 80.6465, 'Reliance Jio Infocomm Limited'),
    (21.9974, 79.0011, 'Tata Communications Ltd.'),
    (-33.8601, 151.2101, 'Tata Communications Ltd.'),
    (37.751, -97.822, 'Globo Comunicacao e Participacoes SA')
]


l13 = [
    (17.3724, 78.4378, 'IIT Hyderabad'),
    (16.5033, 80.6465, 'Reliance Jio Infocomm Limited'),
    (21.9974, 79.0011, 'Reliance Jio Infocomm Pte Ltd Singapore'),
    (34.0544, -118.2441, 'LEVEL3'),
    (37.751, -97.822, 'NTT-LTD-2914'),
    (35.6897, 139.6895, 'NTT-LTD-2914'),
    (35.7277, 139.8964, 'NTT Communications Corporation'),
    (35.1926, 136.906, 'NTT Communications Corporation')
]

l14 = [
    (52.3785, 4.9, 'DataCamp Limited'),
    (50.0879, 14.4208, 'DataCamp Limited'),
    (49.4478, 11.0683, 'Core-Backbone GmbH'),
    (45.4643, 9.1885, 'MIX S.r.L. - Milan Internet eXchange'),
    (43.7175, 10.9414, 'Leonet4Cloud srl')
]

l15 = [
    (52.3785, 4.9, 'DataCamp Limited'),
    (50.0879, 14.4208, 'Unknown'),
    (48.8591, 2.2935, 'Cogent Communications Inc.'),
    (43.2629, -2.9254, 'Cogent Communications Inc.'),
    (38.881, -77.1043, 'Cogent Communications Inc.'),
    (33.7488, -84.3875, 'Newfold Digital'),
    (30.1911, -81.493, 'Newfold Digital'),
    (30.3321, -81.6557, 'WebsiteWelcome.com')
]


l16 = [
    (52.3785, 4.9, 'DataCamp Limited'),
    (49.4478, 11.0683, 'Core-Backbone GmbH'),
    (45.4643, 9.1885, 'MIX S.r.L. - Milan Internet eXchange'),
    (43.7175, 10.9414, 'Leonet4Cloud srl')
]


l17 = [
    (52.3785, 4.9, 'DataCamp Limited'),
    (51.5308, 4.4654, 'NForce Entertainment B.V.'),
    (37.7757, -122.3952, 'CloudFlare Inc.')
]


l18 = [
    (52.3785, 4.9, 'DataCamp Limited'),
    (50.0879, 14.4208, 'DataCamp Limited'),
    (53.3442, -6.2672, 'Amazon Technologies Inc.'),
    (47.6275, -122.3462, 'Amazon Technologies Inc.'),
]


l19 = [
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


l20 = [
    (-33.8678, 151.207, 'Resilans AB'),
    (45.4643, 9.1885, 'Venus Business Communications Limited'),
    (22.2855, 114.1577, 'Telstra Global'),
    (35.6895, 139.6923, 'Telstra Global')
]


l21 = [
    (-33.8678, 151.207, 'NetActuate Inc'),
    (-31.9522, 115.8614, 'Telstra Internet'),
    (22.2855, 114.1577, 'Reach Multi Media Satellite Services'),
    (37.4441, -122.1602, 'Reach Multi Media Satellite Services'),
    (45.5235, -122.6765, 'Amazon.com Inc.')
]

l22 = [
    (-33.8678, 151.207, 'Resilans AB'),
    (45.4643, 9.1885, 'Venus Business Communications Limited'),
    (50.1109, 8.682, 'M247 Europe SRL'),
    (53.4809, -2.2374, 'M247 Europe SRL'),
    (37.7757, -122.3952, 'CloudFlare Inc.')
]

l23 = [
    (-33.8678, 151.207, 'NetActuate Inc'),
    (47.6024, -122.326, 'F5 Inc.'),
    (37.7749, -122.4194, 'PayPal Inc.'),
    (37.323, -122.0322, 'PayPal Inc.')
]


l24 = [
    (-33.8678, 151.207, 'OVH Australia Pty Ltd'),
    (-31.9522, 115.8614, 'They Call Me Joe'),
    (22.2855, 114.1577, 'OVH AP'),
    (47.6829, -122.1209, 'Microsoft Corporation')
]


l25 = [
    (-33.8678, 151.207, 'Amazon.com Inc.'),
    (-32.0077, 151.9633, 'Telstra Amazon'),
    (37.5483, -121.9886, 'Telstra Global'),
    (37.3394, -121.895, 'Tinet GmbH'),
    (40.7132, -74.0061, 'GTT Communications Inc.'),
    (38.8954, -77.0395, 'GTT'),
    (40.79, -74.0621, 'InterServer Inc.')
]


l26 = [
    (-33.8678, 151.207, 'Resilans AB'),
    (45.4643, 9.1885, 'Venus Business'),
    (50.1109, 8.682, 'M247 Europe SRL'),
    (53.4809, -2.2374, 'M247 Europe SRL'),
    (37.7757, -122.3952, 'Fastly Inc.')
]

l27 = [
    (34.6942, 135.5022, 'xTom GmbH'),
    (35.6895, 139.6923, 'DataCamp Limited'),
    (50.0879, 14.4208, 'DataCamp Limited'),
    (51.5085, -0.1257, 'Vodafone Ltd'),
    (37.9576, -121.2907, 'Vodafone Ltd'),
    (45.4643, 9.1885, 'Vodafone Ltd'),
    (50.8508, 4.3488, 'Vodafone Ltd'),
    (37.9795, 23.7162, 'Vodafone-Panafon Hellenic')
]

lines = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14,
         l15, l16, l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27]

c = [
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
line_comments = []
for i in lines:
    line_comments.append(c)

additional_points = []

custom_map = CustomMap(lines, line_comments, additional_points)
m = custom_map.create_map()
map_filename = 'all_understanding.html'
m.save(map_filename)

with open(map_filename, 'r') as f:
    html_content = f.read()
