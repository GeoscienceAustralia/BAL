"""
:mod:`bal_database` - relevant dictionaries for calculating the
bushfire attack level (BAL)

===============================================================

These dictionaries are translated from tables from 2.4.2 to 2.4.5 in 
AS 3959 (2009) to determine the BAL for an area of interest within Australia.

:moduleauthor: Tina Yang <tina.yang@ga.gov.au>

"""

FDI = [100, 80, 50, 40]

# 1: Forest, 2: Woodland, 3: Shrubland, 4: Scrub, 5: Mallee/Mulga
# 6: Rainforest, 7: Grassland/Tussock moorland
VEG_CLASS =  [1, 2, 3, 4, 5, 6, 7]

# 1: 0, 2: 0 ~ 5, 3: 5 ~ 10, 4: 10 ~ 15, 5: 15 ~ 20, 6: > 20
SLOPE = [1, 2, 3, 4, 5, 6]

# distance uplimits for each vegetation class at upslope/flat areas
DIST_LIMIT_UPSLOPE = dict([(FDI[0], dict([(VEG_CLASS[0], [19, 25, 35, 48]),
                                          (VEG_CLASS[1], [12, 16, 24, 33]),
                                          (VEG_CLASS[2], [7, 9, 13, 19]),
                                          (VEG_CLASS[3], [10, 13, 19, 27]),
                                          (VEG_CLASS[4], [6, 8, 12, 17]),
                                          (VEG_CLASS[5], [8, 11, 16, 23]),
                                          (VEG_CLASS[6], [6, 9, 13, 19])])),
                            (FDI[1], dict([(VEG_CLASS[0], [16, 21, 31, 42]),
                                          (VEG_CLASS[1], [10, 14, 20, 29]),
                                          (VEG_CLASS[2], [7, 9, 13, 19]),
                                          (VEG_CLASS[3], [10, 13, 19, 27]),
                                          (VEG_CLASS[4], [6, 8, 12, 17]),
                                          (VEG_CLASS[5], [6, 9, 13, 19]),
                                          (VEG_CLASS[6], [6, 8, 12, 17])])),
                            (FDI[2], dict([(VEG_CLASS[0], [12, 16, 23, 32]),
                                          (VEG_CLASS[1], [7, 10, 15, 22]),
                                          (VEG_CLASS[2], [7, 9, 13, 19]),
                                          (VEG_CLASS[3], [10, 13, 19, 27]),
                                          (VEG_CLASS[4], [6, 8, 12, 17]),
                                          (VEG_CLASS[5], [5, 6, 9, 14]),
                                          (VEG_CLASS[6], [7, 9, 14, 20])])),
                            (FDI[3], dict([(VEG_CLASS[0], [10, 13, 20, 28]),
                                          (VEG_CLASS[1], [6, 9, 13, 19]),
                                          (VEG_CLASS[2], [7, 9, 13, 19]),
                                          (VEG_CLASS[3], [10, 13, 19, 27]),
                                          (VEG_CLASS[4], [6, 8, 12, 17]),
                                          (VEG_CLASS[5], [4, 5, 8, 12]),
                                          (VEG_CLASS[6], [4, 5, 8, 12])]))])

