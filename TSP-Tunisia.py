import networkx as nx


graph = nx.Graph()

#Distance from Bizerte to other cities

graph.add_edge('Bizerte','Ariana', weight = 64)
graph.add_edge('Bizerte', 'Beja', weight = 116)
graph.add_edge('Bizerte', 'Ben Arous', weight = 80)
graph.add_edge('Bizerte', 'Gabes', weight = 484)
graph.add_edge('Bizerte', 'Gafsa', weight = 432)
graph.add_edge('Bizerte', 'Jendouba', weight = 158)
graph.add_edge('Bizerte', 'Kairouan', weight = 231)
graph.add_edge('Bizerte', 'Kasserine', weight = 367)
graph.add_edge('Bizerte', 'Kebili', weight = 579)
graph.add_edge('Bizerte', 'Kef', weight = 236)
graph.add_edge('Bizerte', 'Mahdia', weight = 279)
graph.add_edge('Bizerte', 'Manouba', weight = 77)
graph.add_edge('Bizerte', 'Medenine', weight = 557)
graph.add_edge('Bizerte', 'Monastir', weight = 238)
graph.add_edge('Bizerte', 'Nabeul', weight = 137)
graph.add_edge('Bizerte', 'Sfax', weight = 339)
graph.add_edge('Bizerte', 'Sidi Bouzid', weight = 338)
graph.add_edge('Bizerte', 'Siliana', weight = 200)
graph.add_edge('Bizerte', 'Sousse', weight = 216)
graph.add_edge('Bizerte', 'Tataouine', weight = 644)
graph.add_edge('Bizerte', 'Tozeur', weight = 524)
graph.add_edge('Bizerte', 'Tunis', weight = 70)
graph.add_edge('Bizerte', 'Zaghouan', weight = 126)


#Distance from Ariana to other cities

graph.add_edge('Ariana','Beja', weight =119)
graph.add_edge('Ariana','Ben Arous', weight =21)
graph.add_edge('Ariana','Gabes', weight = 426)
graph.add_edge('Ariana','Gafsa', weight = 374)
graph.add_edge('Ariana','Jendouba', weight = 160)
graph.add_edge('Ariana','Kairouan', weight = 173)
graph.add_edge('Ariana','Kasserine', weight = 310)
graph.add_edge('Ariana','Kebili', weight = 521)
graph.add_edge('Ariana','Kef', weight = 172)
graph.add_edge('Ariana','Mahdia', weight = 221)
graph.add_edge('Ariana','Manouba', weight =14)
graph.add_edge('Ariana','Medenine', weight = 500)
graph.add_edge('Ariana','Monastir', weight = 180)
graph.add_edge('Ariana','Nabeul', weight =79)
graph.add_edge('Ariana','Sfax', weight =281)
graph.add_edge('Ariana','Sidi Bouzid', weight = 280)
graph.add_edge('Ariana','Siliana', weight =137)
graph.add_edge('Ariana','Sousse', weight =159)
graph.add_edge('Ariana','Tataouine', weight =466)
graph.add_edge('Ariana','Tozeur', weight =137)
graph.add_edge('Ariana','Tunis', weight =13)
graph.add_edge('Ariana','Zaghouan', weight =68)

#Distance from Beja to other cities
graph.add_edge('Beja','Ben Arous', weight =122)
graph.add_edge('Beja','Gabes', weight = 408)
graph.add_edge('Beja','Gafsa', weight = 335)
graph.add_edge('Beja','Jendouba', weight = 50)
graph.add_edge('Beja','Kairouan', weight = 187)
graph.add_edge('Beja','Kasserine', weight = 233)
graph.add_edge('Beja','Kebili', weight = 503)
graph.add_edge('Beja','Kef', weight = 105)
graph.add_edge('Beja','Mahdia', weight = 265)
graph.add_edge('Beja','Manouba', weight =109)
graph.add_edge('Beja','Medenine', weight = 482)
graph.add_edge('Beja','Monastir', weight = 224)
graph.add_edge('Beja','Nabeul', weight =179)
graph.add_edge('Beja','Sfax', weight = 325)
graph.add_edge('Beja','Sidi Bouzid', weight = 261)
graph.add_edge('Beja','Siliana', weight =102)
graph.add_edge('Beja','Sousse', weight =203)
graph.add_edge('Beja','Tataouine', weight = 568)
graph.add_edge('Beja','Tozeur', weight = 427)
graph.add_edge('Beja','Tunis', weight = 117)
graph.add_edge('Beja','Zaghouan', weight = 133)

