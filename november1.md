- [ ] choosing capital for treeland
- [x] tandem repeats
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
- [x] 1
- [x] 2
- [x] 3
- [x] 4
- [ ] 5
2017 amc 12b
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5
2018 amc12a
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5
2018 amc12b
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5



Use git over SSH with the hotspot laptop as the remote. It's always at 10.42.0.1 on the hotspot network.
sudo systemctl enable --now sshd
git -C ~/path/to/repo config receive.denyCurrentBranch updateInstead
```

The second line allows pushes into this repo even though it has a branch checked out. Its working files update automatically, as long as it has no uncommitted changes at the time. If this laptop runs Debian or Ubuntu, the service is called `ssh` instead of `sshd`.

**On the other laptop (once):**

```
cd ~/path/to/repo
git remote add laptop yourusername@10.42.0.1:path/to/repo
```

The path is relative to that user's home folder on the hotspot laptop.

**Then use normal git, run from the joining laptop for both directions:**

```
git pull laptop main
git push laptop main
```

Running everything from the joining side means only the hotspot laptop needs SSH turned on.
