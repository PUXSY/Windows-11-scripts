@echo off
echo Start
winget upgrade
echo  winget upgrade: Finished
winget upgrade --all
echo  winget upgrade --all: Finished
echo  Finished upgrade

chkdsk
DISM /Online /Commit-Image /Remount-Wim /RestoreHealth

cls
echo [32mAll Finished[0m
pause
exit