#Distance from Ben Arous to other cities

graph.add_edge('Ben Arous','Gabes', weight = 408)
graph.add_edge('Ben Arous','Gafsa', weight = 356)
graph.add_edge('Ben Arous','Jendouba', weight = 162)
graph.add_edge('Ben Arous','Kairouan', weight = 155)
graph.add_edge('Ben Arous','Kasserine', weight = 291)
graph.add_edge('Ben Arous','Kebili', weight = 503)
graph.add_edge('Ben Arous','Kef', weight = 174)
graph.add_edge('Ben Arous','Mahdia', weight = 203)
graph.add_edge('Ben Arous','Manouba', weight =21)
graph.add_edge('Ben Arous','Medenine', weight = 481)
graph.add_edge('Ben Arous','Monastir', weight = 162)
graph.add_edge('Ben Arous','Nabeul', weight =61)
graph.add_edge('Ben Arous','Sfax', weight = 263)
graph.add_edge('Ben Arous','Sidi Bouzid', weight = 262)
graph.add_edge('Ben Arous','Siliana', weight = 124)
graph.add_edge('Ben Arous','Sousse', weight = 140)
graph.add_edge('Ben Arous','Tataouine', weight = 568)
graph.add_edge('Ben Arous','Tozeur', weight = 448)
graph.add_edge('Ben Arous','Tunis', weight = 11)
graph.add_edge('Ben Arous','Zaghouan', weight = 50)

#Distance from Gabes to other cities
graph.add_edge('Gabes','Gafsa', weight = 155)
graph.add_edge('Gabes','Jendouba', weight = 386)
graph.add_edge('Gabes','Kairouan', weight = 221)
graph.add_edge('Gabes','Kasserine', weight = 250)
graph.add_edge('Gabes','Kebili', weight = 118)
graph.add_edge('Gabes','Kef', weight = 155)
graph.add_edge('Gabes','Mahdia', weight = 262)
graph.add_edge('Gabes','Manouba', weight = 424)
graph.add_edge('Gabes','Medenine', weight = 82)
graph.add_edge('Gabes','Monastir', weight = 281)
graph.add_edge('Gabes','Nabeul', weight = 376)
graph.add_edge('Gabes','Sfax', weight = 160)
graph.add_edge('Gabes','Sidi Bouzid', weight = 176)
graph.add_edge('Gabes','Siliana', weight = 298)
graph.add_edge('Gabes','Sousse', weight = 279)
graph.add_edge('Gabes','Tataouine', weight = 169)
graph.add_edge('Gabes','Tozeur', weight = 209)
graph.add_edge('Gabes','Tunis', weight = 414)
graph.add_edge('Gabes','Zaghouan', weight = 370)

#Distance from Gafsa to other cities

graph.add_edge('Gafsa','Jendouba', weight = 287)
graph.add_edge('Gafsa','Kairouan', weight = 203)
graph.add_edge('Gafsa','Kasserine', weight = 111)
graph.add_edge('Gafsa','Kebili', weight = 111)
graph.add_edge('Gafsa','Kef', weight = 233)
graph.add_edge('Gafsa','Mahdia', weight = 325)
graph.add_edge('Gafsa','Manouba', weight = 343)
graph.add_edge('Gafsa','Medenine', weight = 230)
graph.add_edge('Gafsa','Monastir', weight = 275)
graph.add_edge('Gafsa','Nabeul', weight = 326)
graph.add_edge('Gafsa','Sfax', weight = 202)
graph.add_edge('Gafsa','Sidi Bouzid', weight = 103)
graph.add_edge('Gafsa','Siliana', weight = 250)
graph.add_edge('Gafsa','Sousse', weight = 261)
graph.add_edge('Gafsa','Tataouine', weight = 317)
graph.add_edge('Gafsa','Tozeur', weight = 92)
graph.add_edge('Gafsa','Tunis', weight = 364)
graph.add_edge('Gafsa','Zaghouan', weight = 300)

