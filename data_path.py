"""
This file records the directory paths to the different datasets.
You will need to configure it for training the model.

All datasets follows the following format, where fgr and pha points to directory that contains jpg or png.
Inside the directory could be any nested formats, but fgr and pha structure must match. You can add your own
dataset to the list as long as it follows the format. 'fgr' should point to foreground images with RGB channels,
'pha' should point to alpha images with only 1 grey channel.
{
    'YOUR_DATASET': {
        'train': {
            'fgr': 'PATH_TO_IMAGES_DIR',
            'pha': 'PATH_TO_IMAGES_DIR',
        },
        'valid': {
            'fgr': 'PATH_TO_IMAGES_DIR',
            'pha': 'PATH_TO_IMAGES_DIR',
        }
    }
}
"""

DATA_PATH = {
    'sketches': {
        'train': {
            'fgr': 'sketches/train/fgr',
            'pha': 'sketches/train/pha'
        },
        'valid': {
            'fgr': 'sketches/test/fgr',
            'pha': 'sketches/test/pha'
        }
    },
 
    'backgrounds': {
        'train': 'backgrounds/train',
        'valid': 'backgrounds/valid'
    },
}
 