# distance uplimits for each slope and vegetation class at downslope areas
DIST_LIMIT_DOWNSLOPE = dict([(FDI[0],
                            dict([((SLOPE[1], VEG_CLASS[0]), [24, 32, 43, 57]),
                                  ((SLOPE[1], VEG_CLASS[1]), [15, 21, 29, 41]),
                                  ((SLOPE[1], VEG_CLASS[2]), [7, 10, 15, 22]),
                                  ((SLOPE[1], VEG_CLASS[3]), [11, 15, 22, 31]),
                                  ((SLOPE[1], VEG_CLASS[4]), [7, 9, 13, 20]),
                                  ((SLOPE[1], VEG_CLASS[5]), [10, 14, 20, 29]),
                                  ((SLOPE[1], VEG_CLASS[6]), [7, 10, 15, 22]),
                                  ((SLOPE[2], VEG_CLASS[0]), [31, 39, 53, 69]),
                                  ((SLOPE[2], VEG_CLASS[1]), [20, 26, 37, 50]),
                                  ((SLOPE[2], VEG_CLASS[2]), [8, 11, 17, 25]),
                                  ((SLOPE[2], VEG_CLASS[3]), [12, 17, 24, 35]),
                                  ((SLOPE[2], VEG_CLASS[4]), [7, 10, 15, 23]),
                                  ((SLOPE[2], VEG_CLASS[5]), [13, 18, 26, 36]),
                                  ((SLOPE[2], VEG_CLASS[6]), [8, 11, 17, 25]),
                                  ((SLOPE[3], VEG_CLASS[0]), [39, 49, 64, 82]),
                                  ((SLOPE[3], VEG_CLASS[1]), [25, 33, 45, 60]),
                                  ((SLOPE[3], VEG_CLASS[2]), [9, 13, 19, 28]),
                                  ((SLOPE[3], VEG_CLASS[3]), [14, 19, 28, 39]),
                                  ((SLOPE[3], VEG_CLASS[4]), [8, 11, 18, 26]),
                                  ((SLOPE[3], VEG_CLASS[5]), [17, 23, 33, 45]),
                                  ((SLOPE[3], VEG_CLASS[6]), [9, 13, 20, 28]),
                                  ((SLOPE[4], VEG_CLASS[0]), [50, 61, 78, 98]),
                                  ((SLOPE[4], VEG_CLASS[1]), [32, 41, 56, 73]),
                                  ((SLOPE[4], VEG_CLASS[2]), [10, 15, 22, 31]),
                                  ((SLOPE[4], VEG_CLASS[3]), [15, 21, 31, 43]),
                                  ((SLOPE[4], VEG_CLASS[4]), [9, 13, 20, 29]),
                                  ((SLOPE[4], VEG_CLASS[5]), [22, 29, 42, 56]),
                                  ((SLOPE[4], VEG_CLASS[6]), [11, 15, 23, 32])
                                  ])),
                             (FDI[1],
                            dict([((SLOPE[1], VEG_CLASS[0]), [20, 27, 37, 50]),
                                  ((SLOPE[1], VEG_CLASS[1]), [13, 17, 25, 35]),
                                  ((SLOPE[1], VEG_CLASS[2]), [7, 10, 15, 22]),
                                  ((SLOPE[1], VEG_CLASS[3]), [11, 15, 22, 31]),
                                  ((SLOPE[1], VEG_CLASS[4]), [7, 9, 13, 20]),
                                  ((SLOPE[1], VEG_CLASS[5]), [8, 11, 17, 24]),
                                  ((SLOPE[1], VEG_CLASS[6]), [7, 9, 14, 20]),
                                  ((SLOPE[2], VEG_CLASS[0]), [26, 33, 46, 61]),
                                  ((SLOPE[2], VEG_CLASS[1]), [16, 22, 31, 43]),
                                  ((SLOPE[2], VEG_CLASS[2]), [8, 11, 17, 25]),
                                  ((SLOPE[2], VEG_CLASS[3]), [12, 17, 24, 35]),
                                  ((SLOPE[2], VEG_CLASS[4]), [7, 10, 15, 23]),
                                  ((SLOPE[2], VEG_CLASS[5]), [11, 15, 22, 31]),
                                  ((SLOPE[2], VEG_CLASS[6]), [8, 10, 16, 23]),
                                  ((SLOPE[3], VEG_CLASS[0]), [33, 42, 56, 73]),
                                  ((SLOPE[3], VEG_CLASS[1]), [21, 28, 39, 53]),
                                  ((SLOPE[3], VEG_CLASS[2]), [9, 13, 19, 28]),
                                  ((SLOPE[3], VEG_CLASS[3]), [14, 19, 28, 39]),
                                  ((SLOPE[3], VEG_CLASS[4]), [8, 11, 18, 26]),
                                  ((SLOPE[3], VEG_CLASS[5]), [14, 19, 28, 39]),
                                  ((SLOPE[3], VEG_CLASS[6]), [9, 12, 18, 26]),
                                  ((SLOPE[4], VEG_CLASS[0]), [42, 52, 68, 87]),
                                  ((SLOPE[4], VEG_CLASS[1]), [27, 35, 48, 64]),
                                  ((SLOPE[4], VEG_CLASS[2]), [10, 15, 22, 31]),
                                  ((SLOPE[4], VEG_CLASS[3]), [15, 21, 31, 43]),
                                  ((SLOPE[4], VEG_CLASS[4]), [9, 13, 20, 29]),
                                  ((SLOPE[4], VEG_CLASS[5]), [18, 25, 36, 48]),
                                  ((SLOPE[4], VEG_CLASS[6]), [10, 14, 21, 30])
                                  ])),
                             (FDI[2],
                            dict([((SLOPE[1], VEG_CLASS[0]), [14, 19, 27, 38]),
                                  ((SLOPE[1], VEG_CLASS[1]), [9, 12, 18, 26]),
                                  ((SLOPE[1], VEG_CLASS[2]), [7, 10, 15, 22]),
                                  ((SLOPE[1], VEG_CLASS[3]), [11, 15, 22, 31]),
                                  ((SLOPE[1], VEG_CLASS[4]), [7, 9, 13, 20]),
                                  ((SLOPE[1], VEG_CLASS[5]), [6, 8, 12, 17]),
                                  ((SLOPE[1], VEG_CLASS[6]), [8, 10, 16, 23]),
                                  ((SLOPE[2], VEG_CLASS[0]), [18, 24, 34, 46]),
                                  ((SLOPE[2], VEG_CLASS[1]), [11, 15, 23, 32]),
                                  ((SLOPE[2], VEG_CLASS[2]), [8, 11, 17, 25]),
                                  ((SLOPE[2], VEG_CLASS[3]), [12, 17, 24, 35]),
                                  ((SLOPE[2], VEG_CLASS[4]), [7, 10, 15, 23]),
                                  ((SLOPE[2], VEG_CLASS[5]), [7, 10, 15, 22]),
                                  ((SLOPE[2], VEG_CLASS[6]), [9, 12, 18, 26]),
                                  ((SLOPE[3], VEG_CLASS[0]), [22, 30, 41, 56]),
                                  ((SLOPE[3], VEG_CLASS[1]), [14, 19, 28, 40]),
                                  ((SLOPE[3], VEG_CLASS[2]), [9, 13, 19, 28]),
                                  ((SLOPE[3], VEG_CLASS[3]), [14, 19, 28, 39]),
                                  ((SLOPE[3], VEG_CLASS[4]), [8, 11, 18, 26]),
                                  ((SLOPE[3], VEG_CLASS[5]), [9, 13, 19, 28]),
                                  ((SLOPE[3], VEG_CLASS[6]), [10, 13, 20, 29]),
                                  ((SLOPE[4], VEG_CLASS[0]), [28, 37, 51, 67]),
                                  ((SLOPE[4], VEG_CLASS[1]), [18, 25, 36, 48]),
                                  ((SLOPE[4], VEG_CLASS[2]), [10, 15, 22, 31]),
                                  ((SLOPE[4], VEG_CLASS[3]), [15, 21, 31, 43]),
                                  ((SLOPE[4], VEG_CLASS[4]), [9, 13, 20, 29]),
                                  ((SLOPE[4], VEG_CLASS[5]), [12, 17, 25, 35]),
                                  ((SLOPE[4], VEG_CLASS[6]), [11, 15, 23, 33])
                                  ])),
                             (FDI[3],
                            dict([((SLOPE[1], VEG_CLASS[0]), [12, 16, 24, 34]),
                                  ((SLOPE[1], VEG_CLASS[1]), [8, 11, 16, 23]),
                                  ((SLOPE[1], VEG_CLASS[2]), [7, 10, 15, 22]),
                                  ((SLOPE[1], VEG_CLASS[3]), [11, 15, 22, 31]),
                                  ((SLOPE[1], VEG_CLASS[4]), [7, 9, 13, 20]),
                                  ((SLOPE[1], VEG_CLASS[5]), [5, 7, 10, 15]),
                                  ((SLOPE[1], VEG_CLASS[6]), [4, 6, 9, 14]),
                                  ((SLOPE[2], VEG_CLASS[0]), [15, 20, 29, 41]),
                                  ((SLOPE[2], VEG_CLASS[1]), [9, 13, 19, 28]),
                                  ((SLOPE[2], VEG_CLASS[2]), [8, 11, 17, 25]),
                                  ((SLOPE[2], VEG_CLASS[3]), [12, 17, 24, 35]),
                                  ((SLOPE[2], VEG_CLASS[4]), [7, 10, 15, 23]),
                                  ((SLOPE[2], VEG_CLASS[5]), [6, 8, 13, 19]),
                                  ((SLOPE[2], VEG_CLASS[6]), [5, 7, 11, 16]),
                                  ((SLOPE[3], VEG_CLASS[0]), [19, 25, 36, 49]),
                                  ((SLOPE[3], VEG_CLASS[1]), [12, 16, 24, 35]),
                                  ((SLOPE[3], VEG_CLASS[2]), [9, 13, 19, 28]),
                                  ((SLOPE[3], VEG_CLASS[3]), [14, 19, 28, 39]),
                                  ((SLOPE[3], VEG_CLASS[4]), [8, 11, 18, 26]),
                                  ((SLOPE[3], VEG_CLASS[5]), [8, 11, 16, 24]),
                                  ((SLOPE[3], VEG_CLASS[6]), [6, 8, 13, 19]),
                                  ((SLOPE[4], VEG_CLASS[0]), [24, 31, 44, 59]),
                                  ((SLOPE[4], VEG_CLASS[1]), [15, 21, 31, 42]),
                                  ((SLOPE[4], VEG_CLASS[2]), [10, 15, 22, 31]),
                                  ((SLOPE[4], VEG_CLASS[3]), [15, 21, 31, 43]),
                                  ((SLOPE[4], VEG_CLASS[4]), [9, 13, 20, 29]),
                                  ((SLOPE[4], VEG_CLASS[5]), [10, 14, 21, 30]),
                                  ((SLOPE[4], VEG_CLASS[6]), [7, 9, 15, 22])
                                  ]))])

# distance classes
DIST_CLASS = [1, 2, 3, 4, 5]

# BAL
BAL_CLASS = dict([(DIST_CLASS[0], 100),
                  (DIST_CLASS[1], 40),
                  (DIST_CLASS[2], 29),
                  (DIST_CLASS[3], 19),
                  (DIST_CLASS[4], 12.5)
                  ])
