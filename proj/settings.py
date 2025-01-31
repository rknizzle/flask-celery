"""
Application config / settings

"""
import os

# ============================================================================
# Celery config
# ============================================================================

CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']

# ============================================================================
# EOF
# ============================================================================
