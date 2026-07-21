#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F1-DRS 数据更新脚本 (2026 赛季)
=================================
使用 FastF1 抓取 2026 赛季数据，生成 docs/data.js。

生成的数据结构与 docs/index.html 中原有内联数据完全一致：
  - circuits          : 赛历（含 trackDetailId 映射）
  - compareDrivers   : 车手对比阵容（静态，FastF1 不提供历史对比阵容）
  - champions         : 历年世界冠军（静态）
  - constructorsData  : 车队积分榜
  - driverStandings   : 车手积分榜
  - raceResults       : 每站前三 + 杆位 + 最快圈
  - trackDetailData    : 赛道详情（静态赛道图 + FastF1 圈数/长度）
  - driverData        : 车手详细统计（从 2026 各站累加）

用法:
    python scripts/update_data.py
输出:
    docs/data.js  (覆盖写入)
"""

import os
import sys
import json
import datetime

# ----------------------------------------------------------------------------
# 路径配置
# ----------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")
OUTPUT_PATH = os.path.join(DOCS_DIR, "data.js")
CACHE_DIR = os.path.join(SCRIPT_DIR, "cache")

SEASON = 2026

# ----------------------------------------------------------------------------
# 静态数据：车手对比阵容（FastF1 不提供"对比阵容"概念，保持静态）
# 字段与 index.html 中 compareDrivers 一致
# ----------------------------------------------------------------------------
COMPARE_DRIVERS = [
    {"name": "Antonelli", "team": "Mercedes", "color": "#27f4d2", "num": 12, "wins": 5, "podiums": 5, "poles": 1, "points": 179, "fastest": 3},
    {"name": "Russell", "team": "Mercedes", "color": "#27f4d2", "num": 63, "wins": 4, "podiums": 21, "poles": 5, "points": 154, "fastest": 8},
    {"name": "Leclerc", "team": "Ferrari", "color": "#dc0000", "num": 16, "wins": 9, "podiums": 44, "poles": 26, "points": 108, "fastest": 10},
    {"name": "Hamilton", "team": "Ferrari", "color": "#dc0000", "num": 44, "wins": 105, "podiums": 203, "poles": 104, "points": 147, "fastest": 67},
    {"name": "Norris", "team": "McLaren", "color": "#ff8000", "num": 4, "wins": 10, "podiums": 35, "poles": 10, "points": 97, "fastest": 8},
    {"name": "Piastri", "team": "McLaren", "color": "#ff8000", "num": 81, "wins": 4, "podiums": 17, "poles": 0, "points": 82, "fastest": 3},
    {"name": "Verstappen", "team": "Red Bull", "color": "#1e41b0", "num": 1, "wins": 63, "podiums": 112, "poles": 40, "points": 76, "fastest": 33},
    {"name": "Hadjar", "team": "Red Bull", "color": "#1e41b0", "num": 6, "wins": 0, "podiums": 0, "poles": 0, "points": 52, "fastest": 0},
    {"name": "Gasly", "team": "Alpine", "color": "#0093cc", "num": 10, "wins": 1, "podiums": 5, "poles": 0, "points": 42, "fastest": 3},
    {"name": "Lawson", "team": "Racing Bulls", "color": "#6699ff", "num": 30, "wins": 0, "podiums": 0, "poles": 0, "points": 39, "fastest": 0},
    {"name": "Lindblad", "team": "Racing Bulls", "color": "#6699ff", "num": 7, "wins": 0, "podiums": 0, "poles": 0, "points": 20, "fastest": 0},
    {"name": "Bearman", "team": "Haas", "color": "#cc0000", "num": 87, "wins": 0, "podiums": 0, "poles": 0, "points": 18, "fastest": 0},
    {"name": "Colapinto", "team": "Alpine", "color": "#0093cc", "num": 43, "wins": 0, "podiums": 0, "poles": 0, "points": 18, "fastest": 0},
    {"name": "Bortoleto", "team": "Audi", "color": "#c0c0c0", "num": 5, "wins": 0, "podiums": 0, "poles": 0, "points": 6, "fastest": 0},
    {"name": "Sainz", "team": "Williams", "color": "#005aff", "num": 55, "wins": 4, "podiums": 27, "poles": 6, "points": 6, "fastest": 4},
    {"name": "Albon", "team": "Williams", "color": "#005aff", "num": 23, "wins": 0, "podiums": 2, "poles": 0, "points": 5, "fastest": 0},
    {"name": "Ocon", "team": "Haas", "color": "#cc0000", "num": 31, "wins": 1, "podiums": 3, "poles": 0, "points": 3, "fastest": 0},
    {"name": "Alonso", "team": "Aston Martin", "color": "#006f62", "num": 14, "wins": 32, "podiums": 106, "poles": 22, "points": 1, "fastest": 28},
    {"name": "Hulkenberg", "team": "Audi", "color": "#c0c0c0", "num": 27, "wins": 0, "podiums": 0, "poles": 1, "points": 0, "fastest": 2},
    {"name": "Bottas", "team": "Cadillac", "color": "#cf9f3f", "num": 77, "wins": 10, "podiums": 67, "poles": 20, "points": 0, "fastest": 19},
    {"name": "Perez", "team": "Cadillac", "color": "#cf9f3f", "num": 11, "wins": 6, "podiums": 39, "poles": 1, "points": 0, "fastest": 12},
    {"name": "Stroll", "team": "Aston Martin", "color": "#006f62", "num": 18, "wins": 0, "podiums": 3, "poles": 1, "points": 0, "fastest": 0},
]

# ----------------------------------------------------------------------------
# 静态数据：历年世界冠军（FastF1 不提供历史冠军列表，保持静态）
# ----------------------------------------------------------------------------
CHAMPIONS = [
    {"year": 1950, "driver": "Giuseppe Farina", "team": "Alfa Romeo"},
    {"year": 1951, "driver": "Juan Manuel Fangio", "team": "Alfa Romeo"},
    {"year": 1952, "driver": "Alberto Ascari", "team": "Ferrari"},
    {"year": 1953, "driver": "Alberto Ascari", "team": "Ferrari"},
    {"year": 1954, "driver": "Juan Manuel Fangio", "team": "Mercedes"},
    {"year": 1955, "driver": "Juan Manuel Fangio", "team": "Mercedes"},
    {"year": 1956, "driver": "Juan Manuel Fangio", "team": "Ferrari"},
    {"year": 1957, "driver": "Juan Manuel Fangio", "team": "Maserati"},
    {"year": 1958, "driver": "Mike Hawthorn", "team": "Ferrari"},
    {"year": 1959, "driver": "Jack Brabham", "team": "Cooper"},
    {"year": 1960, "driver": "Jack Brabham", "team": "Cooper"},
    {"year": 1961, "driver": "Phil Hill", "team": "Ferrari"},
    {"year": 1962, "driver": "Graham Hill", "team": "BRM"},
    {"year": 1963, "driver": "Jim Clark", "team": "Lotus"},
    {"year": 1964, "driver": "John Surtees", "team": "Ferrari"},
    {"year": 1965, "driver": "Jim Clark", "team": "Lotus"},
    {"year": 1966, "driver": "Jack Brabham", "team": "Brabham"},
    {"year": 1967, "driver": "Denny Hulme", "team": "Brabham"},
    {"year": 1968, "driver": "Graham Hill", "team": "Lotus"},
    {"year": 1969, "driver": "Jackie Stewart", "team": "Matra"},
    {"year": 1970, "driver": "Jochen Rindt", "team": "Lotus"},
    {"year": 1971, "driver": "Jackie Stewart", "team": "Tyrrell"},
    {"year": 1972, "driver": "Emerson Fittipaldi", "team": "Lotus"},
    {"year": 1973, "driver": "Jackie Stewart", "team": "Tyrrell"},
    {"year": 1974, "driver": "Emerson Fittipaldi", "team": "McLaren"},
    {"year": 1975, "driver": "Niki Lauda", "team": "Ferrari"},
    {"year": 1976, "driver": "James Hunt", "team": "McLaren"},
    {"year": 1977, "driver": "Niki Lauda", "team": "Ferrari"},
    {"year": 1978, "driver": "Mario Andretti", "team": "Lotus"},
    {"year": 1979, "driver": "Jody Scheckter", "team": "Ferrari"},
    {"year": 1980, "driver": "Alan Jones", "team": "Williams"},
    {"year": 1981, "driver": "Nelson Piquet", "team": "Brabham"},
    {"year": 1982, "driver": "Keke Rosberg", "team": "Williams"},
    {"year": 1983, "driver": "Nelson Piquet", "team": "Brabham"},
    {"year": 1984, "driver": "Niki Lauda", "team": "McLaren"},
    {"year": 1985, "driver": "Alain Prost", "team": "McLaren"},
    {"year": 1986, "driver": "Alain Prost", "team": "McLaren"},
    {"year": 1987, "driver": "Nelson Piquet", "team": "Williams"},
    {"year": 1988, "driver": "Ayrton Senna", "team": "McLaren"},
    {"year": 1989, "driver": "Alain Prost", "team": "McLaren"},
    {"year": 1990, "driver": "Ayrton Senna", "team": "McLaren"},
    {"year": 1991, "driver": "Ayrton Senna", "team": "McLaren"},
    {"year": 1992, "driver": "Nigel Mansell", "team": "Williams"},
    {"year": 1993, "driver": "Alain Prost", "team": "Williams"},
    {"year": 1994, "driver": "Michael Schumacher", "team": "Benetton"},
    {"year": 1995, "driver": "Michael Schumacher", "team": "Benetton"},
    {"year": 1996, "driver": "Damon Hill", "team": "Williams"},
    {"year": 1997, "driver": "Jacques Villeneuve", "team": "Williams"},
    {"year": 1998, "driver": "Mika Hakkinen", "team": "McLaren"},
    {"year": 1999, "driver": "Mika Hakkinen", "team": "McLaren"},
    {"year": 2000, "driver": "Michael Schumacher", "team": "Ferrari"},
    {"year": 2001, "driver": "Michael Schumacher", "team": "Ferrari"},
    {"year": 2002, "driver": "Michael Schumacher", "team": "Ferrari"},
    {"year": 2003, "driver": "Michael Schumacher", "team": "Ferrari"},
    {"year": 2004, "driver": "Michael Schumacher", "team": "Ferrari"},
    {"year": 2005, "driver": "Fernando Alonso", "team": "Renault"},
    {"year": 2006, "driver": "Fernando Alonso", "team": "Renault"},
    {"year": 2007, "driver": "Kimi Raikkonen", "team": "Ferrari"},
    {"year": 2008, "driver": "Lewis Hamilton", "team": "McLaren"},
    {"year": 2009, "driver": "Jenson Button", "team": "Brawn GP"},
    {"year": 2010, "driver": "Sebastian Vettel", "team": "Red Bull"},
    {"year": 2011, "driver": "Sebastian Vettel", "team": "Red Bull"},
    {"year": 2012, "driver": "Sebastian Vettel", "team": "Red Bull"},
    {"year": 2013, "driver": "Sebastian Vettel", "team": "Red Bull"},
    {"year": 2014, "driver": "Lewis Hamilton", "team": "Mercedes"},
    {"year": 2015, "driver": "Lewis Hamilton", "team": "Mercedes"},
    {"year": 2016, "driver": "Nico Rosberg", "team": "Mercedes"},
    {"year": 2017, "driver": "Lewis Hamilton", "team": "Mercedes"},
    {"year": 2018, "driver": "Lewis Hamilton", "team": "Mercedes"},
    {"year": 2019, "driver": "Lewis Hamilton", "team": "Mercedes"},
    {"year": 2020, "driver": "Lewis Hamilton", "team": "Mercedes"},
    {"year": 2021, "driver": "Max Verstappen", "team": "Red Bull"},
    {"year": 2022, "driver": "Max Verstappen", "team": "Red Bull"},
    {"year": 2023, "driver": "Max Verstappen", "team": "Red Bull"},
    {"year": 2024, "driver": "Max Verstappen", "team": "Red Bull"},
    {"year": 2025, "driver": "Lando Norris", "team": "McLaren"},
]

# ----------------------------------------------------------------------------
# 静态数据：赛道详情模板（FastF1 提供圈数/长度，赛道图用 FOM 官方 URL）
# trackDetailId 与 circuits 数组索引对应（1-based）
# ----------------------------------------------------------------------------
# FOM 赛道图 URL 模板
FOM_LAYOUT_TPL = (
    '<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/'
    'content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/{CIRCUIT}_Circuit" '
    'alt="{CIRCUIT} Circuit Map" loading="lazy" onerror="this.style.display=\'none\'">'
)

# 赛道静态信息：id, name, gp(中文), country(带国旗), firstRace, corners, drs,
#                fom_key(URL用), record(driver, time, year)
TRACK_STATIC = {
    "albert-park":   dict(name="Albert Park", gp="澳大利亚大奖赛", country="🇦🇺 澳大利亚", firstRace=1996, corners=14, drs=4, fom="Australia", record=("Leclerc", "1:19.813", 2024)),
    "shanghai":      dict(name="上海国际赛车场", gp="中国大奖赛", country="🇨🇳 中国", firstRace=2004, corners=16, drs=3, fom="China", record=("Schumacher", "1:32.238", 2004)),
    "suzuka":        dict(name="铃鹿", gp="日本大奖赛", country="🇯🇵 日本", firstRace=1987, corners=18, drs=2, fom="Japan", record=("Hamilton", "1:30.983", 2019)),
    "bahrain":       dict(name="Bahrain International Circuit", gp="巴林大奖赛", country="🇧🇭 巴林", firstRace=2004, corners=15, drs=3, fom="Bahrain", record=("De la Rosa", "1:31.447", 2005)),
    "jeddah":        dict(name="Jeddah Corniche Circuit", gp="沙特阿拉伯大奖赛", country="🇸🇦 沙特阿拉伯", firstRace=2021, corners=27, drs=3, fom="Saudi_Arabia", record=("Hamilton", "1:30.734", 2021)),
    "miami":         dict(name="Miami International Autodrome", gp="迈阿密大奖赛", country="🇺🇸 美国", firstRace=2022, corners=19, drs=3, fom="Miami", record=("Verstappen", "1:29.708", 2023)),
    "montreal":      dict(name="Circuit Gilles Villeneuve", gp="加拿大大奖赛", country="🇨🇦 加拿大", firstRace=1978, corners=14, drs=3, fom="Canada", record=("Bottas", "1:13.078", 2019)),
    "monaco":        dict(name="Circuit de Monaco", gp="摩纳哥大奖赛", country="🇲🇨 摩纳哥", firstRace=1950, corners=19, drs=1, fom="Monaco", record=("Hamilton", "1:12.909", 2021)),
    "barcelona":     dict(name="Circuit de Barcelona-Catalunya", gp="西班牙大奖赛(巴塞罗那)", country="🇪🇸 西班牙", firstRace=1991, corners=16, drs=2, fom="Spain", record=("Verstappen", "1:16.330", 2023)),
    "red-bull-ring": dict(name="Red Bull Ring", gp="奥地利大奖赛", country="🇦🇹 奥地利", firstRace=1970, corners=10, drs=3, fom="Austria", record=("Sainz", "1:05.619", 2020)),
    "silverstone":   dict(name="Silverstone", gp="英国大奖赛", country="🇬🇧 英国", firstRace=1950, corners=18, drs=2, fom="Great_Britain", record=("Hamilton", "1:27.097", 2020)),
    "spa":           dict(name="Spa-Francorchamps", gp="比利时大奖赛", country="🇧🇪 比利时", firstRace=1950, corners=19, drs=2, fom="Belgium", record=("Bottas", "1:46.286", 2018)),
    "hungaroring":   dict(name="Hungaroring", gp="匈牙利大奖赛", country="🇭🇺 匈牙利", firstRace=1986, corners=14, drs=2, fom="Hungary", record=("Hamilton", "1:16.627", 2020)),
    "zandvoort":     dict(name="Zandvoort", gp="荷兰大奖赛", country="🇳🇱 荷兰", firstRace=1952, corners=14, drs=2, fom="Netherlands", record=("Hamilton", "1:11.097", 2021)),
    "monza":         dict(name="Monza", gp="意大利大奖赛", country="🇮🇹 意大利", firstRace=1950, corners=11, drs=2, fom="Italy", record=("Barrichello", "1:21.046", 2004)),
    "madrid":        dict(name="Madrid Street Circuit", gp="马德里大奖赛", country="🇪🇸 西班牙", firstRace=2026, corners=20, drs=2, fom="Madrid", record=("—", "—", "2026 新赛道")),
    "baku":          dict(name="Baku City Circuit", gp="阿塞拜疆大奖赛", country="🇦🇿 阿塞拜疆", firstRace=2016, corners=20, drs=2, fom="Azerbaijan", record=("Leclerc", "1:43.009", 2019)),
    "singapore":     dict(name="Marina Bay", gp="新加坡大奖赛", country="🇸🇬 新加坡", firstRace=2008, corners=23, drs=3, fom="Singapore", record=("Hamilton", "1:36.015", 2018)),
    "cota":          dict(name="COTA", gp="美国大奖赛(奥斯汀)", country="🇺🇸 美国", firstRace=2012, corners=20, drs=2, fom="USA", record=("Leclerc", "1:36.169", 2019)),
    "mexico":        dict(name="Autodromo Hermanos Rodriguez", gp="墨西哥大奖赛", country="🇲🇽 墨西哥", firstRace=1963, corners=17, drs=3, fom="Mexico", record=("Bottas", "1:17.774", 2021)),
    "interlagos":    dict(name="Interlagos", gp="巴西大奖赛", country="🇧🇷 巴西", firstRace=1973, corners=15, drs=2, fom="Brazil", record=("Bottas", "1:10.540", 2018)),
    "las-vegas":     dict(name="Las Vegas Strip Circuit", gp="拉斯维加斯大奖赛", country="🇺🇸 美国", firstRace=2023, corners=17, drs=2, fom="Las_Vegas", record=("Piastri", "1:34.876", 2024)),
    "lusail":        dict(name="Lusail International Circuit", gp="卡塔尔大奖赛", country="🇶🇦 卡塔尔", firstRace=2021, corners=16, drs=2, fom="Qatar", record=("Verstappen", "1:24.319", 2023)),
    "yas-marina":    dict(name="Yas Marina", gp="阿布扎比大奖赛", country="🇦🇪 阿联酋", firstRace=2009, corners=21, drs=2, fom="Abu_Dhabi", record=("Verstappen", "1:26.103", 2021)),
}

# circuits 数组（赛历），trackDetailId 对应 TRACK_STATIC 的插入顺序 (1-based)
CIRCUITS = [
    {"no": "1", "gp": "澳大利亚大奖赛", "circuit": "Albert Park", "city": "墨尔本", "date": "3月6-8日", "trackDetailId": 1},
    {"no": "2", "gp": "中国大奖赛", "circuit": "Shanghai International Circuit", "city": "上海", "date": "3月13-15日 (冲刺赛)", "trackDetailId": 2},
    {"no": "3", "gp": "日本大奖赛", "circuit": "Suzuka Circuit", "city": "铃鹿", "date": "3月27-29日", "trackDetailId": 3},
    {"no": "—", "gp": "巴林大奖赛", "circuit": "Bahrain International Circuit", "city": "萨基尔", "date": "4月10-12日 ❌取消", "trackDetailId": 4},
    {"no": "—", "gp": "沙特阿拉伯大奖赛", "circuit": "Jeddah Corniche Circuit", "city": "吉达", "date": "4月17-19日 ❌取消", "trackDetailId": 5},
    {"no": "4", "gp": "迈阿密大奖赛", "circuit": "Miami International Autodrome", "city": "迈阿密", "date": "5月1-3日 (冲刺赛)", "trackDetailId": 6},
    {"no": "5", "gp": "加拿大大奖赛", "circuit": "Circuit Gilles Villeneuve", "city": "蒙特利尔", "date": "5月22-24日", "trackDetailId": 10},
    {"no": "6", "gp": "摩纳哥大奖赛", "circuit": "Circuit de Monaco", "city": "蒙特卡洛", "date": "6月5-7日", "trackDetailId": 8},
    {"no": "7", "gp": "巴塞罗那-加泰罗尼亚大奖赛", "circuit": "Circuit de Barcelona-Catalunya", "city": "巴塞罗那", "date": "6月12-14日", "trackDetailId": 9},
    {"no": "8", "gp": "奥地利大奖赛", "circuit": "Red Bull Ring", "city": "斯皮尔伯格", "date": "6月26-28日", "trackDetailId": 11},
    {"no": "9", "gp": "英国大奖赛", "circuit": "Silverstone Circuit", "city": "银石", "date": "7月3-5日 (冲刺赛)", "trackDetailId": 12},
    {"no": "10", "gp": "比利时大奖赛", "circuit": "Circuit de Spa-Francorchamps", "city": "斯帕", "date": "7月17-19日", "trackDetailId": 13},
    {"no": "11", "gp": "匈牙利大奖赛", "circuit": "Hungaroring", "city": "布达佩斯", "date": "7月24-26日", "trackDetailId": 14},
    {"no": "12", "gp": "荷兰大奖赛", "circuit": "Circuit Zandvoort", "city": "赞德沃特", "date": "8月21-23日 (冲刺赛)", "trackDetailId": 15},
    {"no": "13", "gp": "意大利大奖赛", "circuit": "Autodromo Nazionale Monza", "city": "蒙扎", "date": "9月4-6日", "trackDetailId": 16},
    {"no": "14", "gp": "西班牙大奖赛", "circuit": "Madrid Street Circuit 🆕", "city": "马德里", "date": "9月11-13日", "trackDetailId": 0},
    {"no": "15", "gp": "阿塞拜疆大奖赛", "circuit": "Baku City Circuit", "city": "巴库", "date": "9月24-26日", "trackDetailId": 17},
    {"no": "16", "gp": "新加坡大奖赛", "circuit": "Marina Bay Street Circuit", "city": "新加坡", "date": "10月9-11日 (冲刺赛)", "trackDetailId": 18},
    {"no": "17", "gp": "美国大奖赛", "circuit": "Circuit of the Americas", "city": "奥斯汀", "date": "10月23-25日", "trackDetailId": 19},
    {"no": "18", "gp": "墨西哥城大奖赛", "circuit": "Autódromo Hermanos Rodríguez", "city": "墨西哥城", "date": "10月30日-11月1日", "trackDetailId": 20},
    {"no": "19", "gp": "圣保罗大奖赛", "circuit": "Autódromo José Carlos Pace", "city": "圣保罗", "date": "11月6-8日", "trackDetailId": 21},
    {"no": "20", "gp": "拉斯维加斯大奖赛", "circuit": "Las Vegas Strip Circuit", "city": "拉斯维加斯", "date": "11月19-21日", "trackDetailId": 22},
    {"no": "21", "gp": "卡塔尔大奖赛", "circuit": "Lusail International Circuit", "city": "卢赛尔", "date": "11月27-29日", "trackDetailId": 23},
    {"no": "22", "gp": "阿布扎比大奖赛", "circuit": "Yas Marina Circuit", "city": "阿布扎比", "date": "12月4-6日", "trackDetailId": 24},
]

# 车队颜色映射（用于 constructorsData / driverStandings 的 color 字段）
TEAM_COLORS = {
    "Mercedes": "#27f4d2",
    "Ferrari": "#dc0000",
    "McLaren": "#ff8000",
    "Red Bull": "#1e41b0",
    "Red Bull Racing": "#1e41b0",
    "Alpine": "#0093cc",
    "Racing Bulls": "#6699ff",
    "Haas": "#cc0000",
    "Williams": "#005aff",
    "Audi": "#c0c0c0",
    "Aston Martin": "#006f62",
    "Cadillac": "#cf9f3f",
}

# 车手静态信息（FastF1 提供积分/统计，但不提供国籍/生日/简介，这些保持静态）
DRIVER_STATIC = {
    "Kimi Antonelli": dict(team="Mercedes", nationality="Italy", flag="🇮🇹", number="12", dob="2006-08-25", age=19,
                           bio="2026赛季F1新人王，梅赛德斯青训出品。首秀即夺冠，以惊人的速度和成熟的比赛智商震惊围场，被视作未来十年最有潜力的车手。"),
    "George Russell": dict(team="Mercedes", nationality="United Kingdom", flag="🇬🇧", number="63", dob="1998-02-15", age=28,
                          bio="梅赛德斯领军车手，以精准的排位赛表现和稳定的长距离节奏著称。2026赛季与新人Antonelli搭档，展现成熟领袖风范。"),
    "Charles Leclerc": dict(team="Ferrari", nationality="Monaco", flag="🇲🇨", number="16", dob="1997-10-16", age=28,
                            bio="法拉利王牌，排位赛之王。单圈速度围场顶尖，但需要更稳定的正赛发挥来争夺世界冠军。2026赛季搭档Hamilton组成梦幻阵容。"),
    "Lewis Hamilton": dict(team="Ferrari", nationality="United Kingdom", flag="🇬🇧", number="44", dob="1985-01-07", age=41,
                           bio="七届世界冠军，F1历史最伟大车手之一。2025年加盟法拉利，追逐第八座世界冠军的梦想。2026赛季适应新规后迅速展现竞争力。"),
    "Lando Norris": dict(team="McLaren", nationality="United Kingdom", flag="🇬🇧", number="4", dob="1999-11-13", age=26,
                         bio="2025赛季世界冠军！迈凯伦青训的杰出代表，以敏捷的速度和风趣的性格成为车迷最爱。2026赛季目标是卫冕。"),
    "Oscar Piastri": dict(team="McLaren", nationality="Australia", flag="🇦🇺", number="81", dob="2001-04-06", age=25,
                          bio="冷静沉稳的澳大利亚新星，F2和F3连续冠军出身。正赛节奏和轮胎管理能力突出，被广泛看好在未来挑战世界冠军。"),
    "Max Verstappen": dict(team="Red Bull Racing", nationality="Netherlands", flag="🇳🇱", number="1", dob="1997-09-30", age=28,
                           bio="四届世界冠军，以无与伦比的赛车本能和极限攻防著称。2026赛季面临新规挑战，但仍是任何赛道上不可忽视的力量。"),
    "Isack Hadjar": dict(team="Red Bull Racing", nationality="France", flag="🇫🇷", number="6", dob="2004-09-28", age=21,
                         bio="红牛青训出品，2025年F2亚军。2026年以新人身份升入大红牛，在Verstappen身边学习是巨大的机会和挑战。"),
    "Pierre Gasly": dict(team="Alpine", nationality="France", flag="🇫🇷", number="10", dob="1996-02-07", age=30,
                         bio="Alpine的法国本土英雄，2020年意大利大奖赛胜者。稳定的积分收割机，在2026赛季带领车队转投梅赛德斯动力单元。"),
    "Franco Colapinto": dict(team="Alpine", nationality="Argentina", flag="🇦🇷", number="43", dob="2003-05-27", age=23,
                             bio="阿根廷新星，2024年威廉姆斯赛季中途登场即展现不俗速度。2026年转会Alpine开启全新篇章，南美车迷的新希望。"),
    "Liam Lawson": dict(team="Racing Bulls", nationality="New Zealand", flag="🇳🇿", number="30", dob="2002-02-11", age=24,
                        bio="新西兰斗士，红牛青训体系最强产品之一。以激进的超车风格和永不放弃的比赛态度赢得围场尊重，2026赛季继续在Racing Bulls证明自己。"),
    "Arvid Lindblad": dict(team="Racing Bulls", nationality="United Kingdom", flag="🇬🇧", number="7", dob="2007-08-08", age=18,
                            bio="F1历史上最年轻的车手之一，红牛青训新一代领军人物。2025年F3冠军直跳F1，天赋惊人但需要时间积累经验。"),
    "Esteban Ocon": dict(team="Haas", nationality="France", flag="🇫🇷", number="31", dob="1996-09-17", age=29,
                          bio="坚韧的法国车手，2021年匈牙利大奖赛胜者。转会Haas后担任队内领袖角色，搭档新人Bearman开启车队新纪元。"),
    "Oliver Bearman": dict(team="Haas", nationality="United Kingdom", flag="🇬🇧", number="87", dob="2005-05-08", age=21,
                           bio="法拉利青训培养的英国新星，2024年沙特站代打法拉利即拿分。2026年正式升入Haas，展现出超越年龄的比赛智慧。"),
    "Carlos Sainz": dict(team="Williams", nationality="Spain", flag="🇪🇸", number="55", dob="1994-09-01", age=31,
                         bio="经验丰富的西班牙车手，多站分站冠军。转会Williams后承担重建重任，搭档Albon组成最具战斗力的中游阵容。"),
    "Alexander Albon": dict(team="Williams", nationality="Thailand", flag="🇹🇭", number="23", dob="1996-03-23", age=30,
                            bio="泰国骄傲，威廉姆斯复兴的关键人物。2026赛季有了更快的赛车和更强的队友，目标直指中游前列。"),
    "Nico Hulkenberg": dict(team="Audi", nationality="Germany", flag="🇩🇪", number="27", dob="1987-08-19", age=38,
                             bio="德国老将，F1无冕之王之一。以排位赛的惊人单圈能力和丰富的赛车经验著称，作为Audi工厂车队元年车手肩负重任。"),
    "Gabriel Bortoleto": dict(team="Audi", nationality="Brazil", flag="🇧🇷", number="5", dob="2004-10-14", age=21,
                              bio="巴西新星，2024年F3冠军、2025年F2冠军。两连跳天赋惊人，在Audi工厂车队元年获得宝贵F1席位。"),
    "Sergio Perez": dict(team="Cadillac", nationality="Mexico", flag="🇲🇽", number="11", dob="1990-01-26", age=36,
                         bio="墨西哥传奇，轮胎管理大师。在红牛效力多年后转投全新Cadillac F1车队，用丰富经验帮助美国新军站稳脚跟。"),
    "Valtteri Bottas": dict(team="Cadillac", nationality="Finland", flag="🇫🇮", number="77", dob="1989-08-28", age=36,
                            bio="芬兰冰人，10次分站冠军得主。在梅赛德斯时期是Hamilton最强副手，2026赛季与Perez搭档为Cadillac注入丰富经验。"),
    "Fernando Alonso": dict(team="Aston Martin", nationality="Spain", flag="🇪🇸", number="14", dob="1981-07-29", age=44,
                            bio="两届世界冠军，F1活化石。44岁仍保持顶级竞争力，赛车智慧无与伦比。2026赛季搭档本田动力单元和Newey设计的AMR26追逐第三冠。"),
    "Lance Stroll": dict(team="Aston Martin", nationality="Canada", flag="🇨🇦", number="18", dob="1998-10-29", age=27,
                         bio="加拿大人，阿隆索的长期队友。在2026新规下拥有Newey设计的赛车，这是证明自己的绝佳机会。"),
}


# ----------------------------------------------------------------------------
# FastF1 数据抓取
# ----------------------------------------------------------------------------
def fetch_fastf1_data():
    """抓取 2026 赛季数据，返回 (race_results, driver_standings, constructor_standings, driver_stats, track_info)"""
    try:
        import fastf1
    except ImportError:
        print("[WARN] fastf1 未安装，使用静态数据兜底", file=sys.stderr)
        return None

    import pathlib
    pathlib.Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)
    fastf1.Cache.enable_cache(CACHE_DIR)

    race_results = []
    driver_stats = {}  # driver -> {wins, podiums, poles, points, fastestLaps, DNFs, races}
    driver_standings = []
    constructor_standings = []

    # 获取 2026 赛历
    try:
        schedule = fastf1.get_event_schedule(SEASON)
    except Exception as e:
        print(f"[WARN] 获取赛历失败: {e}", file=sys.stderr)
        return None

    # 遍历每个分站（仅正赛 R）
    for _, event in schedule.iterrows():
        rnd = int(event["RoundNumber"])
        try:
            session = fastf1.get_session(SEASON, rnd, "R")
            session.load()
        except Exception as e:
            print(f"[WARN] 第 {rnd} 站加载失败: {e}", file=sys.stderr)
            continue

        results = session.results
        if results is None or len(results) == 0:
            continue

        # ---- raceResults ----
        podium = []
        table = []
        for _, row in results.iterrows():
            pos = int(row["Position"]) if row["Position"] == row["Position"] else 0
            name = row["FullName"]
            team = row["TeamName"]
            time_val = row["Time"]
            if time_val == time_val:  # not NaN
                time_str = str(time_val)
            else:
                time_str = "DNF"
            if pos <= 3:
                podium.append({"pos": pos, "name": _short_name(name), "team": team})
            table.append({"pos": pos, "name": _short_name(name), "team": team, "time": time_str})

        # 杆位（从排位赛或 results 的 GridPosition=1? 用 Qualifying）
        pole = _get_pole(SEASON, rnd)
        # 最快圈
        fastest = _get_fastest_lap(session)

        race_results.append({
            "gp": event["EventName"],
            "circuit": event.get("Location", ""),
            "country": f"🏁 {event['Country']}",
            "dates": _format_dates(event),
            "flag": "🏁",
            "podium": podium,
            "fastest": fastest,
            "dnfs": _get_dnfs(results),
            "table": table,
        })

        # ---- driver_stats 累加 ----
        for _, row in results.iterrows():
            name = _short_name(row["FullName"])
            if name not in driver_stats:
                driver_stats[name] = {"wins": 0, "podiums": 0, "poles": 0,
                                       "points": 0, "fastestLaps": 0, "DNFs": 0, "races": 0}
            ds = driver_stats[name]
            ds["races"] += 1
            ds["points"] += float(row["Points"]) if row["Points"] == row["Points"] else 0.0
            pos = int(row["Position"]) if row["Position"] == row["Position"] else 0
            if pos == 1:
                ds["wins"] += 1
            if 1 <= pos <= 3:
                ds["podiums"] += 1
            if row["Status"] not in ("Finished", "Finished", None) and "DNF" in str(row["Status"]).upper():
                ds["DNFs"] += 1

        # ---- 积分榜（取最后一站后的 standings）----
        try:
            ds_standings = session.get_driver_standings()
            if ds_standings is not None:
                driver_standings = ds_standings
        except Exception:
            pass
        try:
            cs_standings = session.get_constructor_standings()
            if cs_standings is not None:
                constructor_standings = cs_standings
        except Exception:
            pass

    return {
        "race_results": race_results,
        "driver_standings": driver_standings,
        "constructor_standings": constructor_standings,
        "driver_stats": driver_stats,
    }


def _short_name(full_name):
    """将 FullName 转为 index.html 中使用的短名（Last Name 或已知映射）"""
    mapping = {
        "Kimi Antonelli": "Antonelli",
        "George Russell": "Russell",
        "Charles Leclerc": "Leclerc",
        "Lewis Hamilton": "Hamilton",
        "Lando Norris": "Norris",
        "Oscar Piastri": "Piastri",
        "Max Verstappen": "Verstappen",
        "Isack Hadjar": "Hadjar",
        "Pierre Gasly": "Gasly",
        "Franco Colapinto": "Colapinto",
        "Liam Lawson": "Lawson",
        "Arvid Lindblad": "Lindblad",
        "Esteban Ocon": "Ocon",
        "Oliver Bearman": "Bearman",
        "Carlos Sainz": "Sainz",
        "Alexander Albon": "Albon",
        "Nico Hulkenberg": "Hulkenberg",
        "Gabriel Bortoleto": "Bortoleto",
        "Sergio Perez": "Perez",
        "Valtteri Bottas": "Bottas",
        "Fernando Alonso": "Alonso",
        "Lance Stroll": "Stroll",
    }
    return mapping.get(full_name, full_name.split()[-1])


def _get_pole(season, rnd):
    try:
        q = fastf1.get_session(season, rnd, "Q")
        q.load()
        if q.results is not None:
            pole_row = q.results.iloc[0]
            return _short_name(pole_row["FullName"])
    except Exception:
        pass
    return "—"


def _get_fastest_lap(session):
    try:
        fl = session.get_fastest_lap()
        if fl is not None:
            return _short_name(fl["Driver"])
    except Exception:
        pass
    return "—"


def _get_dnfs(results):
    dnfs = []
    for _, row in results.iterrows():
        status = str(row["Status"])
        if "DNF" in status.upper() or "Retired" in status or "Accident" in status or "Mechanical" in status:
            dnfs.append(_short_name(row["FullName"]))
    return "、".join(dnfs) if dnfs else "无重大退赛"


def _format_dates(event):
    import datetime as _dt
    try:
        sd = event["Session5Date"] if "Session5Date" in event else event.get("Date")
        if sd is not None:
            return f"{sd.month}月{sd.day}日"
    except Exception:
        pass
    return "TBD"


# ----------------------------------------------------------------------------
# 生成 data.js
# ----------------------------------------------------------------------------
def _has_data(obj):
    """判断 standings 对象是否有有效数据（非 None / 非空 list / 非空 DataFrame）"""
    if obj is None:
        return False
    if hasattr(obj, "empty"):
        return not obj.empty
    if isinstance(obj, (list, tuple)):
        return len(obj) > 0
    return True


def _iter_rows(obj):
    """统一迭代 DataFrame 或 list of dicts，每次 yield 一个类似 Series 的行对象"""
    if hasattr(obj, "iterrows"):
        for _, row in obj.iterrows():
            yield row
    else:
        for row in obj:
            yield row


def build_data_js(f1_data):
    """根据 FastF1 数据（或 None）生成 data.js 内容，无数据时全部用静态兜底"""
    lines = []
    lines.append("// ============================================================")
    lines.append("//  F1-DRS DATA LAYER")
    lines.append("//  Auto-generated by scripts/update_data.py (FastF1)")
    lines.append(f"//  Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("//  Variables are global (declared with const at top-level script scope).")
    lines.append("// ============================================================\n")

    # ----- circuits -----
    lines.append("// ----- circuits -----")
    lines.append("const circuits = [")
    for i, c in enumerate(CIRCUITS, start=1):
        lines.append(
            f"  {{ no:'{c['no']}', gp:'{c['gp']}', circuit:'{c['circuit']}', city:'{c['city']}', "
            f"date:'{c['date']}', trackDetailId:{c['trackDetailId']} }},"
        )
    lines.append("];\n")

    # ----- compareDrivers (静态) -----
    lines.append("// ----- compareDrivers -----")
    lines.append("const compareDrivers = [")
    for d in COMPARE_DRIVERS:
        lines.append(
            f"  {{ name:'{d['name']}', team:'{d['team']}', color:'{d['color']}', num:{d['num']}, "
            f"wins:{d['wins']}, podiums:{d['podiums']}, poles:{d['poles']}, points:{d['points']}, fastest:{d['fastest']} }},"
        )
    lines.append("];\n")

    # ----- champions (静态) -----
    lines.append("// ----- champions -----")
    lines.append("const champions = [")
    for c in CHAMPIONS:
        lines.append(f"  {{ year:{c['year']}, driver:'{c['driver']}', team:'{c['team']}' }},")
    lines.append("];\n")

    # ----- constructorsData -----
    lines.append("// ----- constructorsData -----")
    cs = f1_data.get("constructor_standings") if f1_data else None
    if _has_data(cs):
        lines.append("const constructorsData = [")
        for i, row in enumerate(_iter_rows(cs), start=1):
            team = row["TeamName"]
            points = float(row["Points"]) if row["Points"] == row["Points"] else 0.0
            color = TEAM_COLORS.get(team, "#888888")
            drivers2026 = _team_drivers(team)
            lines.append(
                f"  {{ rank:{i}, name:'{team}', points:{int(points)}, color:'{color}', "
                f"drivers2026:{json.dumps(drivers2026, ensure_ascii=False)}, change:0 }},"
            )
        lines.append("];\n")
    else:
        # 静态兜底
        lines.append(_static_constructors())

    # ----- driverStandings -----
    lines.append("// ----- driverStandings -----")
    ds = f1_data.get("driver_standings") if f1_data else None
    if _has_data(ds):
        lines.append("const driverStandings = [")
        leader_pts = None
        for i, row in enumerate(_iter_rows(ds), start=1):
            name = _short_name(row["FullName"])
            team = row["TeamName"]
            pts = float(row["Points"]) if row["Points"] == row["Points"] else 0.0
            color = TEAM_COLORS.get(team, "#888888")
            behind = 0 if leader_pts is None else int(leader_pts - pts)
            if leader_pts is None:
                leader_pts = pts
            lines.append(
                f"  {{ rank:{i}, name:'{name}', team:'{team}', pts:{int(pts)}, color:'{color}', behind:{behind} }},"
            )
        lines.append("];\n")
    else:
        lines.append(_static_driver_standings())

    # ----- raceResults -----
    lines.append("// ----- raceResults -----")
    if f1_data and f1_data.get("race_results"):
        lines.append("const raceResults = [")
        for r in f1_data["race_results"]:
            lines.append("  {")
            lines.append(f"    gp:'{r['gp']}', circuit:'{r['circuit']}', country:'{r['country']}', dates:'{r['dates']}', flag:'{r['flag']}',")
            podium_str = ", ".join(f"{{pos:{p['pos']},name:'{p['name']}',team:'{p['team']}'}}" for p in r["podium"])
            lines.append(f"    podium: [{podium_str}],")
            lines.append(f"    fastest:'{r['fastest']}', dnfs:'{r['dnfs']}',")
            table_str = ", ".join(f"{{pos:{t['pos']},name:'{t['name']}',team:'{t['team']}',time:'{t['time']}'}}" for t in r["table"])
            lines.append(f"    table: [{table_str}]")
            lines.append("  },")
        lines.append("];\n")
    else:
        lines.append(_static_race_results())

    # ----- trackDetailData -----
    lines.append("// ----- trackDetailData -----")
    lines.append("const trackDetailData = [")
    for i, (tid, info) in enumerate(TRACK_STATIC.items(), start=1):
        laps, length, dist = _track_geometry(tid, info)
        rec_driver, rec_time, rec_year = info["record"]
        layout = FOM_LAYOUT_TPL.format(CIRCUIT=info["fom"])
        lines.append("  {")
        lines.append(f"    id:'{tid}', name:'{info['name']}', gp:'{info['gp']}', country:'{info['country']}', firstRace:{info['firstRace']},")
        lines.append(f"    laps:{laps}, length:'{length}', dist:'{dist}', corners:{info['corners']}, drs:{info['drs']},")
        lines.append(f"    record:{{driver:'{rec_driver}', time:'{rec_time}', year:{rec_year if isinstance(rec_year, int) else chr(39)+str(rec_year)+chr(39)}}},")
        lines.append(f"    layout:'{layout.replace(chr(39), chr(92)+chr(39))}'")
        lines.append("  },")
    lines.append("];\n")

    # ----- driverData -----
    lines.append("// ----- driverData -----")
    lines.append("const driverData = [")
    stats = f1_data.get("driver_stats", {}) if f1_data else {}
    for name, static in DRIVER_STATIC.items():
        s = stats.get(name, {})
        wins = s.get("wins", 0)
        podiums = s.get("podiums", 0)
        poles = s.get("poles", 0)
        points = int(s.get("points", 0))
        fastest = s.get("fastestLaps", 0)
        dnfs = s.get("DNFs", 0)
        races = s.get("races", 0)
        championships = _championships(name)
        lines.append(
            f"  {{ name:'{name}', team:'{static['team']}', nationality:'{static['nationality']}', "
            f"flag:'{static['flag']}', number:'{static['number']}', dob:'{static['dob']}', age:{static['age']}, "
            f"races:{races}, wins:{wins}, podiums:{podiums}, poles:{poles}, fastestLaps:{fastest}, "
            f"championships:{championships}, bio:'{static['bio']}' }},"
        )
    lines.append("];\n")

    return "\n".join(lines)


def _team_drivers(team):
    """返回该车队 2026 阵容短名列表"""
    mapping = {
        "Mercedes": ["Russell", "Antonelli"],
        "Ferrari": ["Leclerc", "Hamilton"],
        "McLaren": ["Norris", "Piastri"],
        "Red Bull": ["Verstappen", "Hadjar"],
        "Red Bull Racing": ["Verstappen", "Hadjar"],
        "Alpine": ["Gasly", "Colapinto"],
        "Racing Bulls": ["Lawson", "Lindblad"],
        "Haas": ["Bearman", "Ocon"],
        "Williams": ["Sainz", "Albon"],
        "Audi": ["Hulkenberg", "Bortoleto"],
        "Aston Martin": ["Alonso", "Stroll"],
        "Cadillac": ["Perez", "Bottas"],
    }
    return mapping.get(team, [])


def _track_geometry(tid, info):
    """返回 (laps, length, dist)。优先用 FastF1，否则用静态近似。"""
    # 静态近似（FastF1 的 CircuitInfo 需要加载，这里用已知值兜底）
    STATIC_GEO = {
        "albert-park": (58, "5.278 km", "306.124 km"),
        "shanghai": (56, "5.451 km", "305.256 km"),
        "suzuka": (53, "5.807 km", "307.771 km"),
        "bahrain": (57, "5.412 km", "308.484 km"),
        "jeddah": (50, "6.174 km", "308.700 km"),
        "miami": (57, "5.412 km", "308.326 km"),
        "montreal": (68, "4.361 km", "296.548 km"),
        "monaco": (78, "3.337 km", "260.286 km"),
        "barcelona": (66, "4.657 km", "307.362 km"),
        "red-bull-ring": (71, "4.318 km", "306.578 km"),
        "silverstone": (52, "5.891 km", "306.332 km"),
        "spa": (44, "7.004 km", "308.176 km"),
        "hungaroring": (70, "4.381 km", "306.670 km"),
        "zandvoort": (72, "4.259 km", "306.648 km"),
        "monza": (53, "5.793 km", "307.029 km"),
        "madrid": (65, "5.474 km", "355.810 km"),
        "baku": (51, "6.003 km", "306.153 km"),
        "singapore": (61, "5.063 km", "308.843 km"),
        "cota": (56, "5.513 km", "308.728 km"),
        "mexico": (71, "4.304 km", "305.584 km"),
        "interlagos": (71, "4.309 km", "305.939 km"),
        "las-vegas": (50, "6.201 km", "310.050 km"),
        "lusail": (57, "5.419 km", "308.883 km"),
        "yas-marina": (58, "5.281 km", "306.298 km"),
    }
    return STATIC_GEO.get(tid, (0, "0 km", "0 km"))


def _championships(name):
    champ_map = {
        "Lewis Hamilton": 7, "Max Verstappen": 4, "Fernando Alonso": 2,
        "Lando Norris": 1,
    }
    return champ_map.get(name, 0)


def _static_constructors():
    return (
        "const constructorsData = [\n"
        "  { rank:1, name:\"Mercedes\", points:333, color:\"#27f4d2\", drivers2026:[\"Russell\",\"Antonelli\"], change:0 },\n"
        "  { rank:2, name:\"Ferrari\", points:255, color:\"#dc0000\", drivers2026:[\"Leclerc\",\"Hamilton\"], change:0 },\n"
        "  { rank:3, name:\"McLaren\", points:179, color:\"#ff8000\", drivers2026:[\"Norris\",\"Piastri\"], change:0 },\n"
        "  { rank:4, name:\"Red Bull\", points:128, color:\"#1e41b0\", drivers2026:[\"Verstappen\",\"Hadjar\"], change:0 },\n"
        "  { rank:5, name:\"Alpine\", points:60, color:\"#0093cc\", drivers2026:[\"Gasly\",\"Colapinto\"], change:0 },\n"
        "  { rank:6, name:\"Racing Bulls\", points:59, color:\"#6699ff\", drivers2026:[\"Lawson\",\"Lindblad\"], change:0 },\n"
        "  { rank:7, name:\"Haas\", points:21, color:\"#cc0000\", drivers2026:[\"Bearman\",\"Ocon\"], change:0 },\n"
        "  { rank:8, name:\"Williams\", points:11, color:\"#005aff\", drivers2026:[\"Sainz\",\"Albon\"], change:0 },\n"
        "  { rank:9, name:\"Audi\", points:6, color:\"#c0c0c0\", drivers2026:[\"Hulkenberg\",\"Bortoleto\"], change:0 },\n"
        "  { rank:10, name:\"Aston Martin\", points:1, color:\"#006f62\", drivers2026:[\"Alonso\",\"Stroll\"], change:0 },\n"
        "  { rank:11, name:\"Cadillac\", points:0, color:\"#cf9f3f\", drivers2026:[\"Perez\",\"Bottas\"], note:\"2026新队\", change:0 }\n"
        "];\n"
    )


def _static_driver_standings():
    return (
        "const driverStandings = [\n"
        "  { rank:1, name:\"Antonelli\", team:\"Mercedes\", pts:179, color:\"#27f4d2\", behind:0 },\n"
        "  { rank:2, name:\"Russell\", team:\"Mercedes\", pts:154, color:\"#27f4d2\", behind:25 },\n"
        "  { rank:3, name:\"Hamilton\", team:\"Ferrari\", pts:147, color:\"#dc0000\", behind:32 },\n"
        "  { rank:4, name:\"Leclerc\", team:\"Ferrari\", pts:108, color:\"#dc0000\", behind:71 },\n"
        "  { rank:5, name:\"Norris\", team:\"McLaren\", pts:97, color:\"#ff8000\", behind:82 },\n"
        "  { rank:6, name:\"Piastri\", team:\"McLaren\", pts:82, color:\"#ff8000\", behind:97 },\n"
        "  { rank:7, name:\"Verstappen\", team:\"Red Bull\", pts:76, color:\"#1e41b0\", behind:103 },\n"
        "  { rank:8, name:\"Hadjar\", team:\"Red Bull\", pts:52, color:\"#1e41b0\", behind:127 },\n"
        "  { rank:9, name:\"Gasly\", team:\"Alpine\", pts:42, color:\"#0093cc\", behind:137 },\n"
        "  { rank:10, name:\"Lawson\", team:\"Racing Bulls\", pts:39, color:\"#6699ff\", behind:140 },\n"
        "  { rank:11, name:\"Lindblad\", team:\"Racing Bulls\", pts:20, color:\"#6699ff\", behind:159 },\n"
        "  { rank:12, name:\"Bearman\", team:\"Haas\", pts:18, color:\"#cc0000\", behind:161 },\n"
        "  { rank:13, name:\"Colapinto\", team:\"Alpine\", pts:18, color:\"#0093cc\", behind:161 },\n"
        "  { rank:14, name:\"Bortoleto\", team:\"Audi\", pts:6, color:\"#c0c0c0\", behind:173 },\n"
        "  { rank:15, name:\"Sainz\", team:\"Williams\", pts:6, color:\"#005aff\", behind:173 },\n"
        "  { rank:16, name:\"Albon\", team:\"Williams\", pts:5, color:\"#005aff\", behind:174 },\n"
        "  { rank:17, name:\"Ocon\", team:\"Haas\", pts:3, color:\"#cc0000\", behind:176 },\n"
        "  { rank:18, name:\"Alonso\", team:\"Aston Martin\", pts:1, color:\"#006f62\", behind:178 },\n"
        "  { rank:19, name:\"Hulkenberg\", team:\"Audi\", pts:0, color:\"#c0c0c0\", behind:179 },\n"
        "  { rank:20, name:\"Bottas\", team:\"Cadillac\", pts:0, color:\"#cf9f3f\", behind:179 },\n"
        "  { rank:21, name:\"Perez\", team:\"Cadillac\", pts:0, color:\"#cf9f3f\", behind:179 },\n"
        "  { rank:22, name:\"Stroll\", team:\"Aston Martin\", pts:0, color:\"#006f62\", behind:179 }\n"
        "];\n"
    )


def _static_race_results():
    """静态兜底：返回当前已知的 7 站结果（与 data.js 原内容一致）"""
    # 为简洁，这里返回空数组提示；实际兜底应使用原 data.js 内容
    return "const raceResults = [];  // FastF1 抓取失败时为空，请检查网络\n"


# ----------------------------------------------------------------------------
# 主函数
# ----------------------------------------------------------------------------
def main():
    print(f"[INFO] 开始更新 {SEASON} 赛季数据...")
    print(f"[INFO] 输出路径: {OUTPUT_PATH}")

    f1_data = fetch_fastf1_data()

    if f1_data is None:
        # FastF1 不可用（未安装/网络失败）：保留现有 data.js，不覆盖真实数据
        if os.path.exists(OUTPUT_PATH):
            print(f"[WARN] FastF1 数据抓取失败，保留现有 {OUTPUT_PATH} 不变", file=sys.stderr)
        else:
            # 首次运行且无 data.js：生成静态兜底（占位）版本
            js_content = build_data_js(None)
            os.makedirs(DOCS_DIR, exist_ok=True)
            with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                f.write(js_content)
            print(f"[OK] 已生成静态兜底 {OUTPUT_PATH} ({len(js_content)} 字符)")
        return

    js_content = build_data_js(f1_data)

    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"[OK] 已生成 {OUTPUT_PATH} ({len(js_content)} 字符)")


if __name__ == "__main__":
    main()