#Distance from Jendouba to other cities

graph.add_edge('Jendouba','Kairouan', weight = 202)
graph.add_edge('Jendouba','Kasserine', weight = 185)
graph.add_edge('Jendouba','Kebili', weight = 399)
graph.add_edge('Jendouba','Kef', weight = 57)
graph.add_edge('Jendouba','Mahdia', weight = 360)
graph.add_edge('Jendouba','Manouba', weight = 148)
graph.add_edge('Jendouba','Medenine', weight = 462)
graph.add_edge('Jendouba','Monastir', weight = 320)
graph.add_edge('Jendouba','Nabeul', weight = 219)
graph.add_edge('Jendouba','Sfax', weight = 319)
graph.add_edge('Jendouba','Sidi Bouzid', weight = 213)
graph.add_edge('Jendouba','Siliana', weight = 103)
graph.add_edge('Jendouba','Sousse', weight = 298)
graph.add_edge('Jendouba','Tataouine', weight = 548)
graph.add_edge('Jendouba','Tozeur', weight = 379)
graph.add_edge('Jendouba','Tunis', weight = 157)
graph.add_edge('Jendouba','Zaghouan', weight = 173)

#Distance from Kairouan to other cities

graph.add_edge('Kairouan','Kasserine', weight = 138)
graph.add_edge('Kairouan','Kebili', weight = 318)
graph.add_edge('Kairouan','Kef', weight = 171)
graph.add_edge('Kairouan','Mahdia', weight = 102)
graph.add_edge('Kairouan','Manouba', weight = 154)
graph.add_edge('Kairouan','Medenine', weight = 296)
graph.add_edge('Kairouan','Monastir', weight = 69)
graph.add_edge('Kairouan','Nabeul', weight = 124)
graph.add_edge('Kairouan','Sfax', weight = 138)
graph.add_edge('Kairouan','Sidi Bouzid', weight = 106)
graph.add_edge('Kairouan','Siliana', weight = 101)
graph.add_edge('Kairouan','Sousse', weight = 55)
graph.add_edge('Kairouan','Tataouine', weight = 383)
graph.add_edge('Kairouan','Tozeur', weight = 294)
graph.add_edge('Kairouan','Tunis', weight = 162)
graph.add_edge('Kairouan','Zaghouan', weight = 110)

#Distance from Kasserine to other cities

graph.add_edge('Kasserine','Kebili', weight = 223)
graph.add_edge('Kasserine','Kef', weight = 130)
graph.add_edge('Kasserine','Mahdia', weight = 243)
graph.add_edge('Kasserine','Manouba', weight = 270)
graph.add_edge('Kasserine','Medenine', weight = 324)
graph.add_edge('Kasserine','Monastir', weight = 210)
graph.add_edge('Kasserine','Nabeul', weight = 261)
graph.add_edge('Kasserine','Sfax', weight = 199)
graph.add_edge('Kasserine','Sidi Bouzid', weight = 74)
graph.add_edge('Kasserine','Siliana', weight = 145)
graph.add_edge('Kasserine','Sousse', weight = 196)
graph.add_edge('Kasserine','Tataouine', weight = 411)
graph.add_edge('Kasserine','Tozeur', weight = 202)
graph.add_edge('Kasserine','Tunis', weight = 299)
graph.add_edge('Kasserine','Zaghouan', weight = 235)

#Distance from Kebili to other cities

