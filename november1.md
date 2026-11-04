- [ ] choosing capital for treeland
- [ ] tandem repeats
- [ ] chat screenshots
- [ ] peculiar movie preferences
- [ ] mysterious present
- [ ] 4 from 1800
25b
- [ ] 4
- [ ] 5
- [ ] passport application
- [ ] journalling

# 300 creative
- [ ] 51
- [ ] 52
- [ ] 53
- [ ] 54
- [ ] 55
- [ ] 56
- [ ] 57
- [ ] 58
- [ ] 59
- [ ] 60
- [ ] 61
- [ ] 62
- [ ] 63
- [ ] 64
- [ ] 65
- [ ] 66
- [ ] 67
- [ ] 68
- [ ] 69
- [ ] 70
# amc
2017 amc 12a
- [ ] 1
- [ ] 2
- [ ] 3
2017 amc 12b
- [ ] 1
- [ ] 2
- [ ] 3
2018 amc12a
- [ ] 1
- [ ] 2
- [ ] 3
2018 amc12b
- [ ] 1
- [ ] 2
- [ ] 3

sudo dnf install --skip-unavailable --skip-broken --exclude='kernel*,grub2*,shim*,*firmware*,*microcode*,intel-*,amd-*,nvidia-*,gdm,gnome-shell*,gnome-session*,gnome-classic-session,chatgpt,*proton*' $(cat ~/asahi-migration/packages.txt)

sudo dnf install flatpak

flatpak remote-add --user --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

xargs -r -n1 flatpak install --user -y flathub < ~/asahi-migration/flatpaks.txt
