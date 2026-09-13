#!/usr/bin/env bash
set -u
echo '=== LinuxPulse Health Check ==='
echo "Timestamp: $(date)"
echo
echo '[CPU]'; uptime || true
echo; echo '[Memory]'; free -h || true
echo; echo '[Disk]'; df -h || true
echo; echo '[Top processes]'; ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 10 || true
echo; echo '[Listening ports]'; ss -lnt 2>/dev/null | head -n 20 || true
echo; echo '[Failed systemd units]'; systemctl --failed --no-legend 2>/dev/null || true
echo; echo '=== End Health Check ==='
