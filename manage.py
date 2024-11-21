#!/usr/bin/env python3
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ArtesanosMarket.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado correctamente?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()