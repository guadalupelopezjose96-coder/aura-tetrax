#!/bin/bash
LOG_FILE="/data/data/com.termux/files/home/watchdog.log"
ARCHIVE_DIR="/data/data/com.termux/files/home/logs_archive"
mkdir -p "$ARCHIVE_DIR"
if [ -f "$LOG_FILE" ] && [ $(stat -c%s "$LOG_FILE") -gt 1048576 ]; then
    mv "$LOG_FILE" "$ARCHIVE_DIR/watchdog_$(date +%Y%m%d_%H%M%S).log"
    touch "$LOG_FILE"
fi
