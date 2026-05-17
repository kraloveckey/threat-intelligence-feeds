# 🛡️ Threat Intelligence Feeds

![Weekly Update](https://github.com/kraloveckey/threat-intelligence-feeds/actions/workflows/weekly-update.yml/badge.svg)

A curated, open-source collection of Threat Intelligence / IOC feeds.  
Most feeds are **free and publicly accessible** — no account or API key required.  
Feeds that require registration are clearly marked as [`RESTRICTED`](#restricted).

Sources aggregated from:
- [FireWALL-E: ipsets-blocklists](https://github.com/kraloveckey/ipsets-blocklist);
- [MISP default feeds](https://www.misp-project.org/feeds/);
- [Bert-JanP/Open-Source-Threat-Intel-Feeds](https://github.com/Bert-JanP/Open-Source-Threat-Intel-Feeds);
- [awesome-threat-intelligence](https://github.com/hslatman/awesome-threat-intelligence/);
- [mthcht/awesome-lists](https://github.com/mthcht/awesome-lists);
- Additional community projects.

> [!IMPORTANT]
> Content is served as-is. Verify licensing terms before using in a business environment.

---

## 📊 Feed Statistics

> [!NOTE]
> Auto-updated weekly by GitHub Actions: 🟢 Active – 🔴 Offline – 🔒 Restricted – ⚪ Not checked.

<!-- STATS_TABLE_START -->
| Category | Description | Count |
| --- | --- | --- |
| `IP` | Malicious / suspicious IPv4 addresses and CIDR ranges | 162 |
| `DNS` | Malicious or suspicious domain names | 28 |
| `URL` | Malicious / phishing / C2 URLs | 29 |
| `MD5` | MD5 hashes of malicious files | 6 |
| `SHA1` | SHA1 hashes of malicious files | 3 |
| `SHA256` | SHA256 hashes of malicious files | 4 |
| `SSL` | Malicious SSL certificate fingerprints | 1 |
| `JA3` | JA3 TLS client fingerprints | 1 |
| `CVEID` | Known exploited CVE identifiers | 4 |
| `RANSOMWARELEAK` | Ransomware leak site victim data aggregated from multiple gang leak sites | 1 |
| `MISP` | Structured MISP-format feeds (importable directly into MISP platform) | 5 |
| `IOC` | Mixed-type IOC feeds containing multiple indicator types (IP, domain, URL, hash, etc.) | 9 |
| `BLOCKLIST` | General-purpose IP blocklists — ISPs, ASNs, gaming, ad-trackers (not strictly threat intel) | 43 |
| `REPO` | GitHub repositories with IOC collections — no direct machine-readable feed URL | 23 |
| `RESTRICTED` | Feeds requiring registration or an API key (free or commercial) to access | 5 |
| `GEOIP` | IP geolocation databases — country/ASN/region mapping (not threat intel) | 3 |
| **Total** | | **327** |
<!-- STATS_TABLE_END -->

---

## 📁 Repository Structure

```
threat-intelligence-feeds/
├── threat-intelligence-feeds.csv           ← master feed database (source of truth)
├── README-STATISTICS.md                    ← auto-generated, do not edit manually
├── README.md                               ← auto-updated stats + feeds table
├── requirements.txt
├── scripts/
│   ├── tif-validator.py                    ← validates CSV format & categories
│   ├── tif-status-checker.py               ← checks live HTTP status of all URLs
│   ├── tif-generate-table-statistics.py    ← generates README-STATISTICS.md (standalone)
│   └── tif-update-readme.py                ← regenerates stats + feeds table in README
└── .github/workflows/
    └── weekly-update.yml                   ← runs every Monday at 06:00 UTC
```

### About threat-intelligence-feeds.csv

`threat-intelligence-feeds.csv` is the **single source of truth** for this project.  
It is maintained manually (you add/remove feeds here) but the `FeedStatus` column is **auto-filled** weekly by `tif-status-checker.py` via GitHub Actions. The README tables are then auto-regenerated from this CSV by `tif-update-readme.py`.

**Format:**

```csv
Vendor;Description;Category;Url;FeedStatus
Abuse.ch;Botnet C2 IP Blacklist;IP;https://sslbl.abuse.ch/blacklist/sslipblacklist.csv;Active
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- `git`

### Local setup

```bash
# 1. Clone the repository
git clone https://github.com/kraloveckey/threat-intelligence-feeds.git
cd threat-intelligence-feeds

# 2. (Optional but recommended) create a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Validate the CSV (always a good first step)
cd scripts
python3 tif-validator.py

# 5. Check live HTTP status of all feed URLs
#    Writes/updates the FeedStatus column in threat-intelligence-feeds.csv
#    Takes ~3–5 minutes (runs 25 workers in parallel)
python3 tif-status-checker.py

# 6. Regenerate README-STATISTICS.md and inject tables into README.md
python3 tif-update-readme.py
```

> [!TIP]
> You can run steps 4–6 independently. For example, run only `tif-validator.py` after adding new feeds to the CSV before opening a `Pull Request`.

### GitHub Actions (automatic)

After the first push, the workflow runs **every Monday at 06:00 UTC** and:
1. Validates the CSV format and categories.
2. Checks HTTP status of all feed URLs → updates `FeedStatus` column in CSV.
3. Regenerates stats and both tables in README.
4. Commits and pushes if anything changed.

You can also trigger it manually: **Actions → Weekly Threat Intelligence Feeds Update → Run workflow**

---

## 📋 All Feeds

Status legend: 🟢 Active – 🔴 Offline – 🔒 Restricted (requires API key) – ⚪ Not yet checked.

> [!NOTE]
> **`BLOCKLIST`** entries (ISPs, ASNs, gaming companies, IANA ranges) are general-purpose blocklists, not threat intelligence in the strict sense — use them for network filtering, not for SIEM correlation.  
> **`REPO`** entries point to GitHub repositories without a direct machine-readable URL — you need to browse or clone them manually.  
> **`RESTRICTED`** entries require free or commercial registration to download.

<!-- FEEDS_TABLE_START -->

### IP (162)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| Abuse.ch | Botnet C2 IP Blacklist (CSV) | <abbr title="Active">🟢</abbr> | [↗](https://sslbl.abuse.ch/blacklist/sslipblacklist.csv) |
| Abuse.ch | Botnet C2 IP Blacklist (TXT) | <abbr title="Active">🟢</abbr> | [↗](https://sslbl.abuse.ch/blacklist/sslipblacklist.txt) |
| Abuse.ch | Botnet C2 IP Blacklist Aggressive (CSV) | <abbr title="Active">🟢</abbr> | [↗](https://sslbl.abuse.ch/blacklist/sslipblacklist_aggressive.csv) |
| Abuse.ch | Botnet C2 IP Blacklist Aggressive (TXT) | <abbr title="Active">🟢</abbr> | [↗](https://sslbl.abuse.ch/blacklist/sslipblacklist_aggressive.txt) |
| Abuse.ch | Botnet C2 Indicators of Compromise – Recommended Blocklist | <abbr title="Active">🟢</abbr> | [↗](https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt) |
| Abuse.ch | Botnet C2 Indicators of Compromise | <abbr title="Active">🟢</abbr> | [↗](https://feodotracker.abuse.ch/downloads/ipblocklist.txt) |
| Abuse.ch | All botnet C2s Feodo Tracker has ever seen | <abbr title="Active">🟢</abbr> | [↗](https://feodotracker.abuse.ch/blocklist/) |
| Abuse.ch | Feodo IP Blocklist Aggressive | <abbr title="Active">🟢</abbr> | [↗](https://feodotracker.abuse.ch/downloads/ipblocklist_aggressive.txt) |
| AbuseIPDB | AbuseIPDB Score 100 – Last 1 day | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/borestad/blocklist-abuseipdb/main/abuseipdb-s100-1d.ipv4) |
| AbuseIPDB | AbuseIPDB Score 100 – Last 30 days | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/borestad/blocklist-abuseipdb/main/abuseipdb-s100-30d.ipv4) |
| AlienVault | Alienvault IP Reputation | <abbr title="Active">🟢</abbr> | [↗](http://reputation.alienvault.com/reputation.data) |
| AlienVault | IP Reputation Generic | <abbr title="Active">🟢</abbr> | [↗](https://reputation.alienvault.com/reputation.generic) |
| APNIC Honeynet | SSH Bruteforce IPs | <abbr title="Active">🟢</abbr> | [↗](https://feeds.honeynet.asia/bruteforce/latest-sshbruteforce-unique.csv) |
| APNIC Honeynet | Telnet Bruteforce IPs | <abbr title="Active">🟢</abbr> | [↗](https://feeds.honeynet.asia/bruteforce/latest-telnetbruteforce-unique.csv) |
| Binarydefense | Binary Defense Artillery Threat Intelligence Banlist | <abbr title="Active">🟢</abbr> | [↗](https://www.binarydefense.com/banlist.txt) |
| Blocklist.de | All IPs that attacked a customer/server in the last 48 hours | <abbr title="Active">🟢</abbr> | [↗](https://lists.blocklist.de/lists/all.txt) |
| Blocklist.de | IPs that attacked SSH in the last 48 hours | <abbr title="Active">🟢</abbr> | [↗](https://lists.blocklist.de/lists/ssh.txt) |
| Blocklist.de | IPs that attacked Mail/Postfix in the last 48 hours | <abbr title="Active">🟢</abbr> | [↗](https://lists.blocklist.de/lists/mail.txt) |
| Blocklist.de | IPs that attacked Apache in the last 48 hours | <abbr title="Active">🟢</abbr> | [↗](https://lists.blocklist.de/lists/apache.txt) |
| Blocklist.de | IPs that attacked IMAP/SASL/POP3 in the last 48 hours | <abbr title="Active">🟢</abbr> | [↗](https://lists.blocklist.de/lists/imap.txt) |
| Blocklist.de | IPs reported for IRC/BadBots/RFI-Attacks in the last 48 hours | <abbr title="Active">🟢</abbr> | [↗](https://lists.blocklist.de/lists/bots.txt) |
| Blocklist.de | IPs with Brute-Force attacks on Joomla/Wordpress/Web-Logins | <abbr title="Active">🟢</abbr> | [↗](https://lists.blocklist.de/lists/bruteforcelogin.txt) |
| Blocklist.de | IPs older than 2 months with more than 5000 attacks | <abbr title="Active">🟢</abbr> | [↗](https://lists.blocklist.de/lists/strongips.txt) |
| Blocklist.de | IPs that attacked FTP in the last 48 hours | <abbr title="Active">🟢</abbr> | [↗](https://lists.blocklist.de/lists/ftp.txt) |
| Blocklist.de | IPs that attacked SIP in the last 48 hours | <abbr title="Active">🟢</abbr> | [↗](https://lists.blocklist.de/lists/sip.txt) |
| Blocklist.net.ua | Ukrainian Blocklist (Ukraine CERT) | <abbr title="Active">🟢</abbr> | [↗](https://blocklist.net.ua/blocklist.csv) |
| BotScout.com | Most recently-caught web bots | <abbr title="Active">🟢</abbr> | [↗](http://botscout.com/last_caught_cache.htm) |
| Botvrij.eu | Botvrij IOC IP Destination (raw) | <abbr title="Active">🟢</abbr> | [↗](http://www.botvrij.eu/data/ioclist.ip-dst.raw) |
| Botvrij.eu | Botvrij IOC IP Source (raw) | <abbr title="Active">🟢</abbr> | [↗](http://www.botvrij.eu/data/ioclist.ip-src.raw) |
| BruteForceBlocker | SSH BruteForce Blocker IPs | <abbr title="Active">🟢</abbr> | [↗](http://danger.rulez.sk/projects/bruteforceblocker/blist.php) |
| C2IntelFeeds | C2 IP addresses – 30 day verified | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/IPC2s-30day.csv) |
| C2IntelFeeds | Unverified C2 IPs | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/unverified/IPC2s.csv) |
| Carbon Black | Cobalt Strike LuckyMouse / TA428 | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/carbonblack/active_c2_ioc_public/main/cobaltstrike/actor-specific/cobaltstrike_luckymouse_ta428.csv) |
| Carbon Black | Cobalt Strike Pyxie | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/carbonblack/active_c2_ioc_public/main/cobaltstrike/actor-specific/cobaltstrike_pyxie.csv) |
| CINSscore | CINS Bad IP List (ci-badguys) | <abbr title="Active">🟢</abbr> | [↗](https://cinsscore.com/list/ci-badguys.txt) |
| CleanTalk | CleanTalk Blacklist – Submitted Today | <abbr title="Offline">🔴</abbr> | [↗](https://cleantalk.org/blacklists/submited_today) |
| CleanTalk | CleanTalk Blacklist – Updated Today | <abbr title="Active">🟢</abbr> | [↗](https://cleantalk.org/blacklists/updated_today) |
| CleanTalk | CleanTalk Blacklist – Top 20 | <abbr title="Offline">🔴</abbr> | [↗](https://cleantalk.org/blacklists/top20) |
| CriticalPathSecurity | Abuse.ch IP Blocklist Feed | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/CriticalPathSecurity/Public-Intelligence-Feeds/master/abuse-ch-ipblocklist.txt) |
| CriticalPathSecurity | Log4j Scanners and Exploiters | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/CriticalPathSecurity/Public-Intelligence-Feeds/master/log4j.txt) |
| CriticalPathSecurity | CPS collected IOCs (Zeek intel format) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/CriticalPathSecurity/Zeek-Intelligence-Feeds/master/cps-collected-iocs.intel) |
| CriticalPathSecurity | CPS LockBit ransomware IPs | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/CriticalPathSecurity/Zeek-Intelligence-Feeds/master/lockbit_ip.intel) |
| CriticalPathSecurity | CPS stalkerware indicators | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/CriticalPathSecurity/Zeek-Intelligence-Feeds/master/stalkerware.intel) |
| CriticalPathSecurity | CPS Ragnar Locker ransomware IOCs | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/CriticalPathSecurity/Zeek-Intelligence-Feeds/master/ragnar.intel) |
| cybercrime-tracker.net | Command and Control tracking IP list | <abbr title="Active">🟢</abbr> | [↗](http://cybercrime-tracker.net/fuckerz.php) |
| dan.me.uk | Dynamic list of TOR nodes (full) | <abbr title="Active">🟢</abbr> | [↗](https://www.dan.me.uk/torlist/) |
| Daniel Austin MBCS | TOR Exit Nodes | <abbr title="Active">🟢</abbr> | [↗](https://www.dan.me.uk/torlist/?exit) |
| Daniel Austin MBCS | TOR All Nodes | <abbr title="Active">🟢</abbr> | [↗](https://www.dan.me.uk/torlist/?full) |
| darklist.de | Darklist.de IP Blacklist | <abbr title="Active">🟢</abbr> | [↗](http://www.darklist.de/raw.php) |
| DataPlane | SIP Query Source IPs | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/sipquery.txt) |
| DataPlane | SSH Password Auth Source IPs | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/sshpwauth.txt) |
| DataPlane | SSH Client Source IPs | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/sshclient.txt) |
| DataPlane | SIP Registration Source IPs | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/sipregistration.txt) |
| DataPlane | VNC RFB Source IPs | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/vncrfb.txt) |
| DataPlane | DNS Recursion Desired | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/dnsrd.txt) |
| DataPlane | DNS Recursion Desired IN ANY | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/dnsrdany.txt) |
| DataPlane | DNS CH TXT version.bind | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/dnsversion.txt) |
| DataPlane | SIP Invitation Source IPs | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/sipinvitation.txt) |
| DataPlane | SMTP Data Source IPs | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/smtpdata.txt) |
| DataPlane | SMTP Greet Source IPs | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/smtpgreet.txt) |
| DataPlane | IP Protocol 41 Source IPs | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/proto41.txt) |
| DataPlane | Telnet Login Source IPs | <abbr title="Active">🟢</abbr> | [↗](https://dataplane.org/telnetlogin.txt) |
| DShield | Top 20 attacking subnets | <abbr title="Active">🟢</abbr> | [↗](https://feeds.dshield.org/block.txt) |
| Ellio | Firewall Threat List (Community) | <abbr title="Active">🟢</abbr> | [↗](https://cdn.ellio.tech/community-feed) |
| Emerging Threats | Emerging Threats Tor Rules | <abbr title="Active">🟢</abbr> | [↗](http://rules.emergingthreats.net/blockrules/emerging-tor.rules) |
| Emerging Threats | Emerging Threats Block IPs | <abbr title="Active">🟢</abbr> | [↗](http://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt) |
| Emerging Threats | ET compromised hosts (includes openbl/bruteforceblocker/sidreporter) | <abbr title="Active">🟢</abbr> | [↗](http://rules.emergingthreats.net/blockrules/compromised-ips.txt) |
| Emerging Threats | ET Spamhaus DROP blocklist (PIX/ACL format) | <abbr title="Active">🟢</abbr> | [↗](http://rules.emergingthreats.net/fwrules/emerging-PIX-DROP.rules) |
| Emerging Threats | ET DShield top 20 attackers (PIX/ACL format) | <abbr title="Active">🟢</abbr> | [↗](http://rules.emergingthreats.net/fwrules/emerging-PIX-DSHIELD.rules) |
| etnetera.cz | Etnetera aggressive IP blocklist (Czech ISP security team) | <abbr title="Active">🟢</abbr> | [↗](https://security.etnetera.cz/feeds/etn_aggressive.txt) |
| Firehol | Firehol Level 1 Blocklist (netset) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/ktsaou/blocklist-ipsets/master/firehol_level1.netset) |
| Github | Fox-IT Cobalt Strike Servers | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/fox-it/cobaltstrike-extraneous-space/master/cobaltstrike-servers.csv) |
| GPF Comics | IPs that attacked GPF Comics (spam/exploits/scans) | <abbr title="Active">🟢</abbr> | [↗](https://www.gpf-comics.com/dnsbl/export.php) |
| GraphiclineWeb | Universally banned IPs (spiders/spambots/hackers/harvesters) | <abbr title="Active">🟢</abbr> | [↗](https://graphiclineweb.wordpress.com/tech-notes/ip-blacklist/) |
| GreenSnow.co | Bruteforce/scan/exploit attacking IPs | <abbr title="Active">🟢</abbr> | [↗](http://blocklist.greensnow.co/greensnow.txt) |
| GriffinGuard | GriffinGuard Abuse 7-day Top 10K | <abbr title="Active">🟢</abbr> | [↗](https://griffinguard.io/feeds/abuse7d_top10k.txt) |
| home.nuug.no | POP3 Gropers | <abbr title="Active">🟢</abbr> | [↗](https://home.nuug.no/~peter/pop3gropers.txt) |
| iBlocklist.com | Open Proxies IPs (without TOR) | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=xoebmbyexwuiogmbyprb&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Known malicious Spyware and Adware IP ranges | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=llvtlsjyoyiczbkjsxpf&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Hijacked IP-Blocks and known Spam delivery ranges | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=usrcshglbiilevmyfhse&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Web server hack and exploit attempt IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=ghlzqtqxnzctvvajwwag&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Suspicious IPs under investigation | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=plkehquoahljmyxjixpu&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Advertising trackers and bad/intrusive sites | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=dgxtneitpuvgqqcpfulq&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Hostile web spiders | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=mcvxsnihddgutbjfbghy&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Known hackers and DShield reported IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=xpbqleszmajjesnzddhv&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Forum spam IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=ficutxiwawokxlcyoeye&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | CruzIT compromised machines scanning for vulnerabilities | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=czvaehmjpsnwwttrdoyl&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Spamhaus DROP list (p2p format) | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=zbdlwrqkabxbcppvrnos&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | SpyEye tracker abuse.ch IP blocklist | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=zvjxsfuvdhoxktpeiokq&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Palevo tracker abuse.ch IP blocklist | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=erqajhwrxiuvjxqrrwfj&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | CIArmy malicious IPs (Sentinel network) | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=npkuuhuxcsllnhoamkvm&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Malc0de malware distribution IPs (last 30 days) | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=pbqcylkejciyhmwttify&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Tor / Onion Router IP addresses | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=togdoptykrlolpddwbvz&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | IP ranges sharing child pornography in p2p community | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=dufcxgnbjsdwmwctgfuj&fileformat=p2p&archiveformat=gz) |
| ipspamlist | IP Spam List | <abbr title="Active">🟢</abbr> | [↗](http://www.ipspamlist.com/public_feeds.csv) |
| IPsum | Malicious and/or suspicious IP addresses – Level 1 | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/1.txt) |
| IPsum | Malicious and/or suspicious IP addresses – Level 2 | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/2.txt) |
| IPsum | Malicious and/or suspicious IP addresses – Level 3 | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/3.txt) |
| IPsum | Malicious and/or suspicious IP addresses – Level 4 | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/4.txt) |
| IPsum | Malicious and/or suspicious IP addresses – Level 5 | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/5.txt) |
| IPsum | Malicious and/or suspicious IP addresses – Level 6 | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/6.txt) |
| IPsum | Malicious and/or suspicious IP addresses – Level 7 | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/7.txt) |
| IPsum | Malicious and/or suspicious IP addresses – Level 8 | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/8.txt) |
| IPsum | IPsum combined threat feed – all blacklists merged with occurrence count | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt) |
| James Brine | Daily malicious IPs from honeypots (SSH/FTP/RDP/GIT/SNMP/REDIS) | <abbr title="Offline">🔴</abbr> | [↗](https://jamesbrine.com.au/csv) |
| MalSilo | MalSilo IPv4 List | <abbr title="Active">🟢</abbr> | [↗](https://malsilo.gitlab.io/feeds/dumps/ip_list.txt) |
| Maltrail | Maltrail Mass Scanner IPs | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/stamparm/maltrail/master/trails/static/mass_scanner.txt) |
| MyIP.ms | Web bot IPs identified in last 10 days | <abbr title="Active">🟢</abbr> | [↗](http://www.myip.ms/files/blacklist/csf/latest_blacklist.txt) |
| MyIP.ms | Full blacklist database (ZIP) | <abbr title="Active">🟢</abbr> | [↗](https://myip.ms/files/blacklist/general/full_blacklist_database.zip) |
| NETSHIELD | Active IP Blacklist – Score ≥65 last 30 days (firewall recommended) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/active_blacklist_ipv4.txt) |
| NETSHIELD | IP Blacklist – Score ≥40 extended rules | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/blacklist_confidence40_ipv4.txt) |
| NETSHIELD | Combined Threat Blacklist – 180-day window for SIEM/audit | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/combined_threat_blacklist_ipv4.txt) |
| NETSHIELD | Watchlist – Score 25-39 monitoring only | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/watchlist_confidence25to39_ipv4.txt) |
| NETSHIELD | CVE exploit and active C2 server IPs (daily) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/cve_exploit_ips.txt) |
| NETSHIELD | Honeypot-confirmed attacker IPs (daily) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/honeypot_ips.txt) |
| NETSHIELD | HoneyDB community honeypot IPs (API) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/honeydb_ips.txt) |
| NETSHIELD | Bot and scanner IPs (daily) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/bot_detector_blacklist_ipv4.txt) |
| NETSHIELD | AbuseIPDB top reported IPs Score ≥50 (API) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/abuseipdb_api_blacklist.txt) |
| NETSHIELD | High-risk ASN blocklist Score ≥50 | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/juergen2025sys/NETSHIELD/main/asn_blocklist_firewall.txt) |
| opsxcq | Open Proxy List | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt) |
| pan-unit42 | DiamondFox Panels | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/pan-unit42/iocs/master/diamondfox/diamondfox_panels.txt) |
| ProjectHoneypot.org | Email harvesters (RSS feed) | <abbr title="Active">🟢</abbr> | [↗](http://www.projecthoneypot.org/list_of_ips.php?t=h&rss=1) |
| ProjectHoneypot.org | Spam servers (RSS feed) | <abbr title="Active">🟢</abbr> | [↗](http://www.projecthoneypot.org/list_of_ips.php?t=s&rss=1) |
| ProjectHoneypot.org | Bad web hosts (RSS feed) | <abbr title="Active">🟢</abbr> | [↗](http://www.projecthoneypot.org/list_of_ips.php?t=b&rss=1) |
| ProjectHoneypot.org | Comment spammers (RSS feed) | <abbr title="Active">🟢</abbr> | [↗](http://www.projecthoneypot.org/list_of_ips.php?t=c&rss=1) |
| ProjectHoneypot.org | Directory/dictionary attackers (RSS feed) | <abbr title="Active">🟢</abbr> | [↗](http://www.projecthoneypot.org/list_of_ips.php?t=d&rss=1) |
| SANS ICS | SANS ICS Intel Feed – community threat indicators | <abbr title="Active">🟢</abbr> | [↗](https://isc.sans.edu/api/intelfeed) |
| SANS ICS / DShield | DShield suggested IP blocklist | <abbr title="Active">🟢</abbr> | [↗](https://isc.sans.edu/block.txt) |
| Sblam | Sblam Spam Comment IPs | <abbr title="Active">🟢</abbr> | [↗](http://sblam.com/blacklist.txt) |
| SecOps-Institute | Tor Nodes List | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-nodes.lst) |
| SecOps-Institute | Tor Exit Nodes List | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-exit-nodes.lst) |
| SentinelPhishFeed | Malicious IP address feed | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/rjn32s/SentinelPhishFeed/main/ips.txt) |
| snort.org | ip-block-list | <abbr title="Active">🟢</abbr> | [↗](https://snort.org/downloads/ip-block-list) |
| socks-proxy.net | Open SOCKS proxies | <abbr title="Active">🟢</abbr> | [↗](http://www.socks-proxy.net/) |
| Spamhaus | Spamhaus DROP List (legacy txt) | <abbr title="Active">🟢</abbr> | [↗](http://www.spamhaus.org/drop/drop.txt) |
| Spamhaus Project | Don't Route Or Peer (DROP) List | <abbr title="Active">🟢</abbr> | [↗](https://www.spamhaus.org/drop/drop_v4.json) |
| spydisec | High Confidence IP Blocklist – confirmed by 5+ independent sources (~5K IPs) | <abbr title="Active">🟢</abbr> | [↗](https://spydisec.com/high_confidence_limited.txt) |
| spydisec | High Confidence IP Blocklist – validated by 3+ independent sources (unlimited) | <abbr title="Active">🟢</abbr> | [↗](https://spydisec.com/high_confidence_unlimited.txt) |
| spydisec | Medium Confidence IP Blocklist – corroborated by 2+ sources (~25K IPs) | <abbr title="Active">🟢</abbr> | [↗](https://spydisec.com/medium_confidence_limited.txt) |
| spydisec | Medium Confidence IP Blocklist – corroborated by 2+ sources (unlimited) | <abbr title="Active">🟢</abbr> | [↗](https://spydisec.com/medium_confidence_unlimited.txt) |
| spydisec | Low Confidence IP Blocklist – single source reports (use with caution) | <abbr title="Active">🟢</abbr> | [↗](https://spydisec.com/low_confidence.txt) |
| spydisec | Full Research IP Blocklist (all tiers combined) | <abbr title="Active">🟢</abbr> | [↗](https://spydisec.com/fullIPblocklist.txt) |
| spydisec | Permanent append-only IP Blocklist archive | <abbr title="Active">🟢</abbr> | [↗](https://spydisec.com/permanentfullIPblocklist.txt) |
| SSLProxies.org | Open SSL proxies | <abbr title="Active">🟢</abbr> | [↗](http://www.sslproxies.org/) |
| StopForumSpam | Forum Spammer IPs – 90 days (zip) | <abbr title="Active">🟢</abbr> | [↗](http://www.stopforumspam.com/downloads/listed_ip_90.zip) |
| StopForumSpam | Forum Spammer IPs – 180 days (zip) | <abbr title="Active">🟢</abbr> | [↗](http://www.stopforumspam.com/downloads/listed_ip_180.zip) |
| StopForumSpam | Forum Spammer IPs – 1 day (zip) | <abbr title="Active">🟢</abbr> | [↗](http://www.stopforumspam.com/downloads/listed_ip_1.zip) |
| StopForumSpam | Forum Spammer IPs – 7 days (zip) | <abbr title="Active">🟢</abbr> | [↗](http://www.stopforumspam.com/downloads/listed_ip_7.zip) |
| StopForumSpam | Forum Spammer IPs (last 1 day) | <abbr title="Active">🟢</abbr> | [↗](https://www.stopforumspam.com/downloads/listed_ip_1.txt) |
| StopForumSpam | Forum Spammer IPs – 30 days (zip) | <abbr title="Active">🟢</abbr> | [↗](http://www.stopforumspam.com/downloads/listed_ip_30.zip) |
| StopForumSpam | Toxic IPs CIDR | <abbr title="Offline">🔴</abbr> | [↗](http://www.stopforumspam.com/downloads/toxic_ip_cidr.txt) |
| StopForumSpam | Banned IPs – all time (ZIP) | <abbr title="Offline">🔴</abbr> | [↗](http://www.stopforumspam.com/downloads/bannedips.zip) |
| StopForumSpam | Forum spammer IPs – last 365 days (ZIP) | <abbr title="Offline">🔴</abbr> | [↗](http://www.stopforumspam.com/downloads/listed_ip_365.zip) |
| StopForumSpam | Forum spammer IPs – last 180 days ALL (ZIP) | <abbr title="Offline">🔴</abbr> | [↗](https://www.stopforumspam.com/downloads/listed_ip_180_all.zip) |
| threatview.io | OSINT IOCs from Twitter and Pastebin | <abbr title="Active">🟢</abbr> | [↗](https://threatview.io/Downloads/Experimental-IOC-Tweets.txt) |
| threatview.io | High Confidence Cobalt Strike C2 Feed | <abbr title="Active">🟢</abbr> | [↗](https://threatview.io/Downloads/High-Confidence-CobaltStrike-C2%20-Feeds.txt) |
| threatview.io | IP High Confidence Feed | <abbr title="Active">🟢</abbr> | [↗](https://threatview.io/Downloads/IP-High-Confidence-Feed.txt) |
| TorProject | Tor Exit Addresses (TorProject official) | <abbr title="Active">🟢</abbr> | [↗](https://check.torproject.org/exit-addresses) |
| Turris | Turris Greylist – IPs observed attacking Turris routers | <abbr title="Active">🟢</abbr> | [↗](https://www.turris.cz/greylist-data/greylist-latest.csv) |
| Ultimate-Hosts-Blacklist | Ultimate Hosts Blacklist IPs | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist/master/ips/ips0.list) |
| X4BNet | VPN IPs | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/X4BNet/lists_vpn/main/output/vpn/ipv4.txt) |
| Yoyo | Yoyo Ad Server IPs | <abbr title="Active">🟢</abbr> | [↗](http://pgl.yoyo.org/adservers/iplist.php?ipformat=plain&showintro=0&mimetype=plaintext) |

### DNS (28)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| Abuse.ch | The host file contains Payload delivery domains and Botnet C2 domains (last 6 months) | <abbr title="Active">🟢</abbr> | [↗](https://threatfox.abuse.ch/downloads/hostfile/) |
| Botvrij.eu | Blacklist Domain | <abbr title="Active">🟢</abbr> | [↗](https://www.botvrij.eu/data/blocklist/blocklist_domain.csv) |
| C2IntelFeeds | C2 domain list – 30 day filter abused | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/domainC2s-30day-filter-abused.csv) |
| C2IntelFeeds | C2 domains with URLs – 30 day filter abused | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/domainC2swithURL-30day-filter-abused.csv) |
| C2IntelFeeds | C2 domains with URLs – filter abused | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/domainC2swithURL-filter-abused.csv) |
| C2IntelFeeds | C2 domains with URL and IP – 30 day filter abused | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/domainC2swithURLwithIP-30day-filter-abused.csv) |
| C2IntelFeeds | C2 domains list | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/domainC2s.csv) |
| CERT-PL | List of malicious domains in Poland (txt) | <abbr title="Active">🟢</abbr> | [↗](https://hole.cert.pl/domains/domains.txt) |
| Cert.PL | Malicious Domains | <abbr title="Active">🟢</abbr> | [↗](https://hole.cert.pl/domains/domains.csv) |
| elliotwutingfeng | Inversion DNSBL – scam and phishing domains | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/elliotwutingfeng/Inversion-DNSBL-Blocklists/main/Google_hostnames.txt) |
| hagezi | DNS Pro Blocklist – comprehensive DNS blocklist (ads, tracking, malware, phishing) | <abbr title="Not checked">⚪</abbr> | [↗](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/pro.txt) |
| hagezi | DNS Pro++ Blocklist – more aggressive version of Pro list | <abbr title="Not checked">⚪</abbr> | [↗](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/pro.plus.txt) |
| hagezi | DNS Threat Intelligence Blocklist – malware and phishing domains | <abbr title="Not checked">⚪</abbr> | [↗](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/threat.txt) |
| jarelllama | Scam Blocklist – phishing and scam domains (wildcard format) | <abbr title="Not checked">⚪</abbr> | [↗](https://raw.githubusercontent.com/jarelllama/Scam-Blocklist/main/lists/wildcard_domains/scams.txt) |
| MalSilo | MalSilo Domain List | <abbr title="Active">🟢</abbr> | [↗](https://malsilo.gitlab.io/feeds/dumps/domain_list.txt) |
| phishdestroy | PhishDestroy blocklist – phishing and malicious domains | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/phishdestroy/destroylist/refs/heads/main/list.txt) |
| SANS ICS | Suspicious Domains – High sensitivity (few false positives) | <abbr title="Offline">🔴</abbr> | [↗](https://isc.sans.edu/feeds/suspiciousdomains_High.txt) |
| SANS ICS | Suspicious Domains – Medium sensitivity | <abbr title="Offline">🔴</abbr> | [↗](https://isc.sans.edu/feeds/suspiciousdomains_Medium.txt) |
| SANS ICS | Suspicious Domains – Low sensitivity (more false positives) | <abbr title="Offline">🔴</abbr> | [↗](https://isc.sans.edu/feeds/suspiciousdomains_Low.txt) |
| SentinelPhishFeed | Phishing and malware domains feed | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/rjn32s/SentinelPhishFeed/main/domains.txt) |
| shreshtait.com | Newly Registered Domains – 1 month | <abbr title="Active">🟢</abbr> | [↗](https://shreshtait.com/newly-registered-domains/nrd-1m) |
| shreshtait.com | Newly Registered Domains – 1 week | <abbr title="Active">🟢</abbr> | [↗](https://shreshtait.com/newly-registered-domains/nrd-1w) |
| spydisec | Malicious Domains Blocklist | <abbr title="Active">🟢</abbr> | [↗](https://spydisec.com/maliciousblocklist.txt) |
| spydisec | Spam/Scam/Abuse Domains Blocklist | <abbr title="Active">🟢</abbr> | [↗](https://spydisec.com/spamblocklist.txt) |
| spydisec | Ads and Tracking Domains Blocklist | <abbr title="Active">🟢</abbr> | [↗](https://spydisec.com/adsblocklist.txt) |
| spydisec | Permanent append-only Malicious Domains archive | <abbr title="Offline">🔴</abbr> | [↗](https://spydisec.com/permanentMaliciousDomainList.txt) |
| threatview.io | Domain High Confidence Feed | <abbr title="Active">🟢</abbr> | [↗](https://threatview.io/Downloads/DOMAIN-High-Confidence-Feed.txt) |
| tsirolnik | Spam Domains List | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/tsirolnik/spam-domains-list/master/spamdomains.txt) |

### URL (29)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| Abuse.ch | Recent Payload delivery and Botnet C2 URLs (ThreatFox) | <abbr title="Active">🟢</abbr> | [↗](https://threatfox.abuse.ch/export/csv/urls/recent/) |
| Abuse.ch | Recent Malware URLs (URLhaus) | <abbr title="Active">🟢</abbr> | [↗](https://urlhaus.abuse.ch/downloads/csv_recent/) |
| Abuse.ch | ThreatFox IOCs – Recent (all types) | <abbr title="Active">🟢</abbr> | [↗](https://threatfox.abuse.ch/export/csv/recent/) |
| APNIC Honeynet | URL Seen in Honeypots | <abbr title="Active">🟢</abbr> | [↗](https://feeds.honeynet.asia/url/latest-url-unique.csv) |
| CriticalPathSecurity | CPS file transfer portal IOCs | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/CriticalPathSecurity/Zeek-Intelligence-Feeds/master/filetransferportals.intel) |
| cybercrime-tracker.net | Cybercrime Tracker – All C2s | <abbr title="Active">🟢</abbr> | [↗](https://cybercrime-tracker.net/all.php) |
| cybercrime-tracker.net | Cybercrime Tracker – Gatelist | <abbr title="Active">🟢</abbr> | [↗](https://cybercrime-tracker.net/ccamgate.php) |
| ExtSentry | Malicious browser extension IDs (all) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/ExtSentry/ExtSentry.github.io/main/feeds/ioc_all_extension_ids.txt) |
| ExtSentry | Malicious browser extension IDs only | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/ExtSentry/ExtSentry.github.io/main/feeds/ioc_malicious_extension_ids.txt) |
| ExtSentry | Suspicious browser extension IDs only | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/ExtSentry/ExtSentry.github.io/main/feeds/ioc_suspicious_extension_ids.txt) |
| ExtSentry | Browser extensions enriched IOC feed (CSV) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/ExtSentry/ExtSentry.github.io/main/feeds/extsentry_ioc_feed.csv) |
| Github | APT Notes CSV | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/aptnotes/data/master/APTnotes.csv) |
| MalSilo | MalSilo URL List | <abbr title="Active">🟢</abbr> | [↗](https://malsilo.gitlab.io/feeds/dumps/url_list.txt) |
| MISP Abuse.ch | MISP Abuse.ch URLhaus | <abbr title="Active">🟢</abbr> | [↗](https://urlhaus.abuse.ch/downloads/misp/) |
| MISP Project | MISP Default Feeds (metadata) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/MISP/MISP/2.4/app/files/feed-metadata/defaults.json) |
| OpenPhish | Phishing URLs | <abbr title="Active">🟢</abbr> | [↗](https://openphish.com/feed.txt) |
| Phishing Army | Phishing Army Blocklist | <abbr title="Active">🟢</abbr> | [↗](https://phishing.army/download/phishing_army_blocklist.txt) |
| Phishing Army | Phishing Army Blocklist Extended | <abbr title="Active">🟢</abbr> | [↗](https://phishing.army/download/phishing_army_blocklist_extended.txt) |
| PhishTank | PhishTank Online Valid Phishing | <abbr title="Active">🟢</abbr> | [↗](https://data.phishtank.com/data/online-valid.csv) |
| PhishTank | PhishTank Online Valid Phishing (JSON) | <abbr title="Active">🟢</abbr> | [↗](http://data.phishtank.com/data/online-valid.json) |
| SentinelPhishFeed | Phishing URLs feed (auto-updated multiple times daily) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/rjn32s/SentinelPhishFeed/main/urls.txt) |
| threatview.io | URL High Confidence Feed | <abbr title="Active">🟢</abbr> | [↗](https://threatview.io/Downloads/URL-High-Confidence-Feed.txt) |
| urlabuse | URL Abuse Blacklist Feed | <abbr title="Active">🟢</abbr> | [↗](https://urlabuse.com/public/data/data.txt) |
| urlabuse | Malware URL Feed | <abbr title="Active">🟢</abbr> | [↗](https://urlabuse.com/public/data/malware_url.txt) |
| urlabuse | Phishing URL Feed | <abbr title="Active">🟢</abbr> | [↗](https://urlabuse.com/public/data/phishing_url.txt) |
| urlabuse | Hacked URL Feed | <abbr title="Active">🟢</abbr> | [↗](https://urlabuse.com/public/data/hacked_url.txt) |
| urlabuse | URL Abuse DB – Latest 500 entries (CSV) | <abbr title="Active">🟢</abbr> | [↗](https://urlabuse.com/public/data/data_csv.txt) |
| VXVault | VXVault Malware URL List | <abbr title="Active">🟢</abbr> | [↗](http://vxvault.net/ViriList.php?s=0&m=100) |
| VXVault | VXVault URL List | <abbr title="Active">🟢</abbr> | [↗](http://vxvault.net/URL_List.php) |

### MD5 (6)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| Abuse.ch | MD5 hashes – Recent additions (MalwareBazaar) | <abbr title="Active">🟢</abbr> | [↗](https://bazaar.abuse.ch/export/txt/md5/recent/) |
| Abuse.ch | MD5 hashes – Recent malicious files on C2 (ThreatFox) | <abbr title="Active">🟢</abbr> | [↗](https://threatfox.abuse.ch/export/csv/md5/recent/) |
| Botvrij.eu | IOC List MD5 | <abbr title="Active">🟢</abbr> | [↗](https://www.botvrij.eu/data/ioclist.md5) |
| cybercrime-tracker.net | Cybercrime Tracker – Hash List | <abbr title="Active">🟢</abbr> | [↗](https://cybercrime-tracker.net/ccamlist.php) |
| malshare.com | Malshare Current All | <abbr title="Active">🟢</abbr> | [↗](https://malshare.com/daily/malshare.current.all.txt) |
| threatview.io | MD5 Hash Blocklist | <abbr title="Active">🟢</abbr> | [↗](https://threatview.io/Downloads/MD5-HASH-ALL.txt) |

### SHA1 (3)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| Abuse.ch | SHA1 hashes – Recent additions (MalwareBazaar) | <abbr title="Active">🟢</abbr> | [↗](https://bazaar.abuse.ch/export/txt/sha1/recent/) |
| Botvrij.eu | IOC List SHA1 | <abbr title="Active">🟢</abbr> | [↗](https://www.botvrij.eu/data/ioclist.sha1) |
| threatview.io | SHA File Hash Feed | <abbr title="Active">🟢</abbr> | [↗](https://threatview.io/Downloads/SHA-HASH-FEED.txt) |

### SHA256 (4)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| Abuse.ch | SHA256 hashes – Recent additions (MalwareBazaar) | <abbr title="Active">🟢</abbr> | [↗](https://bazaar.abuse.ch/export/txt/sha256/recent/) |
| Abuse.ch | SHA256 hashes – Recent malicious files on C2 (ThreatFox) | <abbr title="Active">🟢</abbr> | [↗](https://threatfox.abuse.ch/export/csv/sha256/recent/) |
| Botvrij.eu | IOC List SHA256 | <abbr title="Active">🟢</abbr> | [↗](https://www.botvrij.eu/data/ioclist.sha256) |
| ExtSentry | Browser extension CRX SHA-256 file hashes | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/ExtSentry/ExtSentry.github.io/main/feeds/ioc_crx_sha256_hashes.txt) |

### SSL (1)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| Abuse.ch | SSL Certificate Blacklist | <abbr title="Active">🟢</abbr> | [↗](https://sslbl.abuse.ch/blacklist/sslblacklist.csv) |

### JA3 (1)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| Abuse.ch | JA3 Fingerprints Blacklist | <abbr title="Active">🟢</abbr> | [↗](https://sslbl.abuse.ch/blacklist/ja3_fingerprints.csv) |

### CVEID (4)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| CISA | Known Exploited Vulnerabilities Catalog (CSV) | <abbr title="Active">🟢</abbr> | [↗](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv) |
| CISA | Known Exploited Vulnerabilities Catalog (JSON) | <abbr title="Active">🟢</abbr> | [↗](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) |
| eCrimeLabs | Vulnerabilities with Metasploit exploit available | <abbr title="Active">🟢</abbr> | [↗](https://feeds.ecrimelabs.net/data/metasploit-cve) |
| NIST | National Vulnerability Database CVEs | <abbr title="Active">🟢</abbr> | [↗](https://services.nvd.nist.gov/rest/json/cves/2.0) |

### RANSOMWARELEAK (1)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| ransomware.live | All ransomware victims on leak sites | <abbr title="Active">🟢</abbr> | [↗](https://api.ransomware.live/allcyberattacks) |

### MISP (5)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| abuse.ch | MalwareBazaar MISP feed (hashes + metadata) | <abbr title="Active">🟢</abbr> | [↗](https://bazaar.abuse.ch/downloads/misp/) |
| abuse.ch | ThreatFox MISP feed (IOCs) | <abbr title="Active">🟢</abbr> | [↗](https://threatfox.abuse.ch/downloads/misp/) |
| Botvrij.eu | Botvrij.eu OSINT MISP feed | <abbr title="Active">🟢</abbr> | [↗](https://www.botvrij.eu/data/feed-osint) |
| MISP CIRCL | MISP CIRCL OSINT Feed – Hashes | <abbr title="Active">🟢</abbr> | [↗](https://www.circl.lu/doc/misp/feed-osint/) |
| MISP Feed CERT-FR | MISP Feed CERT-FR Hashes | <abbr title="Active">🟢</abbr> | [↗](https://misp.cert.ssi.gouv.fr/feed-misp/hashes.csv) |

### IOC (9)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| fsrm.experiant.ca | Ransomware file extension blocklist for File Server Resource Manager (FSRM) | <abbr title="Not checked">⚪</abbr> | [↗](https://fsrm.experiant.ca/api/v1/get) |
| montysecurity | C2-Tracker – active C2 servers aggregated from multiple sources (all types combined) | <abbr title="Not checked">⚪</abbr> | [↗](https://raw.githubusercontent.com/montysecurity/C2-Tracker/main/data/all.txt) |
| SentinelPhishFeed | File hash IOCs (MD5/SHA) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/rjn32s/SentinelPhishFeed/main/hashes.txt) |
| threatview.io | Bitcoin Address Intel | <abbr title="Active">🟢</abbr> | [↗](https://threatview.io/Downloads/MALICIOUS-BITCOIN_FEED.txt) |
| tweetfeed.live | IOCs shared by infosec community on Twitter – Today (IP/URL/DNS/Hash) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/0xDanielLopez/TweetFeed/master/today.csv) |
| tweetfeed.live | IOCs shared by infosec community on Twitter – Week (IP/URL/DNS/Hash) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/0xDanielLopez/TweetFeed/master/week.csv) |
| tweetfeed.live | IOCs shared by infosec community on Twitter – Month (IP/URL/DNS/Hash) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/0xDanielLopez/TweetFeed/master/month.csv) |
| tweetfeed.live | IOCs shared by infosec community on Twitter – Year (IP/URL/DNS/Hash) | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/0xDanielLopez/TweetFeed/master/year.csv) |
| WSTNPHX | Email addresses used by malware | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/WSTNPHX/scripts-n-tools/master/malware-email-addresses.txt) |

### BLOCKLIST (43)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| iBlocklist.com | Level 1 – anti-p2p companies/media/government/legal ranges | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=ydxerpxkpcfqjaybcssw&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Level 2 – corporate/labs/proxy ranges | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=gyisgnzbhppbvsphucsw&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Level 3 – paranoid list (portals/ISPs/unusual ranges) | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=uwnukjqktoggdknzrhgh&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Yoyo.org ad servers (p2p format) | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=zhogegszwduurnvsyhdf&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Educational Institution IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=imlmncgrkbnacgcwfjvh&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Microsoft IP ranges | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=xshktygkujudfnjfioro&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | IANA Reserved IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=bcoepfyewziejvcqyhqo&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | IANA Private IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=cslpybexmxyuacbyuvib&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | IANA Multicast IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=pwqnlynprfgtjbgqoizj&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | IP blocklist for non-LAN computers | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=jhaoawihmfxgnvmaqffp&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Exclusions list | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=mtxmiireqmjzazcsoiem&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Apple IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=aphcqvpxuqgrkgufjruj&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | LogMeIn IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=tgbankumtwtrzllndbmb&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Steam IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=cnxkgiklecdaihzukrud&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | XFire IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=ppqqnyihmcrryraaqsjo&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Blizzard IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=ercbntshuthyykfkmhxc&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Ubisoft IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=etmcrglomupyxtaebzht&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Nintendo IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=pevkykuhgaegqyayzbnr&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Activision IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=gfnxlhxsijzrcuxwzebb&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Sony Online Entertainment IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=tukpvrvlubsputmkmiwg&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Crowd Control Productions IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=eveiyhgmusglurfmjyag&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Linden Lab IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=qnjdimxnaupjmpqolxcv&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Electronic Arts IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=ejqebpcdmffinaetsvxj&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Square Enix IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=odyaqontcydnodrlyina&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | NCsoft IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=mwjuwmebrnzyyxpbezxu&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Riot Games IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=sdlvfabdjvrdttfjotcy&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Punkbuster IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=zvwwndvzulqcltsicwdg&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Joost IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=alxugfmeszbhpxqfdits&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Pandora IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=aevzidimyvwybzkletsg&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | The Pirate Bay IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=nzldzlpkgrcncdomnttb&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | AOL IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=toboaiysofkflwgrttmb&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Comcast IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=rsgyxvuklicibautguia&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Cablevision IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=dwwbsmzirrykdlvpqozb&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Verizon IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=cdmdbprvldivlqsaqjol&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | AT&T IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=grbtkzijgrowvobvessf&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Cox Communications IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=nlgdvmvfxvoimdunmuju&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Time Warner Cable IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=aqtsnttnqmcucwrjmohd&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Charter IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=htnzojgossawhpkbulqw&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Qwest IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=jezlifrpefawuoawnfez&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Embarq IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=twdblifaysaqtypevvdp&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Suddenlink IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=psaoblrwylfrdsspfuiq&fileformat=p2p&archiveformat=gz) |
| iBlocklist.com | Sprint IPs | <abbr title="Offline">🔴</abbr> | [↗](http://list.iblocklist.com/?list=hngtqrhhuadlceqxbrob&fileformat=p2p&archiveformat=gz) |
| Ngosang | BitTorrent Trackers IP List | <abbr title="Active">🟢</abbr> | [↗](https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt) |

### REPO (23)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| Avast | Avast IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/avast/ioc) |
| Black Lotus Labs | Black Lotus Labs IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/blacklotuslabs/IOCs) |
| blocklistproject | Block Lists – comprehensive domain blocklists (ads, malware, phishing, ransomware, scam) | <abbr title="N/A">➖</abbr> | [↗](https://github.com/blocklistproject/Lists) |
| Cisco Talos | Cisco Talos IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/Cisco-Talos/IOCs) |
| DoctorWeb | Dr.Web malware IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/DoctorWebLtd/malware-iocs) |
| Elastic Security Labs | Elastic Security Labs threat indicators repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/elastic/labs-releases) |
| ESET | ESET Malware IOC Repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/eset/malware-ioc) |
| executemalware | Community Malware IOCs (GitHub repo) | <abbr title="N/A">➖</abbr> | [↗](https://github.com/executemalware/Malware-IOCs) |
| FireHOL | FireHOL blocklist-ipsets — curated IP blocklist collections (multiple sets) | <abbr title="N/A">➖</abbr> | [↗](https://github.com/firehol/blocklist-ipsets) |
| HarfangLab | HarfangLab IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/HarfangLab/iocs) |
| kraloveckey | FireWALL-E: ipsets-blocklist | <abbr title="N/A">➖</abbr> | [↗](https://github.com/kraloveckey/ipsets-blocklist) |
| mthcht | SOC/DFIR detection lists – VPN IPs, Named Pipes, Suspicious Services, Extensions and more | <abbr title="N/A">➖</abbr> | [↗](https://github.com/mthcht/awesome-lists) |
| Palo Alto Unit42 | Unit42 IOC Repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/pan-unit42/iocs) |
| Palo Alto Unit42 | Unit42 Timely Threat Intelligence IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel) |
| Palo Alto Unit42 | Unit42 Threat Intelligence Article IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/PaloAltoNetworks/Unit42-Threat-Intelligence-Article-Information) |
| pr0xylife | pr0xylife malware IOC collections (DarkGate, QakBot, Emotet, IcedID and more) | <abbr title="N/A">➖</abbr> | [↗](https://github.com/pr0xylife) |
| prodaft | prodaft malware IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/prodaft/malware-ioc) |
| SecurityScorecard | Public IoCs from SecurityScorecard technical blog posts | <abbr title="N/A">➖</abbr> | [↗](https://github.com/securityscorecard/SSC-Threat-Intel-IoCs) |
| Sekoia | Sekoia Community IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/SEKOIA-IO/Community) |
| Sophos | Sophos Labs IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/sophoslabs/IoCs) |
| ThreatMon | ThreatMon Daily C2 Feeds | <abbr title="N/A">➖</abbr> | [↗](https://github.com/ThreatMon/ThreatMon-Daily-C2-Feeds) |
| Volexity | Volexity Threat Intelligence IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/volexity/threat-intel) |
| Zscaler ThreatLabz | Zscaler ThreatLabz IOC repository | <abbr title="N/A">➖</abbr> | [↗](https://github.com/threatlabz/iocs) |

### RESTRICTED (5)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| MaxMind | GeoLite2 ASN Database – IP to ASN mapping (requires free license key at maxmind.com) | <abbr title="Restricted">🔒</abbr> | [↗](https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-ASN-CSV&license_key=YOUR_KEY&suffix=zip) |
| MaxMind | GeoLite2 Country Database – IP to Country mapping (requires free license key at maxmind.com) | <abbr title="Restricted">🔒</abbr> | [↗](https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country-CSV&license_key=YOUR_KEY&suffix=zip) |
| osint.bambenekconsulting.com | All current domains belonging to known malicious DGAs (requires license for commercial use) | <abbr title="Restricted">🔒</abbr> | [↗](https://osint.bambenekconsulting.com/feeds/dga-feed-high.csv) |
| osint.bambenekconsulting.com | Domains from High-Confidence DGA-based C&C Domains Actively Resolving (requires license for commercial use) | <abbr title="Restricted">🔒</abbr> | [↗](https://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt) |
| osint.bambenekconsulting.com | IPs from High-Confidence DGA-Based C&Cs Actively Resolving (requires license for commercial use) | <abbr title="Restricted">🔒</abbr> | [↗](https://osint.bambenekconsulting.com/feeds/c2-ipmasterlist-high.txt) |

### GEOIP (3)

| Vendor | Description | Status | URL |
| --- | --- | :---: | --- |
| DB-IP | DB-IP Country Lite – free IP to Country database (monthly updated, fixed URL) | <abbr title="Offline">🔴</abbr> | [↗](https://download.db-ip.com/free/dbip-country-lite.csv.gz) |
| IP2Location | IP2Location LITE DB1 – IP to Country database (free, no key required) | <abbr title="Active">🟢</abbr> | [↗](https://download.ip2location.com/lite/IP2LOCATION-LITE-DB1.CSV.ZIP) |
| IPDeny.com | IPDeny country IP blocks – all zones (tar.gz, updated daily) | <abbr title="Active">🟢</abbr> | [↗](http://www.ipdeny.com/ipblocks/data/countries/all-zones.tar.gz) |
<!-- FEEDS_TABLE_END -->

---

## 🤝 Contributing

1. **Add a row** to `threat-intelligence-feeds.csv`:

   ```csv
   Vendor;Description;Category;Url
   ```

2. **Choose the right category** — see the table above for descriptions. Key rules:
   - Feed must have a **direct, machine-readable URL** (raw text, CSV, JSON) — if not, use `REPO`.
   - If the feed requires **registration or an API key**, use `RESTRICTED` and note it in the Description. Status will be shown as 🔒 and the URL will not be checked automatically.
   - If it's a **GitHub repository** without a direct machine-readable URL, use `REPO`. Status will be checked automatically (🟢 if reachable, 🔴 if deleted/unavailable).
   - If the feed contains **mixed IOC types** (IP + domain + hash in one file), use `IOC`.
   - If it's a general **ISP / ASN / ad-tracker blocklist** (not malware-specific), use `BLOCKLIST`.
   - If it's an **IP geolocation database** (country/ASN mapping, not malicious IPs), use `GEOIP`.
  
3. **Free and publicly accessible** feeds without registration are preferred. `RESTRICTED` feeds are accepted if they are well-known and valuable.
   
4. **Validate** before opening a PR:
   
   ```bash
   cd scripts
   python3 tif-validator.py
   python3 tif-update-readme.py
   ```

5. **Open a Pull Request** with a short description of the feed and why it belongs here.

Valid categories: `IP` `DNS` `URL` `MD5` `SHA1` `SHA256` `SSL` `JA3` `CVEID` `RANSOMWARELEAK` `MISP` `IOC` `BLOCKLIST` `REPO` `RESTRICTED` `GEOIP`.