graph.add_edge('Kebili','Kef', weight = 344)
graph.add_edge('Kebili','Mahdia', weight = 361)
graph.add_edge('Kebili','Manouba', weight = 519)
graph.add_edge('Kebili','Medenine', weight = 192)
graph.add_edge('Kebili','Monastir', weight = 380)
graph.add_edge('Kebili','Nabeul', weight = 475)
graph.add_edge('Kebili','Sfax', weight = 255)
graph.add_edge('Kebili','Sidi Bouzid', weight = 205)
graph.add_edge('Kebili','Siliana', weight = 352)
graph.add_edge('Kebili','Sousse', weight = 378)
graph.add_edge('Kebili','Tataouine', weight = 279)
graph.add_edge('Kebili','Tozeur', weight = 96)
graph.add_edge('Kebili','Tunis', weight = 510)
graph.add_edge('Kebili','Zaghouan', weight = 465)

#Distance from Kef to other cities

graph.add_edge('Kef','Mahdia', weight = 275)
graph.add_edge('Kef','Manouba', weight = 160)
graph.add_edge('Kef','Medenine', weight = 415)
graph.add_edge('Kef','Monastir', weight = 242)
graph.add_edge('Kef','Nabeul', weight = 230)
graph.add_edge('Kef','Sfax', weight = 290)
graph.add_edge('Kef','Sidi Bouzid', weight = 165)
graph.add_edge('Kef','Siliana', weight = 72)
graph.add_edge('Kef','Sousse', weight = 228)
graph.add_edge('Kef','Tataouine', weight = 502)
graph.add_edge('Kef','Tozeur', weight = 324)
graph.add_edge('Kef','Tunis', weight = 168)
graph.add_edge('Kef','Zaghouan', weight = 148)

#Distance from Mahdia to other cities

graph.add_edge('Mahdia','Manouba', weight = 219)
graph.add_edge('Mahdia','Medenine', weight = 337)
graph.add_edge('Mahdia','Monastir', weight = 49)
graph.add_edge('Mahdia','Nabeul', weight = 172)
graph.add_edge('Mahdia','Sfax', weight = 119)
graph.add_edge('Mahdia','Sidi Bouzid', weight = 187)
graph.add_edge('Mahdia','Siliana', weight = 204)
graph.add_edge('Mahdia','Sousse', weight = 59)
graph.add_edge('Mahdia','Tataouine', weight = 424)
graph.add_edge('Mahdia','Tozeur', weight = 449)
graph.add_edge('Mahdia','Tunis', weight = 209)
graph.add_edge('Mahdia','Zaghouan', weight = 165)

#Distance from Manouba to other cities

graph.add_edge('Manouba','Medenine', weight = 498)
graph.add_edge('Manouba','Monastir', weight = 179)
graph.add_edge('Manouba','Nabeul', weight = 78)
graph.add_edge('Manouba','Sfax', weight = 280)
graph.add_edge('Manouba','Sidi Bouzid', weight = 279)
graph.add_edge('Manouba','Siliana', weight = 126)
graph.add_edge('Manouba','Sousse', weight = 157)
graph.add_edge('Manouba','Tataouine', weight = 585)
graph.add_edge('Manouba','Tozeur', weight = 435)
graph.add_edge('Manouba','Tunis', weight = 10)
graph.add_edge('Manouba','Zaghouan', weight = 63)

#Distance from Medenine to other cities

graph.add_edge('Medenine','Monastir', weight = 352)
graph.add_edge('Medenine','Nabeul', weight = 447)
graph.add_edge('Medenine','Sfax', weight = 231)
graph.add_edge('Medenine','Sidi Bouzid', weight = 247)
graph.add_edge('Medenine','Siliana', weight = 369)
graph.add_edge('Medenine','Sousse', weight = 350)
graph.add_edge('Medenine','Tataouine', weight = 52)
graph.add_edge('Medenine','Tozeur', weight = 282)
graph.add_edge('Medenine','Tunis', weight = 485)
graph.add_edge('Medenine','Zaghouan', weight = 440)

#Distance from Monastir to other cities

graph.add_edge('Monastir','Nabeul', weight = 131)
graph.add_edge('Monastir','Sfax', weight = 138)
graph.add_edge('Monastir','Sidi Bouzid', weight = 176)
graph.add_edge('Monastir','Siliana', weight = 172)
graph.add_edge('Monastir','Sousse', weight = 21)
graph.add_edge('Monastir','Tataouine', weight = 443)
graph.add_edge('Monastir','Tozeur', weight = 366)
graph.add_edge('Monastir','Tunis', weight = 169)
graph.add_edge('Monastir','Zaghouan', weight = 124)

