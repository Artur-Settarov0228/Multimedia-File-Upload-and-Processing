import uuid
import hashlib
from django.utils import timezone

def generate_unique_filename(original_filename: str) -> str:
    """
    Unikal fayl nomi yaratish
    """
    timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
    unique_id = str(uuid.uuid4())[:8]
    
    # Fayl nomini hash qilish
    name_hash = hashlib.md5(original_filename.encode()).hexdigest()[:8]
    
    return f"{timestamp}_{unique_id}_{name_hash}"

def format_file_size(size_bytes: int) -> str:
    """
    Fayl hajmini formatlash
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"