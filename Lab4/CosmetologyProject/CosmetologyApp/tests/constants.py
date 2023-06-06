NONUSER_VIEWS = [
    'home',
    'registration',
    'service',
    ('detail_service', 1),
    'static_info',
]

USER_VIEWS = [
    'shedule',
    'client',
    ('detail_shedule', 3),
    ('detail_client', 2),
]

ADMIN_VIEWS = [
    'add_service',
    ('delete_service', 1),
    'add_shedule',
    ('delete_shedule', 3),
    ('delete_client', 2),
    ('edit_client', 2),
    ('edit_shedule', 3),
    'diagram',
]