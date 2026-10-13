def map_cat_string(cat_string):
    cats = cat_string.replace('CAT__', '').split('--')
    if len(cats) == 1:
        cats = cats + [None]
    return cats


cat_tuples = [
    ('Content', 'Narrative'),
    ('Content', 'Other'),
    ('Content', 'Quote'),
    ('Content', 'Theme'),
    ('Reader_response', 'Evaluation_of_quality'),
    ('Reader_response', 'Feelings'),
    ('Reader_response', 'Identification_and_immersion'),
    ('Reader_response', 'Reading_Context'),
    ('Reader_response', 'Reception'),
    ('Reader_response', 'Reflection'),
    ('Style', 'Context'),
    ('Style', 'Structure'),
    ('Style', 'Stylistic_features'),
    ('Author', None),
    ('Classification', None),
    ('Content', None),
    ('Other_works', None),
    ('Reader_response', None),
    ('Recommendations', None),
    ('Style', None)
]