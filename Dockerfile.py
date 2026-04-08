FROM archlinux:latest
RUN pacman -Sy --noconfirm python
COPY main.py main.py
COPY books/ books/
CMD ["python", "main.py"]
