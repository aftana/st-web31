import os

dirct = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG = {
    'mode': 'wsgi',
    'working_dir': dirct,
    'args': (
        '--bind=0.0.0.0:8080',
 #       '--daemon',
        '--workers=16',
        '--timeout=60',
        'hello:app',
    ),
}
