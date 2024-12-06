"""
Configuration settings for the face recognition system
"""
import yaml
import os

def load_config():
    """Load configuration from YAML file"""
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

# Load configuration
config = load_config()

# Export configuration sections
CAMERA = config['camera']
FACE_DETECTION = config['face_detection']
TRAINING = config['training']
PATHS = config['paths']

# Confidence threshold
CONFIDENCE_THRESHOLD = config['confidence_threshold']