#Distance from Nabeul to other cities

graph.add_edge('Nabeul','Sfax', weight = 232)
graph.add_edge('Nabeul','Sidi Bouzid', weight = 232)
graph.add_edge('Nabeul','Siliana', weight = 158)
graph.add_edge('Nabeul','Sousse', weight = 110)
graph.add_edge('Nabeul','Tataouine', weight = 538)
graph.add_edge('Nabeul','Tozeur', weight = 417)
graph.add_edge('Nabeul','Tunis', weight = 68)
graph.add_edge('Nabeul','Zaghouan', weight = 66)

#Distance from Sfax to other cities

graph.add_edge('Sfax','Sidi Bouzid', weight = 132)
graph.add_edge('Sfax','Siliana', weight = 239)
graph.add_edge('Sfax','Sousse', weight = 133)
graph.add_edge('Sfax','Tataouine', weight = 321)
graph.add_edge('Sfax','Tozeur', weight = 346)
graph.add_edge('Sfax','Tunis', weight = 268)
graph.add_edge('Sfax','Zaghouan', weight = 223)

#Distance from Sidi Bouzid to other cities

graph.add_edge('Sidi Bouzid','Siliana', weight = 165)
graph.add_edge('Sidi Bouzid','Sousse', weight = 162)
graph.add_edge('Sidi Bouzid','Tataouine', weight = 337)
graph.add_edge('Sidi Bouzid','Tozeur', weight = 194)
graph.add_edge('Sidi Bouzid','Tunis', weight = 269)
graph.add_edge('Sidi Bouzid','Zaghouan', weight = 215)

#Distance from Siliana to other cities

graph.add_edge('Siliana','Sousse', weight = 158)
graph.add_edge('Siliana','Tataouine', weight = 461)
graph.add_edge('Siliana','Tozeur', weight = 342)
graph.add_edge('Siliana','Tunis', weight = 133)
graph.add_edge('Siliana','Zaghouan', weight = 92)

#Distance from Sousse to other cities

graph.add_edge('Sousse','Tataouine', weight = 441)
graph.add_edge('Sousse','Tozeur', weight = 353)
graph.add_edge('Sousse','Tunis', weight = 147)
graph.add_edge('Sousse','Zaghouan', weight = 103)

#Distance from Tataouine to other cities

graph.add_edge('Tataouine','Tozeur', weight = 334)
graph.add_edge('Tataouine','Tunis', weight = 572)
graph.add_edge('Tataouine','Zaghouan', weight = 492)

#Distance from Tozeur to other cities

graph.add_edge('Tozeur','Tunis', weight = 455)
graph.add_edge('Tozeur','Zaghouan', weight = 391)

#Distance from Tunis to Zaghouan

graph.add_edge('Tunis','Zaghouan', weight = 57)


#Network graph

node_sizes = 3000
node_colors = 'lightgreen'
nx.draw(graph, with_labels=True, node_size=node_sizes, node_color=node_colors)


starting_city = 'Bizerte'
tsp_path = nx.approximation.traveling_salesman_problem(graph, cycle= False)

start_idx = tsp_path.index(starting_city)

#TSP solution

tsp_path = tsp_path[start_idx:] + tsp_path[:start_idx]
print("The shortest possible route that visits each city and returns to Bizerte", tsp_path)

#Total cost

total_cost = sum(graph[u][v]['weight'] for u, v in zip(tsp_path, tsp_path[1:]))
total_cost += graph[tsp_path[-1]][tsp_path[0]]['weight']

print("Total cost of the trip", total_cost)

#Highest distance between two cities in TSP path

max_distance = 0
for i in range(len(tsp_path) - 1):
    city1 = tsp_path[i]
    city2 = tsp_path[i + 1]

    edge_weight = graph[city1][city2]['weight']

    if edge_weight > max_distance:
        max_distance = edge_weight

print("The highest distance between two consecutive cities in the TSP path:", max_distance)
