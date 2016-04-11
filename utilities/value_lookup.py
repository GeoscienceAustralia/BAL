"""
:mod:`value_lookup` - helpful dictionaries for calculating the
bushfire attack level (BAL)

===============================================================

These dictionaries are helpful to adapt the algorithm spatially to Method 1 
in AS 3959 (2009).

:moduleauthor: Tina Yang <tina.yang@ga.gov.au>

"""

# give each aspect a value
DIRE_ASPECT = dict([('none', 9),
                    ('n', 1),
                    ('ne', 2),
                    ('e', 3),
                    ('se', 4),
                    ('s', 5),
                    ('sw', 6),
                    ('w', 7),
                    ('nw', 8)])

# find the number of all neighbours in a direction
ALL_NEIGHB = dict([('w', lambda i, jj, rows, cols: jj),
                   ('e', lambda i, jj, rows, cols: cols-jj-1),
                   ('n', lambda i, jj, rows, cols: i),
                   ('s', lambda i, jj, rows, cols: rows-i-1),
                   ('nw', lambda i,jj, rows, cols: min(i, jj)),
                   ('ne', lambda i,jj, rows, cols: min(i, cols-jj-1)),
                   ('sw', lambda i,jj, rows, cols: min(rows-i-1, jj)),
                   ('se', lambda i,jj, rows, cols: min(rows-i-1, cols-jj-1))])

# find the row index of the neighbour
POINT_R = dict([('w', lambda i, m: i),
                ('e', lambda i, m: i),
                ('n', lambda i, m: i-m),
                ('s', lambda i, m: i+m),
                ('nw', lambda i, m: i-m),
                ('ne', lambda i, m: i-m),
                ('sw', lambda i, m: i+m),
                ('se', lambda i, m: i+m)])

# find the column index of the neighbour
POINT_C = dict([('w', lambda jj, m: jj-m),
                ('e', lambda jj, m: jj+m),
                ('n', lambda jj, m: jj),
                ('s', lambda jj, m: jj),
                ('nw', lambda jj, m: jj-m),
                ('ne', lambda jj, m: jj+m),
                ('sw', lambda jj, m: jj-m),
                ('se', lambda jj, m: jj+m)])